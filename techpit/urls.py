from django.contrib import admin
from django.urls import path, include #includeを追加

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('financial_　analysis.urls')),
]