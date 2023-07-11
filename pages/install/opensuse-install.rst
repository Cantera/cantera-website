.. title: Installing Cantera on openSUSE 
.. date: 2022-01-23 16:16:00 UTC+02:00
.. description: Installation instructions for Cantera on openSUSE
.. type: text
.. _sec-install-opensuse:

.. jumbotron::

   .. raw:: html

      <h1 class="display-4">Installing on openSUSE</h1>

   .. class:: lead

      RPM packages are provided for openSUSE Tumbleweed.
      Note that the Matlab interface is not available from this archive;
      to install the Matlab interface on openSUSE, you must :ref:`compile the source code <sec-compiling>`.

As of Cantera 2.6.0, packages are available for openSUSE Tumbleweed from a
community repository.

Installation is as follows:

.. code-block:: bash

   $ zypper addrepo https://download.opensuse.org/repositories/home:fuller/openSUSE_Tumbleweed/home:fuller.repo
   $ zypper refresh
   $ zypper install cantera
