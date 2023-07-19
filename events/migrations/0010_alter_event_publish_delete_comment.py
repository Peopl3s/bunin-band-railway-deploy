# Generated by Django 4.2.2 on 2023-07-05 16:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("events", "0009_alter_event_publish"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="publish",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 7, 5, 16, 18, 26, 977032, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.DeleteModel(
            name="Comment",
        ),
    ]
