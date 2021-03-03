from django.db import models
from uuid import uuid4
from django.core import validators


class Author(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    birthday_year = models.PositiveIntegerField()
