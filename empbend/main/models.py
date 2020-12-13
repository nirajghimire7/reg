from django.db import models

class Employee(models.Model):
    full_name=models.CharField(max_length=200)
    address=models.TextField()
    phone=models.CharField(max_length=20)
    email=models.CharField(max_length=100)


    def __str__(self):
        return self.full_name
        