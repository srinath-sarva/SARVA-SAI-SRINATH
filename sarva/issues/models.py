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