from django.db import models
from utils.models import TimeBasedStampModel


class Event(TimeBasedStampModel):
    CATEGORY_CHOICES = [
        ("work", "work"),
        ("personal", "personal"),
        ("health", "health"),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.title
