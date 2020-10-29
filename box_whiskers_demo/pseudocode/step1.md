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

Step 1: Data entered into system
---
- Show link to a valid CSV file, the user can download for demo purposes.
- Show button "Grasp CSV file"
- Read CSV file and store it in database
- Database in Django are [`model.py`](../../boxplot/models.py). Models are declared as 
- Show button "Proceed to student selection" ([step 2](./step2.md))

`django/box_whiskers_demo$ python manage.py runserver` gives me a neat 
Django [landing page](http:::127.0.0.1:8000), and from here, I continue tracking the 
[Django tutorial](https://docs.djangoproject.com/en/3.1/intro/tutorial02/).

Test suite
---
But I also have to locate in which script files to put the following tests.
In terms of certification, [pydoc](https://docs.python.org/3/library/pydoc.html) 
shows up but also [doctest](https://docs.pytest.org/en/stable/doctest.html):
1. Link to data file properly formed HTML: Anchor, `<a `...`href="`URL`"`...`>`txt`</a>`.
   - [Directive](https://docs.python.org/3/library/doctest.html#doctest-directives)
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
