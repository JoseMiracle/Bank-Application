from django.db import models

# Create your models here.


class Banks(models.Model):
    bank_name = models.CharField(max_length=100, null=False, blank=False)
