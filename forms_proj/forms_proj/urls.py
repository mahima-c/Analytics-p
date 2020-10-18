from django.contrib import admin
from django.urls import path
from infos.views import info_add_views




urlpatterns = [
    path('admin/', admin.site.urls),
    path('',info_add_views,name='main-view'),
]
