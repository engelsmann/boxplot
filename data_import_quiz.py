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

# Pick all students from class '1test'
# Note that 'Elev.klasse' i a ForeignKey, as is 'Klasse.navn'.
# And 'Klasse.id' is the referred-to primary key.
flok = bm.Elev.objects.filter( klasse = bm.Klasse.objects.get(navn='1test').id )
