.. title: Special Compiling Cases

.. _sec-special-compiling-cases:

.. jumbotron::

   .. raw:: html

      <h1 class="display-4">Special Compiling Cases</h1>

   .. class:: lead

      This guide explains some of the less common ways to build Cantera

.. _conda-build:

Building the Conda Package
==========================

* The recipe for the Cantera Conda package is located at https://github.com/Cantera/conda-recipes

* See the ``README.md`` in that repository for instructions.

.. _sec-intel-compilers:

Intel Compilers
===============

* The following instructions refer to the `Intel OneAPI Toolkit
  <https://www.intel.com/content/www/us/en/developer/tools/oneapi/toolkits.html>`__.

* Before compiling Cantera, you may need to set up the appropriate environment
  variables for the Intel compiler suite. For example:

  .. code:: bash

     source /opt/intel/oneapi/setvars.sh

* For the Intel compiler to work with SCons, these environment variables need
  to be passed through SCons by using the command line option:

  .. code:: bash

     env_vars=all

* If you want to use the Intel MKL versions of BLAS and LAPACK, you will need
  to provide additional options. The following are typically correct on
  64-bit Linux systems:

  .. code:: bash

     blas_lapack_libs=mkl_rt blas_lapack_dir=$(MKLROOT)/lib/intel64

  Your final SCons call might then look something like:

  .. code:: bash

     scons build env_vars=all CC=icx CXX=icpx FORTRAN=ifx blas_lapack_libs=mkl_rt blas_lapack_dir=$(MKLROOT)/lib/intel64

* When installing Cantera after building with the Intel compiler, the normal
  method of using ``sudo`` to install Cantera to the system default directories
  will not work because ``sudo`` does not pass the environment variables needed
  by the Intel compiler. Instead, you will need to do something like:

  .. code:: bash

     scons build ...
     sudo -s
     source /path/to/setvars.sh
     scons install
     exit

  Another option is to set the :ref:`prefix <prefix>` option to a directory
  for which you have write permissions, and specify the ``USER`` value to the
  :ref:`python_prefix <python-prefix>` option.

.. container:: container

 .. container:: row

    .. container:: col-6 text-left

       .. container:: btn btn-primary
          :tagname: a
          :attributes: href=dependencies.html

          Previous: Dependencies


    .. container:: col-6 text-right

       .. container:: btn btn-primary
          :tagname: a
          :attributes: href=config-options.html

          Next: Configuration Options
