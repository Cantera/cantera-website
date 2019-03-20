.. title: Community
.. description: All about the Cantera community and how to contribute
.. slug: community

.. jumbotron::

   .. raw:: html

      <h1 class="display-3">The Cantera Community</h1>

   .. class:: lead

      Resources to help you participate in the community of Cantera users and developers

.. contents:: :depth: 2

About the Cantera Community
---------------------------

Cantera was originally developed by :doc:`Prof. David G. Goodwin <dave>` at the California
Institute of Technology. Building on Prof. Goodwin's legacy, Cantera is licensed
under a `permissive 3-Clause BSD license
<https://github.com/Cantera/cantera/blob/master/License.txt>`__, ensuring that the
software will remain open source and available for all to use.

In this vein, Cantera software relies exclusively upon the volunteer
contributions of its users. These contributions range from diagnosing and
reporting problems/bugs, to helping others learn to use Cantera, to developing
and implementing new software capabilities.

While Cantera provides some standalone models and applications, numerous external
packages exist that provide more specialized functionality and rely on Cantera. We
provide a non-exhaustive list of these :doc:`affiliated packages <affiliated-packages>`.

Governance
~~~~~~~~~~

Cantera is governed by a Steering Committee; more information about our project's
governance policies can be found on the :doc:`governance <governance>` page.


The Cantera Users' Group
~~~~~~~~~~~~~~~~~~~~~~~~

The `Cantera Users’ Group
<https://groups.google.com/forum/#!forum/cantera-users>`__ on Google Groups is
the forum where most Cantera users have their questions asked and answered. If
you need help using Cantera and cannot find an answer in the tutorials or
documentation at Cantera's website, consider joining and asking a question
there. A few notes:

* Please use the search feature before posting to see if your question has been
  answered before.
* If you are not running the current stable release of Cantera, please upgrade
  first, and see if the problem persists.
* This group is moderated, so it may take some time for your posts to appear if
  you are a new member.

For installation/compilation problems, please provide:

* The contents of the ``cantera.conf`` and ``config.log`` files, and the output of the ``scons
  build`` and ``scons build dump`` commands. You can direct this output to a file
  called ``buildlog.txt`` by running::

       scons build >buildlog.txt 2>&1

* The exact version of Cantera you are trying to compile, and how it was
  obtained (i.e., downloaded source tarball or the specific Git commit).
* Your operating system, compiler versions, and the versions of any other
  relevant software.

For application problems (i.e., not related to installation or compilation),
please:

* Provide a minimal, complete, and verifiable example that demonstrates
  the problem when making your post; in short this means include a code example
  and input files.
* Please also provide information about your operating system and Cantera
  version. This will enable other members of the group to efficiently
  understand the problem and offer suggestions on how to fix it.
* Please DO NOT post screenshots of code or error messages! They cannot be
  searched by anyone looking to solve a similar problem, and also cannot be
  read by text readers for visually impaired users. Instead, please copy and
  paste any relevant text directly into your message. Thanks!

Gitter
~~~~~~

For less formal and not-directly-relevant-to-Cantera discussions, we have set up
a `Cantera chat room <https://gitter.im/Cantera/Lobby>`__ on Gitter. This is a
forum where you can have conversations with other Cantera community members
which are not directly relevant to the broader Cantera Users' Group. This may
involve discussing applications based on Cantera, the scientific theory
underpinning some of Cantera's functionality, broader questions about the
scientific computing landscape, or perhaps just conversations to get to know
other members of the Cantera community.

A few notes:

* This forum is not directly moderated or supported by the Cantera developers
  or Steering Committee. While developers may periodically read or respond to
  posts, there is no expectation of any official Cantera support through
  this forum.
* Posts or questions directly relevant to Cantera usage or support should
  still be directed to the Cantera Users' Group. Having this information in a
  single, searchable repository is a great benefit to our users, and we do not
  want Cantera-relevant information spread across multiple venues.

Interacting with the Cantera Community
--------------------------------------

Code of Conduct
~~~~~~~~~~~~~~~

All online and in-person interactions and communications related to Cantera are
governed by the `Cantera Code of Conduct
<https://github.com/Cantera/cantera/blob/master/CODE_OF_CONDUCT.md>`__. This code
of conduct sets expectations for the community to ensure that users and
contributors are able to participate in a respectful and welcoming environment.

Please adhere to this code of conduct in any interactions you have in the Cantera
community. It is strictly enforced on all official Cantera repositories, websites,
users' group, and other resources. If you encounter someone violating these terms,
please `contact the code of conduct team <mailto:conduct@cantera.org>`__
(`@speth <https://github.com/speth>`__,
`@bryanwweber <https://github.com/bryanwweber>`__, and
`@kyleniemeyer <https://github.com/kyleniemeyer>`__) and we will address it as
soon as possible.

Contributing Code
~~~~~~~~~~~~~~~~~

If there is a feature you would like to see added to Cantera, please consider
becoming part of the developer community and contributing code!
`Cantera's code repository <https://github.com/Cantera/cantera>`__ is developed
openly on `GitHub <https://github.com/>`__. Contributions are welcomed from
anyone in the community; please see the `Contributors' guide
<https://github.com/Cantera/cantera/blob/master/CONTRIBUTING.md>`__ for
assistance in getting started. There are also plenty of current contributors
who are happy to help, if you do not know how to get started.

Bug Reporting
~~~~~~~~~~~~~

**What should I do if I think I've found a bug in Cantera?**

- Check to see if you're using the most recent version of Cantera, and
  upgrade if not.
- Check the `Issue Tracker
  <https://github.com/Cantera/cantera/issues>`_ to see if the issue
  has already been reported.
- Try to generate a `minimal, complete, and verifiable example
  <https://stackoverflow.com/help/mcve>`_ that demonstrates the observed bug.
- Create a new issue on the tracker (the "New issue" button is toward the
  upper right-hand corner, just above the list of open issues). Include as
  much information as possible about your system configuration (operating
  system, compiler versions, Python versions, installation method, etc.)

**What information should I include in my bug report?**

- The version of Cantera are you using, and how you installed it
- The operating system you are using
- If you compiled Cantera, what compiler you used, and what compilation
  options you specified
- The version of Python or Matlab are you using, if applicable
- The necessary *input* to generate the reported behavior
- The full text of any error message you receive

Supporting Cantera
------------------

Citing Cantera
~~~~~~~~~~~~~~

If you use Cantera in a publication, we would appreciate if you cited the
version of Cantera that you used. This helps to improve the reproducibility of
your work, as well as giving credit to the many `authors
<https://github.com/Cantera/cantera/blob/master/AUTHORS>`_ who have contributed
their time to developing Cantera. The recommended citation for Cantera is as
follows:

   David G. Goodwin, Raymond L. Speth, Harry K. Moffat, and Bryan W. Weber.
   *Cantera: An object-oriented software toolkit for chemical kinetics,
   thermodynamics, and transport processes*. https://www.cantera.org,
   2018. Version 2.4.0. doi:10.5281/zenodo.170284

The following BibTeX entry may also be used:

.. code:: bibtex

   @misc{cantera,
       author = "David G. Goodwin and Raymond L. Speth and Harry K. Moffat
                 and Bryan W. Weber",
       title = "Cantera: An Object-oriented Software Toolkit for Chemical
                Kinetics, Thermodynamics, and Transport Processes",
       year = 2018,
       note = "Version 2.4.0",
       howpublished = "\url{https://www.cantera.org}",
       doi = {10.5281/zenodo.1174508}
   }

If you are using a different version of Cantera, update the ``note`` and
``year`` fields accordingly.

Donations
~~~~~~~~~

Finally, please consider financially supporting Cantera's development! Cantera
is a fiscally sponsored project of NumFOCUS, a 501(c)3 nonprofit dedicated to
supporting the open source scientific computing community. If you have found
Cantera to be useful to your research or company, please consider making a
`donation <https://numfocus.salsalabs.org/donate-to-cantera/index.html>`_
to support our efforts. All donations will be used exclusively to fund the
development of Cantera's source code, documentation, or community.

.. image:: /assets/img/SponsoredProject.png
    :alt: Powered by NumFOCUS
    :target: https://numfocus.org
    :align: center
    :width: 250px

.. container:: text-center

   .. container:: btn btn-primary
      :tagname: a
      :attributes: href=https://numfocus.salsalabs.org/donate-to-cantera/index.html
                   title="Donate to Cantera"
                   rel=nofollow

      Donate to Cantera
