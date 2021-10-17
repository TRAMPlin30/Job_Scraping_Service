from django import forms
from scraping.models import City, Specialization


class FindForm(forms.Form):

    city = forms.ModelChoiceField(queryset=City.objects.all(), #заполнит форму выбора списком обэектов из БД
                                  to_field_name="slug", #обратиться к параметру slug у конкретной модели
                                  required=False, #можно оставлять незаполненным
                                  label='Выбирете город для поиска',
                                  empty_label='выбирете город из списка городов ',
                                  widget=forms.Select(attrs={'class': 'любой класс CSS для оформления формы'}))

    specialization = forms.ModelChoiceField(queryset=Specialization.objects.all(), #заполнит форму выбора списком обэектов из БД
                                            to_field_name="slug", #обратиться к параметру slug у конкретной модели
                                            required=False, #можно оставлять незаполненным
                                            label='Выбирете специальность',
                                            empty_label='выбирете специальность из списка ',
                                            widget=forms.Select(attrs={'class': 'любой класс CSS для оформления формы'}))
