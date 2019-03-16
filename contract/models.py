from django.contrib.auth.models import User
from django.db import models


# Create your models here.
RATING_TYPE_CHOICE = (
    ('F', 'FTI Rating'),
    ('O', 'Official Rating')
)

RATING_CHOICE = (
    ('5+', '*****+'),
    ('5', '*****'),
    ('4+', '****+'),
    ('4', '****'),
    ('3+', '***+'),
    ('3', '***'),
    ('2+', '**+'),
    ('2', '**'),
    ('1+', '*+'),
    ('1', '*')
)

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
    city_code = models.CharField(max_length=10, null=True)
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
    email = models.EmailField(max_length=80, default='', null=True)


class HotelChain(models.Model):
    hotel_chain_id = models.AutoField(primary_key=True)
    hotel_chain_code = models.CharField(max_length=10)
    hotel_chain = models.CharField(max_length=50)


class Team(models.Model):
    team_id = models.AutoField(primary_key=True)
    team_code = models.CharField(max_length=10, null=True, default=True)
    team = models.CharField(max_length=50)
    emails = models.CharField(max_length=200, default='', null=True)


class Hotel(models.Model):
    hotel_id = models.BigAutoField(primary_key=True)
    hotel_code = models.CharField(max_length=10)
    hotel = models.CharField(max_length=100)
    rating_type = models.CharField(max_length=1, default='F', choices=RATING_TYPE_CHOICE)
    rating = models.CharField(max_length=2, choices=RATING_CHOICE)
    hotel_chain = models.ForeignKey(HotelChain, on_delete=models.CASCADE, null=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True)
    i5_code = models.CharField(max_length=10, default='', null=True)
    gwg_code = models.CharField(max_length=10, default='', null=True)
    giata_code = models.CharField(max_length=10, default='', null=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True)

