from django.db import models
from django.utils import timezone


class User(models.Model):
    user_num = models.ForeignKey('auth.User')
    job_function = models.CharField(max_length=200)
    job_industry = models.CharField(max_length=200)
    major_study = models.CharField(max_length=200)
    city_location = models.CharField(max_length=200)

    def __str__(self):
        return self.name # Create your models here.
