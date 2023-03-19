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
from django.contrib.auth import views as auth_views
from django.urls import path
from accounts import views as accounts_views
from alloylookup import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', accounts_views.account_login, name='account_login'),
    path('logout/', accounts_views.account_logout, name='account_logout'),
    path('', accounts_views.account_login, name='account_login'),
    path('alloys/', views.get_alloy_list, name='get_alloy_list'),
    path('alloy_search/', views.alloy_search, name='alloy_search'),
    path('countries/', views.get_countries_list, name='get_countries_list'),
    path('categories/', views.get_categories_list, name='get_categories_list'),
    path(
        'primary_footnotes/',
        views.get_primary_footnotes_list,
        name='get_primary_footnotes_list'
    ),
    path(
        'secondary_footnotes/',
        views.get_secondary_footnotes_list,
        name='get_secondary_footnotes_list'
    ),
    path(
        'subcategories/',
        views.get_subcategories_list,
        name='get_subcategories_list'
    ),
    path(
        'create_alloy/',
        views.create_alloy,
        name='create_alloy'
    ),
    path(
        'update_alloy/<str:pk>/',
        views.update_alloy,
        name='update_alloy'
    ),
    path(
        'delete-alloy/<str:pk>/',
        views.delete_alloy,
        name='delete_alloy'),
    path(
        'create_category/',
        views.create_category,
        name='create_category'
    ),
    path(
        'update_category/<str:pk>/',
        views.update_category,
        name='update_category'
    ),

]
