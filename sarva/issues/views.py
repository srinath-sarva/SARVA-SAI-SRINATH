from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.forms import UserCreationForm

from .forms import CreateUserForm,changeform
from django.contrib  import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

