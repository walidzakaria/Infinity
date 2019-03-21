from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect

from .models import City, Country, Hotel


# Create your views here.
@login_required
def home(request):
    countries = Country.objects.order_by('country').all()
    return render(request, 'contract/index.html',
                  {'countries': countries})
