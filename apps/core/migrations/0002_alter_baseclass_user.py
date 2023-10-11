# Generated by Django 4.2.5 on 2023-10-11 18:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="baseclass",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="publication",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]