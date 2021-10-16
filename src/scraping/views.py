from django.shortcuts import render
from .models import Vacancy


def main_navbar(request):
    qs = Vacancy.objects.all() # выведет в таком виде: <QuerySet [<Vacancy: Python developer (FoodTech)>]>

    context = {'title': 'Job Finder', 'objects_list': qs}
    return render(request, "main_navbar.html", context)
