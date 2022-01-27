.. title: Installing Cantera on Fedora
.. date: 2022-01-23 16:16:00 UTC+02:00
.. description: Installation instructions for Cantera on Fedora
.. type: text
.. _sec-install-fedora-rhel:

.. jumbotron::

   .. raw:: html

      <h1 class="display-3">Installing on Fedora</h1>

   .. class:: lead

      RPM packages are provided for supported versions of Fedora Linux using a Community Projects
      (COPR) repository. Note that the Matlab interface is not available from this archive;
      to install the Matlab interface on Fedora, you must :ref:`compile the source code <sec-compiling>`.

As of Cantera 2.6.0, packages are available for currently supported releases of Fedora Linux
and Fedora Rawhide as well as Enterprise Linux 8.

The available packages are:

- ``python3-cantera`` - The Cantera Python module for Python 3.

- ``cantera-devel`` - Shared object libraries and header files for compiling your own C++ and
  Fortran 90 programs that use Cantera.

- ``cantera-common`` - Cantera data files and example programs.

- ``cantera-static`` - Static libraries for C++ and Fortran 90 development.

Cantera is available in the official repositories for Fedora - no configuration
changes are required.

On Enterprise Linux, if not already enabled, add the "Extra Packages for Enterprise
Linux" (EPEL) repository:

.. code-block:: bash

   $ dnf install epel-release

To install all of the Cantera packages:

.. code-block:: bash

   $ dnf install python3-cantera cantera-devel

or install whichever subset you need by adjusting the above command. The ``cantera-common``
package is installed as a dependency if any other Cantera packages are selected.

If you plan on using Cantera from Python, you may also want to install IPython
(an advanced interactive Python interpreter) and Matplotlib (a plotting
library). Matplotlib is required to run some of the Python examples. These packages
can be installed with:

.. code-block:: bash

    $ dnf install python3-matplotlib python3-ipython
