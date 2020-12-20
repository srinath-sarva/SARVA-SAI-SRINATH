from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.forms import UserCreationForm

from .forms import CreateUserForm,Createcomplaint,Statusform
from django.contrib  import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

def register(request):
    
    form=CreateUserForm()
    
    if request.method=="POST":
        form=CreateUserForm(request.POST,request.FILES)
        if form.is_valid():
            form.save() 
            
            username=form.cleaned_data.get('username').lower()
            email=form.cleaned_data.get('email')
            phone=form.cleaned_data.get('phone')
            user=User.objects.get(username=username)
            gender=form.cleaned_data.get('gender')
            propic=form.cleaned_data.get('propic')
            address=form.cleaned_data.get('address')
            print(user)
            p=person(user=user,name=username,email=email,phone=phone,gender=gender,propic=propic,address=address)
            p.save()
            messages.info(request,"registration success")
            return redirect('login')
    context={'form':form}
    return render(request,"issues/register.html",context) 
def loginpage(request):
    if(request.method=='POST'):
        username=request.POST.get('username').lower()
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        print(user)
        if user is not None: 
            login(request,user)
            profile=request.user.get_username() 
            print(profile)
            if(profile=='srinath'):
                return redirect('adminedit') 
            else:
                return redirect('posts')
        else:
            messages.info(request,"wrong")


    return render(request,"issues/login.html")

def logoutuser(request):
    logout(request)
    return redirect('login') 
@login_required(login_url='login')
def mydetails(request):
    persons=person.objects.all()

    profile=request.user.get_username()

    print(profile)
    print(persons)
    if request.method=="POST":
        uemail=request.POST.get('email')
        uphone=request.POST.get('phone') 
        uaddress=request.POST.get('address')
        s=persons.objects.filter(name=profile).update(phone=uphone,email=uemail,address=uaddress)

    for i in persons:

        if(i.name==profile):
            
            name=i.name 
             
            email=i.email
            gender=i.gender
            phone=i.phone
            address=i.address
            return render(request,"issues/mydetails.html",{"persons":persons,"phone":phone,"name":name,"email":email,"gender":gender,"address":address,"i":i})

            break
    return render(request,"issues/mydetails.html",{"persons":persons,"phone":phone,"name":name,"email":email,"gender":gender,"address":address,"i":i})

def makecomplaint(request):

    complaints.objects.filter(propic="").delete()

    profile=request.user.get_username()
    
    propic=request.user.person.propic.url
    form=Createcomplaint()
    if request.method=="POST":
        form=Createcomplaint(request.POST,request.FILES)
        form.save()
        profile=request.user.get_username()
        propic=request.user.person.propic.url

        compname=form.cleaned_data.get("compname")
        pic1=form.cleaned_data.get("pic1")
        pic2=form.cleaned_data.get("pic2")
        pic3=form.cleaned_data.get("pic3")
        place=form.cleaned_data.get("place")
    
        city=form.cleaned_data.get("city")
        desc=form.cleaned_data.get("desc")
        c=complaints(name=profile,compname=compname,pic1=pic1,pic2=pic2,pic3=pic3,place=place,city=city,desc=desc,propic=propic)
        c.save()
        complaints.objects.filter(propic=None).delete()
        return redirect('posts')

    return render(request,"issues/makecomplaint.html",{"form":form})    
def showcomplaint(request):
    complaints.objects.filter(propic="").delete()

    if request.method=="POST":
        u=request.POST.get('up') 
        mess=request.POST.get('mess')
        id=request.POST.get('id')
        profile=request.user.get_username()
        if(len(mess)>0):
            o=chat(cid=id,name=profile,chat=mess)
            o.save()
        if(u):
            s=complaints.objects.filter(id=u).values("upvote")
            k=str(s).split(":")[-1]
            h=k.split("}]>")[0]
            c=int(h)
            s=complaints.objects.filter(id=u).update(upvote=c+1)
    com=complaints.objects.all()
    for i in com:
        print(i)
    cha=chat.objects.all()
    return render(request,"issues/posts.html",{"p":com,"cha":cha})
def showmycomplaint(request):
    profile=request.user.get_username()
    com=complaints.objects.filter(name=profile)
   
    if request.method=="POST":
        id=request.POST.get('id')
        id1=request.POST.get('id1')
        pom=complaints.objects.filter(id=id).delete()
        return render(request,"issues/myposts.html",{"p":com})
        
    for i in com:
        print(i.status)
    return render(request,"issues/myposts.html",{"p":com})
    
def adminedit(request):

    complaints.objects.filter(propic="").delete()
    complaints.objects.filter(compname="").delete()
    

    com=complaints.objects.all()
    form=Statusform()
    if request.method=="POST":
        complaints.objects.filter(propic="").delete()
        complaints.objects.filter(compname="").delete()

        
        form=Statusform(request.POST,request.FILES)
        form.save()
        g=form.cleaned_data.get('status')
        id=request.POST.get('id')
        complaints.objects.filter(id=id).update(status=g)

        complaints.objects.filter(propic="").delete()
        complaints.objects.filter(compname="").delete()



    return render(request,"issues/adminedit.html",{"p":com,"form":form})
