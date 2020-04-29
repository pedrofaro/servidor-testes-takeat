# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.conf import settings
from . import views

app_name = 'onshop_report'

urlpatterns = [
    url(r'^$', views.report, name='report'), #Página de Relatórios Premiums
]