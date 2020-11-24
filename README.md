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
   - Python programming 
     1. using (importing) builtin libraries,
     1. own functions and classes (OOP),
     1. design patterns
     1. document code, access formal documentation and other sources of info
        regarding the functioning of Python code
   - Python calls using various Python environments:
     1. script files from command line, 
     1. iPython and
     1. Jupyter Notebook,
   - Visual Studio Code (Integrated Development Environment),
     - Editor,
     - Linting and integrated documentation,
     - Debugging.
   - Django (one Python *web application framework* amongst dozens),
   - Automate testing with Selenium, Python's `unittest` and Django `test`:
     1. [Strategy](https://docs.djangoproject.com/en/3.1/intro/tutorial05/#basic-testing-strategies)
        for test design, not limited to listening to
        [the goat](https://www.obeythetestinggoat.com/book/part1.harry.html)
        > Tests [...] focus light on the part that has gone wrong - even if 
        you hadn’t even realized it had gone wrong.

        quoted from [Django's tutorial, 5](https://docs.djangoproject.com/en/3.1/intro/tutorial05/#tests-don-t-just-identify-problems-they-prevent-them).
        - In 
          [TestDriven Development](https://en.wikipedia.org/wiki/Test-driven_development), 
          TDD, **tests are written before code** both as a means of expressing
          specifications to the developer, and to fence the developer's attention
          on the problem specified in order to save development resources.
        - BDD, or 
          [Behaviour-Driven Development](https://www.agilealliance.org/glossary/bdd/)
          goes a step beyond by formulating **user stories**, 
          and the goat book encourages that too.
          Subsequently, the user stories are reformulated as tests, 
          and the TDD process can start.
     1. Setting up code with `unittest` (and Django test).
        Note the subtle psychology of 
        ```
        self.fail('Finish the test!')
        ```
        used in the 
        [Goat-book, ch 2](https://www.obeythetestinggoat.com/book/chapter_02_unittest.html)
        example employing both Selenium and `unittest`: 
        For as long a test fails - and this one will until the `.fail()` is 
        commented out/removed - the developer is required to improve the code 
        (or/and the test).
     1. Testing the web app's **functionality** using Selenium's 
        [WebDriver](https://www.selenium.dev/documentation/en/webdriver/).
     1. Yet to come: 
        [Django test](https://docs.djangoproject.com/en/3.1/topics/testing/tools/), 
        specified in the *app* directory's `test.py` script.
        The 
        ```
        $ python manage.py test
        ```
     
     And, finally:
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

### Version control, test and release
As of October 2020, a *very* basic - *but executable* - version of a web app
is running in my development environment.
From this `main` version, the `test_suite_1` is forked and
the intention is that the latter be merged back 
into `main` upon satisfactory testing.
When writing these words, towards the end of November 2020,
I feel the branch coming very close to being merged back.

## MVC design model
[**Design patterns**](https://en.wikipedia.org/wiki/Software_design_pattern)
are relevant in the shape of
[*Decorator* - prepending `@` to class methods](https://realpython.com/primer-on-python-decorators/)
and as *Model-View-Controller*.
Django challenges the "classical" MVC pattern,
[however](https://djangobook.com/mdj2-django-structure/),
one advocate hereof is
[this blog](https://medium.com/shecodeafrica/understanding-the-mvc-pattern-in-django-edda05b9f43f)
and as a matter of fact, the Django project's own
[FAQ](https://docs.djangoproject.com/en/3.1/faq/general/#django-appears-to-be-a-mvc-framework-but-you-call-the-controller-the-view-and-the-view-the-template-how-come-you-don-t-use-the-standard-names).

In the case of this demo,
- **Model**: For a school *class*, `Klasse`,  
  teacher's *assessment score* `AssessmentScore` data for 
  a named *student*'s (`Elev`) work on a given *assignment*, `Aflevering`,
  are all stored in a database.
- **View** (Django: *Template*): The databse is then queried,
  the dataset visualized as 6+6 boxplots **overlaid** with 
  the performance data of the named student.
  Computationally, `matplotlib` handles drawing its plots in a
  [multithreaded](https://en.wikipedia.org/wiki/Thread_(computing)#Multithreading) 
  fashion, which posed problems until I ran across 
  [this PyPlane blog](https://youtu.be/jrT6NiM46jk).
- **Controller**, which in Django would be the landing page, or `index` *View*:
  Select the (class, assignment and) student.
  However, for demo purposes class and assignment are *pre-selected*.

![MTV or MVC?](https://miro.medium.com/max/500/1*pHlF3KufWwX7svv4Mv4Frg.jpeg "https://medium.com/shecodeafrica/understanding-the-mvc-pattern-in-django")

## Oprette projekt lokalt
Apart from all the buzz in this README, I describe the program execution in
[three steps of pseudocode](box_whiskers_demo/pseudocode/step1.md),
which hopefully will clarify my approach.
This pseudocode is converted to Python code (see #3 in this list):

1. Initialize **project** with the command line from the **empty** project root directory
   ```
   $ django-admin startproject box-whiskers-demo
   ```
   This creates a directory tree within root.
1. Staying in the root, set up the project's **first app** 
   ```
   $ python manage.py startapp boxplot
   ```
   This will be the demo. But it is intended to be used over again in
   a **dashboard** focusing on the student selected.
   Django-apps are 
   [*pluggable*](https://docs.djangoproject.com/en/3.1/intro/tutorial01/#creating-the-polls-app).
   The dashboard is foreseen to become a **mosaic of apps** displaying
   various aspects of behaviour/assessment relating to the student in focus,
   each app may be
   [specified](https://suebehaviouraldesign.com/what-is-behavioural-design/ "Behavioural Design"),
   coded to pass tests and deployed.
   The MVC **Controller** used in the demo's boxplot-app - in Django terms: the index *View* -
   will transfer rather directly to the production version of the dashboard project.
   Each app will have its specific **Model**-component:
   - quiz-app (subject do/list comprehension) 
     will have a number of right/wrong answers,
   - behavioural observations-app (seek help, assist, academic formulation, problem solving), 
     will hold the teacher's scores (between 1 and 4) of the selected dimensions.
   - a time line of the student's
     [SOLO performance](https://youtu.be/3mzz_o0F6FY?t=103 "YouTube pres by PhysEd teacher Jo Bailey"): 
     1. Type (Definition, Description, Group, Sequence, Compare & Contrast,
     Cause & Effect, Evaluate or Predict).
     1. Date (lead time from beginning of subject course = learning curve steepness).
     1. SOLO level of the activity: Self assessed, teacher assessed.

   I have jotted down notes on how to structure a dialogue with the students on their
   [SOLO progression](https://trello.com/b/gJnFeRt6/solo-i-forl%C3%B8b).
1. Implement app in Django (note the disctinction between
   *project* and *applikation* - for
   [inside Django they make this distinction](https://docs.djangoproject.com/en/3.0/ref/applications/#projects-and-applications)) and in general Python:
   1. Model, `sqlite3` databasestruktur: Tabeller, kolonner, datatyper.
      In Azure, I might need to migrate from SQLite.
   1. Controller: Validate choice of the user and filter data based hereupon.
   1. View, Template: show list of student names and display a **performance plot**
      to support the
      [feedback](https://www.eva.dk/ungdomsuddannelse/feedback-gymnasiet)
      dialogue between teacher and student 
      ([formative](https://www.edutopia.org/blog/providing-feedback-as-formative-assessment-troy-hicks)).

   Presently, a development version is compiling and running locally on my machine.
   The Jupyter Notebook with Django used to experiment my way into 
   plotting the  boxplot with overlay and embedding the PNG,
   are not needed anymore and thus deleted. 
   That means the notebook only resides on the repository up to 
   the commmit `Ready for testing` of mid-November 2020. 
   It is deleted from the "live" code t that point in time.
1. Set up [tests](https://wiki.python.org/moin/PythonTestingToolsTaxonomy)
   to assert validity of project code and functionality:
   1. **Unit tests** using a 
      [framework for testing](https://realpython.com/python-testing/), 
      such as 
      [`doctest`](https://docs.python.org/3/library/doctest.html)
      or `unittest2`.
   1. **Functional tests**
      using browser automation with 
     [`Selenium`](http://www.testingit.dk/testautomatisering/selenium/) 
     and `geckodriver`.
     The [script file](./functional_tests.py) has a "story" of comments,
     outlining what actions to do and what to expect from these actions.
   
   Well, in order to really 
   [Obey the testing goat](https://www.obeythetestinggoat.com/book/part1.harry.html),
   one should formulate the tests beforehand and **then** code,
   because then you are not so tempted to run down blind alleys - "all you need" 
   is to *code to pass the test*.
   This time around, however, I ask for your forgiveness as I am learning
   to code Python, and a bunch of other stuff, while crawling along.
   I find myself on a rather steep learning curve.
   I opted to turn the goat around, as I found formulating tests beforehand
   too hard for my poor little brains in this learning situation.
1. Carry out the tests - develop code and refactor as needed.
   I have two options: 
   [Django "official" tutorial part 5](https://docs.djangoproject.com/en/3.1/intro/tutorial05/),
   and the O'Reilly book
   [Obey the testing goat](https://www.obeythetestinggoat.com/book/part1.harry.html).
   When ass tests are passed, **merge version branch** `test_suite_1` with `main`.
   Unit and functional tests in **development environment**. 
   Functional tests in **production environment**.

# Django-projekt, Django-app
*To be translated*:
- Jeg har kaldt **projektet** `box-whiskers-demo`.
  Jeg har oprettet projektet med 
  ```
  django-admin startproject box-whiskers-demo
  ```
  Derved oprettes bl.a. filerne `settings.py` og `urls.py`, samt `manage.py` og
  undermappe med samme navn som projektmappen, altså `box-whiskers-demo/box-whiskers-demo`.
  Og her har jeg lagt mapper med statiske filer, `box-whiskers-demo/static`,
  og med skabeloner til app'en, `box-whiskers-demo/templates/boxplot`.
  Det er fra **projektmappen**, at jeg kører 
    ```
    python manage runserver
   ```
   ... ` makemigrations` og ... `migrate`, og hvor jeg fedtede lidt rundt med
   ```
   python manage.py shell
  ```
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