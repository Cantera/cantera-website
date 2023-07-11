.. title: Installing Cantera on Windows
.. slug: windows-install
.. date: 2018-08-23 20:16:00 UTC-04:00
.. description: Installation instructions for Cantera on Windows
.. type: text
.. _sec-install-windows:

.. jumbotron::

   .. raw:: html

      <h1 class="display-4">Installing on Windows</h1>

   .. class:: lead

      Windows installers are provided for stable versions of Cantera. These installers
      provide the Matlab toolbox and header/library files that can be used to compile
      C++ applications.

To install the Cantera Python package, see the :ref:`pip <sec-install-pip>` or
:ref:`conda <sec-install-conda>` instructions. The Python package is required if:

- You need to convert Chemkin-format input files to YAML
- You need to convert legacy CTI or XML input files to YAML

**Remove old versions of Cantera**

- Use The Windows "Add/Remove Programs" interface to remove previous versions of
  the `Cantera` package.

**Install Cantera**

- Go to the `Cantera Releases <https://github.com/Cantera/cantera/releases>`_
  page and download **Cantera-3.0.0-x64.msi**.

- Run the installer and follow the prompts.

**Configure Matlab**

- Launch Matlab

- Go to *File->Set Path...*

- Select *Add with Subfolders*

- Browse to the folder ``C:\Program Files\Cantera\matlab\toolbox``

- Select *Save*, then *Close*.

**Test the installation**

- From the Matlab prompt, run:

  .. code-block:: matlab

     gas = Solution('gri30.yaml')
     h2o = Solution('liquidvapor.yaml', 'water')
