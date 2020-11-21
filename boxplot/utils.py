"""Utility function get_graph()
and get_elev_aflevering_plot()
Paradigm copied from https://youtu.be/jrT6NiM46jk
"""
# pylint: disable=maybe-no-member
import matplotlib.pyplot as plt
import base64
from io import BytesIO
import pandas as pd
from .models import Aflevering, AssesmentScore, Elev, Klasse # Skole
import pickle

def get_graph():
    """Grabs current plot, converts to PNG and returns base64-utf8-encoded string.
    """
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    del(buffer)
    return graph

def get_elev_aflevering_plot(elev_id, klasse_navn='1test', aflevering='covid'):
    """Creates a boxplot for `klasse_navn` of the assessment scores on assignment,
    `aflevering`, as boxplots overlaid by a dot plot of student `elev`.

    Param

    `elev_id` int Primary key of Django model Elev (unique identifier, from HTML form).

    `klasse_navn` str Exact name of the class 

    `aflevering`  str The assignment is identified `icontains` by the string.
    
    Returns str with base64-encoded PNG graph
    
    Together with function get_graph(), function is very much inspired
    by this PyPlane video tutorial https://youtu.be/jrT6NiM46jk

    TODO in just two years, same teacher may be assigned two classes with the same name.
    A better classifier should be deployed.

    TODO As identical assignments may be given to multiple classes
    and assignments with the same (string in the) title may be given repeatedly for
    several years, the identification using (part of) the title is far from unique.
"""
    elev = Elev.objects.get(pk=elev_id)
    
    plt.switch_backend('AGG')
    plt.figure(figsize=(10,5))

    roster = Elev.objects.filter( klasse = Klasse.objects.get( navn = klasse_navn ))
    pile_assessed = Aflevering.objects.filter( titel__icontains = aflevering )
    scores = AssesmentScore.objects.filter(
        aflevering__in = pile_assessed
    ).filter(
        elev__in = roster 
    )

    # Create DataFrame
    klasse_comprehension = [ass.elev.fulde_navn for ass in scores]
    col_name_list = [f'opg{i}' for i in range(1,7)] # opg1...opg6
    # Append last six fields
    col_name_list += [field.name for field in AssesmentScore._meta.fields][-6:]
    df = pd.DataFrame(
        data   =scores.values(),
        columns=col_name_list,
        index  =klasse_comprehension
    )

    # Conversion avoids TypeError: cannot perform reduce with flexible type
    klasse_data = df.to_numpy()
    # type(df.to_numpy > method > TypeError. Corrected by adding '()'
    plt.boxplot(klasse_data)
    plt.ylabel('Score')
    plt.xlabel('Kriterium')
    plt.boxplot(klasse_data)
    plt.xticks(
        range(1,1+df.shape[1]),
        df.columns.values,
        rotation=45
    )
    plt.yticks([6*i for i in range(1,5)])

    plt.title('sales of items')
    plt.tight_layout()
    cached = False # TODO
    #if not cached:
    #    df, boxplot = box_backdrop( klasse_navn, aflevering )
    #    # function calls pyplot which creates a CURRENT FIGURE object, hence CGF()
    #    pickle.dump( plt.gcf(), open( "current_plot.p", "wb" ) )
    #    pickle.dump( df, open( f"boxplot_klasse{klasse_navn}.p", "wb" ) )
    #    plt.close()
    #else:
    #    with open( f"current_plot.p", "rb" ) as c:
    #            pickle.load( c )
    #    with open( f"boxplot_klasse{klasse_navn}.p", "rb" ) as k:
    #        klasse_scores = pickle.load( k )

    ### Set plot title
    plt.title(elev.fulde_navn+', '+klasse_navn)

    ### Overlay
    ### The row for this student
    ########## local variable 'klasse_scores' referenced before assignment ############
    #elev_score = klasse_scores.loc[elev_navn].to_numpy()
    elev_score = df.loc[elev.fulde_navn].to_numpy()
    ### Plot circled dots, 'o' in color RED, 'r'
    ### Range 1..12 needs to be explicitated (X-values).
    plt.plot(
        #range(1, 1+klasse_scores.shape[1]), 
        range(1, 1+df.shape[1]), 
        elev_score, 
        'or'
    )

    ### Convert matplotlib object and tidy up
    ### Save plot to a temporary buffer.
    #buf = BytesIO()
    #plt.savefig(buf, format="png")
    # Embed the result in the html output.
    #imgdata = base64.b64encode(buf.getbuffer()).decode("ascii")
    #plt.close()
    #del(buf)


    graph = get_graph()
    return graph
