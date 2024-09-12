from django.db import models

# Create your models here.

class Student(models.Model):
    Name = models.CharField(max_length=100)
    Dob = models.DateField()
    Age = models.IntegerField()
    Email = models.EmailField()
    Address = models.TextField(null=True , blank=True)
    #Image = models.ImageField()
    #File = models.FileField()


class College(models.Model):
    Name = models.CharField(max_length=100)
    SubjectNo = models.IntegerField()   
    Email = models.EmailField()
    Address = models.TextField()

class Car(models.Model):
    Name = models.CharField(max_length=100)
    Speed = models.IntegerField(default=50)

    def __str__(self) -> str:
     return self.Name

