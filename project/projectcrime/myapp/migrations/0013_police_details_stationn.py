# Generated by Django 4.1.5 on 2023-03-14 09:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_station'),
    ]

    operations = [
        migrations.AddField(
            model_name='police_details',
            name='stationn',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='myapp.station'),
            preserve_default=False,
        ),
    ]
