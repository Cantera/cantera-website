---
title: GSoC 2019 PyCanChemAndYouCan2
date: 2019-06-22 13:03:00 UTC-17:03:00
slug: GSoC_2019_Project_First_Evaluation
tags: GSoC 2019
description: 2019 Google Summer of Code Cnatera Project Blog
type: text
author: Chao Xu
---

# GSoC 2019 PyCanChemAndYouCan2 (ChemCheck) First Evaluation

  Thanks for the instructions from mentors Richard West([@rwest](https://github.com/rwest)), 
Bryan Weber([@bryanwweber](https://github.com/bryanwweber)) and Kyle Niemeyer([@kyleniemeyer](https://github.com/kyleniemeyer)), the website
is functioning after first month, and we will keep improving it in the rest of GSoC time. From what I mentioned in last post, ChemCheck is a
web-based application for visualizing and diagnosing syntax and chemical errors in cantera input files. In this case, we created basic 
functions which allow users convert their mechanism files to cantera yaml input files easily (Cantera input file is going to be changed
from cti file to yaml file, so we made some ajustments as well.).

## Upload Page

  Apparently, users should upload their files to ChemCheck first, so we created upload page wich allows users upload their mechanism, transport,
thermo, and surface file. Here is the view of upload page.

![image of upload page](https://github.com/12Chao/myproject/blob/master/images/upload%20page.png)

## List Page

  After files are uploaded, ChemCheck returns to a list page which lists all uploaded files in the app with id for each group of files.
Users are able to either click on "Details" button to do further operation to their files or hit "Upload new mechanism" button to upload new files.

![image of list page](https://github.com/12Chao/myproject/blob/master/images/list%20page.png)
 
## Detail Page
 
  In this page, users can either edit their files or hit "convert to YAML" button to convert files. Editing function is still in developing, so the web will jump to an editing page without loading contents once "Edit" button is hit.
Also, there is a "Back to mechanism list" link for users going back to list view.

![image of detail page](https://github.com/12Chao/myproject/blob/master/images/detail%20page.png)

## Convert Page
 
  If the file is converted successfully, "Going to try this... Saved to /home/chao/ChemCheck/ChemCheck/media/uploads/1/cantera.txt" message will be shown on the page.
Users can see details and download the files from this page.

![image of successfully uploaded page](https://github.com/12Chao/myproject/blob/master/images/convert%20succ.png)

However, if the file is not converted successfully, the error message will be shown.

![image of successfully uploaded page](https://github.com/12Chao/myproject/blob/master/images/convert%20fail.png)

## Future Improvement 

ChemCheck currently meets very basic requirements of our GSoC project, there are bunch of things could be improved in the future.
Here I make a list for improvements in next month:

- Add function which allows users replace their files 
- Report more detail about the error (like full stack trace and ck2yaml logging message) rather than just a error message.
- Add Django login module, this function can help ChemCheck separate files because files uploaded by different users will saved under different
folders named by user id. This is neccessary before publishing it.
- Finish editing function. This part is not a neccessary part, but it would be nice to have it.
- Suggest fix method with syntax error message.
- Improve web UI (make it looks awesome!)
These are improevements that I plan to achieve in following month, and I will keep working on making ChemCheck robust and user-friendly.

## What I Learned From First Month

From the first month, I learned HTML language, how to use it into Django to interact with web server, and a little javascript. This experience is valuable to me
because I am a starter in Django, this project helps me familiarize how Django actually work and what can I achieve with Django.
Solving problems in development improved me a lot. For instance, I was stucking at how to handle list view for a week, and I searched for solutions from various
sources. It gave me a chance to see different ways to handle list views, which led to a final solution for my project.
I also struggled with how to make Cantera ck2yaml file convert files and return message. My mentor Richard helped me on solving this problem, and I learned how to
import and integrate external functions into Django. Additionally, I learned how to use git by maintaining and updating project on Github.
It was very exciting while seeing improvement, and I am looking forward to making more progress in the future.
