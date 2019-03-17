from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView

from .views import home

urlpatterns = [
    url(r'$', home),
    url(r'accounts/login',
        LoginView.as_view(template_name="contract/login_form.html"),
        name="user_login"),
    url(r'logout',
        LogoutView.as_view(),
        name="user_logout")
]
