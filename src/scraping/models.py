from django.db import models
from django.template.defaultfilters import slugify


class City(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Наименование города')
    slug = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name='Город'
        verbose_name_plural = 'Города'

    def __str__(self):
        return self.name
#------------------------------------------автоматическое формирование поля slug из поля name-----------------
#поле SlugAutoField - формирует слаги только из латинских букв (так же как и функция slugify(name)
    #def save(self, *args, **kwargs):
        #if not self.slug:
            #self.slug = slugify(self.name)
        #super(City, self).save(*args, **kwargs)
#-------------------------------------------------------------------------------------------------------------
class Specialization(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Наименование специальности')
    slug = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = 'Специальность'
        verbose_name_plural = 'Специальности'

    def __str__(self):
        return self.name

class Vacancy(models.Model):
    url = models.URLField(unique=True)
    title = models.CharField(max_length=250, verbose_name='Заголовок вакансии')
    company =models.CharField(max_length=250, verbose_name='Работодатель')
    description = models.TextField(verbose_name='Описание вакансии')
    city = models.ForeignKey('City', on_delete=models.CASCADE, verbose_name='Город')
    specialization = models.ForeignKey('Specialization', on_delete=models.CASCADE, verbose_name='Специальность')
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата/Время создания записи')

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'

    def __str__(self):
        return self.title

