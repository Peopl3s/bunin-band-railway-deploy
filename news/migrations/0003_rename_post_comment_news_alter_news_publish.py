# Generated by Django 4.2.2 on 2023-06-23 15:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("news", "0002_alter_news_publish"),
    ]

    operations = [
        migrations.RenameField(
            model_name="comment",
            old_name="post",
            new_name="news",
        ),
        migrations.AlterField(
            model_name="news",
            name="publish",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 6, 23, 15, 30, 14, 804898, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]