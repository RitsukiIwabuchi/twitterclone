# Generated by Django 3.1.7 on 2021-09-29 16:30

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('twitterclone', '0003_auto_20210928_0349'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='favorites',
            field=models.ManyToManyField(related_name='favorites', to=settings.AUTH_USER_MODEL),
        ),
    ]
