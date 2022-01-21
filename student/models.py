from django.db import models

# Create your models here.

import uuid

class Student(models.Model):
    student_name = models.CharField(max_length=200)
    student_class = models.CharField(max_length=10)
    student_gender = models.CharField(max_length=20)
    student_enrollment_id = models.IntegerField()
    student_subject = models.CharField(max_length=200,default="All")
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.student_name
