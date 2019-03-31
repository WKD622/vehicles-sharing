from django.db import models


# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    login = models.CharField(max_length=11)
    password = models.CharField(max_length=50, null=False)
    mail = models.CharField(null=False)
    photo = models.BinaryField(null=True)


class Reservation(models.Model):
    owner_id = models.IntegerField()
    client_id = models.IntegerField()
    car_id = models.IntegerField()
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=False)
    active = models.BooleanField(default=False)
    message = models.CharField(max_length=3000)
