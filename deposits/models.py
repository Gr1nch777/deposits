from django.db import models

class Deposit(models.Model):

    deposit = models.IntegerField()
    term = models.IntegerField()
    rate = models.FloatField(max_length=10)
    interest = models.FloatField(max_length=10)
