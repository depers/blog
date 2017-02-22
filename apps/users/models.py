# coding=utf-8
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class UserProfile(AbstractUser):
    image = models.ImageField(upload_to='uploads/%Y/%m/%d/', default="image/default.png", max_length=100, verbose_name='头像')

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username