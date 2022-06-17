.. title: Installing Cantera with Conda
.. slug: conda-install
.. date: 2018-08-23 20:16:00 UTC-04:00
.. description: Installation instructions for Cantera using Conda
.. type: text
.. _sec-install-conda:

.. jumbotron::

    .. raw:: html

        <h1 class="display-3">Installing with Conda</h1>

    .. class:: lead

      `Anaconda <https://www.anaconda.com/products/individual#Downloads>`__ and
      `Miniconda <https://docs.conda.io/en/latest/miniconda.html>`__ are Python
      distributions that include the ``conda`` package manager, which can be used to
      install Cantera.

Both the Anaconda and Miniconda distributions are available for Linux, macOS (Intel and
ARM/M1), and Windows. Note that installing Cantera using Conda will only provide
the Cantera :ref:`Python <sec-conda-python-interface>` or :ref:`MATLAB
<sec-conda-matlab-interface>` interfaces. If you want to use the other Cantera
interfaces (to use Cantera from Fortran, C++, or C) then see the :ref:`OS-specific
installation options <sec-install>`. Windows users should install a 64-bit version of
Anaconda or Miniconda, since the Cantera Conda packages are only available for 64-bit
installations.

Both Anaconda and Miniconda include the ``conda`` package manager; the difference is
that Anaconda includes a large number of Python packages that are widely used in
scientific applications, while Miniconda is a minimal distribution that only includes
Python and Conda, although all of the packages available in Anaconda can be installed in
Miniconda. For more details on how to use conda, see the `conda
documentation <https://docs.conda.io/projects/conda/en/latest/user-guide/index.html>`__.

Conda can install a large set of packages by default and it is possible to install
packages such as Cantera that are maintained independently. These additional channels
from which packages may be obtained are specified by adding the ``--channel`` option in
the ``install`` or ``create`` commands.

For instructions on upgrading an existing conda-based installation of Cantera, see
:ref:`Upgrading from an earlier Cantera version <sec-conda-python-upgrade>`.

.. _sec-conda-python-interface:

Python interface
================

Cantera's Python interface is available from two channels:

1. The official ``cantera`` channel. This channel should be used if you installed
   Python from the default channel in conda. This channel also has pre-release versions
   of Cantera for testing. Cantera packages are available in this channel for the
   following platforms:

   - Windows (32- and 64-bit Intel)
   - Linux (64-bit Intel)
   - macOS (64-bit Intel)

2. The ``conda-forge`` channel. This channel should be used if you installed Python from
   the ``conda-forge`` channel or if your OS/processor combination is not supported by
   the ``cantera`` channel. Cantera packages are available in this channel for the
   following platforms:

   - Linux (64-bit Intel, 64-bit ARM, and 64-bit PPCLE)
   - macOS (64-bit Intel and 64-bit ARM (M1))

**Option 1: Create a new environment for Cantera**

The following instructions will create a conda environment where you can use Cantera
from Python. For this example, the environment is named ``ct-env``. From the command
line (or the Anaconda Prompt on Windows), run:

.. code:: shell

   conda create --name ct-env --channel cantera cantera ipython matplotlib jupyter

This will create an environment with Cantera, IPython, Matplotlib, and all their
dependencies installed. In this case, we want to install Cantera from the
``cantera`` channel, so we add ``--channel cantera`` and to tell Conda to look at the
``cantera`` channel in addition to the default channels.

If you want to use the ``conda-forge`` channel, replace ``--channel cantera`` with
``--channel conda-forge``.

To use the scripts and modules installed in the ``ct-env`` environment, including Jupyter,
you must activate it it by running:

.. code:: shell

   conda activate ct-env

**Option 2: Create a new environment using an environment file**

This option is similar to **Option 1** but includes a few other packages that
you may find helpful as you're working with Cantera. Copy and paste the contents
of the file shown below into a file called ``environment.yaml``. Then, save the
the file somewhere and remember that location.

.. code:: yaml

   name: ct-env
   channels:
   - cantera  # or use cantera/label/dev for alpha/beta packages
   - defaults
   dependencies:
   - python  # Cantera supports Python 3.7 and up
   - cantera
   - ipython  # optional (needed for nicer interactive command line)
   - jupyter  # optional (needed for Jupyter Notebook)
   - matplotlib  # optional (needed for plots)
   - python-graphviz  # optional (needed for reaction path diagrams)
   - h5py  # optional (needed for HDF/H5 output)
   - pandas  # optional (needed for pandas interface)

From the command line (or the
Anaconda Prompt on Windows), change directory into the folder where you saved
``environment.yaml``:

.. code:: shell

   cd folder/where/you/saved

and then run:

.. code:: shell

   conda env create -f environment.yaml

This will create an environment called ``ct-env``. Once you've done that, you
need to activate the environment before using any scripts or modules that you
just installed:

.. code:: shell

   conda activate ct-env

**Option 3: Install the development version of Cantera**

To install a recent development snapshot (that is, an alpha or beta version) of
Cantera, use the ``cantera/label/dev`` channel. Assuming you have an environment
named ``ct-dev``, you can type:

.. code:: shell

   conda activate ct-dev
   conda install --channel cantera/label/dev cantera

If you later want to revert back to the stable version in that environment, first
remove and then reinstall Cantera:

.. code:: shell

   conda activate ct-dev
   conda remove cantera
   conda install --channel cantera cantera

Alternatively, you can remove the ``ct-dev`` environment and follow Options 1 or 2
above to create a new environment.

.. _sec-conda-python-upgrade:

Upgrading from an earlier Cantera version
-----------------------------------------

If you already have Cantera installed in a conda environment (named, for example,
``ct-dev``), you can upgrade it to the latest version available by running the commands:

.. code:: shell

   conda activate ct-dev
   conda update --channel cantera cantera

This assumes you are using Python from the default conda channel. If you installed
Python from the ``conda-forge`` channel, you should specify the option
``--channel conda-forge``.

.. _sec-conda-matlab-interface:

MATLAB interface
================

Cantera's MATLAB interface can be installed from the ``cantera`` channel. In this
example, the command will create a new conda environment named ``ct-dev``. From the
command line (or the Anaconda Prompt on Windows), run:

.. code:: shell

   conda create --name ct-dev --channel cantera cantera cantera-matlab

This will create an environment with Cantera's Python and MATLAB interfaces. Even if you
plan to use Cantera via MATLAB, the Python interface is required to convert input files.
In this case, Cantera must be installed from the ``cantera`` channel, so we add
``--channel cantera`` and to tell Conda to look at the ``cantera`` channel in addition
to the default channels.

Upgrading from an earlier Cantera version
-----------------------------------------

If you already have the Cantera MATLAB interface installed in a conda environment
(named, for example, ``ct-dev``), you can upgrade it to the latest version available
by running the commands:

.. code:: shell

   conda activate ct-dev
   conda update --channel cantera cantera cantera-matlab

.. _sec-conda-development-interface:

Development (C++ & Fortran 90) Interface
========================================

**Warning:** The ``conda`` package for Cantera's development interface is experimental.
For the most recent version of the package, use the ``cantera/label/dev`` channel
instead of the stable ``cantera`` channel. The development interface for stable releases
is also available from the ``conda-forge`` channel.

In the following example, Cantera's development interface is installed from the
``cantera/label/dev`` channel. From the command line (or the Anaconda Prompt on
Windows), create a new conda environment named ``ct-dev`` using:

.. code:: shell

   conda create --name ct-dev --channel cantera/label/dev libcantera-devel

This will create an environment with Cantera's development interface. In this case,
the addition of ``--channel cantera/label/dev`` ensures that the package is pulled
from the most recent available Cantera version. Note that ``label/dev`` refers to the
experimental development *channel* of Cantera, and not the development *interface*.

C++ header and libraries are installed within the ``ct-dev`` environment folder, which
itself depends on the type of ``conda`` installation, and is abbreviated as
``path/to/conda/envs`` below. Within the ``ct-dev`` folder, locations follow ``conda``
recommendations for a given operating system.

Linux and macOS Systems
-----------------------

Installation folders for the C++ and Fortran 90 interface are:

.. code:: shell

   library files               path/to/conda/envs/ct-dev/lib
   pkg-config                  path/to/conda/envs/ct-dev/lib/pkgconfig
   C++ headers                 path/to/conda/envs/ct-dev/include
   samples                     path/to/conda/envs/ct-dev/share/cantera/samples
   data files                  path/to/conda/envs/ct-dev/share/cantera/data

In addition to ``libcantera-devel``, installation of additional packages is recommended:

.. code:: shell

   $ conda activate ct-dev
   $ conda install make cmake scons pkg-config

C++ programs can be compiled according to instructions outlined in the
:ref:`C++ Guide <sec-compiling-cplusplus>`. Sample folders for C++ and Fortran include
preconfigured instruction files to facilitate compilation using the build tools
``Make``, ``SCons`` and ``CMake``, for example:

.. code:: shell

   $ cd /path/to/conda/envs/ct-dev/share/cantera/samples/cxx/demo
   $ make  # uses Makefile; or
   $ scons  # uses SConstruct; or
   $ cmake . && cmake --build .  # uses CMakeLists.txt

In addition, individual C++ Cantera sample programs can also be compiled using the
``pkg-config`` build system:

.. code:: shell

   $ export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/path/to/conda/envs/ct-dev/lib
   $ export PKG_CONFIG_PATH=$PKG_CONFIG_PATH:/path/to/conda/envs/ct-dev/lib/pkgconfig
   $ g++ demo.cpp -o demo $(pkg-config --cflags --libs cantera)

In all cases, the build process yields the executable ``demo``, which is run as:

.. code:: shell

   $ ./demo

Windows Systems
---------------

Installation folders for the C++ interface are:

.. code:: shell

   library files               path/to/conda/envs/ct-dev/Library/lib
   C++ headers                 path/to/conda/envs/ct-dev/Library/include
   samples                     path/to/conda/envs/ct-dev/share/cantera/samples
   data files                  path/to/conda/envs/ct-dev/share/cantera/data

The development package on Windows is experimental, with Fortran 90 currently not being
supported.

Upgrading from an earlier Cantera version
-----------------------------------------

If you already have the Cantera development interface installed in a conda environment
(named, for example, ``ct-dev``), you can upgrade it to the latest version available
by running the commands:

.. code:: shell

   conda activate ct-dev
   conda update --channel cantera/label/dev libcantera-devel
