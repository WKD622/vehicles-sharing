# Generated by Django 2.2.3 on 2019-07-02 19:52

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles_sharing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='drive_train',
            field=models.CharField(choices=[('AWD', 'All Wheel Drive'), ('FWD', 'Front Wheel Drive'), ('RWD', 'Rear Wheel Drive')], max_length=4),
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('photo_id', models.AutoField(primary_key=True, serialize=False)),
                ('photo', models.FileField(max_length=255, null=True, upload_to='')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photo', to='vehicles_sharing.Vehicle')),
            ],
        ),
    ]