.. title: Installing Cantera with Pip
.. slug: pip-install
.. description: Installation instructions for Cantera using Pip
.. type: text
.. _sec-install-pip:

.. jumbotron::

   .. raw:: html

      <h1 class="display-4">Installing with Pip</h1>

   .. class:: lead

      `Pip <https://pip.pypa.io/en/stable/>`__ is a package installer for Python that
      can be used to install the Cantera Python module from
      `PyPI <https://pypi.org/project/Cantera/>`__.

Prerequisites
=============

The first step in installing the Cantera Python module using ``pip`` is to make sure you
have a compatible version of Python installed and are able to run ``pip`` from the
command line. Packages for Cantera 2.6.0 are available for Python versions 3.7, 3.8,
3.9, and 3.10.

If you don't already have Python installed, it can be downloaded from
`python.org <https://www.python.org/>`__ or installed using your operating system's
package manager.

To check that you are able run `pip`, open a terminal / command prompt and run the
following command:

*Linux / macOS*:

.. code:: shell

   python3 -m pip --version

*Windows*:

.. code:: shell

   py -m pip --version

If the above command doesn't work, see the instructions at
`packaging.python.org <https://packaging.python.org/en/latest/tutorials/installing-packages/>`__
for how to get `pip` working with your Python installation.

Virtual Environments
====================

Virtual environments provide a way keeping separate sets of Python packages installed
for different projects, where different environments can have different versions of
packages that might otherwise conflict. To create and activate a virtual environment
named ``ct-env`` to be used with Cantera, run the commands:

*Linux / macOS*:

.. code:: shell

   python3 -m venv ct-env
   source ct-env/bin/activate


*Windows*:

.. code:: bat

   py -m venv ct-env
   ct-env\Scripts\activate

The second command should be run in the terminal each time you want to use the specified
environment.

Installing Cantera
==================

To install the Cantera Python module, first activate your virtual environment, if you're
using one. Then, run the command:

*Linux / macOS*:

.. code:: shell

   python3 -m pip install cantera

*Windows*:

.. code:: bat

   py -m pip install cantera

You can test that your installation is working by running one of the examples included
with Cantera:

*Linux / macOS*:

.. code:: shell

   python3 -m cantera.examples.thermo.critical_properties

*Windows*:

.. code:: bat

   py -m cantera.examples.thermo.critical_properties

You should get the following output::

   Critical State Properties
                  Fluid      Tc [K]     Pc [Pa]          Zc
                  water        647.3    2.209E+07      0.2333
               nitrogen        126.2      3.4E+06      0.2891
                methane        190.6    4.599E+06      0.2904
               hydrogen        32.94    1.284E+06      0.3013
                 oxygen        154.6    5.043E+06      0.2879
         carbon dioxide        304.2    7.384E+06      0.2769
                heptane        537.7     2.62E+06      0.2972
                hfc134a        374.2    4.059E+06        0.26
