.. title: Installing Cantera on Gentoo
.. slug: gentoo-install
.. date: 2019-06-26 20:00:00 UTC-04:00
.. description: Installation instructions for Cantera on Gentoo
.. type: text
.. _sec-install-gentoo:

.. jumbotron::

   .. raw:: html

      <h1 class="display-3">Installing on Gentoo</h1>

   .. class:: lead

      Gentoo `sci-libs/cantera <https://packages.gentoo.org/packages/sci-libs/cantera>`__ package is provided using a main portage tree.
      Additionally the `app-doc/cantera-docs <https://packages.gentoo.org/packages/app-doc/cantera-docs>`__ package
      is provided for offline Documentation API reference for Cantera package libraries.
      Note that the Matlab interface is not available from this package; to install the
      Matlab interface on Gentoo, you must :ref:`compile the source code <sec-compiling>`.

The following interfaces and tools are installed by default:

- C++ Libraries and header files for compiling your own programs that use Cantera.

- `YAML tools <../tutorials/ck2yaml-tutorial.html>`__.

- Python module for Python 3 (``python`` USE flag with appropriate ``PYTHON_SINGLE_TARGET``, optional).

The following additional interface is available:

- Fortran Library and module files for compiling your own programs that use Cantera (``fortran`` USE flag, optional)

More information about ``USE flags`` can be found in the `Gentoo Handbook <https://wiki.gentoo.org/wiki/Handbook:Parts/Working/USE>`__.
To know about per-package control of ``USE flags`` please refer to the `/etc/portage/package.use <https://wiki.gentoo.org/wiki//etc/portage/package.use>`__ article.

To install ``sci-libs/cantera`` and ``app-doc/cantera-docs`` packages:

.. code-block:: bash

    emerge --ask cantera cantera-docs

Most likely the latest versions of these packages and/or some of their dependencies still have unstable status in the Gentoo portage tree
and then you have to ``unmask`` (allow to install within stable system) them preliminarily using `/etc/portage/package.accept_keywords <https://wiki.gentoo.org/wiki//etc/portage/package.accept_keywords>`__.

If ``/etc/portage/package.accept_keywords`` is present in your system as file then (for 64-bit architecture) you could unmask ``sci-libs/cantera`` package by running command (as root)

.. code-block:: bash

    echo "sci-libs/cantera ~amd64" >> /etc/portage/package.accept_keywords

Otherwise if ``/etc/portage/package.accept_keywords`` is present in your system as directory then run command (as root)

.. code-block:: bash

    echo "sci-libs/cantera ~amd64" >> /etc/portage/package.accept_keywords/cantera

If you plan on using Cantera from Python, you may also want to install IPython
(`dev-python/ipython <https://packages.gentoo.org/packages/dev-python/ipython>`__, an advanced interactive Python interpreter)
and Matplotlib (`dev-python/matplotlib <https://packages.gentoo.org/packages/dev-python/matplotlib>`__, a plotting
library). Matplotlib is required to run some of the Python examples. These packages can be installed with:

.. code-block:: bash

    emerge --ask ipython matplotlib
