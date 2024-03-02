---
date: 2019-07-20 15:03
tags: GSoC 2019
author: Chao Xu
---

# GSoC 2019 Fourth Blog

After two months, the functions of ChemCheck are fairly robust. We improved editing and ck2yaml error reporting pages this week, and we added pages for user account management.

We have included a download function for the editing page, so users can download the edited file to their local directory. It would be more convenient
if changes can be saved to the original file online, so that users do not have to re-upload their files, but we will leave it for now since an
editing function is not the most important part. The current exception handling (how to handle unrecognized character) for the editing page is stripping out all the characters in encodings that cannot
be recognized by ace-editor, and it could also be improved by implementing some Python library to guess the encoding of the file in the future.
Here is what the page looks like:

:::{card} Updated Editor Page
```{image} /_static/images/GSoC_2019_images/updated_editor.png
:align: center
:width: 100%
```
:::


The page shown when conversion fails is also improved. Logging messages are added to error messages if a conversion failed. In addition, ChemCheck looks through
four lines ahead and after the line where the error occurs, so that users could have an idea about how to fix the error. Here is the page:

:::{card} Convert Fail Page
```{image} /_static/images/GSoC_2019_images/convert_fail_page.png
:align: center
:width: 100%
```
:::

A series of account management pages including signup page, login page, logout page, password change page (changing password for users who are logged in), and password reset (for users who forget their password) pages, among others.
have been included. The signup function will be used only if users want to retrieve their uploaded files. A built-in Django module (`django.contrib.auth.urls`) is implemented for this part; however, the password reset page did not work as expected, because it did not send an email to the user to reset the password.
I am working on getting this part to work. Except the password reset function, other pages work well.

:::{card} Signup Page
```{image} /_static/images/GSoC_2019_images/signup.png
:align: center
:width: 100%
```
:::

:::{card} Login Page
```{image} /_static/images/GSoC_2019_images/login.png
:align: center
:width: 100%
```
:::

:::{card} Password Change Page
```{image} /_static/images/GSoC_2019_images/password_change.png
:align: center
:width: 100%
```
:::

## Goals in next two weeks

As we discussed before, the website will eventually save a user's uploaded files into separate folders depending on
the user id instead of the primary key. Also, we will get the password-reset page work and collect various CHEMKIN files to
diagnose the errors and test the website.
