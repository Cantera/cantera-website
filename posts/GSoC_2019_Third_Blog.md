---
title: GSoC 2019 Third Blog
date: 2019-07-06 13:59 UTC-17:59
slug: GSoC_2019_Third_Blog
tags: GSoC 2019
description: 2019 Google Summer of Code Cnatera Project Blog
type: text
author: Chao Xu
---

# GSoC Third Blog --- Function update

As we planned after the first evaluation, the functionality of ChemCheck should be more robust. File replacement was added, and users are able to
update and delete files arbitrarily. The page looks like this:

{{% thumbnail "/images/GSoC_2019_images/detail_page2.png" alt="Updated Detail Page" align="center" %}}

Updated Detail Page

{{% /thumbnail %}}

The delete button leads to a delete page, which will delete files in both the database and the directory.

{{% thumbnail "/images/GSoC_2019_images/delete_page.png" alt="Delete Page" align="center" %}}

Delete Page

{{% /thumbnail %}}

In the update page, users can either replace their files or delete it by checking "clear". 

{{% thumbnail "/images/GSoC_2019_images/update_page.png" alt="Update Page" align="center" %}}

Update Page

{{% /thumbnail %}}

In addition to these, new features ChemCheck can provide the traceback message instead of only one line error.

{{% thumbnail "/images/GSoC_2019_images/error_page.png" alt="Error Page" align="center" %}}

Error Page

{{% /thumbnail %}}

An editing function is also included:

{{% thumbnail "/images/GSoC_2019_images/ace_editor.png" alt="Editor Page" align="center" %}}

Editor Page

{{% /thumbnail %}}

## Next Step

I am working toward catching logging messages to make the error understandable and making the error page looks nicer. Also, I will improve editing function (adding download function in editor page, and change highlight settings of ace editor).  After that, I will test different
defective mechanism files and providing fix suggestions.
