# Generated by Django 4.1.5 on 2023-03-14 12:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_complaint'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaint',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
