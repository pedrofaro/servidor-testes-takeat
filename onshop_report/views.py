# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from datetime import datetime 
import pytz

from onshop_auto.models import ItemPedidoAuto, CompradorPedidoAuto

# Create your views here.
def report(request):

	return render(request, 'onshop_auto/relatorio_de_clientes.html', {})