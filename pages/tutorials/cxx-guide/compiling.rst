.. title: Compiling Cantera C++ Programs
.. _sec-compiling-cplusplus:

.. jumbotron::

   .. raw:: html

      <h1 class="display-4">Compiling Cantera C++ Programs</h1>

   .. class:: lead

      This guide shows you how to build C++ programs that use Cantera's features

Build Systems
*************

In general, it should be possible to use Cantera with any build system by
specifying the appropriate header and library paths, and specifying the required
libraries when linking. It is also necessary to specify the paths for libraries
used by Cantera, such as Sundials, BLAS, and LAPACK.

Instructions below assume a Linux operating system where Cantera's libraries are
installed in a standard location such as ``/usr/lib`` or ``/usr/local/lib``. If Cantera
is installed to a custom location, environment variables ``LD_LIBRARY_PATH`` and
``PKG_CONFIG_PATH`` need to be specified. If they are not already set elsewhere, they
can be set from the command line as:

.. code:: bash

   export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/path/to/lib
   export PKG_CONFIG_PATH=$PKG_CONFIG_PATH:/path/to/lib/pkgconfig

where ``/path/to/lib`` should be replaced by Cantera's library installation path.

pkg-config
==========

On systems where the ``pkg-config`` program is installed, it can be used to
determine the correct compiler and linker flags for use with Cantera. For
example:

.. code:: bash

   g++ myProgram.cpp -o myProgram $(pkg-config --cflags --libs cantera)

It can also be used to populate variables in a Makefile:

.. code:: make

   CFLAGS += $(shell pkg-config --cflags cantera)
   LIBS += $(shell pkg-config --libs cantera)

Or in an SConstruct file:

.. code:: python

   env.ParseConfig("pkg-config --cflags --libs cantera")

Note that ``pkg-config`` will work only if it can find the ``cantera.pc``
file. If Cantera's libraries are not installed in a standard location such as
``/usr/lib`` or ``/usr/local/lib``, you may need to set the ``PKG_CONFIG_PATH``
environment variable appropriately before using ``pkg-config``.

SCons
=====

SCons is a multi-platform, Python-based build system. It is the build system
used to compile Cantera. The description of how to build a project is contained
in a file named ``SConstruct``. The ``SConstruct`` file is actually a Python
script, which makes it very straightforward to add functionality to a
SCons-based build system.

A typical ``SConstruct`` file for compiling a program that uses Cantera might
look like this:

.. code:: python

   env = Environment()

   env.Append(CCFLAGS='-g -std=c++17',
              CPPPATH=['/usr/local/cantera/include'],
              LIBS=['cantera_shared'],
              LIBPATH=['/usr/local/cantera/lib'],
              RPATH=['/usr/local/cantera/lib']
              LINKFLAGS=['-g', '-pthread'])

   sample = env.Program('sample', 'sample.cpp')
   Default(sample)

This script establishes what SCons refers to as a "construction environment"
named ``env``, and sets the header (``CPPPATH``) and library (``LIBPATH``) paths
to include the directories containing the Cantera headers and libraries. Then,
a program named ``sample`` is compiled using the single source file ``sample.cpp``.

The appropriate path definitions and flags depend on your system configuration and the
options that were used to compile Cantera. Several example ``SConstruct`` files are
included with the C++ examples contained in the ``samples/cxx`` subdirectory of the
Cantera installation directory, with contents customized for your Cantera installation.

For more information on SCons, see the `SCons Wiki <https://github.com/SCons/scons/wiki/>`__
and the `SCons homepage <https://www.scons.org>`__.

CMake
=====

CMake is a multi-platform build system that uses a high-level project
description to generate platform-specific build scripts (for example, on Linux,
CMake will generate Makefiles). The configuration file for a CMake project is
called ``CMakeLists.txt``. A typical ``CMakeLists.txt`` file for compiling a
program that uses Cantera might look like this:

.. code:: cmake

   cmake_minimum_required(VERSION 3.1)
   project (sample)

   set(CMAKE_VERBOSE_MAKEFILE ON)
   set(CMAKE_CXX_STANDARD 17)

   find_package(Threads REQUIRED)

   include_directories("/opt/cantera/include")
   link_directories("/opt/cantera/lib")

   add_executable(sample sample.cpp)
   target_link_libraries(sample cantera_shared Threads::Threads)

Several example ``CMakeLists.txt`` files are included with the C++ examples
contained in the ``samples/cxx`` subdirectory of the Cantera installation directory,
which have the paths and lists of libraries correctly configured for the
system on which they are installed.

.. container:: container

   .. container:: row

      .. container:: col-4 text-center offset-4

         .. container:: btn btn-primary
            :tagname: a
            :attributes: href=index.html

            Return: C++ Interface Tutorial

      .. container:: col-4 text-right

         .. container:: btn btn-primary
            :tagname: a
            :attributes: href=headers.html

            Next: C++ Header Files
