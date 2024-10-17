from .models import Event
from django.utils.timezone import now


# def delete_past_events():
#     current_time = now()
#     past_events = Event.objects.filter(date__lt=current_time.date())
#     deleted_count, _ = past_events.delete()
#     if deleted_count > 0:
#         print(f"{deleted_count} past events deleted.")
