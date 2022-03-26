.. title: Installing Cantera on Ubuntu
.. slug: ubuntu-install
.. date: 2018-08-23 20:16:00 UTC-04:00
.. description: Installation instructions for Cantera on Ubuntu
.. type: text
.. _sec-install-ubuntu:

.. jumbotron::

   .. raw:: html

      <h1 class="display-3">Installing on Ubuntu</h1>

   .. class:: lead

      Ubuntu packages are provided for recent versions of Ubuntu using a Personal Package Archive
      (PPA). Note that the Matlab packages are not available from this archive; to install the
      Matlab packages on Ubuntu, you must :ref:`compile the source code <sec-compiling>`.

As of Cantera 2.5.1, packages are available for Ubuntu 18.04 (Bionic Beaver), Ubuntu 20.04
(Focal Fossa), Ubuntu 20.10 (Groovy Gorilla), Ubuntu 21.04 (Hirsute Hippo), and
Ubuntu 21.10 (Impish Indri). To see which Ubuntu releases and Cantera versions are
currently available, visit https://launchpad.net/~cantera-team/+archive/ubuntu/cantera.

The available packages are:

- ``cantera-python3`` - The Cantera Python module for Python 3.

- ``cantera-dev`` - Libraries and header files for compiling your own C++ and
  Fortran 90 programs that use Cantera.

- ``cantera-common`` - Cantera data files and example programs

To add the Cantera PPA:

.. code-block:: bash

   sudo apt install software-properties-common
   sudo apt-add-repository ppa:cantera-team/cantera

To install all of the Cantera packages:

.. code-block:: bash

   sudo apt install cantera-python3 cantera-dev

or install whichever subset you need by adjusting the above command. The ``cantera-common``
package is installed as a dependency if any other Cantera packages are selected.

If you plan on using Cantera from Python, you may also want to install IPython
(an advanced interactive Python interpreter) and Matplotlib (a plotting
library). Matplotlib is required to run some of the Python examples. These packages
can be installed with:

.. code-block:: bash

    sudo apt install python3-pip
    pip3 install ipython matplotlib

Upgrading from an earlier Cantera version
-----------------------------------------

If you already have Cantera installed from the ``cantera-team`` PPA, you can ensure that
you have the latest available version installed by running:

.. code-block:: bash

    sudo apt update
    sudo apt install cantera-python3

If you also have the ``cantera-dev`` package installed, it should also be included on
the ``apt install`` command line.
