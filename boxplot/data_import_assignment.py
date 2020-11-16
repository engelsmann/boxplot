# coding: utf-8

# This file is to record the importation done by hand 
# (copied from `$ python manage.py shell` iPython sesson  
# with `%save data_import.py` in the iPython prompt).
import csv
import boxplot.models as bm
# get() assures at most 1 record is returned 
# pylint: disable=no-member
klassen = bm.Klasse.objects.get(navn='1test')
klassen.id
# 3

with open("/home/morten/Dropbox/Python/bedom/quiz1.csv") as quiz:
    quiz = csv.reader(quiz)
    i = 0
    for linje in quiz:
        # First line, i=0, header
        if i:
            # Put student in class '1test', leftmost column is full name
            elev = bm.Elev(fulde_navn=linje[0], klasse_id=klassen.id)
            # Store in Django database
            elev.save()
        i += 1
   
len(bm.Elev.objects.all())
# 25

## Getting data from Google Analysis (preprocessed)
import pandas as pd
df = pd.read_csv("/home/morten/Dropbox/Mat-ungdomsudd/stx/FG 2020/2f/f Ma - Aflever.9 (processkriv) COVID afsluttes/cov-11x51-2f.csv")
df.shape
# (11, 52)

# Der er 11 afleveringer (11 brugere) i den importerede pandas DataFrame. 
# Og det er altså ikke hele klassen... 
# Jeg må tilbage til  R  og få proppet de resterende elever ind i datasættene,
# `google_shit`  listen. 
#
# Ved granskning kommer jeg frem til, at det lave antal hovedsagelig skyldes samaflevering. 
# De elleve (11) bedømmelser, som ligger i datasættet er altså bedømmelser af samtlige 
# de besvarelser, der skal være for klassen.
# 
# Til demo-brug kan jeg så `cycle` de foreliggende besvarelser og
# dermed simulere samarbejde ??
#Nej from itertools import cycle
#Nej df_cycle = cycle(df)
# Men måske?
def ass_gen(df=df):
    """Generator yielding pandas Series of AssessmentScores
    i a cyclic manner.
    Why do I need to put the limit of 100 elements?
    I thought YIELD would only produce the NEEDED elements,
    but with no limit, the generator continues indefinitely..."""
    count = 1
    tmp = 0
    while tmp<100:
        tmp += 1
        # Row from DataFrame to yield
        ass = df.iloc[count,:]
        if count >= len(df.index)-1:
            # Reset counting, from the beginning
            count = 0
        else:
            # Continue counting
            count += 1
        yield ass
compreh = [a for a in ass_gen()]

# Pick all students from class '1test'
# Note that 'Elev.klasse' i a ForeignKey, as is 'Klasse.navn'.
# And 'Klasse.id' is the referred-to primary key.
flok = bm.Elev.objects.filter( klasse = bm.Klasse.objects.get(navn='1test').id )
# Distribute df row to each of the students in flok QuerySet
# Store as  AssessmentScore  Django Model entries (but first print)
aflev = bm.Aflevering.objects.get(titel__icontains='covid')
aflev

i = 0
for e in flok:
    a = compreh[i]
    a.Brugernavn = e.id
    i += 1
    
i = 0
# Iterate over the QuerySet of students (from Django model "Elev")
for e in flok:
    a = compreh[i]
    # Anonymize
    a.Brugernavn = e.id
    i += 1

    # Make Dictionary with keyword arguments
    kwargs = dict( elev = bm.Elev.objects.get(id=a.Brugernavn ),  aflevering = aflev )
    # Expand Dictionary
    # Django Model field     Column from CSV, DataFrame
    kwargs['opg1']       =   a['opg.1']
    kwargs['opg2']       =   a['opg.2']
    kwargs['opg3']       =   a['opg.3']
    kwargs['opg4']       =   a['opg.4']
    kwargs['opg5']       =   a['opg.5']
    kwargs['opg6']       =   a['opg.6']
    kwargs['tankegang']  =   a['tankegang']
    kwargs['fagsprog']   =   a['fagsprog']
    kwargs['cas']        =   a['cas']
    kwargs['diagram']    =   a['diagram']
    kwargs['sammenhæng'] =   a['sammenhng']
    kwargs['konklusion'] =   a['konklusion']

    # Unpack Dictionary with  **  operator
    # https://python-reference.readthedocs.io/en/latest/docs/operators/dict_unpack.html
    a_score = bm.AssesmentScore(**kwargs)
    print(a_score)
