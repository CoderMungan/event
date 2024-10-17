from .models import CustomUser
from .serializers import UserSerializer
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated


class UserListApi(ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
