
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.utils import json

from .models import Country, Region, City


@login_required
def show_country(request):
    countries = Country.objects.all().values('country_id', 'country')
    result = list(countries)

    return JsonResponse(result, safe=False)


@login_required
def show_regions(request, country_id):
    selected_country = Country.objects.get(country_id=country_id)
    if selected_country:
        regions = Region.objects.filter(country=selected_country).all().values('region_id', 'region')
        result = list(regions)
    else:
        result = {'region_id': 0, 'region': 'null'}

    return JsonResponse(result, safe=False)


@login_required
def show_cities(request, region_id):
    selected_region = Region.objects.get(region_id=region_id)
    if selected_region:
        cities = City.objects.filter(region=selected_region).all().values('city_id', 'city')
        result = list(cities)
    else:
        result = {'city_id': 0, 'city': 'null'}

    return JsonResponse(result, safe=False)
