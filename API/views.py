from django.contrib.auth.models import User
from rest_framework import viewsets
from .pagination import CustomPagination
from .models import ToDo
from .serializers import ToDoSerializer


class ToDoViewSet(viewsets.ModelViewSet):
    serializer_class = ToDoSerializer
    pagination_class = CustomPagination
    def get_serializer_context(self):
        return {'user_id': self.request.user.id}

    def get_queryset(self):
        user = self.request.user
        user_id = User.objects.only('id').get(id=user.id)
        return ToDo.objects.filter(user_id=user_id)
