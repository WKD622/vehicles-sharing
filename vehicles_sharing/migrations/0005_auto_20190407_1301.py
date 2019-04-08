# Generated by Django 2.2 on 2019-04-07 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles_sharing', '0004_auto_20190407_1245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='drive_train',
            field=models.CharField(choices=[('AWD', 'All Wheel Drive'), ('RWD', 'Rear Wheel Drive'), ('FWD', 'Front Wheel Drive')], max_length=4),
        ),
    ]