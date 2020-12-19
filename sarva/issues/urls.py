from django.urls import path
from . import views 
from django.contrib.auth import views as auth_views

urlpatterns=[

    path('register/',views.register,name="register"),
    path('login/',views.loginpage,name="login"),
    path('mydetails/',views.mydetails,name="mydetails"),
    path('logout/',views.logoutuser,name="logout"),
    path('makecomplaint/',views.makecomplaint,name="makecomplaint"),

]