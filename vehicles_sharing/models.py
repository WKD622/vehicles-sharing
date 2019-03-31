from django.db import models
from django.core.validators import EmailValidator


# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=50)
    mail = models.CharField(validators=EmailValidator)
    photo = models.ImageField(upload_to='pic_folder/', default='pic_folder/None/no-img.jpg')


class Reservation(models.Model):
    owner_id = models.IntegerField()
    client_id = models.IntegerField()
    car_id = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    active = models.BooleanField(default=False)
    message = models.CharField(max_length=3000)
