# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SonnenBattery',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('consumption', models.SmallIntegerField()),
                ('frequency', models.PositiveSmallIntegerField()),
                ('gridConsumption', models.SmallIntegerField()),
                ('isSystemInstalled', models.BooleanField()),
                ('pacTotal', models.SmallIntegerField()),
                ('production', models.SmallIntegerField()),
                ('rsoc', models.SmallIntegerField()),
                ('timestamp', models.DateTimeField(db_index=True)),
                ('ts', models.IntegerField()),
                ('usoc', models.SmallIntegerField()),
                ('uAC', models.PositiveSmallIntegerField()),
                ('uBat', models.PositiveSmallIntegerField()),
            ],
        ),
    ]
