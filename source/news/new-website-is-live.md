---
date: 2018-07-02 15:02
author: "Bryan Weber"
category: website
language: English
---

# The New Cantera Website is Here!

This summer, Bryan Weber and Steven DeCaluwe took on the project of revamping the Cantera website.
The old website was, well, old and needed to be refreshed. Thanks to a grant from
[NumFOCUS][numfocus], Bryan and Steven were able to completely redo the website!

<!-- TEASER_END -->

The main focus of the update was to make it much easier for all users of Cantera to quickly find the
information they need. The older website was a list of links to locations deeper in the website,
which made it hard for new and expert users of Cantera to find the page they were looking for. On
the new website, we have clearly marked sections for new users and advanced users to find what
they're looking for. All of the same content is available, we've just reorganized it and
(hopefully!) made things easier to find.

{{% thumbnail "/images/new-website-is-live/old-cantera-website.png" alt="Old Cantera Website" align="center" %}}<p class="text-center">Old Cantera Website</p>{{% /thumbnail %}}

We have a [Tutorials section][tutorials] to get new users started with using Cantera, we have a
separate ["Science" section][science] that explains some of the basic equations and principles
underlying the models that Cantera uses, and we still have all the API documentation that you need
over in the [Documentation section][docs]. There is also a [Community section][community] with
information about how to reach the Cantera steering community and where our code and discussions
live.

## NumFOCUS

This work was sponsored by NumFOCUS through their Small Development Grants program. This program
gives small grants to NumFOCUS sponsored projects to help improve their code or their community.
Cantera was awarded the grant as part of the [Spring 2018 round of funding][nf-blog-post]. If you
are interested in more information about this grant, or future grants, please email the [steering
committee][steering-committee]. More information about [NumFOCUS][numfocus] can be found in the
[Community section][donate] of our new website! Thank you NumFOCUS!

## Nuts and bolts

The website is now built with the Nikola static site generator and much of the content has been
migrated to a [new repository][website-repo]. The allows us to update the website content without
pushing commits to the main Cantera repository and rebuilding all of the documentation. The website
is themed with the [Bootstrap 4][bootstrap] theme. The documentation of the Cantera API is still
done with Sphinx and Doxygen in the [main code repository][main-repo].

All of the links to the old website structure should be automatically redirected to the equivalent
location in the new structure. If you find any redirects that don't work, or any broken links within
cantera.org, please [file an issue][file] on our website repository.

There are still a few things we're working out with the new site. If you would like to contribute,
check out the [issues page][issues] on our repository and leave a comment!

[website-repo]: https://github.com/Cantera/cantera-website
[issues]: https://github.com/Cantera/cantera-website/issues
[tutorials]: https://cantera.org/tutorials/index.html
[science]: https://cantera.org/science/index.html
[docs]: https://cantera.org/documentation/index.html
[community]: https://cantera.org/community.html
[bootstrap]: https://getbootstrap.com
[nf-blog-post]:https://www.numfocus.org/blog/numfocus-awards-development-grants-to-open-source-projects-spring-2018
[numfocus]: https://numfocus.org
[donate]: https://cantera.org/community.html#supporting-cantera
[file]: https://github.com/Cantera/cantera-website/issues/new
[main-repo]: https://github.com/Cantera/cantera
[steering-committee]: mailto:steering@cantera.org
