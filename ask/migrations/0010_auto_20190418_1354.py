# Generated by Django 2.0.13 on 2019-04-18 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ask', '0009_auto_20190418_1353'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answer',
            options={'ordering': ['-create_date']},
        ),
    ]
