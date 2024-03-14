from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.db import models
from utils.choices import BloodGroup


class User(AbstractUser):

    first_name = models.CharField(max_length=31, null=True, default=None, blank=True)
    last_name = models.CharField(max_length=31, null=True, default=None, blank=True)

    image = models.ImageField(upload_to='images/profile/', null=True,
                              default=None, blank=True)
    phone_number = models.CharField(max_length=7, null=True,
                                    default=None, blank=True)
    height = models.FloatField(null=True, default=None, blank=True)
    weight = models.FloatField(null=True, default=None, blank=True)
    blood_gr = models.CharField(max_length=4, choices=BloodGroup.choices,
                                default=None, null=True, blank=True)
    age = models.IntegerField(blank=True, null=True)


