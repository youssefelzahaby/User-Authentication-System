from django.db import models

# Create your models here.
class Sign (models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('no', 'Prefer not to say'),
    ]
    f_name=models.CharField(max_length=150)
    username=models.CharField(max_length=150)
    password=models.CharField(max_length=150)
    email=models.CharField(max_length=150)
    number=models.IntegerField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES,default='no')


