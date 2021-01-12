# Generated by Django 3.1.3 on 2020-12-16 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0007_remove_cart_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='total',
            field=models.DecimalField(decimal_places=3, default=0.0, max_digits=5),
        ),
    ]