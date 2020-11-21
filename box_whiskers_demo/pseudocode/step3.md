Graphically show selected student's profile in class context
- For selected Class generate box-whiskers-plot for each criterion, resulting in 6+6 boxplots
- For selected Student generate dot-plot  for 6+6 criteria
- Show both layers of plot with student and assignment name
- Produce embeddable image file and pass to View template 
  using Django dictionary `context`.
- Render plot on new page with
  [template](https://docs.djangoproject.com/en/3.1/ref/templates/language/#template-inheritance) 
  that now needs inheritance/extension to keep looking uniform across pages.

![Paradigmatisk R plot](https://www.dropbox.com/s/5890fx1dcn5fml4/plot_covid_aflev.png?dl=1 "Paradigmatic R plot from the spring 2020")

The How-to: 
[use matplotlib for web applications](https://matplotlib.org/3.1.1/faq/howto_faq.html?highlight=save#howto-webapp "How to use Matplotlib in a web application server")
mentions an article on using IMAGEMAP to make plots clickable.
[Virksom Youtube tutorial](https://youtu.be/jrT6NiM46jk "Django and matplotilb integration | How to use matplotlib with Django")
Two use for clickable maps would be to slice the plot in vertical slices, 
one slice for each boxplot:
1. Link top-to-buttom zone to distribution of that excercise / parameter;
1. Link student dot to uncompressed data for the student regarding that excercise / parameter.


<https://trello.com/c/UmVk65dQ>

Summarizing the generate-and-show-plot-based-on-data-at-hand flow:
1. The necessary **modules are imported** 
   (*performance issues as to when import takes place?*).
1. A **function**, the product of which is to be used as backdrop for each student's dot plot is **defined**.
1. Using the function, the produced plot is **stored as Python object** using `pickle`.
1. The pickled plot is retrieved and **overlaid** with a student's dot plot
1. The final plot is converted to a PNG *image file*, 
   which is **stored to a buffered stream** (rather than to a hard drive).
1. The image file is then collected from the stream and **converted** to a `base64` string.
1. This string is exported using Django View `context` to 
   be **embedded** in a Template's HTML `img` tag.