.. title: Installing Cantera on FreeBSD
.. date: 2021-12-17 14:16:00 UTC-05:00
.. description: Installation instructions for Cantera on FreeBSD
.. type: text
.. _sec-install-freebsd:

.. jumbotron::

   .. raw:: html

      <h1 class="display-3">Installing on FreeBSD</h1>

   .. class:: lead

      A FreeBSD package is maintained by the Cantera community in the ``science`` port.
      Note that the Matlab interface is not available from this port; to install the
      Matlab interface on FreeBSD, you must :ref:`compile Cantera's source code
      <sec-compiling>`.

Further information about the Cantera package can be found on `FreeBSD.org
<https://www.freebsd.org/cgi/ports.cgi?query=cantera&stype=all>`__ and `FreshPorts.org
<https://www.freshports.org/science/cantera/>`__. The package can be installed via

.. code:: shell

   pkg install cantera
