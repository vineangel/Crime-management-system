# Generated by Django 4.1.5 on 2023-04-09 16:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0020_alter_criminaldetails_criminal_date_of_birth_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='criminaldetails',
            name='criminal_password',
        ),
    ]