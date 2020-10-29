from django.db import models
from datetime import date

# My models here
class Klasse(models.Model):
    """Skoleklasses 'navn', startår, og navn på skolen
    """
    id       = models.AutoField('Nøgle', primary_key=True)
    skole    = models.CharField('Skolens navn', max_length=70, default="Frederiksborg Gymnasium og HF")
    navn     = models.CharField('Betegnelse', max_length=10, default='1a')
    start_år = models.IntegerField('Startår', default=2019)

class Elev(models.Model):
    """Person. Kun fulde navn registreret.
    Kan ikke skille for- og efternavn.
    """
    id         = models.AutoField('Nøgle', primary_key=True)
    klasse     = models.ForeignKey(Klasse, models.DO_NOTHING)
    fulde_navn = models.CharField('Fulde navn', max_length=70)

class Aflevering(models.Model):
    """Opgaven, der afleveres
    niveau: Hvilket år får klassen denne opgave?
    """
    id     = models.AutoField('Nøgle', primary_key=True)
    klasse = models.ForeignKey(Klasse, models.DO_NOTHING)
    niveau = models.IntegerField('Klassetrin for aflevering', default=1)
    titel  = models.CharField('Afleveringens titel', max_length=30, default='Model af CoVID19')
    frist  = models.DateField('Afleveringsfrist', default=date(2020, 11, 28))

class AssesmentScores(models.Model):
    """Tabel med aflevering og (for indeværende) 12 score-felter"""
    id = models.AutoField('Nøgle', primary_key=True)
    aflevering = models.ForeignKey(Aflevering,models.DO_NOTHING)
    elev       = models.ForeignKey(Elev,models.DO_NOTHING)
    opg1       = models.IntegerField('Opg1')
    opg2       = models.IntegerField('Opg2')
    opg3       = models.IntegerField('Opg3')
    opg4       = models.IntegerField('Opg4')
    opg5       = models.IntegerField('Opg5')
    opg6       = models.IntegerField('Opg6')
    tankegang  = models.IntegerField('Tankegang')
    fagsprog   = models.IntegerField('Fagsprog')
    cas        = models.IntegerField('CAS-brug')
    diagram    = models.IntegerField('Grafer')
    sammenhæng = models.IntegerField('Sammenhæng')
    konklusion = models.IntegerField('Konklusion')

# Django-opfølgning
# - Dette modul ()= denne fil) tilføjes listen INSTALLED_APPS (fil: projekt-mappe/settings.py)
#   ??? Men er modulets navn er så 'django.contrib.models' eller 'boxplot.models' ???
# Bootstrapping