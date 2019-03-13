from django.contrib import admin
from .models import Country, Region, City, Season, Supplier

# Register your models here.
admin.site.register(Country)
admin.site.register(Region)

admin.site.register(City)
admin.site.register(Season)
admin.site.register(Supplier)
# @admin.register(City)
# class CityAdmin(admin.ModelAdmin):
#    list_display = ('city_id', 'region_id', 'city', 'region')
#    list_editable = ('region',)
