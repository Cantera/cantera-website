---
title: GSoC 2019 First Evaluation
date: 2019-06-22 17:41
slug: GSoC_2019_Project_First_Evaluation
tags: GSoC 2019
description: 2019 Google Summer of Code Cantera Project Blog
type: text
author: Chao Xu
---

# GSoC 2019 First Evaluation

Thanks to the instructions from mentors Richard West ([@rwest](https://github.com/rwest)),
Bryan Weber ([@bryanwweber](https://github.com/bryanwweber)) and Kyle Niemeyer ([@kyleniemeyer](https://github.com/kyleniemeyer)), the website
is functioning after the first month, and we will keep improving it in the rest of the GSoC time. From what I mentioned in the last post, ChemCheck is a
web-based application for visualizing and diagnosing syntax and chemical errors in Chemkin and Cantera input files. In this case, we created basic
functions that allow users to convert their mechanism files to Cantera YAML input files easily (Cantera input file is going to be changed
from CTI file to YAML file, so we made some adjustments as well).

<!-- TEASER_END -->

## Upload Page

Users will upload their files to ChemCheck for checking, so we created an upload page which allows users to upload their mechanism, transport,
thermo, and surface file. Here is the view of upload page.

{{% thumbnail "/images/GSoC_2019_images/upload_page.png" alt="Upload Page" align="center" %}}<p class="text-center">Upload Page</p>{{% /thumbnail %}}

## List Page

After files are uploaded, ChemCheck returns to a list page which lists all uploaded files in the app with id for each group of files.
Users are able to either click on "Details" button to do further operation to their files or hit "Upload new mechanism" button to upload new files.

{{% thumbnail "/images/GSoC_2019_images/list_page.png" alt="List Page" align="center" %}}<p class="text-center">List Page</p>{{% /thumbnail %}}

## Detail Page

In this page, users can either edit their files or hit the "convert to YAML" button to convert files. The editing function is still in development.
Also, there is a "Back to mechanism list" link for users going back to list view.

{{% thumbnail "/images/GSoC_2019_images/detail_page.png" alt="Detail Page" align="center" %}}<p class="text-center">Detail Page</p>{{% /thumbnail %}}

## Convert Page

If the file is converted successfully, a success message will be shown on the page.
Users can see details and download the files from this page.

{{% thumbnail "/images/GSoC_2019_images/convert_success.png" alt="Convert Success Page" align="center" %}}<p class="text-center">Convert Success Page</p>{{% /thumbnail %}}

However, if the file is not converted successfully, the error message will be shown.

{{% thumbnail "/images/GSoC_2019_images/convert_fail.png" alt="Convert Fail Page" align="center" %}}<p class="text-center">Convert Fail Page</p>{{% /thumbnail %}}

## Future Improvement

ChemCheck currently meets very basic requirements of our GSoC project, but there are bunch of things to be improved in the future.
Here I make a list for improvements in next month:

- Add function which allows users replace their files
- Report more detail about the error (like full stack trace and `ck2yaml` logging message) rather than just a error message.
- Add Django login module, this function can help ChemCheck separate files because files uploaded by different users will be saved under different
folders named by user id.
- Finish editing function. This part is not a necessary part, but it would be nice to have it.
- Suggest fix method with syntax error message.
- Improve web UI (make it looks awesome!)
These are improvements that I plan to achieve in following month, and I will keep working on making ChemCheck robust and user-friendly.

## What I Learned From First Month

From the first month, I learned HTML language, how to use it into Django to interact with web server, and a little javascript. This experience is valuable to me
because I am a starter in Django, this project helps me familiarize how Django actually work and what can I achieve with Django.
Solving problems in development improved me a lot. For instance, I was stuck at how to handle list view for a week, and I searched for solutions from various
sources. It gave me a chance to see different ways to handle list views, which led to a final solution for my project.
I also struggled with how to make Cantera `ck2yaml` file convert files and return message. My mentor Richard helped me on solving this problem, and I learned how to
import and integrate external functions into Django. Additionally, I learned how to use git by maintaining and updating project on Github.
It was very exciting while seeing improvement, and I am looking forward to making more progress in the future.
