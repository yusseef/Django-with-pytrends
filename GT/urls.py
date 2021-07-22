
from django.contrib import admin
from django.urls import path
from trends.views import list_regions, list_historical, show_data, show_data2
urlpatterns = [
    path('admin/', admin.site.urls),
    path('region/', list_regions),
    path('historical/', list_historical),
    path('', show_data),
    path('regions/', show_data2),
]

