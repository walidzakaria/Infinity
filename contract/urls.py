from django.conf.urls import url, include
from .routers import router
from .viewsets import HotelSearchList

from .views import home
from .api import show_country, show_regions, show_cities

urlpatterns = [
    url(r'home$', home, name='user_home'),
    url(r'^$', home, name='home_page'),
    url(r'^api/', include(router.urls)),
    url('^hotel/search/(?P<search_string>[\w\+]+)/$', HotelSearchList.as_view()),

]
