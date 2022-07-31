from ast import keyword
from datetime import date, datetime
from pyexpat import model
from turtle import title
from unicodedata import name
from django.db import models


# Create your models here.

class Register(models.Model):
    name = models.CharField(max_length=55)
    img = models.ImageField(upload_to='uploads')
    email = models.EmailField(max_length=100)
    dob = models.CharField(max_length=15)
    password =  models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=datetime.today)

class GetIP(models.Model):
    ip_address = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    browser = models.CharField(max_length=255)
    device = models.CharField(max_length=255)
    device_type = models.CharField(max_length=255)
    visited_at = models.CharField(max_length=255,null=True)
    created_at = models.DateTimeField(default=datetime.today)

class About(models.Model):
    specialization = models.CharField(max_length=255,default='')
    about = models.TextField(max_length=255,default='')
    birthday = models.DateField()
    degree = models.CharField(max_length=100,default='')
    experience = models.CharField(max_length=55,default='')
    phone = models.CharField(max_length=255,default='')
    github = models.CharField(max_length=255,default='')
    linkedin = models.CharField(max_length=255,default='')
    updated_at = models.DateTimeField(default=datetime.today)


class Education(models.Model):
    degree = models.CharField(max_length=255)
    university = models.CharField(max_length=255)
    start_year = models.CharField(max_length=6)
    end_year = models.CharField(max_length=6)
    desp = models.CharField(max_length=255)
    updated_at = models.DateTimeField(default=datetime.today)


class Experience(models.Model):
    role = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    start_year = models.CharField(max_length=6)
    end_year = models.CharField(max_length=6)
    desp = models.CharField(max_length=255)
    updated_at = models.DateTimeField(default=datetime.today)


class Blogs(models.Model):
    title = models.CharField(max_length=255)
    short_desp = models.CharField(max_length=255)
    tags = models.CharField(max_length=255)
    keyword = models.CharField(max_length=255)
    img = models.ImageField(upload_to='blog_img')
    body = models.CharField(max_length=255)
    author = models.CharField(max_length=55)
    updated_at = models.DateTimeField(default=datetime.today)

class Hero(models.Model):
    title = models.CharField(max_length=55)
    specialization = models.CharField(max_length=255)
    hero_img = models.ImageField(upload_to='uploads')
    cv_file = models.FileField(upload_to='info')
    embedded_link = models.CharField(max_length=255)
    updated_at = models.DateTimeField(default=datetime.today)





