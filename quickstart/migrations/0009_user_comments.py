# Generated by Django 3.1.2 on 2021-03-11 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0008_auto_20210312_0020'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Comments',
            fields=[
                ('commnentID', models.IntegerField(primary_key=True, serialize=False)),
                ('userID', models.IntegerField()),
                ('articleID', models.IntegerField()),
                ('content', models.TextField()),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'user_comments',
            },
        ),
    ]
