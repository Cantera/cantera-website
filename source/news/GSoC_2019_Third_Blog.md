---
date: 2019-07-06 13:59
tags: GSoC 2019
author: Chao Xu
---

# GSoC Third Blog -- Function update

As we planned after the first evaluation, the functionality of ChemCheck should be more robust. File replacement was added, and users are able to
update and delete files arbitrarily.

The page looks like this:

:::{card} Updated Detail Page
```{image} /_static/images/GSoC_2019_images/detail_page2.png
:align: center
:width: 100%
```
:::

The delete button leads to a delete page, which will delete files in both the database and the directory.

:::{card} Delete Page
```{image} /_static/images/GSoC_2019_images/delete_page.png
:align: center
:width: 100%
```
:::

In the update page, users can either replace their files or delete it by checking "clear". 

:::{card} Update Page
```{image} /_static/images/GSoC_2019_images/update_page.png
:align: center
:width: 100%
```
:::

In addition to these, new features ChemCheck can provide the traceback message instead of only one line error.

:::{card} Error Page
```{image} /_static/images/GSoC_2019_images/error_page.png
:align: center
:width: 100%
```
:::

An editing function is also included:

:::{card} Editor Page
```{image} /_static/images/GSoC_2019_images/ace_editor.png
:align: center
:width: 100%
```
:::

## Next Steps

I am working toward catching logging messages to make the error understandable and
making the error page look nicer. Also, I will improve editing function (adding download
function in editor page, and change highlight settings of ace editor).  After that, I
will test different defective mechanism files and providing fix suggestions.
