from django.shortcuts import render
from rest_framework import viewsets
from .models import tasks
from .serializers import tasksSerializer


class tasksView(viewsets.ModelViewSet):
    queryset = tasks.objects.all()
    serializer_class = tasksSerializer
