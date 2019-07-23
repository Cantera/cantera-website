---
title: GSoC 2019 Third Blog
date: 2019-07-20 15:03 UTC-19:03
slug: GSoC_2019_Fourth_Blog
tags: GSoC 2019
description: 2019 Google Summer of Code Cantera Project Blog
type: text
author: Chao Xu
---

# GSoC 2019 Fourth Blog

After two months, the functions of ChemCheck are fairly robust. We improved editing page and ck2yaml error reporting page this week, and we
added pages for user accounts management.

<!-- TEASER_END -->

We have included download function for the editing page, which users can download the edited file to their local directory. It would be more convenient
if changes can be saved to the original file online, so that users do not have to reupload their files, but we will leave it for now since an
editing function is not the most important part. The current exception handling (how to handel unrecognized character) for editing page is striping out all the special signs which cannot
be recognized by ace-editor, and it could also be improved by implementing some python library to guess encoding in the future. 
Here is what the page looks like:

{{% thumbnail "/images/GSoC_2019_images/updated_editor.png" alt="Updated Editor Page" align="center" %}}

<p class="text-center">Editor Page</p>

{{% /thumbnail %}}

The convert-fail page is also improved. Logging messages are added to error messages if a conversion failed. In addition, ChemCheck looks through
three lines ahead and after the line where the error occurs, so that users could have an idea about how to fix the error. Here is the page:

{{% thumbnail "/images/GSoC_2019_images/convert_fail_page.png" alt="Convert Fail Page" align="center" %}}

<p class="text-center">Convert Fail Page</p>

{{% /thumbnail %}}

A series of accounts management page including signup page, login page, logout page, password change page(changing password for users who has logged in), password reset page(for users who forgets password), 
etc. have been included. The signup function will be used only if users want to retrieve their uploaded files. A built-in django module (django.contrib.auth.urls) is implemented for this part; however, the password reset page did not work as expected, which did not send a email to user for password resetting as it supposed to.
I am working on getting this part work. Except password reset function, other pages work well.

Signup Page:

{{% thumbnail "/images/GSoC_2019_images/signup.png" alt="Signup Page" align="center" %}}

<p class="text-center">Signup Page</p>

{{% /thumbnail %}}

Login Page:

{{% thumbnail "/images/GSoC_2019_images/login.png" alt="Login Page" align="center" %}}

<p class="text-center">Login Page</p>

{{% /thumbnail %}}

Password Change Page:

{{% thumbnail "/images/GSoC_2019_images/password_change.png" alt="Password Change Page" align="center" %}}

<p class="text-center">Password Change Page</p>

{{% /thumbnail %}}

## Goals in next two weeks

As we discussed before, the website will eventually save user's uploaded files into separate folders depending on
the user id instead of the primary key. Also, we will get the password-reset page work and collect various CHEMKIN files to
diagnose the errors and test the website.
