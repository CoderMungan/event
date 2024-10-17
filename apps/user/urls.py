from django.urls import path
from .views import UserListApi


urlpatterns = [
    path("list/", UserListApi.as_view(), name="users"),
]
