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
    usoc = models.SmallIntegerField()
    uAC = models.PositiveSmallIntegerField()
    uBat = models.PositiveSmallIntegerField()

    def __str__(self):
        return 'TS: %s, Consumption %s' % (self.timestamp, self.consumption)