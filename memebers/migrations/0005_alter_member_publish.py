# Generated by Django 4.2.2 on 2023-06-25 08:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("memebers", "0004_alter_member_publish"),
    ]

    operations = [
        migrations.AlterField(
            model_name="member",
            name="publish",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 6, 25, 8, 49, 34, 29145, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
