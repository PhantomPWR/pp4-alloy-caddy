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
from alloylookup import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.account_login, name='account_login'),
    path('logout/', views.account_logout, name='account_logout'),
    path('', views.account_login, name='account_login'),
    path('alloys/', views.get_alloy_list, name='get_alloy_list'),
    path('alloy-search/', views.alloy_search, name='alloy_search'),
    path('countries/', views.get_countries_list, name='get_countries_list'),
    path('categories/', views.get_categories_list, name='get_categories_list'),
    path(
        'footnotes/',
        views.get_footnotes_list,
        name='get_footnotes_list'
    ),
    path(
        'subcategories/',
        views.get_subcategories_list,
        name='get_subcategories_list'
    ),
    path(
        'create-alloy/',
        views.create_alloy,
        name='create_alloy'
    ),
    path(
        'update-alloy/<str:pk>/',
        views.update_alloy,
        name='update_alloy'
    ),
    path(
        'delete-alloy/<str:pk>/',
        views.delete_alloy,
        name='delete_alloy'),
    path(
        'create-category/',
        views.create_category,
        name='create_category'
    ),
    path(
        'update-category/<str:pk>/',
        views.update_category,
        name='update_category'
    ),
    path(
        'delete-category/<str:pk>/',
        views.delete_category,
        name='delete_category'),
    path(
        'create-subcategory/',
        views.create_subcategory,
        name='create_subcategory'
    ),
    path(
        'update-subcategory/<str:pk>/',
        views.update_subcategory,
        name='update_subcategory'
    ),
    path(
        'delete-subcategory/<str:pk>/',
        views.delete_subcategory,
        name='delete_subcategory'),
    path(
        'create-country/',
        views.create_country,
        name='create_country'
    ),
    path(
        'update-country/<str:pk>/',
        views.update_country,
        name='update_country'
    ),
    path(
        'delete-country/<str:pk>/',
        views.delete_country,
        name='delete_country'),
    path(
        'create-footnote/',
        views.create_footnote,
        name='create_footnote'
    ),
    path(
        'update-footnote/<str:pk>',
        views.update_footnote,
        name='update_footnote'
    ),
    path(
        'delete-footnote/<str:pk>',
        views.delete_footnote,
        name='delete_footnote'
    ),
    path(
        'register/',
        views.account_register,
        name='account_register'
    ),
    path(
        'reset-password/',
        auth_views.PasswordResetView.as_view(
            template_name='alloylookup/password_reset.html'
        ),
        name='reset_password'
    ),
    path(
        'reset-password-done/',
        auth_views.PasswordResetDoneView.as_view(
            template_name='alloylookup/password_reset_sent.html'
        ),
        name='password_reset_done'
    ),
    path(
        'reset-password-confirm/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='alloylookup/password_reset_confirm.html'
        ),
        name='password_reset_confirm'
    ),
    path(
        'reset-password-complete/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='alloylookup/password_reset_complete.html'
        ),
        name='password_reset_complete'
    ),
]
