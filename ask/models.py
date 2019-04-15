# coding=utf-8
from __future__ import unicode_literals

from datetime import datetime

import requests
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Usr(AbstractUser):
    upload = models.ImageField(upload_to='images/ask/%Y/%m/%d', verbose_name='Ссылка картинки')
    groups = 123
    user_permissions = 0


class Tag(models.Model):
    title = models.CharField(max_length=120, verbose_name=u"Заголовок ярлыка")

    def __str__(self):
        return self.title


class Profile(models.Model):
    usr = models.OneToOneField(Usr, on_delete=models.CASCADE)


class Question(models.Model):
    author = models.ForeignKey(Usr, on_delete=models.CASCADE)
    title = models.CharField(max_length=120, verbose_name=u"Заголовок вопроса")
    text = models.TextField(verbose_name=u"Полное описание вопроса")

    rating = models.IntegerField(verbose_name="рейтинг", default=0)

    create_date = models.DateTimeField(default=datetime.now, verbose_name=u"Время создания вопроса")

    is_active = models.BooleanField(default=True, verbose_name=u"Доступность вопроса")

    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-create_date']


class Answer(models.Model):
    author = models.ForeignKey(Usr, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.TextField(verbose_name=u"Полное описание ответа")
    create_date = models.DateTimeField(default=datetime.now, verbose_name=u"Время создания ответа")


@receiver(post_save, sender=Question)
def renewal(sender, instance, created, **kwargs):
    if created:
        requests.post("http://localhost:8000/create/message", data={"message": instance.id})


