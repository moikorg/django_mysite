from django.db import models


class SonnenBattery(models.Model):
    consumption = models.SmallIntegerField()
    frequency = models.PositiveSmallIntegerField()
    # gridConsumption:
    #   negativ value = energy consumption from grid
    #   positiv value = energy feed-in to the grid
    gridConsumption = models.SmallIntegerField()
    isSystemInstalled = models.NullBooleanField(blank=True, null=True)
    # pacTotal:
    #   negativ value = battery is charging
    #   postitv value = battery is discharging
    pacTotal = models.SmallIntegerField()
    production = models.SmallIntegerField()
    rsoc = models.SmallIntegerField()   # remain state of charge
    timestamp = models.DateTimeField(db_index=True, )
    usoc = models.SmallIntegerField()
    uAC = models.PositiveSmallIntegerField()
    uBat = models.PositiveSmallIntegerField()

    class Meta:
        ordering = ["-pk"]

    def __str__(self):
        return 'TS: %s, PAC Production: %s, Home cons: %s, Grid cons: %s, PAC cons: %s' % \
               (self.timestamp, self.production, self.consumption, self.gridConsumption, self.pacTotal)
