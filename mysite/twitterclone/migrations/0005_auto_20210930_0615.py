# Generated by Django 3.1.7 on 2021-09-29 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitterclone', '0004_tweet_favorites'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
