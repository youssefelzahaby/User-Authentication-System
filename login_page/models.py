from django.db import models

# Create your models here.
class login(models.Model):
    username=models.CharField(max_length=150)
    password=models.CharField(max_length=150)
    def __str__(self):
        return self.username