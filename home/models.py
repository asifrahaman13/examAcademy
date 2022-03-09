from django.db import models

# Create your models here.
class Contact(models.Model):
    sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255,default='')
    email=models.EmailField(max_length=100)
    phone=models.CharField(max_length=100)
    stream=models.CharField(max_length=100)
    concern=models.CharField(max_length=1000,default='')
    