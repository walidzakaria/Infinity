from rest_framework import serializers
from .models import Country, Region, City, Season, Supplier, HotelChain, Team, Hotel
from django_filters import rest_framework as filters


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
        fields = '__all__'


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'


class HotelChainSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelChain
        fields = '__all__'


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ('hotel_id', 'hotel_code', 'hotel')


class HotelDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'
