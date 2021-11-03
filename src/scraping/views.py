from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Vacancy
from .forms import FindForm

def main_navbar(request):

    form = FindForm() #форма для выбора города и сециальности для поиска (scraping/forms.py)


#----------------------------------------фильтруем БД по городу или специальности---------------------------------------------------------------
    city = request.GET.get('city')
    specialization = request.GET.get('specialization')

    context = {'city': city, 'specialization': specialization, 'title': 'Job Finder', 'form': form}
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

        paginator = Paginator(qs, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['objects_list']= page_obj


    return render(request, "main_navbar.html", context)
