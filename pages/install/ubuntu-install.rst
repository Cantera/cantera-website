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

As of Cantera 2.4.0, packages are available for Ubuntu 16.04 (Xenial Xerus) and Ubuntu 18.04 (Bionic
Beaver). To see which Ubuntu releases and Cantera versions are currently available, visit
https://launchpad.net/~speth/+archive/ubuntu/cantera

The available packages are:

- ``cantera-python`` - The Cantera Python module for Python 2.

- ``cantera-python3`` - The Cantera Python module for Python 3.

- ``cantera-dev`` - Libraries and header files for compiling your own C++ and
  Fortran 90 programs that use Cantera.

To add the Cantera PPA:

.. code-block:: bash

   sudo aptitude install python-software-properties
   sudo apt-add-repository ppa:speth/cantera
   sudo aptitude update

To install all of the Cantera packages:

.. code-block:: bash

   sudo aptitude install cantera-python cantera-python3 cantera-dev

or install whichever subset you need by adjusting the above command.

If you plan on using Cantera from Python, you may also want to install IPython
(an advanced interactive Python interpreter) and Matplotlib (a plotting
library). Matplotlib is required to run some of the Python examples. For Python
2, these packages can be installed with:

.. code-block:: bash

    pip2 install ipython matplotlib

And for Python 3, these packages can be installed with:

.. code-block:: bash

    pip3 install ipython matplotlib

You may need to install ``pip`` first; instructions can be found on the `pip
installation instructions <https://pip.pypa.io/en/latest/installing/index.html#install-pip>`__.
You may need to
have superuser access to install packages into the system directories.
Alternatively, you can add ``--user`` after ``pip install`` but before the
package names to install into your local user directory.
