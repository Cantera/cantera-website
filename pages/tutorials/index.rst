.. title: Tutorials
.. date: 2018-05-30 11:20:56 UTC-04:00
.. description: Cantera Tutorial page
.. type: text

.. container:: jumbotron

   .. raw:: html

      <h1 class="display-3">Getting started with Cantera</h1>

   .. class:: lead

      For those new to Cantera, we present here a set of short
      tutorials to familiarize you with Cantera's basic functionality and basic
      capabilities, give some examples of how to work Cantera within your preferred
      interface language—basic function calls and a few simple applications—and
      demonstrate some basic troubleshooting.

After installing Cantera and finishing these tutorials, you should be
ready to begin using Cantera. The next steps, linked below the tutorials,
provide information in this regard.

First, let's pick an interface language and get started with the
tutorials.  Note that while Cantera can be accessed via other interfaces
(namely Fortran and directly in C++), Python and Matlab present the most
convenient interfaces for learning about Cantera, and are the interface of
preference for the vast majority of Cantera users.

.. container:: card-deck

   .. container:: card

      .. container::
         :tagname: a
         :attributes: href=python-tutorial.html
                      title=Python

         .. container:: card-header section-card

            Python Tutorial

      .. container:: card-body

         .. container:: card-text

            I want to learn about Cantera via the Python module.

   .. container:: card

      .. container::
         :tagname: a
         :attributes: href=matlab-tutorial.html
                      title=Matlab

         .. container:: card-header section-card

            Matlab Tutorial

      .. container:: card-body

         .. container:: card-text

         I want to learn about Cantera via the Matlab toolbox

   .. container:: card

      .. container::
         :tagname: a
         :attributes: href=cxx-guide/compiling.html
                      title="C++ Guide"

         .. container:: card-header section-card

            Advanced: C++ Tutorial

      .. container:: card-body

         .. container:: card-text

         I want to learn about Cantera via the C++ interface

.. jumbotron::

   .. raw:: html

      <h2 class="display-4" id="cantera-next-steps">Next steps</h2>

   .. class:: lead

      Okay, so you've finished the tutorials and understand the basic user functionality of Cantera.
      Now what?

Using Cantera for a range of problems will likely require you to extend
your knowledge in two ways:

- You will need an input file describing the phase(s) of matter
  relevant to your problem.
- Your application may very well require function calls and routines
  not necessarily covered in the tutorials.

The links below will help you take the 'next steps,' and point you to:

- Information on how to locate and work with Cantera input files (which
  contain the thermodynamic, transport, and chemical kinetic information
  for the phases of interest).
- Detailed documentation and user guides for accessing Cantera via
  Python, Matlab, and directly via C++. For advanced and intermediate
  users, the documentation is an easily-searchable repository for
  information on specific functions of interest.
- A repository of examples, demonstrating how to use Cantera to solve a
  diverse range of problems. You can either use these examples directly,
  or use them as a template to develop your own applications.

.. container:: card-deck

   .. container:: card

      .. container::
         :tagname: a
         :attributes: href=input-files.html
                      title="Input Files"

         .. container:: card-header section-card

            Cantera Input Files

      .. container:: card-body

         .. container:: card-text

            Learn how to locate and/or create input files.

   .. container:: card

      .. container::
         :tagname: a
         :attributes: href=/documentation/index.html
                      title="Documentation"

         .. container:: card-header section-card

            Users' Guides and Documentation

      .. container:: card-body

         .. container:: card-text

            Locate documentation on specific Cantera functions.

   .. container:: card

      .. container::
         :tagname: a
         :attributes: href=/examples/index.html
                      title="Documentation"

         .. container:: card-header section-card

            Examples

      .. container:: card-body

         .. container:: card-text

            See examples of Cantera applications
