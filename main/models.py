import email
from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=20)
    age=models.CharField(max_length=20)
    phone=models.CharField(max_length=10)
    gender=models.CharField(max_length=30,default="")
    limage=models.ImageField(upload_to='media/images',default="")
    rimage=models.ImageField(upload_to='media/images',default="")
    res1=models.CharField(max_length=22,default="")
    res2=models.CharField(max_length=22,default="")

    def __str__(self):
        return self.name
