# Generated by Django 4.1.5 on 2023-05-05 03:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0041_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='subject',
            new_name='title',
        ),
    ]
