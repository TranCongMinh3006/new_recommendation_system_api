# Generated by Django 3.1.2 on 2021-03-17 09:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0028_remove_user_comments_userid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articles',
            old_name='articleID',
            new_name='id',
        ),
    ]
