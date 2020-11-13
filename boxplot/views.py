#from django.http import HttpResponse
from django.shortcuts import render

from .models import Aflevering, Elev

# Create your views here.
def index(request):
    """Landingssiden, som brugeren møder uden andet end domæne (og port).
    Listen over afleveringer skal filtreres for skole og klasse i produktion.
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
            'elev': Elev.objects.all()
        }
        )
