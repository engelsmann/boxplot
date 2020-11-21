`file: box_whiskers_demo/README.md`
# Demo
The Website <http://engelsmann.eu.pythonanywhere.com>
presents boxplot-visualisation of a the performance of 
a selected *student*'s (`Elev`) in a given `Klasse` and
with an *assignment* (`Aflevering`) speficied.

This Django web applikation is meant as one component among several of a
teacher's dashboard to support the feed-back dialogue in a fictional class.
For **demonstration** purposes, this app is already supplied with two classes (Django Model) 
from different scools, each `Klasse` model is related to zero or more students, 
the `Elev` Django model. One *assignments*, Django model `Aflevering` here,
is stored, and a fictional set of `AssessmentScore`s are provided.

The functionality of the demo is thus to select a student from the class 
that happened to submit an assignment and have it assessed by their teacher.
As part of a round-up feedback session of a few minutes with each individual student,
the teacher can generate this performance profile on the task specified.

In a **production** setting, students may *enroll* or leave a *class*.
On an ongoing basis, new *assignments*, Django model `Aflevering` here,
will be given and students will submit their answers.
Individually or working and submitting in groups.

This GitHub *repository* is meant to serve as a component in the demo 
of Morten's Python skills 
(under development after a course on Python and Machine Learning in October 2020).

The code, you find on this *repo*, ~~rund~~ *live*, dynamically, interactively
on PythonAnywere and/or Azure.
For the development of this demo, I have been inspired from a lot of sources,
amongst which the most notable are:

- https://tutorial.djangogirls.org/en/deploy/
- https://help.pythonanywhere.com/pages/IntegratingWithPythonAnywhere/
- [Obey the testing Goat](http://www.obeythetestinggoat.com/book/part1.harry.html)
- The [Joel Test](https://www.joelonsoftware.com/2000/08/09/the-joel-test-12-steps-to-better-code/)
- http://www.django-introduction.com/index.en.html#/

Not to mention numerous StackOverflow answers (and a few of my own questions).

And yes, I am painfully aware that the code and the documentation 
sported on this repository is mixed in a most un-Pythonian, 
not-at-all-productive manner.
A refactoring will be necessary in any case for bringing the demo to production.
Included such a refactoring process will be the integration, using `DocString`s
and generating separately-stored documentation files, **will** be a priority.

During the weeks of producing this demo, the priority was focused on
1. Learning the trade of:
   - Git for version control and GitHub for making the code accessible, 
   - Python calls using script files from command line, 
     iPython and Jupyter Notebook,
   - Visual Studio Code (Integrated Development Environment),
   - Django (one Python web application framework amongst dozens),
   - automated testing with probing code with `unittest` and Django test, 
     web functionality using Selenium, and finally:
   - cloud computing using Azure (setting up account, 
     and installing a publicly accessible Web App).
1. Leaving sufficient traces to be able to go down the same route later,
   that is: to **document the learning path** - and 
   to show off to you, the reader.

## Starting git repo locally
Followed <https://tutorial.djangogirls.org/en/deploy/>, but
[this short guide](https://rogerdudler.github.io/git-guide/)
is also fine. Here is what I did:
1. Installed the
   [`git` source control management package](https://git-scm.com/).
1. Created project `box-whiskers-demo` (root folder and paraphernalia)
   using the `django-admin` tool.
1. Started repo with `git  init` in root folder,
   and created the corresponding `boxplot` repo on GitHub, so that I could 
   checkout with `git clone https://github.io/engelsmann/boxplot.git`.
1. Created `.gitignore` and started to populate it.
   Tried a few stagings, `git add`, followed by  `git commit` in order to see
   how **commit message** works, both in CLI and VSCode.
   In VSCode it is easy to make comment a headline and some more text in further lines below.
   Checked that GitHub was appropriately updated on `git push`,
   and tried to use **commit URL** in GitHub comments, which works convincingly.
1. Created Django project using the `$ python manage.py startproject `.
   Branched Got a little better to use line pointers in comments and issues on GitHub.
1. Develop or correct code, so **unit and functional tests** can be passed.
   In other words: *Simulate* Test-Driven Development.
   (To really make the TDD goat happy, you must code **nothing**
   before you have converted specifications into tests).
1. Upload Git-*commit* til production (PythonAnywhere / Azure). - Maybe
   PythonAnywhere's script 
   [upload.py](https://github.com/pythonanywhere/upload-website/blob/master/upload.py)
   is of avail here?
1. *Push commit*s to GitHub. - Can `git` help production and GitHub communicate?
   Or is it better to use a
   [*deploymment key*](https://docs.github.com/en/free-pro-team@latest/developers/overview/managing-deploy-keys#deploy-keys)?

![Wikimedia: Git operations](https://upload.wikimedia.org/wikipedia/commons/thumb/d/d8/Git_operations.svg/500px-Git_operations.svg.png "Wikimedia: Git operations")

## MVC design model
*Soon to be translated...*

[**Designmønstre**](https://en.wikipedia.org/wiki/Software_design_pattern)
er et område, der i nærværende projekt berøres som 
[*Decorator* i form af `@` i klassedefinitioner](https://realpython.com/primer-on-python-decorators/)
og *Model-View-Controller*.
Der er dog [stemmer](https://djangobook.com/mdj2-django-structure/),
som taler for at Django's designmodel ikke rigtig lever op til MVC - også
[denne blog](https://medium.com/shecodeafrica/understanding-the-mvc-pattern-in-django-edda05b9f43f)
og Django-projektets egen betegnelse
[FAQ](https://docs.djangoproject.com/en/3.1/faq/general/#django-appears-to-be-a-mvc-framework-but-you-call-the-controller-the-view-and-the-view-the-template-how-come-you-don-t-use-the-standard-names).
- **Model**: beskriver 6 opgaver og 6 læringsmål på tværs af
  opgaverne for en given aflevering.
  Henter data fra klassen og for en udpeget elev.
- **View**: visualiserer 6+6 boxplots for afleveringsopgaven 
  i denne klasse **samt** fremhæver den valgte elevs præstation.
  Views *kan* benytte sig af skabeloner, **Templates**.
  Sammensat `matplotlib` med et lag af 6+6 boxplots (fordeling for den samlede klasse)
  og et lag af 6+6 prikker (viser den valgte elev).
- **Controller**: vælger elev fra en given klasse.

![MTV eller MVC?](https://miro.medium.com/max/500/1*pHlF3KufWwX7svv4Mv4Frg.jpeg "https://medium.com/shecodeafrica/understanding-the-mvc-pattern-in-django")

## Oprette projekt lokalt
Udover alt fnidderet her har jeg
[en tredelt pseudokode](box_whiskers_demo/pseudocode/step1.md),
der måske vil afklare min fremgangsmåde.

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

# Django-projekt, Django-app
- Jeg har kaldt **projektet** `box-whiskers-demo`.
  Jeg har oprettet projektet med `django-admin startproject box-whiskers-demo`. 
  Derved oprettes bl.a. filerne `settings.py` og `urls.py`, samt `manage.py` og
  undermappe med samme navn som projektmappen, altså `box-whiskers-demo/box-whiskers-demo`.
  Og her har jeg lagt mapper med statiske filer, `box-whiskers-demo/static`,
  og med skabeloner til app'en, `box-whiskers-demo/templates/boxplot`.
  Det er fra **projektmappen**, at jeg kører `python manage runserver`, ... ` makemigrations` og ... `migrate`, og hvor jeg fedtede lidt rundt med `python manage.py shell`
- Jeg har kaldt **appen** `boxplot`.
  Appen er tilknyttet mine *Models* og mine *Views*.
# Klient-forespørgsel og server-svar i Django
![Request-response-cycle](https://tas-dp-prod-media.s3.amazonaws.com/blog/reqresp.jpg)

[Request response cycle](https://www.technoarchsoftwares.com/blog/django-request-response-cycle/)

# Migrere projektet fra lokal udviklingsserver til produktion i skyen
Jeg overvejer pt to muligheder for at lægge et fungerende lokalt projekt
op i skyen:
- [Azure web app](https://docs.microsoft.com/da-dk/azure/app-service/tutorial-python-postgresql-app?tabs=bash%2Cclone)
- [MS Learn path migrate Webapps to Azure](https://docs.microsoft.com/da-dk/users/msignite2019/collections/nqzt3epm3q3p)
  (som måske kræver PostgreSEQL), eller
- [PythonAywhere.com](PythonAywhere.com)
  som er 