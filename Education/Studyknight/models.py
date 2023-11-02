from datetime import datetime
from django.db import models

class SSC(models.Model):
    ssc_txt = models.CharField(max_length= 200)
    email = models.EmailField()

class GD(models.Model):
    gd_txt = models.CharField(max_length= 200)
    pub_date = datetime.now()

class Free(models.Model):
    free_txt = models.CharField(max_length=500)
    age = models.IntegerField()

class Form(models.Model):
    free_txt = models.CharField(max_length=500)
    email = models.EmailField()
    pub_date = models.DateTimeField("Date Published")
    age = models.IntegerField() 


class Context(models.Model):
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=200)
    email=models.CharField(max_length=100)
    content=models.TextField(max_length=100)

    def __str__(self):
        return "Message from" + self.name    


class Omen(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    def __str__(self):
        return "Message from" + self.name

  
