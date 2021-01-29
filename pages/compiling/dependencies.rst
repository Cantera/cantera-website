.. title: Software used by Cantera

.. _sec-dependencies:

.. jumbotron::

   .. raw:: html

      <h1 class="display-3">Software used by Cantera</h1>

   .. class:: lead

      This section lists the versions of third-party software that are required to
      build and use Cantera.

Compilers
---------

You must have one of the following C++ compilers installed on your system. A
Fortran compiler is required only if you plan to build the Fortran module.

* GNU compilers (C/C++/Fortran)

  * Known to work with version 7.4 and 9.3. Expected to work with version >= 4.6.

* Clang/LLVM (C/C++)

  * Known to work with versions 3.5 and 3.8. Expected to work with version
    >= 3.1.
  * Works with the version included with Xcode 8.2.1 and 9.4.1.

* Intel compilers (C/C++/Fortran)

  * Known to work with version 14.0.
  * The 2017 and newer versions of the Intel compiler are **NOT RECOMMENDED** because of a
    bug in the C compiler, which has been reported to Intel:
    https://software.intel.com/en-us/forums/intel-c-compiler/topic/684987

* Microsoft compilers (C/C++)

    * Known to work with Visual Studio 2013 (MSVC 12.0), Visual Studio 2015
      (MSVC 14.0), Visual Studio 2017 (MSVC 14.1), and Visual Studio 2019
      (MSVC 14.2).

* MinGW (C/C++/Fortran)

  * http://mingw-w64.org/doku.php (64-bit and 32-bit)
  * http://tdm-gcc.tdragon.net/ (64-bit and 32-bit)
  * Known to work with Mingw-w64 3.0, which provides GCC 4.8. Expected to work
    with any version that provides a supported version of GCC and includes C++11
    thread support.

Other Required Software
-----------------------

* SCons:

  * http://scons.org/tag/releases.html
  * Cantera 2.3.0 **must** use SCons < 3.0.0
  * Cantera 2.4.0 and up **must** use SCons >= 3.0.0

* Python:

  * https://python.org/downloads/
  * Works with versions >= 3.5.

* Boost

  * https://www.boost.org/users/download/
  * Known to work with version 1.54; Expected to work with versions >= 1.48
  * Only the "header-only" portions of Boost are required. Cantera does not
    currently depend on any of the compiled Boost libraries.

* SUNDIALS

  * If SUNDIALS is not installed, it will be automatically downloaded and the
    necessary portions will be compiled and installed with Cantera.
  * https://computation.llnl.gov/projects/sundials/sundials-software
  * Known to work with versions >= 2.4.
  * To use SUNDIALS with Cantera on a Linux/Unix system, it must be compiled
    with the ``-fPIC`` flag. You can specify this flag when configuring
    SUNDIALS (2.4 or 2.5)::

          configure --with-cflags=-fPIC

    or SUNDIALS 2.6 or higher::

          cmake -DCMAKE_C_FLAGS=-fPIC <other command-line options>

  .. note:: If you are compiling SUNDIALS 2.5.0 on Windows using CMake, you need
            to edit the ``CMakeLists.txt`` file first and change the lines::

              SET(PACKAGE_STRING "SUNDIALS 2.4.0")
              SET(PACKAGE_VERSION "2.4.0")

            to read::

              SET(PACKAGE_STRING "SUNDIALS 2.5.0")
              SET(PACKAGE_VERSION "2.5.0")

            instead, so that Cantera can correctly identify the version of
            SUNDIALS.

* Eigen

  * If Eigen is not installed, it will be automatically downloaded and installed
    with Cantera.
  * http://eigen.tuxfamily.org/index.php?title=Main_Page
  * Known to work with version 3.2.8.

* fmt

  * If fmt (previously known as cppformat) is not installed, it will be
    automatically downloaded and the necessary portions will be compiled and
    installed with Cantera.
  * http://fmtlib.net/latest/index.html
  * Version 3.0.1 or newer is required.

* Google Test

  * If Google Test is not installed, it will be automatically downloaded and the
    necessary portions will be compiled as part of the Cantera build process.
  * https://github.com/google/googletest
  * Known to work with version 1.7.0.

Optional Programs
-----------------

* `Numpy <https://www.numpy.org/>`__

  * Required to build the Cantera Python module, and to run significant portions
    of the test suite.
  * Expected to work with versions >= 1.12.0. 1.14.0 or newer is recommended.

* `Cython <http://cython.org/>`__

  * Required version >=0.23 to build the Python module.

* `Ruamel.yaml <https://pypi.org/project/ruamel.yaml/>`__

  * Required to convert input files from Chemkin, CTI, and XML to the YAML
    format
  * Known to work with versions 0.15.42, 0.15.87, and 0.16.5
  * Expected to work with versions >= 0.15.0

* Matlab

  * Required to build the Cantera Matlab toolbox.
  * Known to work with 2009a and 2014b. Expected to work with versions >= 2009a.

* `Windows Installer XML (WiX) toolset <http://wixtoolset.org/>`__

  * Required to build MSI installers on Windows.
  * Known to work with versions 3.5 and 3.8.

* `Pip <https://pip.pypa.io/en/stable/installing/>`__ (Python)

  * Provides the ``pip`` command which can be used to install most of
    the other Python modules.

* Packages required for building Sphinx documentation

  * `Sphinx <http://www.sphinx-doc.org/en/stable/>`__
  * `Pygments <http://pygments.org/>`__
  * `pyparsing <https://sourceforge.net/projects/pyparsing/>`__
  * `doxylink <https://pythonhosted.org/sphinxcontrib-doxylink/>`__
  * `matlabdomain <https://pypi.org/project/sphinxcontrib-matlabdomain>`__
  * `katex <https://github.com/hagenw/sphinxcontrib-katex/>`__

* `Doxygen <http://doxygen.nl/>`__

  * Required for building the C++ API Documentation
  * Version 1.8 or newer is recommended.

* `Graphviz <https://www.graphviz.org/>`__

  * Required to build the dependency graph images in the C++ API Documentation
  * Known to work with version 2.40.1, expected to work with versions >=2.40.1

.. container:: container

  .. container:: row

     .. container:: col-6 text-left

        .. container:: btn btn-primary
           :tagname: a
           :attributes: href=configure-build.html

           Previous: Configure & Build


     .. container:: col-6 text-right

        .. container:: btn btn-primary
           :tagname: a
           :attributes: href=special-cases.html

           Next: Special Cases
