from django.shortcuts import render
from .models import City, Country
from django.http import JsonResponse
from django.core import serializers


# Create your views here.
def home(request):
    cities = City.objects.all()
    countries = City.objects.all()
    serialized_obj = serializers.serialize('json', [ cities, ])

    #result_list = list(cities)
    return serialized_obj
    return render(request, 'contract/index.html',
                  {'cities': cities, 'countries': countries})
