Step 2: Select a student from the class
===
- Present ~~dropdown~~ list with student names as radio button labels:
  One student can be selected.
  [Django topic: Querying](https://docs.djangoproject.com/en/3.1/topics/db/queries/)
  `Klasse` and `Assignment` from Model database for filtering the relevant 
  students.
- On `Elev` selection (Action buttom clicked), flow continues to 
  [step 3](./step3.md), "Show selected student's profile in class context".

Data from View to Template
---
A  problem with 
[comparison in template `{% if %}` tag](https://stackoverflow.com/a/64835268/888033)
was solved via Stack Overflow:
Using the `slugify` template filter for the `int` type of 
a Django model's primary key makes it **comparable** with 
the `str` output from a `radio`-typed field returned from client browser's HTML form.

Research in Jupyter Lab
---
The Jupyter notebook interactive environment is used to develop
the data from Django **model** data (providing filtered `AssessmentScore` data)
and **controller** data (providing filtering data from `Klasse`, `Elev`, 
`Aflevering` - and ultimately `Skole`, which is not yeat implemented).
(This is really [Step 3](./step3.md):) The data thus collected are then presented to matlibplot's `pyplot`,
and the produced plot is stored as a *Portable Networks Graphics* file and
retrieved by the [View `elev_aflevering`](boxplot/views.py)

- [Real Python on **understanding Matplotlib**](https://realpython.com/python-matplotlib-guide/)
- On [profiling and code optimization](), 
  [this PDF](https://www.ace-net.ca/wp-content/uploads/2016/07/Python-Profiling-and-Optimizing-Code.pdf)
  and the GitHub free-sample repo for
  [IPython Cookbook](https://ipython-books.github.io/42-profiling-your-code-easily-with-cprofile-and-ipython/)
  looks worth some reading.
- Line magic 
  [function `%timeit`](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-timeit)
  for IPython / Jupyter notebook.

After `git merge`, when succesful testing of the app is documented,
the Jupyter notebook will be removed, and thus only appear in
the historical traces on the repo.

Basically, Jupyter is 
1. *started* with the Django settings by issuing in command line, Django project root dir: 
   ```
   DJANGO_PROJECT="box_whiskers_demo" jupyter notebook
   ```
1. *environment initialized* with executing this notebook cell:
   ```
   from django_for_jupyter import init_django
   init_django()
   ```
   Prerequisite: `django_for_jupyter.py` in Django project root dir.
   
From there, you can access Django files as well as any other Python module.


Test suite
---
1. 