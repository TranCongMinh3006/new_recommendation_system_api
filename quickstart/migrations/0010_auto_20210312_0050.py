# Generated by Django 3.1.2 on 2021-03-11 17:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0009_user_comments'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_comments',
            old_name='commnentID',
            new_name='commentID',
        ),
    ]
