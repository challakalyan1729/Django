from django.db import models
class student1(models.Model):
    rollno = models.IntegerField()
    student_name = models.CharField(max_length=20)
class marks1(models.Model):
    subject1 = models.FloatField()
    subject2 = models.FloatField()
class courses(models.Model):
    coursename = models.CharField(max_length=30)
    courseid = models.CharField(max_length=30)



