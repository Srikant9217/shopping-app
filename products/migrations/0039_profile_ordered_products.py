# Generated by Django 2.2.4 on 2020-05-11 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0038_auto_20200511_0832'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='ordered_products',
            field=models.ManyToManyField(blank=True, related_name='ordered_products', to='products.Product'),
        ),
    ]