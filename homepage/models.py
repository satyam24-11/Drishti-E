from django.db import models

from django.contrib.auth.models import User
class UserDetails(models.Model):
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=50)


class UserDetail(models.Model):
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=50)


class option(models.Model):
    option = models.CharField(max_length=100)


class Details:
    email: str
    password: str


class Compose:
    recipient: str
    subject: str
    body: str
