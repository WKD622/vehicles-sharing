# Generated by Django 2.2 on 2019-04-07 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles_sharing', '0005_auto_20190407_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='drive_train',
            field=models.CharField(choices=[('FWD', 'Front Wheel Drive'), ('AWD', 'All Wheel Drive'), ('RWD', 'Rear Wheel Drive')], max_length=4),
        ),
    ]
