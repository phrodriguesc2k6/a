from django.contrib import admin
from Car.models import Car
from Car.models import Brand

class adminBrand(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(Brand, adminBrand)

class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value', 'photo')
    search_fields = ('model',)

admin.site.register(Car, CarAdmin)


