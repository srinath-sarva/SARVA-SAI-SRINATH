from django.urls import path
from . import views 
from django.contrib.auth import views as auth_views

urlpatterns=[

    path('register/',views.register,name="register"),
    path('login/',views.loginpage,name="login"),
    path('mydetails/',views.mydetails,name="mydetails"),
    path('logout/',views.logoutuser,name="logout"),
    path('makecomplaint/',views.makecomplaint,name="makecomplaint"),
    path('posts/',views.showcomplaint,name="posts"),
    path('',views.showcomplaint,name="posts"),
    path('myposts/',views.showmycomplaint,name="myposts"),
    path('adminedit/',views.adminedit,name="adminedit"),
 path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="issues/password_reset.html"),
     name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="issues/password_reset_sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="issues/password_reset_form.html"), 
     name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="issues/password_reset_done.html"), 
        name="password_reset_complete"),


]