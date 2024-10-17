from django.urls import path
from .views import (
    EventListCreate,
    EventRetrieveUpdateDelete,
    UpcomingEvents,
    CategoryEvents,
)

urlpatterns = [
    path("", EventListCreate.as_view(), name="event-list-create"),
    path("<int:pk>/", EventRetrieveUpdateDelete.as_view(), name="event-detail"),
    path("upcoming/", UpcomingEvents.as_view(), name="upcoming-events"),
    path(
        "category/<str:category>/",
        CategoryEvents.as_view(),
        name="category-events",
    ),
]
