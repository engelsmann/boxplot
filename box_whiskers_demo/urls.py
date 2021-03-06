"""box_whiskers_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:             from my_app import views
       Alle URL foranstilles "/", så fx "index" har URL:  "/" + '' = '/'
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:               from other_app.views import Home
    2. Add a URL to urlpatterns:    path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:      path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

# Husk der er PROJEKT oprettet med django-admin:    box_plot_demo,
# og så er der APP oprettet med python manage.py:   boxplot.
# Django VIEWS skal hentes fra APP:
from boxplot import views

# 
urlpatterns = [
    path('',                  views.index,           name='index'          ),
    path('elev_aflevering',   views.elev_aflevering, name='elev_aflevering'),
    path('admin/',            admin.site.urls     ),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
