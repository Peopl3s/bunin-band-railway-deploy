# Generated by Django 4.2.2 on 2023-07-11 02:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("memebers", "0011_remove_member_memebers_me_surname_90ad26_idx_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="member",
            name="publish",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 7, 11, 2, 55, 3, 937946, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
