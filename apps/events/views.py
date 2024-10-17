from rest_framework import generics
from .models import Event
from .serializers import EventSerializer
from django.utils.timezone import now
from datetime import timedelta
from rest_framework.permissions import IsAuthenticated
from django.core.exceptions import PermissionDenied
from django.db import transaction, IntegrityError
from rest_framework.exceptions import ValidationError


class EventListCreate(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        try:
            with transaction.atomic():
                event = serializer.save()
                self.request.user.events.add(event)
        except IntegrityError as e:
            print("Error : ", e)
            raise ValidationError(
                {"detail": "Event could not be created, please try again."}
            )


class EventRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        event = self.get_object()
        try:
            with transaction.atomic():
                if not self.request.user.events.filter(pk=event.id).exists():
                    raise PermissionDenied(
                        "You do not have permission to update this event."
                    )

                serializer.save()
        except IntegrityError as e:
            print("Error : ", e)
            raise ValidationError(
                {"detail": "Event could not be updated, please try again."}
            )

    def perform_destroy(self, instance):

        try:
            with transaction.atomic():
                if not self.request.user.events.filter(pk=instance.id).exists():
                    raise PermissionDenied(
                        "You do not have permission to delete this event."
                    )

                instance.delete()
        except IntegrityError as e:
            print("Error : ", e)
            raise ValidationError(
                {"detail": "Event could not be deleted, please try again."}
            )


class UpcomingEvents(generics.ListAPIView):
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # For the Turkey time added + 3 hour
        today = now() + timedelta(hours=3)
        today_date = today.date()
        today_time = today.time()
        tomorrow = today + timedelta(days=1)
        tomorrow_date = tomorrow.date()

        return Event.objects.filter(
            date=today_date,
            time__gte=today_time,
        ) | Event.objects.filter(date=tomorrow_date, time__lt=today_time)


class CategoryEvents(generics.ListAPIView):
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        category_name = self.kwargs["category"]
        return Event.objects.filter(category=category_name)
