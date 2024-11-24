# Generated by Django 5.0 on 2024-11-20 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0045_notification_is_check'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_check_notification',
            field=models.BooleanField(default=True, verbose_name='Чтение комментариев'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Время'),
        ),
    ]