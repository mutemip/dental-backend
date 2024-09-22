"""
URL configuration for dentalProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from dentalApp.api.views import get_procedures, get_patients, get_doctors, get_clinics

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('dentalApp.api.urls')),
    path('api/procedures/', get_procedures, name='get_procedures'),
    path('api/patients/', get_patients, name='get_patients'),
    path('api/doctors/', get_doctors, name='get_doctors'),
    path('api/clinics/', get_clinics, name='get_clinics'),
]
