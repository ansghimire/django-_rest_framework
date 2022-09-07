import uuid
from django.db import models


class Address(models.Model):
    uuid = models.UUIDField(unique=True, default=uuid.uuid4)
    city = models.CharField(max_length=50)
    area = models.CharField(max_length=50)


class Profile(models.Model):
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
