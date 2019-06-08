---
title: GSoC 2019 PyCanChemAndYouCan2
date: 2019-06-07 12:33:00 UTC-16:33
slug: GSoC_2019_Project_Introduction
tags: GSoC 2019
description: 2019 Google Summer of Code Cnatera Project Blog
type: text
author: Chao Xu
---

# GSoC 2019 PyCanChemAndYouCan2 (ChemCheck)

Hi everyone! I'm Chao Xu, a master student in Chemical Engineering at Northeastern University. I am working on a Cantera project in GSoC 2019 with my mentor Richard West([@rwest](https://github.com/rwest)) and other Cantera committee members([@bryanwweber](https://github.com/bryanwweber), [@kyleniemeyer](https://github.com/kyleniemeyer)). I am glad to introduce my project here!

## What is PyCanChemAndYouCan2(ChemCheck)

PyCanChemAndYouCan2 is a web-based debugging tool developed for Cantera to visualize and diagnose syntax errors and chemical errors in input files. Users can upload  input files and visualize their errors on the website, and they can also download it after editing the input files.

## Why Would I Need It

Cantera uses input files containing mechanism of reactions because mechanism information is the fundamental to do thermo-kinetic calculation. The input files are required to be in .cti format, and users are able to gain them from various sources (e.g.: writing .cti file by hands, adopted from various sources and repositories on the web, or via a hybrid of these two approaches etc.).   However, .cti files always include errors since they are from different sources, which could cause  inaccurate results. The errors include syntax errors and chemical errors, and it is not likely to be found manually especially in large mechanism files. In this case, a debugging tool helping users to find and fix errors is very useful. 

## What Errors Can Be Visualized or Fixed:

The errors being detected by the application will include but not limited:
Syntax errors

- duplicate lines
- missing digits from end of line
- missing 'E'
- whatever else we find

Chemistry errors

- discontinuous polynomicals
- exceeding collision limit
- inconsistent thermo for explicit reverse rates
- negative rate coefficient as a result of sum of Arrhenius or PLOG expressions, eg.  [here](https://github.com/Cantera/cantera-website/issues/77)
- dead-end pathways

General errors

- excess stiffness
- making  [error](https://github.com/comocheng/wiki/issues/375#)  messages from CVODES easier to understand
- making errors from CVODES easier to catch (raise a python Error)


## How Can I Achieve It

The debugging tool PyCanChemAndYouCan2 is a web-based application developed in Django 2.2.  Users can upload original files and download revised files from the website, and the application contains  ACE code editor to allow users edit their files on the website. Cantera has `ck2cti.py` file to convert Chemkin files, so the debugging part will be writing a 'ck2cti.py' wrapper to insert error descriptions and suggested fixes under errors found by ck2cti file, and return the input file with comments. The wrapper script can be developed independently, but interating with a website can make it user-friendly. The Website can highlight the comments returned by the wrapper script, and users can edit their files one the website, which will help people make the debugging process simpler and convenient. 

Here is the workflow of the application:

```
[upload files] --> [list files] --> [choose one and execute by ck2cti.py and wrapper script] 
--> [show input file with added comments on ACE editor] --> [edit file] --> [download edited file] 
```

My project code was posted on https://github.com/comocheng/ChemCheck.

Please feel free to post your suggestions about this project on [Cantera group](https://groups.google.com/forum/#!forum/cantera-users), or email me xu.chao@husky.neu.edu


