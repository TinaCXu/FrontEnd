# Generated by Django 3.0.3 on 2020-04-05 02:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post_app', '0005_auto_20200404_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpost',
            name='post',
            field=models.TextField(blank=True, default="What's new today? Share with Grumbler!", max_length=42, null=True),
        ),
        migrations.AlterField(
            model_name='userpost',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]