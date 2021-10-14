from django.urls import path

from scraping.views import main_navbar

app_name = 'scraping'

urlpatterns = [
    path('', main_navbar, name = 'main_navbar'),


]