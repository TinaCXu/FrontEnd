from django.db import models

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=300)
    principal = models.CharField(max_length=300)
    location = models.CharField(max_length=300)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=300)
    age = models.PositiveIntegerField()
    School = models.ForeignKey(School,related_name='students',on_delete=models.CASCADE)
    # related name: relate School to student

    def __str__(self):
        return self.name