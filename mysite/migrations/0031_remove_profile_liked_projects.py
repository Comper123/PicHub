# Generated by Django 5.0 on 2024-11-16 23:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0030_alter_project_likes_delete_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='liked_projects',
        ),
    ]
