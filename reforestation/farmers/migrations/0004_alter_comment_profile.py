# Generated by Django 4.1.7 on 2023-02-16 05:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('farmers', '0003_remove_comment_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='farmers.profile'),
        ),
    ]
