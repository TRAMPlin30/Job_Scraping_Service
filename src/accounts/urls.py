from django.urls import path

from accounts.views import login_views, logout_views, register_views

app_name = 'accounts'

urlpatterns = [
    path('login_views', login_views, name = 'login_views'),
    path('logout_views', logout_views, name = 'logout_views'),
    path('register_views', register_views, name = 'register_views'),
]
