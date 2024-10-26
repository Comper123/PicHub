from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.index),
    path('account/', include('django.contrib.auth.urls')),
    path('register/', views.register, name="register"),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)