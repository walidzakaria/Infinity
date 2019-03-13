from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Country(models.Model):

    country_id = models.AutoField(primary_key=True)
    country_code = models.CharField(max_length=2)
    country = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "countries"


class Region(models.Model):
    region_id = models.AutoField(primary_key=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    region_code = models.CharField(max_length=3)
    region = models.CharField(max_length=50)


class City(models.Model):
    city_id = models.AutoField(primary_key=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    city_code = models.CharField(max_length=10)
    city = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "cities"


class Season(models.Model):
    season_id = models.AutoField(primary_key=True)
    season_code = models.CharField(max_length=4)
    season = models.CharField(max_length=20)
    season_begin = models.DateField()
    season_end = models.DateField()


class Supplier(models.Model):
    supplier_id = models.AutoField(primary_key=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    supplier_code = models.CharField(max_length=10)
    supplier = models.CharField(max_length=50)
