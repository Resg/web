# Generated by Django 2.0.13 on 2019-04-15 20:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ask', '0004_auto_20190415_2013'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='rating',
            field=models.IntegerField(default=0, verbose_name='рейтинг'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ask.Question'),
        ),
    ]
