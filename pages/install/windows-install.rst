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
      installation instructions are for Cantera 2.5.1. Use these installers if you
      want to work with a copy of Python downloaded from `Python.org
      <https://www.python.org/>`__. If you are using Anaconda / Miniconda, see the
      directions :ref:`for conda <sec-install-conda>`.

**Choose your Python version and architecture**

- On Windows, Installers are provided for Python 3.5, Python 3.6, Python 3.7,
  Python 3.8 and Python 3.9. You can install multiple Cantera Python modules
  simultaneously.

- Cantera supports both 32- and 64-bit Python installations.

- You need choose the matching Cantera installer for your Python version and
  machine architecture.

- The rest of these instructions will refer to your chosen version of Python
  as *3.X*.

- If you are using Matlab, you must use the same architecture for Cantera and
  Matlab. Matlab defaults to 64-bit if you are running a 64-bit operating
  system.

**Install Python**

- Go to `python.org <https://www.python.org/>`__.

  - *64-bit*: Download the most recent "Windows X86-64 MSI Installer" for
    Python *3.X*.
  - *32-bit*: Download the most recent "Windows x86 MSI Installer" for
    Python *3.X*.

- Run the installer. The default installation options should be fine.

- Python is required in order to work with ``.cti`` input files even if you are
  not using the Python interface to Cantera.

- Cantera can also be used with alternative Python distributions such as the
  `Enthought distribution <https://www.enthought.com/enthought-deployment-manager/>`__.
  These distributions will generally be based on the 64-bit
  version of Python, and will include Numpy as well as many other
  packages useful for scientific users.

**Install required and optional Python packages**

- If you plan on using Cantera from Python, note that we highly recommend
  installing the `conda package </install/conda-install.html>`__ instead of
  using the standalone installer. Installation with this procedure is sufficient
  if you will mainly be using a different interface, such as Matlab.

- Open a Command Prompt. If you chose to install Python for all users, you
  should open the Command Prompt as Administrator.

- Install Cantera's required dependencies by running:

  .. code:: bash

     py -m pip install numpy ruamel.yaml

- Some Cantera features and examples require additional Python packages.
  These can be installed by running:

  .. code:: bash

     py -m pip install h5py pandas matplotlib

- You may also want to install IPython, an advanced interactive Python interpreter:

  .. code:: bash

     py -m pip install ipython


**Remove old versions of Cantera**

- Use The Windows "Add/Remove Programs" interface

- Remove both the main Cantera package and the Python module.

- The Python module will be listed as "Python *3.X* Cantera ..."

**Install Cantera**

- Go to the `Cantera Releases <https://github.com/Cantera/cantera/releases>`_
  page.

  - *64-bit*: Download **Cantera-2.5.1-x64.msi** and
    **Cantera-Python-2.5.1-x64-py3.X.msi**.
  - *32-bit*: Download **Cantera-2.5.1-x86.msi** and
    **Cantera-Python-2.5.1-x86-py3.Y.msi**.

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
     gas = cantera.Solution('gri30.yaml')
     h2o = cantera.PureFluid('liquidvapor.yaml', 'water')

- Matlab:

  .. code-block:: matlab

     gas = IdealGasMix('gri30.yaml')
     h2o = Solution('liquidvapor.yaml','water')
