from django.db import models
from datetime import date, datetime

# Does not !?! validate manual inputs 
# (but documentation says form inputs from users are validated)
from django.core.validators import MinValueValidator, MaxValueValidator

# My models here
class Klasse(models.Model):
    """Skoleklasses 'navn', startår, og navn på skolen
    """
    id       = models.AutoField('Nøgle', primary_key=True)
    oprettet = models.DateTimeField('Tid for oprettelse', default=datetime.now)
    skole    = models.CharField('Skolens navn', max_length=70, default="Frederiksborg Gymnasium og HF")
    navn     = models.CharField('Betegnelse', max_length=10, default='1a')
    start_år = models.IntegerField('Startår', default=2019)
    def __str__(self):
        """Klasse (gruppe elever)
        """
        return f"{self.navn} ({self.start_år}), {self.skole}"

class Elev(models.Model):
    """Person. Kun fulde navn registreret.
    Kan ikke skille for- og efternavn.
    """
    id         = models.AutoField('Nøgle', primary_key=True)
    oprettet = models.DateTimeField('Tid for oprettelse', default=datetime.now)
    fulde_navn = models.CharField('Fulde navn', max_length=70)
    # Til hardcoding af FOREIGNKEY:
    # https://stackoverflow.com/a/2846537/888033
    klasse     = models.ForeignKey('Klasse', models.DO_NOTHING)
    
    def __str__(self):
        """Navngiven elev 
        """
        return f"{self.fulde_navn}, {self.klasse}"

class Aflevering(models.Model):
    """Opgaven, der afleveres
    niveau: Hvilket år får klassen denne opgave?
    """
    id       = models.AutoField('Nøgle', primary_key=True)
    oprettet = models.DateTimeField('Tid for oprettelse', default=datetime.now)
    senest   = models.DateTimeField('Seneste ændring', default=datetime.now)
    klasse   = models.ForeignKey('Klasse', models.DO_NOTHING)
    niveau   = models.IntegerField('Klassetrin for aflevering', default=1)
    titel    = models.CharField('Afleveringens titel', max_length=30, default='Model af CoVID19')
    frist    = models.DateField('Afleveringsfrist', default=date(2020, 11, 28))

    def __str__(self):
        """Præsentation af afleveringen
        """
        # pylint: disable=E1101
        # https://stackoverflow.com/a/57019528/888033
        return f"'{self.titel}', {self.klasse.navn} ({self.klasse.start_år}/{self.niveau}) {self.klasse.skole}, senest: {self.frist}"
    def forfalden(self):
        """Returnerer TRUE, hvis afleveringen er over fristen
        """
        return self.frist > date.today()

class AssesmentScores(models.Model):
    """Tabel med aflevering og (for indeværende) 12 score-felter"""
    id         = models.AutoField('Nøgle', primary_key=True)
    oprettet   = models.DateTimeField('Tid for oprettelse', default=datetime.now)
    senest     = models.DateTimeField('Seneste ændring', default=datetime.now)
    aflevering = models.ForeignKey('Aflevering', models.DO_NOTHING)
    elev       = models.ForeignKey('Elev', models.DO_NOTHING)
    
    # Min og Max skal lige prøves af, inden jeg bruger tid på at kode dem for alle 6+6 felter
    # https://docs.djangoproject.com/en/3.1/ref/validators/
    opg1       = models.IntegerField('Opg1', validators=[MinValueValidator(1), MaxValueValidator(4)])
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
    
    @property
    def scores(self):
        """Liste med alle 6+6 scores:
        opg1, opg2, opg3, opg4, opg5, opg6, tankegang, fagsprog, cas, diagram, sammenhæng, konklusion
        """
        return [self.opg1, self.opg2, self.opg3, self.opg4, self.opg5, self.opg6, self.tankegang, self.fagsprog, self.cas, self.diagram, self.sammenhæng, self.konklusion]
    
    def __str__(self):
        """Bedømmelse af en navngiven elev på en bestemt opgave
        """
        # pylint: disable=E1101
        return f"Opgave '{self.aflevering.titel}' fra {self.elev.fulde_navn}: {self.scores}"

# Manual bootstrapping in Django iPython prompt (`python manage.py shell`), see:
# https://docs.djangoproject.com/en/3.1/intro/tutorial02/#playing-with-the-api
# You may want to hit the TAB after having typed
# `from boxplot.models import Klasse, Elev, Aflevering, As`
# (Last class name is automatically extended to `AssertmentScores`)