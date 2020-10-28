from django.db import models

# Create your models here.
class Klasse(models.Model):
    """Skoleklasses 'navn', startår, og navn på skolen
    """
    id = models.AutoField(primary_key=True)
    skole = models.CharField(max_length=70, default="Frederiksborg Gymnasium og HF")
    navn = models.CharField(max_length=10, default='1a')
    start_år = models.IntegerField(default=2019)
class Elev(models.Model):
    """Person. Kun fulde navn registreret.
    Kan ikke skille for- og efternavn.
    """
    id = models.AutoField(primary_key=True)
    klasse = models.ForeignKey(to=Klasse, to_field=id)
    fulde_navn = models.CharField(max_length=70)
class Aflevering(models.Model):
    """Opgaven, der afleveres
    niveau: Hvilket år får klassen denne opgave?
    """
    id = models.AutoField(primary_key=True)
    klasse = models.ForeignKey(to=Klasse, to_field=id)
    niveau = models.IntegerField(default=1)
    titel = models.CharField(max_length=30, default='Model af CoVID19')
    frist = models.DateField(default=date(2020, 11, 28))
class AssesmentScores(models.Model):
    """Tabel med aflevering og (for indeværende) 12 score-felter"""
    id = models.AutoField(primary_key=True)
    aflevering = models.ForeignKey(to=Aflevering, to_field=id)
    aflevering = models.ForeignKey(to=Elev, to_field=navn)
    opg1 = models.IntegerField()
    opg2 = models.IntegerField()
    opg3 = models.IntegerField()
    opg4 = models.IntegerField()
    opg5 = models.IntegerField()
    opg6 = models.IntegerField()
    tankegang = models.IntegerField()
    fagsprog  = models.IntegerField()
    cas = models.IntegerField()
    diagram = models.IntegerField()
    sammenhæng = models.IntegerField()
    konklusion = models.IntegerField()

# Bootstrapping