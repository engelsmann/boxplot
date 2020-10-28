# Demo
Websitet <http://engelsmann.eu.pythonanywhere.com>
præsenterer boxplot-visualisering af en elevs præstation set
på bagtæppet af elevens klasses samlede præstationer.
Applikationen er ment som en blandt flere komponenter i lærerens feed-back
til elever i en fiktiv klasse:
Bedømmelse af en fiktiv opgave med klassens samlede fordeling 
af præstationer for hvert kriterium samt den valgte elevs præstation.

Dette *repository* skal tjene som en komponent i den demo for Morten's Python-færdigheder,
som er under udvikling efter et kursus i september og oktober 2020 om Python og Machine Learning.
Den kode, du finder i dette *repo*, ~~kører~~ *live*, dynamisk, interaktivt 
på PythonAnywere.
Til udviklingen har jeg især hentet inspiration på følgende sider:

- https://tutorial.djangogirls.org/en/deploy/
- https://help.pythonanywhere.com/pages/IntegratingWithPythonAnywhere/
- http://www.obeythetestinggoat.com/book/part1.harry.htmlr

## Starte git repo lokalt
Følger <https://tutorial.djangogirls.org/en/deploy/>:
1. Installér 
   [versionsstyring-programpakken `git`](https://git-scm.com/)
   (*source control management*).
1. Opret rod-bibliotek `box-whiskers-demo` for projektet.
1. Start `git` repo i rod-biblioteket.
1. Opret `.gitignore`.
1. Opret projekt ud fra Django.  Opret tests. 
1. Tilret kode, så tests passeres. *Commit* projekt lokalt med Git.
1. Upload Git-*commit* til PythonAnywhere. - Kan PythonAnywhere's script 
   [upload.py](https://github.com/pythonanywhere/upload-website/blob/master/upload.py)
   bruges her?
1. Upload *commitment* til GitHub. - Kan `git` noget her?
   Eller er det bedre at gå omkring en
   [udbringningsnøgle / *deploymment key*](https://docs.github.com/en/free-pro-team@latest/developers/overview/managing-deploy-keys#deploy-keys)?

![Wikimedia: Git operations](https://upload.wikimedia.org/wikipedia/commons/thumb/d/d8/Git_operations.svg/500px-Git_operations.svg.png "Wikimedia: Git operations")

## MVC-designmodel
[**Designmønstre**](https://en.wikipedia.org/wiki/Software_design_pattern)
er et område, der i nærværende projekt berøres som 
[*Decorator* i form af `@` i klassedefinitioner](https://realpython.com/primer-on-python-decorators/)
og *Model-View-Controller*.
Der er dog [stemmer](https://djangobook.com/mdj2-django-structure/),
som taler for at Django's designmodel ikke rigtig lever op til MVC - også
[denne blog](https://medium.com/shecodeafrica/understanding-the-mvc-pattern-in-django-edda05b9f43f)
og Django-projektets egen
[FAQ](https://docs.djangoproject.com/en/3.1/faq/general/#django-appears-to-be-a-mvc-framework-but-you-call-the-controller-the-view-and-the-view-the-template-how-come-you-don-t-use-the-standard-names).
- **Model**: beskriver 6 opgaver og 6 læringsmål på tværs af
  opgaverne for en given aflevering.
  Henter data fra klassen og for en udpeget elev.
- **View**: visualiserer 6+6 boxplots for afleveringsopgaven 
  i denne klasse **samt** fremhæver den valgte elevs præstation.
  Views *kan* benytte sig af skabeloner, **Templates**.
  Sammensat `matplotlib` med et lag af boxplots (fordeling for den samlede klasse)
  og et lag af prikker (viser den valgte elev).
- **Controller**: vælger elev fra en given klasse.

![MTV eller MVC?](https://miro.medium.com/max/500/1*pHlF3KufWwX7svv4Mv4Frg.jpeg "https://medium.com/shecodeafrica/understanding-the-mvc-pattern-in-django")

## Oprette projekt lokalt
1. Start **projekt**: `$ django-admin startproject mortens-demo-app`, 
   som indrammer webapplikationen.
1. Start projektets **første app** `$ python manage.py startapp box-whiskers`, 
   der vil kunne bruges i andre Django-projekter, 
   fx når en **elev-rettet overbliksside** skal udvikles.
   Django-apps er 
   [*pluggable*](https://docs.djangoproject.com/en/3.1/intro/tutorial01/#creating-the-polls-app).
   Overblikssiden tænkes udarbejdet for et forløb med et givent undervisningsemne,
   fx differentialregning eller analytisk geometri,
   der dækker mere end bare den her viste skriftlige aflevering,
   men også testresultater og lærerens løbende observationer af
   faglige præstationer og adfærd i timerne.
   Overblikssiden vil derfor blive en **mosaik af apps**,
   som kan udvikles og afprøves en ad gangen - og efterfølgende
   tilrettes enkeltvis efter behov.
   Det ses, at den **Controller**, som bruges i nærværende boxplot-app, 
   vil kunne overføres uforandret til hele overblikssiden - der skal stadig vælges en elev -
   mens **Model**-komponenten af hver **app** dækker de øvrige data: quiz-app, adfærds-app, 
   [SOLO-progressions-app](https://trello.com/b/gJnFeRt6/solo-i-forl%C3%B8b)...
1. Opret app med Django (bemærk at jeg her skelner 
   mellem *projekt* og *applikation*, for sådan 
   [skelner Django](https://docs.djangoproject.com/en/3.0/ref/applications/#projects-and-applications)):
   1. View, Template: Visning af netsiderne til udvælgelse af elev fra klassen og 
      til visning af lærerens bedømmelse af eleven.
   1. Controller: Validerer brugerens valg og filterer data herudfra.
   1. Model, `sqlite3` databasestruktur: Tabeller, kolonner, datatyper.
1. [Test](https://wiki.python.org/moin/PythonTestingToolsTaxonomy)
   af projektet i form af:
   1. Enhedstest. Kræver [test-ramme](https://realpython.com/python-testing/), fx 
      [`doctest`](https://docs.python.org/3/library/doctest.html)
      eller `unittest2`.
   1. Funktionelle test. 
      Kræver browserautomatisering med 
     [`Selenium`](http://www.testingit.dk/testautomatisering/selenium/) 
     og `geckodriver`.
1. Gennemføre test lokalt (i udviklingsmiljøet: hovedsageligt enhedstest) 
   og - når lokal test OK - remote 
   (i produktionsmiljøet: hovedsageligt funktionelle test). 