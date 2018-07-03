.. title: Special Compiling Cases

.. _sec-special-compiling-cases:

.. jumbotron::

   .. raw:: html

      <h1 class="display-3">Special Compiling Cases</h1>

   .. class:: lead

      This guide explains some of the less common ways to build Cantera

.. _conda-build:

Building the Conda Package
==========================

* The recipe for the Cantera Conda package is located at https://github.com/Cantera/conda-recipes

* To build the Conda package, an installation of ``conda`` is required, with the package
  ``conda-build`` installed.

* Clone the package repository and build the recipe:

  .. code:: bash

     git clone https://github.com/Cantera/conda-recipes
     cd conda-recipes
     conda build cantera

* This will build Cantera using the same version major version of Python as in the ``base``
  environment. To build for a different version of Python, use the ``--python=X.Y`` flag to
  the build command. To build for a different version of NumPy, use the ``--numpy=X.Y`` flag
  to the build command.

.. _sec-intel-compilers:

Intel Compilers
===============

.. warning::

   We **DO NOT RECOMMEND** using the Intel compilers to build Cantera, due to a bug
   in recent versions, which has been documented on the Intel forums:
   https://software.intel.com/en-us/forums/intel-c-compiler/topic/684987

* Before compiling Cantera, you may need to set up the appropriate environment
  variables for the Intel compiler suite, e.g.:

  .. code:: bash

     source /opt/intel/bin/compilervars.sh intel64

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

     scons build env_vars=all CC=icc CXX=icpc FORTRAN=ifort blas_lapack_libs=mkl_rt blas_lapack_dir=$(MKLROOT)/lib/intel64

* When installing Cantera after building with the Intel compiler, the normal
  method of using ``sudo`` to install Cantera to the system default directories
  will not work because ``sudo`` does not pass the environment variables needed
  by the Intel compiler. Instead, you will need to do something like:

  .. code:: bash

     scons build ...
     sudo -s
     source /path/to/compilervars.sh intel64
     scons install
     exit

  Another option is to set the :ref:`prefix <prefix>` option to a directory
  for which you have write permissions, and specify the ``USER`` value to the
  :ref:`python2_prefix <python2-prefix>` or :ref:`python3_prefix <python3-prefix>`
  option.

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
