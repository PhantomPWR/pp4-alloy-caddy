"""alloycaddy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from alloylookup import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('countries/', views.get_countries_list, name='get_countries_list'),
    path('primary_footnotes/', views.get_primary_footnotes_list, name='get_primary_footnotes_list'),
    path('secondary_footnotes/', views.get_secondary_footnotes_list, name='get_secondary_footnotes_list'),
    path('subcategories/', views.get_subcategories_list, name='get_subcategories_list'),
    path('categories/', views.get_categories_list, name='get_categories_list'),
    path('alloys/', views.get_alloy_list, name='get_alloy_list'),
    path('alloy_categories/', views.get_alloy_categories_list, name='get_alloy_categories_list'),
    path('', views.get_alloy_list, name='get_alloy_list'),
]
