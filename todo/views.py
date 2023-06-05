from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from .permissions import IsAuthorOrReadOnly
from .models import Todo
from .serializers import TodoSerializer


class TodoList(generics.ListCreateAPIView):
    permission_classes = [IsAuthorOrReadOnly,]
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthorOrReadOnly,]
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer