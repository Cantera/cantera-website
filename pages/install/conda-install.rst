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
      install Cantera. Both distributions are available for Linux, macOS (Intel and
      ARM/M1), and Windows. Note that installing Cantera using Conda will only provide
      the Cantera :ref:`Python <sec-conda-python-interface>` or :ref:`MATLAB
      <sec-conda-matlab-interface>` interfaces. If you want to use the other Cantera
      interfaces (to use Cantera from Fortran, C++, or C) then see the :ref:`OS-specific
      installation options <sec-install>`.

Anaconda and Miniconda both include ``conda``; the difference is that Anaconda includes a large
number of Python packages that are widely used in scientific applications, while Miniconda is a
minimal distribution that only includes Python and Conda, although all of the packages available in
Anaconda can be installed in Miniconda. For more details on how to use conda, see the `conda
documentation <https://docs.conda.io/projects/conda/en/latest/user-guide/index.html>`__.

Conda can install a large set of packages by default and it is possible to install
packages such as Cantera that are maintained independently. These additional channels
from which packages may be obtained are specified by adding the ``--channel`` option in
the ``install`` or ``create`` commands.

.. _sec-conda-python-interface:

Python interface
================

Cantera's Python interface is available from two channels:

1. The official ``cantera`` channel. This channel should be used if you installed NumPy
   from the default channel in conda. This channel also has pre-release versions of
   Cantera for testing.
2. The ``conda-forge`` channel. This channel should be used if you installed NumPy from
   the ``conda-forge`` channel. This channel supports more CPU architectures than the
   official channel.

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
   - python  # Cantera supports Python 3.6 and up
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

.. _sec-conda-matlab-interface:

MATLAB interface
================

Cantera's MATLAB interface can be installed from the ``cantera`` channel. In this
example, the command will create a new conda environment named ``ct-env``. From the
command line (or the Anaconda Prompt on Windows), run:

.. code:: shell

   conda create --name ct-env --channel cantera cantera cantera-matlab

This will create an environment with Cantera's Python and MATLAB interfaces. Even if you
plan to use Cantera via MATLAB, the Python interface is required to convert input files.
In this case, Cantera must be installed from the ``cantera`` channel, so we add
``--channel cantera`` and to tell Conda to look at the ``cantera`` channel in addition
to the default channels.
