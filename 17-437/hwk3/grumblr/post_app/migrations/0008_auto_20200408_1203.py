# Generated by Django 3.0.3 on 2020-04-08 04:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('post_app', '0007_auto_20200408_1118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpost',
            name='post_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 8, 4, 3, 56, 322613, tzinfo=utc)),
        ),
    ]
