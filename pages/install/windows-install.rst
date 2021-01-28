.. title: Installing Cantera on Windows
.. slug: windows-install
.. date: 2018-08-23 20:16:00 UTC-04:00
.. description: Installation instructions for Cantera on Windows
.. type: text
.. _sec-install-windows:

.. jumbotron::

   .. raw:: html

      <h1 class="display-3">Installing on Windows</h1>

   .. class:: lead

      Windows installers are provided for stable versions of Cantera. These
      installation instructions are for Cantera 2.4.0. Use these installers if you
      want to work with a copy of Python downloaded from `Python.org
      <https://www.python.org/>`__. If you are using Anaconda / Miniconda, see the
      directions :ref:`for conda <sec-install-conda>`.

**Choose your Python version and architecture**

- On Windows, Installers are provided for Python 3.6, Python 3.7, Python 3.8
  and Python 3.9. You can install multiple Cantera Python modules simultaneously.

- Cantera supports both 32- and 64-bit Python installations.

- You need choose the matching Cantera installer for your Python version and
  machine architecture.

- The rest of these instructions will refer to your chosen version of Python
  as *X.Y*.

- If you are using Matlab, you must use the same architecture for Cantera and
  Matlab. Matlab defaults to 64-bit if you are running a 64-bit operating
  system.

**Install Python**

- Go to `python.org <https://www.python.org/>`__.

  - *64-bit*: Download the most recent "Windows X86-64 MSI Installer" for
    Python *X.Y*.
  - *32-bit*: Download the most recent "Windows x86 MSI Installer" for
     Python *X.Y*.

- Run the installer. The default installation options should be fine.

- Python is required in order to work with ``.cti`` input files even if you are
  not using the Python interface to Cantera.

- Cantera can also be used with alternative Python distributions such as the
  `Enthought distribution <https://www.enthought.com/enthought-deployment-manager/>`__.
  These distributions will generally be based on the 64-bit
  version of Python, and will include Numpy as well as many other
  packages useful for scientific users.

**Install NumPy and optional Python packages**

- Go to the `Unofficial Windows Binaries for Python Extension Packages page
  <http://www.lfd.uci.edu/~gohlke/pythonlibs/#numpy>`_.

- Download the most recent release (distributed as a "wheel" archive) of the
  1.x series for Python *X.Y* that matches your Python architecture. In the
  filename, the digits after "cp" indicate the Python version. For example,
  ``numpy‑1.11.2+mkl‑cp37‑none‑win_amd64.whl`` is the installer for 64-bit
  Python 3.7. The Windows installers for Cantera 2.4.0 require NumPy 1.10 or
  newer.

- From an administrative command prompt, install the downloaded wheel using
  pip. For example::

      c:\python37\scripts\pip.exe install "%USERPROFILE%\Downloads\numpy‑1.11.2+mkl‑cp37‑none‑win_amd64.whl"

- If you plan on using Cantera from Python, note that we highly recommend
  installing the conda package. If you plan to continue using this Python
  installation, you may also want to install IPython (an advanced
  interactive Python interpreter) and Matplotlib (a plotting library), which
  are also available from the above link (note that you may also need to
  download additional dependencies for each of these packages). Matplotlib
  is required to run some of the Python examples.

**Remove old versions of Cantera**

- Use The Windows "Add/Remove Programs" interface

- Remove both the main Cantera package and the Python module.

- The Python module will be listed as "Python *3.X* Cantera ..."

**Install Cantera**

- Go to the `Cantera Releases <https://github.com/Cantera/cantera/releases>`_
  page.

  - *64-bit*: Download **Cantera-2.4.0-x64.msi** and
    **Cantera-Python-2.4.0-x64-pyX.Y.msi**.
  - *32-bit*: Download **Cantera-2.4.0-x86.msi** and
    **Cantera-Python-2.4.0-x86-pyX.Y.msi**.

- If you are only using the Python module, you do not need to download and
  install the base package (the one without Python in the name).

- Run the installer(s).

**Configure Matlab** (optional)

- Set the environment variable ``PYTHON_CMD``

  - From the *Start* screen or menu type "edit environment" and select
    "Edit environment variables for your account".
  - Add a *New* variable with ``PYTHON_CMD`` as the *name* and the full path
    to the Python executable (for example, ``C:\python37\python.exe``) as the
    *value*.
  - Setting ``PYTHON_CMD`` is not necessary if the path to ``python.exe`` is
    in your ``PATH`` (which can be set from the same configuration dialog).

- Launch Matlab

- Go to *File->Set Path...*

- Select *Add with Subfolders*

- Browse to the folder ``C:\Program Files\Cantera\matlab\toolbox``

- Select *Save*, then *Close*.

**Test the installation**

- Python:

  .. code-block:: python

     import cantera
     gas = cantera.Solution('gri30.cti')
     h2o = cantera.PureFluid('liquidvapor.cti', 'water')

- Matlab:

  .. code-block:: matlab

     gas = IdealGasMix('gri30.cti')
     h2o = Solution('liquidvapor.cti','water')
