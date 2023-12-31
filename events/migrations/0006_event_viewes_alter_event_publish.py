# Generated by Django 4.2.2 on 2023-06-28 07:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("viewer", "0001_initial"),
        ("events", "0005_alter_event_publish"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="viewes",
            field=models.ManyToManyField(
                blank=True, related_name="viewes", to="viewer.viewer"
            ),
        ),
        migrations.AlterField(
            model_name="event",
            name="publish",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 6, 28, 7, 30, 25, 334836, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
