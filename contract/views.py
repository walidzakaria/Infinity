from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect

from .models import City, Country, Hotel, HotelChain, Season
import datetime
from django.db.models import Q


# Create your views here.
@login_required
def home(request):
    countries = Country.objects.all()
    hotel_chains = HotelChain.objects.all()
    seasons = Season.objects.filter(current_season=True).all()
    today_date = datetime.date.today()
    current_season = Season.objects.filter(
        season_begin__lte=today_date, season_end__gte=today_date, current_season=True).first()

    return render(request, 'contract/index.html',
                  {'countries': countries,
                   'hotel_chains': hotel_chains,
                   'seasons': seasons,
                   'current_season': current_season.season_id})
