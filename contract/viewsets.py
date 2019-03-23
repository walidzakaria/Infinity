import django_filters
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.serializers import ModelSerializer
from django.db.models import Q

from .models import Country, Region, City, Season, Supplier, HotelChain, Team, Hotel
from .serializers import CountrySerializer, RegionSerializer, CitySerializer, SeasonSerializer, SupplierSerializer, \
    HotelChainSerializer, TeamSerializer, HotelSerializer


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    filter_fields = ('country',)


class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    filter_fields = ('country', )


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    filter_fields = ('region', )


class SeasonViewSet(viewsets.ModelViewSet):
    queryset = Season.objects.all()
    serializer_class = SeasonSerializer
    filter_fields = ('current_season', )


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class HotelChainViewSet(viewsets.ModelViewSet):
    queryset = HotelChain.objects.all()
    serializer_class = HotelChainSerializer


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    filter_fields = ('hotel_code', 'hotel', )


# api for searching --> will be for hotel
class HotelSearchList(generics.ListAPIView):
    serializer_class = HotelSerializer

    def get_queryset(self):
        """
        This view should return a list of all hotels by
        the part of code or name passed in the URL
        """
        search_string = self.kwargs['search_string']
        return Hotel.objects.filter(
            Q(hotel_code__icontains=search_string) | Q(hotel__icontains=search_string)
        ).all()
