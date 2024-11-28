# Generated by Django 5.1.3 on 2024-11-27 14:12

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0048_alter_notification_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='userachievements/')),
                ('uploaded_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': 'достижение',
                'verbose_name_plural': 'Достижения',
            },
        ),
        migrations.AddField(
            model_name='profile',
            name='achievements',
            field=models.ManyToManyField(to='mysite.achievement'),
        ),
    ]
