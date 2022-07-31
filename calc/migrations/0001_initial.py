# Generated by Django 4.0.6 on 2022-07-20 03:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('img', models.ImageField(upload_to='uploads')),
                ('email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(default=datetime.datetime.today)),
            ],
        ),
    ]
