# Generated by Django 2.0.13 on 2019-04-18 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ask', '0004_auto_20190418_1157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='title',
            field=models.CharField(default='default', max_length=120, verbose_name='Заголовок ответа'),
        ),
    ]