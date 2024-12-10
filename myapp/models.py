from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=50 )
    email = models.EmailField()
    phoneNumber = models.CharField(max_length=12)
    description = models.TextField(max_length=500 ,null=True,blank=True)


    def __str__(self):
        return f'Message from {self.name}'