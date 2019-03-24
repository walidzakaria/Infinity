from django.contrib import admin
from .models import Country, Region, City, Season, Supplier, HotelChain, Team, Hotel

# Register your models here.


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('country_id', 'country_code', 'country')
    list_editable = ('country_code', 'country')
    search_fields = ('country_id', 'country_code', 'country')


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('region_id', 'country', 'region_code', 'region')
    list_editable = ('country', 'region_code', 'region')
    search_fields = ('region_id', 'country', 'region_code', 'region')


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('city_id', 'region_id', 'city', 'region')
    list_editable = ('region_id', 'city', 'region')
    search_fields = ('city_id', 'region_id', 'city', 'region')


@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    list_display = ('season_id', 'season_code', 'season', 'season_begin', 'season_end', 'current_season')
    list_editable = ('season_code', 'season', 'season_begin', 'season_end', 'current_season')
    search_fields = ('season_id', 'season_code', 'season', 'season_begin', 'season_end', 'current_season')


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('supplier_id', 'city', 'supplier_code', 'supplier', 'email')
    list_editable = ('city', 'supplier_code', 'supplier', 'email')
    search_fields = ('supplier_id', 'city', 'supplier_code', 'supplier', 'email')


@admin.register(HotelChain)
class HotelChainAdmin(admin.ModelAdmin):
    list_display = ('hotel_chain_id', 'hotel_chain_code', 'hotel_chain')
    list_editable = ('hotel_chain_code', 'hotel_chain')
    search_fields = ('hotel_chain_id', 'hotel_chain_code', 'hotel_chain')


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('team_id', 'team_code', 'team', 'emails')
    list_editable = ('team_code', 'team', 'emails')
    search_fields = ('team_id', 'team_code', 'team', 'emails')


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('hotel_id', 'hotel_code', 'hotel', 'rating_type', 'rating',\
                    'hotel_chain', 'supplier', 'city', 'i5_code', 'gwg_code', 'giata_code',\
                    'team')
    list_editable = ('hotel_code', 'hotel', 'rating_type', 'rating',\
                    'hotel_chain', 'supplier', 'city', 'i5_code', 'gwg_code', 'giata_code',\
                    'team')
    search_fields = ('hotel_id', 'hotel_code', 'hotel', 'rating_type', 'rating',\
                    'hotel_chain', 'supplier', 'city', 'i5_code', 'gwg_code', 'giata_code',\
                    'team')


