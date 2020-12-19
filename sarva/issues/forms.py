from django.contrib.auth.forms import UserCreationForm 
from django import forms 
from .models import * 
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    phone=forms.CharField()
    gen=(
        ('male','male'),
        ("female","female")
    )
    gender=forms.ChoiceField(choices=gen)
    address=forms.CharField()
    propic=forms.FileField()

    class Meta:
        model=User 
        fields=["username","email","password1","password2","phone","gender","address","propic"]

class Createcomplaint(forms.ModelForm):
  
    class Meta:
        model=complaints
        fields=["name","compname","pic1","pic2","place","city","desc"] 

     

         
