from django.db import models
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator

DRIVE_TRAIN_CHOICES = {
    ('RWD', 'Rear Wheel Drive'),
    ('FWD', 'Front Wheel Drive'),
    ('AWD', 'All Wheel Drive'),
}

class Vehicle(models.Model):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    production_year = models.CharField(validators=[RegexValidator(regex='^.{4}$', message='Year must be 4 digits long', code='nomatch')])
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    power = models.IntegerField(null=True)
    capacity = models.IntegerField(validators=[MinValueValidator(2), MaxValueValidator(8)])
    drive_train = models.CharField(choices=DRIVE_TRAIN_CHOICES)
    description = models.CharField(max_length=3000)
    photo = models.ImageField(upload_to='users_pictures/', default='users_pictures/None/no-img.jpg')




