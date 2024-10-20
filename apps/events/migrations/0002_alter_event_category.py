# Generated by Django 5.1.2 on 2024-10-17 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="category",
            field=models.CharField(
                choices=[
                    ("work", "Work"),
                    ("personal", "Personal"),
                    ("health", "Health"),
                ],
                max_length=50,
            ),
        ),
    ]
