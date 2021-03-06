from django.db import models
from django.contrib.auth.models import User
class person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    name=models.CharField(max_length=200,null=False)
    email=models.CharField(max_length=200,null=True)
    date_of_join=models.DateTimeField(auto_now_add=True,null=True)
    gender=models.CharField(max_length=10,null=True,choices=(("male","male"),("female","female")))
    phone=models.CharField(max_length=10,null=True)
    address=models.CharField(max_length=10,null=True)
    propic=models.ImageField(default="propic.png",null=True)

                
    def __str__(self):
        return (self.name)
class chat(models.Model):
    cid=models.IntegerField(default=0)
    name=models.CharField(max_length=200,null=True) 
    chat=models.CharField(max_length=200,null=True)
    date=models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        return (self.chat)
   
class complaints(models.Model):
    propic=models.CharField(max_length=600,null=False)
    name=models.CharField(max_length=400,null=False)
    compname=models.CharField(max_length=400,null=False)
    pic1=models.ImageField(null=False)
    pic2=models.ImageField(null=False)
    pic2=models.ImageField(null=False)
    pic3=models.ImageField(null=False)
    place=models.CharField(max_length=400,null=False)
    city=models.CharField(max_length=400,null=False)
    date=models.DateTimeField(auto_now_add=True,null=True)
    desc=models.CharField(max_length=500,null=True)
    upvote=models.IntegerField(null=True,default=0) 
    status=models.CharField(max_length=100,null=True,choices=(("open","open"),("no action taken","no action taken"),("submitted to the newspaper","submitted to the newspaper"),("resolved","resolved")),default="open")
    def __str__(self):
        return ((self.compname)+(self.city))

   