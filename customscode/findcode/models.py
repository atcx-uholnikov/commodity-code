from django.db import models

class Goods(models.Model):
    code = models.CharField(max_length=10, blank=False)
    description = models.TextField(blank=False)
    source = models.CharField(max_length=50, blank=False)
    date = models.CharField(max_length=10, blank=False)

    def __str__(self):
        return f"{self.code} : {self.description} ({self.source})"

class DuesRate(models.Model):
    code = models.CharField(max_length=10, blank=False)
    duty_preferential = models.CharField(max_length=15, blank=False)
    duty_full = models.CharField(max_length=15, blank=False)
    additional_measuring_units = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.code} : преференційна {self.duty_preferential} %, повна {self.duty_full} %"
