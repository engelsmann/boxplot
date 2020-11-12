#from django.http import HttpResponse
from django.shortcuts import render

from .models import Aflevering

# Create your views here.
def index(request):
    # https://docs.djangoproject.com/en/3.1/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    latest_classes_list = Aflevering.objects.order_by("senest")
    return render(
        request, 
        'boxplot/index.html',
        {'latest_classes_list': latest_classes_list}
        )
