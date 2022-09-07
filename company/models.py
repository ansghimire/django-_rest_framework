from django.db import models

class Shareholders(models.Model):
    shareholder_name = models.CharField(max_length=10)
    share_amount = models.PositiveBigIntegerField()


class Document(models.Model):
    document_name = models.CharField(max_length=10)
    document_details = models.CharField(max_length=100)


class Company(models.Model):
    cmp_name = models.CharField(max_length=10)
    cmp_address = models.CharField(max_length=10)
    cmp_info = models.CharField(max_length=10)
    shareholders = models.ManyToManyField(Shareholders)
    




