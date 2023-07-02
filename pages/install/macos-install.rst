.. title: Installing Cantera on macOS
.. slug: macos-install
.. date: 2018-08-23 20:16:00 UTC-04:00
.. description: Installation instructions for Cantera on macOS/Mac OS X
.. type: text
.. _sec-install-macos:

.. jumbotron::

   .. raw:: html

      <h1 class="display-3">Installing on macOS

   .. class:: lead

      The Cantera Matlab toolbox can be installed using a macOS-specific installer. The
      toolbox requires macOS/Mac OS X version 10.11 (El Capitan) or higher and a 64-bit
      Intel or M1 processor.

To install the Cantera Python package, see the :ref:`pip <sec-install-pip>` or
:ref:`conda <sec-install-conda>` instructions. The Python package is required if:

- You need to convert legacy input files to YAML
- You need to convert Chemkin-format input files to YAML

**Download and run the Matlab Interface Installer**

Download the Matlab Interface Installer package from GitHub:
https://github.com/Cantera/cantera/releases/tag/v2.6.0

When the file has downloaded, find it in Finder, hold Control and click the file. Choose
"Open" from the resulting menu, and select "Open" in the security dialog that appears.
Click "Continue" to proceed in the installer (noting that the installer may open in the background;
you can find its icon on the Dock), agreeing to the
`Cantera license terms <https://github.com/Cantera/cantera/blob/v2.6.0/License.txt>`__
and the terms of the other open source software that we use.

By default, the installer will add some lines to the file ``$HOME/Documents/MATLAB/startup.m``
to enable loading the Cantera toolbox when Matlab starts. If you wish to disable this, click
"Customize" and de-select the "Install startup.m script" option. Finally, clicking "Install"
will install the interface to the ``$HOME/Applications/Cantera`` folder.

**Test the installation**

Open Matlab and enter the following code:

.. code-block:: matlab

   gas = Solution('gri30.yaml')
   h2o = Solution('liquidvapor.yaml','water')

If the installer cannot find the Cantera Python package, it will cause a warning message
to be printed to the Matlab console when Matlab starts. To resolve this, edit the ``startup.m``
script to include the path to the Python interpreter where Cantera is installed in the
line containing ``PYTHON_CMD``.
