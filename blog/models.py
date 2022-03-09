from sqlite3 import Timestamp
from django.db import models

# Create your models here.
class Post(models.Model):
    sno=models.AutoField(primary_key=True)
    head1=models.CharField(max_length=100)
    chead1=models.CharField(max_length=3000)
    head2=models.CharField(max_length=100)
    chead2=models.CharField(max_length=3000)
    head3=models.CharField(max_length=100)
    chead3=models.CharField(max_length=3000)
    author=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    Timestamp=models.DateTimeField(blank=True)
    
    def __str__(self):
        return 'Message from'+'-'+self.email