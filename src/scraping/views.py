from django.shortcuts import render
from .models import Vacancy
from .forms import FindForm

def main_navbar(request):

    form = FindForm() #форма для выбора города и сециальности для поиска (scraping/forms.py)


#----------------------------------------фильтруем БД по городу или специальности---------------------------------------------------------------
    city = request.GET.get('city')
    specialization = request.GET.get('specialization')
    qs = []
    if city or specialization:
        _filter = {} #словарь заполняем ниже
        if city:
            #словарь    #ключ   #значение
            _filter['city__slug'] = city       #чтобы обратиться к городу по его слагу или имени необходимо двойное подчеркивание
        if specialization:
            #словарь             # ключ       #значение
            _filter['specialization__slug'] = specialization
# ----------------------------------------фильтруем БД по городу или специальности---------------------------------------------------------------


        qs = Vacancy.objects.filter(**_filter) # две звездочки - разворачиваем словарь (раскрываем) присваивая объектам класса Vacancy значения из словаря фильтруя их по этим же значениям

    context = {'title': 'Job Finder',
               'objects_list': qs,
               'form': form}


    return render(request, "main_navbar.html", context)
