# Generated by Django 2.0.13 on 2019-04-18 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ask', '0008_remove_like_answers'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Like',
            new_name='QuestionLike',
        ),
        migrations.AlterField(
            model_name='answer',
            name='title',
            field=models.CharField(max_length=120, verbose_name='Заголовок ответа'),
        ),
    ]