# Generated by Django 2.0.13 on 2019-04-18 09:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ask', '0005_auto_20190418_1204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='answers',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='ask.Answer'),
        ),
        migrations.AlterField(
            model_name='like',
            name='questions',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='ask.Question'),
        ),
    ]
