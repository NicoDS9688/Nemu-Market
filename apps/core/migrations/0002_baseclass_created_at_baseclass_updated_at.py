# Generated by Django 4.2.5 on 2023-10-05 20:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="baseclass",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True,
                default=datetime.datetime(2023, 10, 5, 17, 55, 17, 860019),
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="baseclass",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
