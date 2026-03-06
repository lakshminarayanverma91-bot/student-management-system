from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_no = models.CharField(max_length=13)
    image = models.ImageField(null=True, blank=True, upload_to="images/")