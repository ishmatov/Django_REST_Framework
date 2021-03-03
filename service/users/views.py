from django.shortcuts import render
from .models import User
from rest_framework.viewsets import ModelViewSet
from .serializers import UserModelSerializer


class UserModelViewSets(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
