from django.db import models

class About(models.Model):
    name = models.CharField(max_length = 50)
    college = models.CharField(max_length = 50)
    course = models.CharField(max_length = 20)
    phone_no = models.CharField(max_length = 13)
    email = models.EmailField()
    gender = models.CharField(max_length = 6)
    year = models.IntegerField()
