from django.db import models
from django.core.validators import EmailValidator, RegexValidator, MinValueValidator, MaxValueValidator

DRIVE_TRAIN_CHOICES = {
    ('RWD', 'Rear Wheel Drive'),
    ('FWD', 'Front Wheel Drive'),
    ('AWD', 'All Wheel Drive'),
}


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=50)
    mail = models.CharField(validators=[EmailValidator], max_length=100)


class Vehicle(models.Model):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    owner_id = models.ForeignKey(User, on_delete=models.CASCADE)
    production_year = models.CharField(
        validators=[RegexValidator(regex='^.{4}$', message='Year must be 4 digits long', code='nomatch')],
        max_length=4)
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    power = models.IntegerField(null=True)
    capacity = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(8)])
    drive_train = models.CharField(choices=DRIVE_TRAIN_CHOICES, max_length=4)
    description = models.CharField(max_length=10000)


class Reservation(models.Model):
    owner_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner_id')
    client_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='client_id')
    car_id = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='car_id')
    start_date = models.DateField()
    end_date = models.DateField()
    active = models.BooleanField(default=False)
    message = models.CharField(max_length=3000)
