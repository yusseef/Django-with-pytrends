from django.contrib import admin
from .models import Region, Historical
class RegionAdmin(admin.ModelAdmin):
    list_display = ['geoName', 'miami_heat', 'boston_celtics']

class HistoricalAdmin(admin.ModelAdmin):
    list_display = ['date', 'miami_heat', 'isPartial']

admin.site.register(Region, RegionAdmin)
admin.site.register(Historical, HistoricalAdmin)
# Register your models here.
