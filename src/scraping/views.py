from django.shortcuts import render
from .models import Vacancy
from .forms import FindForm

def main_navbar(request):

    form = FindForm() #форма для выбора города и сециальности для поиска (scraping/forms.py)

    qs = Vacancy.objects.all() # выведет в таком виде: <QuerySet [<Vacancy: Python developer (FoodTech)>]>

    context = {'title': 'Job Finder',
               'objects_list': qs,
               'form': form}



    return render(request, "main_navbar.html", context)
