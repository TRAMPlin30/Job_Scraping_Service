
#----------------------------------------------------------------------------------------
    # необходимые зависимости для того что бы можно было работать с функционалом в django - (city = City.objects.filter(slug='kiev'))
    # из файла run_parsers.py, который к самой django никакого отношения не имеет
import os, sys
    # данная строка указывает что файл run_parsers.py нужно искать по абсолютному пути там, где лежит manage.py
path_to_run_parsers_py = os.path.dirname(os.path.abspath('manage.py'))
sys.path.append(path_to_run_parsers_py)
os.environ["DJANGO_SETTINGS_MODULE"] = "a_scraping_service.settings" # строки из документации django
import django
django.setup()
#----------------------------------------------------------------------------------------

from django.db import DatabaseError

import codecs
from parser_djinni_co.djinni import djinni_parser
from parser_dou_ua.dou import dou_parser
from parser_work_ua.work import work_parser
from parser_rabota_ua.rabota import rabota_parser

from scraping.models import Vacancy, City, Specialization


parsers = ((work_parser, 'https://www.work.ua/ru/jobs-kyiv-python/'),
           (dou_parser, 'https://jobs.dou.ua/vacancies/?city=Київ&search=Python'),
           (rabota_parser, 'https://rabota.ua/zapros/python/киев'),
           (djinni_parser, 'https://djinni.co/jobs/location-kyiv/?keywords=Python'))

city = City.objects.filter(slug='kiev').first() # - first() делает из объекта QuerySet объект instance
specialization = Specialization.objects.filter(slug='python').first() # - first() делает из объекта QuerySet объект instance

import time
t = time.time()


jobs = []
errors = []

for func, url in parsers:
    j, e = func(url)
    jobs += j
    errors += e


for job in jobs: # сохраняем вакансии в БД
    v = Vacancy(**job, city=city, specialization=specialization) # раскрываем словарь job
    try:
        v.save()
    except DatabaseError:
        pass

r = int(time.time() - t)
print(f"Время на сбор данных = {r} секунд")
#file = codecs.open('run_parsers.txt', 'w', 'utf-8') #windows-1251 иногда вместо utf-8
#file.write(str(jobs))
#file.close()

# без обработки ошибок (без модели Errors в models.py)

