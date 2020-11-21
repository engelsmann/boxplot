# pylint: disable=maybe-no-member
### Django
#from django.http import HttpResponse
from django.shortcuts import render

### Project internals
from .models import Aflevering, AssesmentScore, Elev, Klasse # Skole
from boxplot.utils import get_elev_aflevering_plot

### General Python 
from matplotlib import pyplot as plt
### https://matplotlib.org/3.1.0/faq/howto_faq.html#matplotlib-in-a-web-application-server
from matplotlib.figure import Figure

import pickle
from io import BytesIO
import base64


### Create your views here.
def index(request):
    """Landingsside, som brugeren møder uden andet end domæne (og port).
    Listen over afleveringer skal filtreres for (TODO: skole og) klasse i produktion.
    Casting af QuerySet til liste
    https://docs.djangoproject.com/en/3.1/ref/models/querysets/#django.db.models.query.QuerySet.order_by

    Returnerer HttpRequest (via django.shortcuts.render) med skabelon og afleveringsliste sat.
    """
    seneste_afleveringer = list(Aflevering.objects.order_by("senest"))
    # STOP-index is length of list but no higher than 5:
    stop = len(seneste_afleveringer) if 6 < len(seneste_afleveringer) else 5
    # Select up to 5 AFLEVERING instances, i.e. the STOP top-most items in the list:
    seneste_afleveringer =  seneste_afleveringer[:stop]
    
    # Return HttpRequest using shortcut
    return render(
        request, 
        # Template, relative path
        'boxplot/index.html',
        # Context
        {
            # QuerySet fra model castet til liste:
            'seneste_aflevering_list': seneste_afleveringer,
            'elev': Elev.objects.all() # TODO filter for user's=teacher's school
        }
        )

def elev_aflevering(request):
    """Provided the requested data and the requested student.

    Returns a call to populate the template.
    """
    # https://stackoverflow.com/a/30035489/888033
    elev_id = int( request.POST['elev'] )
    elev = Elev.objects.get( pk = elev_id )
    return render(
        request,
        "boxplot/elev_aflevering.html",
        context = {
            'chart'     : get_elev_aflevering_plot( elev_id, '1test', 'covid' ), ##boxplot.utils.
            'elev_navn' : elev.fulde_navn if elev.fulde_navn else "Øh",
            'aflevering': 'covid'
            } 
    )
