# Generated by Django 4.1.7 on 2023-02-15 11:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('farmers', '0002_comment_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
    ]
