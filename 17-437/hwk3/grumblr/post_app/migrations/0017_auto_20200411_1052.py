# Generated by Django 3.0.3 on 2020-04-11 02:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('post_app', '0016_auto_20200410_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpost',
            name='post_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 11, 2, 52, 34, 141646, tzinfo=utc)),
        ),
    ]
