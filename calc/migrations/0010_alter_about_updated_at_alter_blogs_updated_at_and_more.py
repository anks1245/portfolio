# Generated by Django 4.0.6 on 2023-02-27 09:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0009_alter_about_about_alter_about_birthday_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='updated_at',
            field=models.TextField(default=datetime.datetime.today),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='updated_at',
            field=models.TextField(default=datetime.datetime.today),
        ),
        migrations.AlterField(
            model_name='education',
            name='updated_at',
            field=models.TextField(default=datetime.datetime.today),
        ),
        migrations.AlterField(
            model_name='experience',
            name='updated_at',
            field=models.TextField(default=datetime.datetime.today),
        ),
        migrations.AlterField(
            model_name='getip',
            name='created_at',
            field=models.TextField(default=datetime.datetime.utcnow),
        ),
        migrations.AlterField(
            model_name='hero',
            name='updated_at',
            field=models.TextField(default=datetime.datetime.today),
        ),
        migrations.AlterField(
            model_name='register',
            name='created_at',
            field=models.TextField(default=datetime.datetime.today),
        ),
    ]