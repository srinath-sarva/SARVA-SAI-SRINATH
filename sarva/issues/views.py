from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.forms import UserCreationForm

from .forms import CreateUserForm
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
    context={'form':form}
    return render(request,"issues/register.html",context) 
