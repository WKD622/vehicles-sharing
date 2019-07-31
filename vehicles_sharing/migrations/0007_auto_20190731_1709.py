# Generated by Django 2.2.1 on 2019-07-31 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles_sharing', '0006_merge_20190724_0141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='drive_train',
            field=models.CharField(choices=[('RWD', 'Rear Wheel Drive'), ('FWD', 'Front Wheel Drive'), ('AWD', 'All Wheel Drive')], max_length=4),
        ),
    ]