# Generated by Django 4.2.2 on 2023-06-25 08:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("events", "0003_event_document_alter_event_publish"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="publish",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 6, 25, 8, 49, 34, 29145, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
