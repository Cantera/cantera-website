.. title: Configure and Build (development version)
.. description: Configure and Build Cantera

.. jumbotron::

   .. raw:: html

      <h1 class="display-4">Configure & Build Cantera</h1>

   .. class:: lead

      These directions are for the development version of Cantera. For
      the current release, see `these instructions <configure-build.html>`_.

.. _sec-determine-config-dev:

Determine configuration options
===============================

* Run ``scons help --options`` to see a list of all of the configuration options for
  Cantera, or see all of the options on the :ref:`Configuration Options <scons-config-dev>`
  page.

* Configuration options are specified as additional arguments to the ``scons``
  command. For example:

  .. code:: bash

     scons command option_name=value

  where ``scons`` is the program that manages the build steps, and ``command``
  is most commonly one of

    * ``build``
    * ``test``
    * ``clean``

  Other commands are explained in the :ref:`Build Commands <sec-build-commands-dev>`
  section.

* SCons saves configuration options specified on the command line in the file
  ``cantera.conf`` in the root directory of the source tree, so generally it is
  not necessary to respecify configuration options when rebuilding Cantera. To
  unset a previously set configuration option, either remove the corresponding
  line from ``cantera.conf`` or use the syntax:

  .. code:: bash

     scons command option_name=

* Sometimes, changes in your environment can cause SCons's configuration tests
  (for example, checking for libraries or compiler capabilities) to unexpectedly fail.
  To force SCons to re-run these tests rather than trusting the cached results,
  run scons with the option ``--config=force``.

* The following lists of options are not complete, they show only some commonly
  used options. The entire list of options can be found on the
  :ref:`Configuration options <scons-config-dev>` page.

Common Options
^^^^^^^^^^^^^^

* :ref:`debug <debug-dev>`
* :ref:`optimize <optimize-dev>`
* :ref:`prefix <prefix-dev>`

Specifying Paths for Cantera's Dependencies
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* :ref:`blas_lapack_libs <blas-lapack-libs-dev>`

  * On OS X, the Accelerate framework is automatically used to provide
    optimized versions of BLAS and LAPACK, so the ``blas_lapack_libs``
    option should generally be left unspecified.

* :ref:`blas_lapack_dir <blas-lapack-dir-dev>`
* :ref:`boost_inc_dir <boost-inc-dir-dev>`
* :ref:`sundials_include <sundials-include-dev>`
* :ref:`sundials_libdir <sundials-libdir-dev>`
* :ref:`hdf_include <hdf-include-dev>`
* :ref:`hdf_libdir <hdf-libdir-dev>`
* :ref:`extra_inc_dirs <extra-inc-dirs-dev>`
* :ref:`extra_lib_dirs <extra-lib-dirs-dev>`

Python Module Options
^^^^^^^^^^^^^^^^^^^^^

Compiling the Cantera Python module requires that NumPy and Cython are installed
for the target installation of Python. The following SCons options control how
the Python module is built:

* :ref:`python_package <python-package-dev>`
* :ref:`python_cmd <python-cmd-dev>`

  * By default, SCons will try to build the full Python interface for copy of
    Python that is running SCons. Use this option if you wish to build Cantera
    for a different Python installation.

* :ref:`python_prefix <python-prefix-dev>`

Windows Only Options
^^^^^^^^^^^^^^^^^^^^

.. note::

    The ``cantera.conf`` file uses the backslash character ``\`` as an escape
    character. When modifying this file, backslashes in paths need to be escaped
    like this: ``boost_inc_dir = 'C:\\Program Files (x86)\\boost\\include'``
    This does not apply to paths specified on the command line. Alternatively,
    you can use forward slashes (``/``) in paths.

* In Windows there aren't any proper default locations for many of the packages
  that Cantera depends on, so you will need to specify these paths explicitly.

* Remember to put double quotes around any paths with spaces in them, such as
  ``"C:\Program Files"``.

* By default, SCons attempts to use the same architecture as the copy of Python
  that is running SCons, and the most recent installed version of the Visual
  Studio compiler. If you aren't building the Python module, you can override
  this with the configuration options ``target_arch`` and ``msvc_toolset_version``.

* To compile with MinGW, specify the :ref:`toolchain <toolchain-dev>` option::

    toolchain=mingw

* :ref:`msvc_toolset_version <_msvc-toolset-version-dev>`
* :ref:`msvc_version <msvc-version-dev>`
* :ref:`target_arch <target-arch-dev>`
* :ref:`toolchain <toolchain-dev>`

MATLAB Toolbox Options
^^^^^^^^^^^^^^^^^^^^^^

Building the MATLAB toolbox requires an installed copy of MATLAB, and the path
to the directory where MATLAB is installed must be specified using the following
option:

* :ref:`matlab_toolbox <matlab-toolbox-dev>`
* :ref:`matlab_path <matlab-path-dev>`

Fortran Module Options
^^^^^^^^^^^^^^^^^^^^^^

Building the Fortran module requires a compatible Fortran compiler. SCons will
attempt to find a compatible compiler by default in the ``PATH`` environment
variable. The following options control how the Fortran module is built:

* :ref:`f90_interface <f90-interface-dev>`
* :ref:`FORTRAN <fortran-dev>`

Documentation Options
^^^^^^^^^^^^^^^^^^^^^

The following options control if the documentation is built:

* :ref:`doxygen_docs <doxygen-docs-dev>`
* :ref:`sphinx_docs <sphinx-docs-dev>`

Less Common Options
^^^^^^^^^^^^^^^^^^^

* :ref:`CC <cc-dev>`
* :ref:`CXX <cxx-dev>`
* :ref:`env_vars <env-vars-dev>`
* :ref:`layout <layout-dev>`
* :ref:`VERBOSE <verbose-dev>`
* :ref:`gtest_flags <gtest-flags-dev>`

.. _sec-build-commands-dev:

Build Commands
==============

The following *commands* are possible as arguments to SCons:

.. code:: bash

   scons command

* ``scons help``
    Print a list of available SCons commands.

* ``scons help --options``
    Print a description of user-specifiable options.

* ``scons build``
    Compile Cantera and the language interfaces using
    default options.

* ``scons clean``
    Delete files created while building Cantera.

* ``scons install``
    Install Cantera.

* ``scons uninstall``
    Uninstall Cantera.

* ``scons test``
    Run all tests which did not previously pass or for which the
    results may have changed.

* ``scons test-reset``
    Reset the passing status of all tests.

* ``scons test-clean``
    Delete files created while running the tests.

* ``scons test-help``
    List available tests.

* ``scons test-NAME``
    Run the test named ``NAME``.

* ``scons <command> dump``
    Dump the state of the SCons environment to the
    screen instead of doing ``<command>``, for example,
    ``scons build dump``. For debugging purposes.

* ``scons samples``
    Compile the C++ and Fortran samples.

* ``scons msi``
    Build a Windows installer (.msi) for Cantera.

* ``scons sphinx``
    Build the Sphinx documentation

* ``scons doxygen``
    Build the Doxygen documentation

Compile Cantera & Test
======================

* Run SCons with the list of desired configuration options:

  .. code:: bash

     scons build ...

* If Cantera compiles successfully, you should see a message that looks like::

    *******************************************************
    Compilation completed successfully.

    - To run the test suite, type 'scons test'.
    - To list available tests, type 'scons test-help'.
    - To install, type 'scons install'.
    *******************************************************

* If you do not see this message, check the output for errors to see what went
  wrong. You may also need to examine the contents of ``config.log``.

* Cantera has a series of tests that can be run with the command:

.. code:: bash

   scons test

* When the tests finish, you should see a summary indicating the number of
  tests that passed and failed.

* If you have tests that fail, try looking at the following to determine the
  source of the error:

  * Messages printed to the console while running ``scons test``
  * Output files generated by the tests

Building Documentation
^^^^^^^^^^^^^^^^^^^^^^

To build the Cantera HTML documentation, run the commands:

.. code:: bash

   scons doxygen
   scons sphinx

or append the options ``sphinx_docs=y`` and ``doxygen_docs=y`` to the build
command:

.. code:: bash

   scons build doxygen_docs=y sphinx_docs=y

.. container:: container

   .. container:: row

      .. container:: col-6 text-left

         .. container:: btn btn-primary
            :tagname: a
            :attributes: href=source-code.html

            Previous: Download the Source Code


      .. container:: col-6 text-right

         .. container:: btn btn-primary
            :tagname: a
            :attributes: href=dependencies.html

            Next: Dependencies
