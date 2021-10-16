from django.contrib import admin

from scraping.models import City, Specialization, Vacancy

#admin.site.register(City)
#admin.site.register(Specialization)

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug',)
    fields = ('name', 'slug',)
    ordering = ('name',)
    search_fields = ('name',)

@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug',)
    fields = ('name', 'slug',)
    ordering = ('name',)
    search_fields = ('name',)

@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'company', 'city', 'specialization', 'description',)
    fields = ('title', 'url', 'company', 'city', 'specialization', 'description',)
    ordering = ('city',)
    search_fields = ('city',)