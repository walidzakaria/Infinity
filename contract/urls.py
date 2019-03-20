from django.conf.urls import url

from .views import home

urlpatterns = [
    url(r'home$', home, name='user_home'),
    url(r'^$', home, name='home_page')
]
