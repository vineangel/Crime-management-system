# Generated by Django 4.1.5 on 2023-04-11 06:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0027_alter_complaint_stationn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='police_details',
            name='police_birthday',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='police_details',
            name='police_department',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='police_details',
            name='police_email',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='police_details',
            name='police_gender',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='police_details',
            name='police_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='police_details',
            name='police_password',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='police_details',
            name='rank',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='police_details',
            name='stationn',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.station'),
        ),
    ]
