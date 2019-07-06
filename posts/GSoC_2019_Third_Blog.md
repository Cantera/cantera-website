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

As we planned after first evaluation, the function of ChemCheck should be more robust. File replacement was added, and users are able to
update and delete files arbitrarily. The page looks like this,

![image of detail page](https://github.com/12Chao/myproject/blob/master/images/detail%20page2.png)

delete button leads to delete page, which delete files in both frontend and backend.

![image of delete page](https://github.com/12Chao/myproject/blob/master/images/delete%20page.png)

In update page, users can either replace their files or delete it with checking "clear". 

![image of update page](https://github.com/12Chao/myproject/blob/master/images/update%20page.png)

Except these, ChemCheck can provide traceback message instead only one line error.

![image of error page](https://github.com/12Chao/myproject/blob/master/images/error%20page.png)

## Next Step

I am working toward catching logging message to make the error understandable and making the error page looks nicer. After that, I believe
that we can start with providing diagnosic message. Also, I am still interested in including ACE editor even if it is not a neccessary part
of this project because it is a good opptunity for me to learn Javascirpt. I am learning toward Javascirpt and hopefully can get it done in
next week.
