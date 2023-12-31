# Generated by Django 4.2.2 on 2023-06-28 13:14

import datetime
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("events", "0007_alter_event_publish"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="likes",
            field=models.ManyToManyField(
                related_name="event_likes", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AlterField(
            model_name="event",
            name="publish",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 6, 28, 13, 14, 38, 855567, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
