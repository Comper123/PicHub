# Generated by Django 5.0 on 2024-11-20 15:40

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0031_remove_profile_liked_projects'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200, verbose_name='Текст уведомления')),
                ('date', models.DateTimeField(auto_now=True, verbose_name='Время')),
                ('autor', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'уведомление',
                'verbose_name_plural': 'Уведомления',
            },
        ),
        migrations.AddField(
            model_name='profile',
            name='notifications',
            field=models.ManyToManyField(to='mysite.notification'),
        ),
    ]