# Generated by Django 4.1.5 on 2023-03-14 11:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_police_details_stationn'),
    ]

    operations = [
        migrations.CreateModel(
            name='complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complaint_title', models.CharField(max_length=100)),
                ('complaint_details', models.CharField(max_length=100)),
                ('suspect', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('supporting_doc', models.ImageField(upload_to='')),
                ('address', models.CharField(max_length=100)),
                ('stationn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.station')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.user_details')),
            ],
        ),
    ]