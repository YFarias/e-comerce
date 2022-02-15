"""
Novo Setup
from django.urls import path, include

path('api/v1/', include('djoser.urls')),
path('api/v1/', include('djoser.urls.authtoken')),
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.authtoken')),
]
