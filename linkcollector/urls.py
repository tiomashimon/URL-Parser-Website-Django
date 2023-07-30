from django.contrib import admin
from django.urls import path
from collector import views as collector_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', collector_views.scrape, name='home'),
    path('delete/', collector_views.clear, name='delete'),
]
