# Generated by Django 4.1.5 on 2023-04-14 14:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0029_alter_complaint_stationn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='stationn',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.station'),
        ),
    ]
