from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView, \
    PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView, PasswordChangeView, PasswordChangeDoneView


urlpatterns = [
    url(r'accounts/login/',
        LoginView.as_view(template_name='accounts/login_form.html'),
        name='user_login'),
    url(r'accounts/logout/',
        LogoutView.as_view(),
        name='user_logout'),
    url(r'accounts/password-reset/$',
        PasswordResetView.as_view(template_name='accounts/password_reset_form.html'),
        name='password_reset'),
    url(r'accounts/password-reset/done/$',
        PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'),
        name='password_reset_done'),
    url(r'accounts/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Zz]{1,13}-[0-9A-Zz-z]{1,20})/$',
        PasswordResetConfirmView.as_view(template_name='accounts/password_reset_complete.html'),
        name='password_reset_confirm'),
    url(r'accounts/reset/done/',
        PasswordResetCompleteView.as_view(template_name='accounts/password_reset_done.html'),
        name='password_reset_complete'),
    url(r'accounts/password-change/$',
        PasswordChangeView.as_view(template_name='accounts/password_change_form.html'),
        name='password_change'),
    url(r'password-change/done/$',
        PasswordChangeDoneView.as_view(template_name='accounts/password_change_done.html'),
        name='password_change_done'),
]
