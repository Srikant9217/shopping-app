# Generated by Django 2.2.4 on 2020-05-26 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_notification_close'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin',
            name='delivered',
            field=models.BooleanField(default=False),
        ),
    ]
