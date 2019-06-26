.. title: Installing Cantera
.. slug: index
.. date: 2019-06-26 20:00:00 UTC-04:00
.. description: Installation instructions for Cantera
.. type: text

.. _sec-install:

.. jumbotron::

   .. raw:: html

      <h1 class="display-3">Installing Cantera</h1>

   .. class:: lead

      The following instructions detail how to install Cantera on a variety of platforms. We highly
      recommend that all new users install the Python interface via Conda. If you want to use one of
      the other interfaces, please select the installation instructions for your platform.

.. container::

   .. row::

      .. container:: card-deck

         .. container:: card

            .. container:: card-header section-card
               :attributes: id=heading-conda
                            href=conda-install.html
               :tagname: a

               Conda (Highly Recommended)

            .. container:: card-body

               Install the Cantera Python interface with Conda (Highly recommended for all users)

         .. container:: card

            .. container:: card-header section-card
               :attributes: id=heading-windows
                            href=windows-install.html
               :tagname: a

               Windows Install Instructions

            .. container:: card-body

               Install Cantera on Windows. Cantera officially supports the versions of Windows that
               Microsoft presently supports, although it may continue working on older versions of
               Windows.

         .. container:: card

            .. container:: card-header section-card
               :attributes: id=heading-macos
                            href=macos-install.html
               :tagname: a

               macOS Install Instructions

            .. container:: card-body

               Install Cantera on macOS/Mac OS X. The Cantera installer supports Mac OS X version
               10.11 (El Capitan) and higher. For older versions of Mac OS X, users should
               :ref:`compile from source <sec-compiling>`.

.. container::

   .. row::

      .. container:: card-deck

         .. container:: card

            .. container:: card-header section-card
               :attributes: id=heading-ubuntu
                            href=ubuntu-install.html
               :tagname: a

               Ubuntu Install Instructions

            .. container:: card-body

               Install Cantera on Ubuntu using a PPA.

         .. container:: card

            .. container:: card-header section-card
               :attributes: id=heading-gentoo
                            href=gentoo-install.html
               :tagname: a

               Gentoo Install Instructions

            .. container:: card-body

               Install Cantera on Gentoo using a portage.

         .. container:: card

            .. container:: card-header section-card
               :attributes: id=heading-other-linux
                            href=other-linux-install.html
               :tagname: a

               Other Linux Distributions Install Instructions

            .. container:: card-body

               Linux distributions other than Ubuntu and Gentoo can install the Python interface via Conda
               (see :ref:`the Conda instructions <sec-install-conda>`). Other interfaces can be
               installed by :ref:`compiling from source <sec-compiling>`.

.. container::

   .. row::

      .. container:: card-deck

         .. container:: card

            .. container:: card-header section-card
               :attributes: id=heading-compiling
                            href=compiling-install.html
               :tagname: a

               Compile Cantera from Source

            .. container:: card-body

               Compile Cantera directly from the source code for your platform.
