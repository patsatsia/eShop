# Generated by Django 3.1.3 on 2020-12-03 08:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('category', '0012_auto_20201202_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='created_by',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='created_by', to=settings.AUTH_USER_MODEL),
        ),
    ]