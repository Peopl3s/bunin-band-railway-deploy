# Generated by Django 4.2.2 on 2023-06-28 13:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("news", "0010_alter_news_publish"),
    ]

    operations = [
        migrations.AlterField(
            model_name="news",
            name="publish",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 6, 28, 13, 14, 38, 871184, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]