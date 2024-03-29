# Generated by Django 4.1.5 on 2023-04-04 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_complaint_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='news',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('newstitle', models.CharField(max_length=100)),
                ('newscontent', models.CharField(max_length=200)),
                ('newsimg', models.ImageField(upload_to='')),
            ],
        ),
        migrations.AlterField(
            model_name='complaint',
            name='status',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='supporting_doc',
            field=models.FileField(upload_to='uploads/'),
        ),
    ]
