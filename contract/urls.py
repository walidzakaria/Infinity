from django.conf.urls import url, include
from .routers import router

from .views import home
from .api import show_country, show_regions, show_cities

urlpatterns = [
    url(r'home$', home, name='user_home'),
    url(r'^$', home, name='home_page'),
    #url(r'^api/country/$', show_country, name='show_country'),
    #url(r'^api/region/(?P<country_id>\d+)/$', show_regions, name='show_regions'),
    #url(r'^api/city/(?P<region_id>\d+)/$', show_cities, name='show_cities'),
    url(r'^api/', include(router.urls))
]
