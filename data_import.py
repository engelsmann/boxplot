# coding: utf-8
# Importation done by hand (copied from `$ python manage.py shell`
# iPython sesson  with `%save data_import.py` in the iPython prompt).
import csv
import boxplot.models as bm
# get() assures at most 1 record is returned 
# pylint: disable=no-member
klassen = bm.Klasse.objects.get(navn='1test')

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
   
