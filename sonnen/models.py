from django.db import models

class SonnenBattery(models.Model):
    consumption = models.SmallIntegerField()
    frequency = models.PositiveSmallIntegerField()
    gridConsumption = models.SmallIntegerField()
    isSystemInstalled = models.BooleanField()
    pacTotal = models.SmallIntegerField()
    production = models.SmallIntegerField()
    rsoc = models.SmallIntegerField()
    timestamp = models.DateTimeField(db_index=True, )
    ts = models.IntegerField()
    usoc = models.SmallIntegerField()
    uAC = models.PositiveSmallIntegerField()
    uBat = models.PositiveSmallIntegerField()
