# Generated by Django 4.2.6 on 2024-03-12 03:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_chat_group_chat_team_delete_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='chat',
        ),
    ]