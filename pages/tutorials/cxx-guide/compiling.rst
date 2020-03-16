.. title: Compiling Cantera C++ Programs

.. jumbotron::

   .. raw:: html

      <h1 class="display-3">Compiling Cantera C++ Programs</h1>

   .. class:: lead

      This guide shows you how to build C++ programs that use Cantera's features

Build Systems
*************

In general, it should be possible to use Cantera with any build system by
specifying the appropriate header and library paths, and specifying the required
libraries when linking. It is also necessary to specify the paths for libraries
used by Cantera, such as Sundials, BLAS, and LAPACK.

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

   env.Append(CCFLAGS='-g',
              CPPPATH=['/usr/local/cantera/include',
                       '/usr/local/sundials/include'],
              LIBS=['cantera', 'sundials_cvodes', 'sundials_ida',
                    'sundials_nvecserial', 'lapack', 'blas'],
              LIBPATH=['/usr/local/cantera/lib',
                       '/usr/local/sundials/lib'],
              LINKFLAGS=['-g', '-pthread'])

   sample = env.Program('sample', 'sample.cpp')
   Default(sample)

This script establishes what SCons refers to as a "construction environment"
named ``env``, and sets the header (``CPPPATH``) and library (``LIBPATH``) paths
to include the directories containing the Cantera headers and libraries, as well
as libraries that Cantera depends on, such as Sundials, BLAS, and LAPACK. Then,
a program named ``sample`` is compiled using the single source file
``sample.cpp``.

Several other example ``SConstruct`` files are included with the C++ examples
contained in the ``samples`` subdirectory of the Cantera installation directory.

For more information on SCons, see the `SCons Wiki <http://scons.org/wiki/>`__
and the `SCons homepage <http://www.scons.org>`__.

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
   set(CMAKE_CXX_STANDARD 11)

   find_package(Threads REQUIRED)

   include_directories("/opt/cantera/include" "/opt/sundials-2.7.0/include")
   link_directories("/opt/cantera/lib" "/opt/sundials-2.7.0/lib")

   add_executable(sample sample.cpp)
   target_link_libraries(sample cantera sundials_cvodes sundials_ida sundials_nvecserial fmt Threads::Threads)

Several example ``CMakeLists.txt`` files are included with the C++ examples
contained in the ``samples`` subdirectory of the Cantera installation directory,
which have the paths and lists of libraries correctly configured for system on
which they are installed.

Make
====

Cantera is distributed with an "include Makefile" that can be used with
Make-based build systems. This file ``Cantera.mak`` is located in the
``samples`` subdirectory of the Cantera installation directory. To use it, add a
line referencing this file to the top of your Makefile:

.. code:: makefile

    include path/to/Cantera.mak

The path specified should be the relative path from the ``Makefile`` to
``Cantera.mak``. This file defines several variables which can be used in your
Makefile. The following is an example ``Makefile`` that uses the definitions
contained in ``Cantera.mak``:

.. code:: makefile

   include ../../Cantera.mak

   CC=gcc
   CXX=g++
   RM=rm -f
   CCFLAGS=-g
   CPPFLAGS=$(CANTERA_INCLUDES)
   LDFLAGS=
   LDLIBS=$(CANTERA_LIBS)

   SRCS=sample.cpp
   OBJS=$(subst .cpp,.o,$(SRCS))

   all: sample

   kinetics1: $(OBJS)
		$(CXX) $(LDFLAGS) -o sample $(OBJS) $(LDLIBS)

   clean:
		$(RM) $(OBJS)

   dist-clean: clean
		$(RM) *~

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
