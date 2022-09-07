from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=50)
    age = models.CharField(max_length=10)

class PersonDetail(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
    address = models.CharField(max_length=50)