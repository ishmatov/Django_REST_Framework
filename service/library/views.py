from django.shortcuts import render
from .models import Author
from rest_framework.viewsets import ModelViewSet
from .serializers import AuthorModelSerializer


class AuthorModelViewSets(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer
