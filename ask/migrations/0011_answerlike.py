# Generated by Django 2.0.13 on 2019-04-18 10:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ask', '0010_auto_20190418_1354'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnswerLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=False, verbose_name='активност лайка')),
                ('answers', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='ask.Answer')),
                ('user', models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='ask.Usr')),
            ],
        ),
    ]
