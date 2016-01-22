from __future__ import unicode_literals

from django.db import models


class IceCreamFlavour(models.Model):
    flavour_name = models.CharField(max_length=255)
    your_name = models.CharField(max_length=255)
