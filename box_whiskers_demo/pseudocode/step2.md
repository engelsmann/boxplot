Step 2: Select a student from the class
---
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
was solved via Stack Overflow.

Test suite
---
1. 