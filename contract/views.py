from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect

from .models import City, Country, Hotel


# Create your views here.
@login_required
def home(request):
    cities = City.objects.all()
    countries = City.objects.all()
    #serialized_obj = serializers.serialize('json', [ cities, ])

    #result_list = list(cities)
    #return serialized_obj

    hotels = Hotel.objects.all()

    return render(request, 'contract/index.html',
                  {'cities': cities, 'countries': countries, 'hotels': hotels}
                  )

#@csrf_protect
#@never_cache
#def login(request, template_name='contract/login.html')
