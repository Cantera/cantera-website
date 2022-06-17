.. title: Compiling Cantera from Source
.. slug: compiling-install
.. date: 2018-08-23 20:16:00 UTC-04:00
.. description: Compiling Cantera from Source
.. type: text
.. _sec-compiling:

.. jumbotron::

   .. raw:: html

      <h1 class="display-3">Compiling Cantera from Source</h1>

   .. class:: lead

      Compiling Cantera from source code uses the SCons build system and a C/C++ compiler. If
      you also want to build the Python, Matlab, or Fortran interfaces, you'll need Cython +
      Numpy, Matlab, or a Fortran compiler installed, respectively. Specific instructions to
      install these things are platform-dependent, and more detail is provided in the sections
      linked below.

**Quickstart**

The recommended way to obtain a copy of the source code is directly from the main
version control repository on GitHub via the command

.. code-block:: bash

   git clone https://github.com/Cantera/cantera.git
   cd cantera

which clones the code into a folder called ``cantera`` and changes into that directory.
At this point, you can run

.. code-block:: bash

   scons help

to see a list of all of the configuration options, including their defaults. On
\*nix-type systems, the defaults will usually pick up the appropriate compilers and
Python versions. The command

.. code-block:: bash

   scons build

will build Cantera using all the default options; additional options can be specified
by

.. code-block:: bash

   scons build option=value option=value

Installing Cantera into the default directories is done by

.. code-block:: bash

   scons install

which may require super-user permissions if the installation directory is protected.

**Compiling Cantera from Source: The Detailed Way**

If you want or need more detail, the following sections go into depth on all of the
options and requirements to build Cantera from source.

* :ref:`Installation Requirements <sec-installation-reqs>`
* :ref:`Getting the Source Code <sec-source-code>`
* :ref:`Determine Configuration Options <sec-determine-config>`
* :ref:`Cantera's Dependencies <sec-dependencies>`
* :ref:`Special Compiling Cases <sec-special-compiling-cases>`
* :ref:`Show me all of the configuration options <scons-config>`
