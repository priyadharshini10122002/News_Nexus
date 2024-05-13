from django.db import models

# Create your models here.

from django.db import models

class Admin_Registration(models.Model):
    name = models.CharField(max_length=50)
    mobile = models.IntegerField(max_length=10)
    email =models.CharField(max_length=50)
    username=models.CharField(max_length=8)
    password=models.CharField(max_length=8)

class User_Registration(models.Model):
    name = models.CharField(max_length=50)
    mobile = models.IntegerField(max_length=10)
    email =models.CharField(max_length=50)
    username=models.CharField(max_length=8)
    password=models.CharField(max_length=8)


class News_Feed(models.Model):
    Feed_Id=models.BigAutoField(primary_key=True)
    username=models.ForeignKey(Admin_Registration,on_delete=models.CASCADE)
    content =models.CharField(max_length=200)

class Saved_Feed(models.Model):
    username=models.ForeignKey(User_Registration,on_delete=models.CASCADE)
    Feed_Id =models.ForeignKey(News_Feed,on_delete=models.CASCADE)

