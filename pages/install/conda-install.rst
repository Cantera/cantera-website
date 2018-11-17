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

      `Anaconda <https://www.anaconda.com/downloads>`__ and
      `Miniconda <https://conda.io/miniconda.html>`__ are Python distributions that include the
      ``conda`` package manager, which can be used to install Cantera. Both distributions are
      available for Linux, macOS, and Windows. Note that installing Cantera using Conda will only
      provide the Cantera Python module. If you want to use the other Cantera interfaces
      (to use Cantera from MATLAB, Fortran, C++, or C) then see the
      :ref:`OS-specific installation options <sec-install>`.

Anaconda and Miniconda both include ``conda``; the difference is that Anaconda includes a large
number of Python packages that are widely used in scientific applications, while Miniconda is a
minimal distribution that only includes Python and Conda, although all of the packages available in
Anaconda can be installed in Miniconda. For more details on how to use conda, see the `conda
documentation <https://conda.io/docs/intro.html>`__.

**Option 1: Create a new environment for Cantera**

If you have just installed Anaconda or Miniconda, the following instructions
will create a conda environment where you can use Cantera. For this example, the
environment is named ``spam``. From the command line (or the Anaconda Prompt
on Windows), run::

    conda create --name spam --channel cantera cantera ipython matplotlib

This will create an environment with Cantera, IPython, Matplotlib, and all their
dependencies installed. Although Conda can install a large set of packages by
default, it is also possible to install packages such as Cantera that are
maintained independently. These additional channels from which packages may be
obtained are specified by adding the ``--channel`` option in the ``install`` or
``create`` commands. In this case, we want to install Cantera from the
``cantera`` channel, so we add ``--channel cantera`` and to tell Conda to look at the
``cantera`` channel in addition to the default channels.

To use the scripts and modules installed in the ``spam`` environment,
you must activate it it by running::

    conda activate spam

**Option 2: Install Cantera in an existing environment**

First, activate your environment (assumed here to be named ``baked_beans``; if you've
forgotten the name of the conda environment you wanted to use, the command
``conda env list`` can help). This is done by running::

    conda activate baked_beans

Then, install Cantera in the active enironment by running::

    conda install --channel cantera cantera

**Option 3: Install the development version of Cantera**

To install a recent development snapshot (i.e., an alpha or beta version) of
Cantera in an existing environment, activate the environment and then run::

    conda install --channel cantera/label/dev cantera

If you later want to revert back to the stable version, first remove and then
reinstall Cantera::

    conda remove cantera
    conda install --channel cantera cantera
