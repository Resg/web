# coding=utf-8
from __future__ import unicode_literals
from datetime import datetime
import requests
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import factory
import factory.django


class ModelManager(models.Manager):

    def new(self):
        return self.order_by('-create_date')

    def hot(self):
        return self.order_by('-rating')


class Usr(AbstractUser):
    upload = models.ImageField(upload_to='images/ask/%Y/%m/%d', blank=True,  verbose_name='Ссылка картинки')
    groups = 123
    user_permissions = 0


class Tag(models.Model):
    title = models.CharField(max_length=120, verbose_name=u"Заголовок ярлыка")
    objects = ModelManager()

    def __str__(self):
        return self.title


class Question(models.Model):
    author = models.ForeignKey(Usr, on_delete=models.CASCADE)
    title = models.CharField(max_length=120, verbose_name=u"Заголовок вопроса")
    text = models.TextField(verbose_name=u"Полное описание вопроса")

    rating = models.IntegerField(verbose_name="рейтинг", default=0)

    create_date = models.DateTimeField(default=datetime.now, verbose_name=u"Время создания вопроса")

    is_active = models.BooleanField(default=True, verbose_name=u"Доступность вопроса")

    tags = models.ManyToManyField(Tag, blank=True)
    objects = ModelManager()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-create_date']


class QuestionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Question

    title = factory.Faker('title')
    text = factory.Faker('text')


class Answer(models.Model):
    author = models.ForeignKey(Usr, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    title = models.CharField(max_length=120, verbose_name=u"Заголовок ответа")
    text = models.TextField(verbose_name=u"Полное описание ответа")
    rating = models.IntegerField(verbose_name="рейтинг", default=0)
    create_date = models.DateTimeField(default=datetime.now, verbose_name=u"Время создания ответа")
    objects = ModelManager()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-create_date']


class QuestionLike(models.Model):
    is_active = models.BooleanField(default=False, verbose_name=u"активност лайка")
    user = models.ForeignKey(Usr, on_delete=models.CASCADE, default=False)
    questions = models.ForeignKey(Question, on_delete=models.CASCADE)


class AnswerLike(models.Model):
    is_active = models.BooleanField(default=False, verbose_name=u"активност лайка")
    user = models.ForeignKey(Usr, on_delete=models.CASCADE, default=False)
    answers = models.ForeignKey(Answer, on_delete=models.CASCADE)


@receiver(post_save, sender=Question)
def renewal(sender, instance, created, **kwargs):
    if created:
        requests.post("http://localhost:8000/create/message", data={"message": instance.id})


