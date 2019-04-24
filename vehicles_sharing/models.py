from django.contrib.auth.models import User
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from rest_framework.authtoken.models import Token

from .pom import Validators as validators


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


DRIVE_TRAIN_CHOICES = {
    ('RWD', 'Rear Wheel Drive'),
    ('FWD', 'Front Wheel Drive'),
    ('AWD', 'All Wheel Drive'),
}


class Vehicle(models.Model):
    brand = models.CharField(max_length=50, validators=[validators.brand])
    model = models.CharField(max_length=50, validators=[validators.alphanumeric])
    price = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(3000000)])
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    production_year = models.IntegerField(
        validators=[MinValueValidator(1800), MaxValueValidator(timezone.now().year + 2)])
    city = models.CharField(max_length=50, validators=[validators.city_street])
    street = models.CharField(max_length=50, validators=[validators.city_street])
    power = models.IntegerField(null=True,
                                validators=[MinValueValidator(0), MaxValueValidator(timezone.now().year + 2)])
    capacity = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(8)])
    drive_train = models.CharField(choices=DRIVE_TRAIN_CHOICES, max_length=4)
    description = models.CharField(max_length=10000)


class Reservation(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='client')
    car = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='car')
    start_date = models.DateField()
    end_date = models.DateField()
    active = models.BooleanField(default=False)
    message = models.CharField(max_length=3000)
