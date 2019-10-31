from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    student_age = models.IntegerField()

class Trail(models.Model):
    trail_name=models.CharField(max_length=200)
    trail_length=models.FloatField()
    trail_elevation=models.IntegerField()