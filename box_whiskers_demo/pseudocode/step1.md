Django application
====
Here, we build a module for a larger dashboard to be used by a teacher
in the feedback dialogue with individual students.
Multiple performance indicators (PI) need to be included,
but in this demo, only the PI of assessment data from 
a single written assignment is included.

Three step overview
---
Within the Django *project* `box_whiskers_demo`, a 
[Django *application*](https://docs.djangoproject.com/en/3.1/intro/tutorial01/#creating-the-polls-app)
with three steps (*View*s, and thus *Templates*) is to be developed.
I'll give the demo app the name `boxplot`.
> `box_whiskers_demo$ python manage.py startapp boxplot `

The `boxplot` demo app will exhibit three pages to the User:
1. **Enter data** to the app:
   (Class, Students, detailed assessment data for one assignment).
   File **upload button** interacts with the User
   (and for convenience, download of valid data set is provided in a hyperlink).
1. For the Class and Assignment given, 
   **select a Student** whose assessment data to display.
   A **dropdown** interacts with the User.
1. Show assessment data for the selected Student.
   Student data (dots)  will be highlighted on a
   backdrop of the whole Class' distribution of assessment data (boxplots).
   This page should interact with the User through a **navigation button** back to Step 2
   or close window.

Possibly the main template may contain **demo**-style links to this GitHub repo
and the like for personal branding of the developers.

### Git interlude
When I Django-created the `boxplot`-application, I realized that my
git repository started one level too deep. 
The `startapp` command had given me the Django project file structure
```
django$ tree box_whiskers_demo/
box_whiskers_demo/
├── boxplot
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── box_whiskers_demo
│   ├── asgi.py
│   ├── __init__.py
│   ├── pseudocode
│   │   ├── step1.md
│   │   ├── step2.md
│   │   └── step3.md
│   ├── __pycache__
│   │   ├── __init__.cpython-38.pyc
│   │   ├── settings.cpython-38.pyc
│   │   └── urls.cpython-38.pyc
│   ├── README.md
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── demo1512.code-workspace
├── manage.py
├── __pycache__
│   └── manage.cpython-38.pyc
└── sketch1603900755770.png

6 directories, 23 files
```
However, my Git repo (and thus GitHub) showed only the files from the 
`box_whiskers_demo/box_whiskers_demo/` downwards.
No `manage.py`, no `sketch1603900755770.png`.
VS Code *Command Palette* `Ctrl+Shift+P`: **Git Close Repository**.
That removed connection to remote GitHub URL, I think, but the command did not
[remove the hidden directory](https://stackoverflow.com/questions/1213430)
`.git`.
To do that I issue `$ rm -rf .git` from the project root directory.
`$ find -name .git` gives med the output `./box_whiskers_demo/.git` so I repeat the `rm` there.

This now results in VS Code displaying a lot of text and two buttons:
- Initialize Repository
- Publish to GitHub

I feel that I am back on track and in the Django project root directory,
`$ find -name .git` gives me no output, indicating that all local repo information is gone.
As requested.

> `$ git init`


Step 1: Data entered into system
---
- Show link to a valid CSV file, the user can download for demo purposes.
- Show button "Grasp CSV file"
- Read CSV file and store it in database
- Show button "Proceed to student selection" ([step 2](./step2.md))

Test suite
---
1. Link to data file properly formed HTML: Anchor, `<a `...`href="`URL`"`...`>`txt`</a>`.
   - [Directive](https://docs.python.org/2.4/lib/doctest-options.html)
     to `doctest`: `+ELLIPSIS`, som tillader `...` i test.
   - Functional test
     (Selenium) actually getting a file?
1. Link to data file points to file
   - URL starts `file://`
1. Link to data file points to file of type CSV
   - URL ends `.csv`
1. Link to data file points to correct file
   - File must be named `sample-class-sample-assignment.csv` 
1. Button to upload file accepts files
   - FORM field type ___
   - Functional test
     (Selenium) Success indicator upon non-failed file upload?
1. (Uploaded file rejected if extension not CSV)
   - Upon attempted upload, ...
   - Functional test
     (Selenium) Failure indicator upon failed file upload?
1. ~~Uploaded file rejected if file encoding not UTF-8~~ (?)
1. Uploaded file rejected if columns count is not 1+1+1+1+6+6=16 (class + student name + 
   asignment deadline + assignment title + 6 excercises + 6 learning objectives)
   - Test `len(col_name_list)==16`
1. Uploaded file rejected if column headers are **not** as tuple of strings (expected col heads)
   - [Convert list of col names to tuple](https://www.geeksforgeeks.org/python-convert-a-list-into-a-tuple/)
     and compare: `tuple(col_name_list)==expedted_col_heads`
1. Uploaded file **accepted** if column headers **are** as tuple of strings (expected col heads)
   - What happens upon acceptance? Look for indicator ...
1. Uploaded file rejected if data in rows does **not** conform to model data types
   - How are CSV data transformed to (NumPy) array / (pandas) DataFrame?
   - How are array columns matched to database columns?
1. Uploaded file accepted if data in rows does conform to model data types
   - What happens upon acceptance? Look for indicator ...
1. Uploaded file rejected if missing data cells
   - [Function `isnan()`](https://numpy.org/doc/stable/reference/generated/numpy.isnan.html)
     deployed ...
1. Uploaded file **accepted** if **no missing** data cells 
   - What happens upon acceptance? Look for indicator ...
   - 
1. All data (multiple rows) for a class of students can be read from database
   - What happens upon success? Look for indicator ...
   - 
1. Data (single row) for a identified student can be read from database
   - What happens upon success? Look for indicator ...
   - 
1. View change on acceptance of data: Button to proceed is shown.
   - Look for button
   - Button should point to next step URL
   - Functional test
     (Selenium)?
