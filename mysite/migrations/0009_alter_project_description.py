# Generated by Django 5.0 on 2024-11-03 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0008_comment_like_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(default='', verbose_name='Описание проекта'),
        ),
    ]
