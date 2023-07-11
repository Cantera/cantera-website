.. title: Configuration Options (development version)

.. _scons-config-dev:

.. jumbotron::

   .. raw:: html

      <h1 class="display-4">Configuration Options</h1>

   .. class:: lead

      This document lists the options available for compiling Cantera with
      SCons. This list is for the development version of Cantera. For
      the current release, see `this list <config-options.html>`_.

   The default values are operating-system dependent. To see the defaults for
   your current operating system, run the command:

   .. code:: bash

      scons help

   from the command prompt.

   The following options can be passed to SCons to customize the Cantera
   build process. They should be given in the form:

   .. code:: bash

      scons build option1=value1 option2=value2

   Variables set in this way will be stored in the ``cantera.conf`` file and reused
   automatically on subsequent invocations of SCons. Alternatively, the
   configuration options can be entered directly into ``cantera.conf`` before
   running ``scons build``. The format of this file is:

   .. code:: python

      option1 = 'value1'
      option2 = 'value2'

..
   The options list is generated using 'scons help --restructured-text --dev'
   and is copied manually into the folder during the GH actions

.. include:: pages/compiling/scons-config-options-dev.rst
