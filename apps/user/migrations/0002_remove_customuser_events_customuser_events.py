# Generated by Django 5.1.2 on 2024-10-17 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0003_alter_event_category"),
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customuser",
            name="events",
        ),
        migrations.AddField(
            model_name="customuser",
            name="events",
            field=models.ManyToManyField(blank=True, null=True, to="events.event"),
        ),
    ]
