# Generated by Django 4.2.2 on 2023-06-28 07:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("events", "0006_event_viewes_alter_event_publish"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="publish",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 6, 28, 7, 32, 29, 964200, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
