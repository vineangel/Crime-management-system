# Generated by Django 4.1.5 on 2023-04-09 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0025_alter_complaint_stationn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='stationn',
            field=models.CharField(max_length=100),
        ),
    ]
