# Generated by Django 4.2.2 on 2023-06-28 13:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("memebers", "0009_alter_member_publish"),
    ]

    operations = [
        migrations.AlterField(
            model_name="member",
            name="publish",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 6, 28, 13, 24, 11, 778141, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
