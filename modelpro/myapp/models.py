from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=80)
    age=models.IntegerField()
    phone=models.CharField(max_length=100)
    email=models.EmailField()

    def __str__(self):
        return self.name
