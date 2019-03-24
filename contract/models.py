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
    country_code = models.CharField(max_length=2, unique=True)
    country = models.CharField(max_length=50, db_index=True)

    class Meta:
        verbose_name_plural = "countries"
        ordering = ('country',)

    def __str__(self):
        return self.country


class Region(models.Model):
    region_id = models.AutoField(primary_key=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    region_code = models.CharField(max_length=3, unique=True)
    region = models.CharField(max_length=50, db_index=True)

    class Meta:
        ordering = ('region',)

    def __str__(self):
        return self.region


class City(models.Model):
    city_id = models.AutoField(primary_key=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    city = models.CharField(max_length=50, db_index=True)

    class Meta:
        verbose_name_plural = "cities"
        ordering = ('city',)

    def __str__(self):
        return self.city


class Season(models.Model):
    season_id = models.AutoField(primary_key=True)
    season_code = models.CharField(max_length=4, db_index=True, unique=True)
    season = models.CharField(max_length=20, unique=True)
    season_begin = models.DateField()
    season_end = models.DateField()
    current_season = models.BooleanField(default=True)

    def __str__(self):
        return self.season_code


class Supplier(models.Model):
    supplier_id = models.AutoField(primary_key=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    supplier_code = models.CharField(max_length=10, unique=True)
    supplier = models.CharField(max_length=50, db_index=True)
    email = models.EmailField(max_length=80, default='', null=True)

    class Meta:
        ordering = ('supplier',)

    def __str__(self):
        return self.supplier


class HotelChain(models.Model):
    hotel_chain_id = models.AutoField(primary_key=True)
    hotel_chain_code = models.CharField(max_length=10, unique=True)
    hotel_chain = models.CharField(max_length=50, db_index=True)

    class Meta:
        ordering = ('hotel_chain',)

    def __str__(self):
        return self.hotel_chain


class Team(models.Model):
    team_id = models.AutoField(primary_key=True)
    team_code = models.CharField(max_length=10, null=True, default=True, unique=True)
    team = models.CharField(max_length=50, db_index=True)
    emails = models.CharField(max_length=200, default='', null=True)

    class Meta:
        ordering = ('team',)

    def __str__(self):
        return self.team


class Hotel(models.Model):
    hotel_id = models.BigAutoField(primary_key=True)
    hotel_code = models.CharField(max_length=10, db_index=True, unique=True)
    hotel = models.CharField(max_length=100, db_index=True)
    rating_type = models.CharField(max_length=1, default='F', choices=RATING_TYPE_CHOICE)
    rating = models.CharField(max_length=2, choices=RATING_CHOICE)
    hotel_chain = models.ForeignKey(HotelChain, on_delete=models.CASCADE, null=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True)
    i5_code = models.CharField(max_length=10, default='', null=True, db_index=True)
    gwg_code = models.CharField(max_length=10, default='', null=True, db_index=True)
    giata_code = models.CharField(max_length=10, default='', null=True, db_index=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ('hotel',)

    def __str__(self):
        return f'{self.hotel_code}; {self.hotel}'
