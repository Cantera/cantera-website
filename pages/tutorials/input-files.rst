.. title: Input Files
.. description: Cantera Input File Tutorial page
.. type: text

.. jumbotron::

   .. raw:: html

      <h1 class="display-3">Working With Input Files</h1>

   .. class:: lead

      As covered in the tutorials (:doc:`Python <python-tutorial>` and :doc:`Matlab
      <matlab-tutorial>`), all calculations in Cantera require an input file to describe the
      properties of the relevant phase(s) of matter.

The required input files can be provided via one of three methods:

- Use one of the pre-existing input files provided with Cantera
- Convert a pre-existing mechanism from Chemkin (CK) format to Cantera (CTI) format
- Create your own CTI file, either from scratch (not recommended) or by editing an existing file

The first two options will suffice for a majority of Cantera users. Advanced
users may, however, need to edit an existing CTI file in order to define
additional species, reactions, or entirely new phases. Even if you need to
create an entirely new CTI file, it is still advisable to start from an existing
file, to cut down on syntax errors.

Whenever you edit a CTI file, it is *highly advised* that you begin by copying the existing file and
saving it under a new name, before editing the new file. Editing a file under its original name can
easily lead to errors, if one forgets that this file does not represent the original mechanism.

CTI files distributed with Cantera
==================================

Several reaction mechanism files in the CTI format are included in the Cantera distribution,
including ones that model natural gas combustion (``gri30.cti``), high-temperature air
(``air.cti``), a hydrogen/oxygen reaction mechanism (``h2o2.cti``), some pure fluids in the
liquid-vapor region (``liquidvapor.cti``), and a few surface reaction mechanisms (such as
``ptcombust.cti``, ``diamond.cti``, etc.), among others. Under Windows, these files may be located
in ``C:\Program Files\Cantera\data`` depending on how you installed Cantera and the options you
specified. On a Unix/Linux/macOS machine, they are usually kept in the ``data`` subdirectory
within the Cantera installation directory.

Please see the tutorials for :doc:`Python <python-tutorial>` and :doc:`Matlab <matlab-tutorial>`
for instructions on how to import from these pre-existing files.

Converting or Creating New CTI Files
====================================

If you want to model a phase not available in the CTI files distributed with Cantera, you will need
to either procure a new CTI file (there are a limited number of CTI files available on the web), or
create a new one.

There are two primary options for creating a new CTI file:

.. container:: container

   .. container:: card-deck

      .. container:: card

         .. container::
            :tagname: a
            :attributes: href=ck2cti-tutorial.html
                         title="Chemkin File Conversion"

            .. container:: card-header section-card

               Conversion from Chemkin

         .. container:: card-body

            .. container:: card-text

               Convert a Chemkin-formatted ('CK') file to the CTI input format.

      .. container:: card

         .. container::
            :tagname: a
            :attributes: href="cti/defining-phases.html"
                         title="Defining Phases"

            .. container:: card-header section-card

               Create a new CTI file

         .. container:: card-body

            .. container:: card-text

               Create a completely new mechanism, by defining new species, phases, and/or reactions.

Understanding CTI Syntax
========================

For any of these options (adapting an external CTI file, converting from CK, or creating a new CTI
file), it can be helpful to understand the CTI syntax requirements. Clearly, anyone writing directly
in the CTI format must conform to these standards. However, even when importing an
externally-provided CTI file or converting from CK format, understanding the CTI file syntax can
help diagnose and correct any errors (although many/most of the CK conversion errors will be related
to errors in the CK syntax formatting).

.. container:: card-deck

   .. container:: card

      .. container::
         :tagname: a
         :attributes: href="cti/cti-syntax.html"
                      title="CTI Syntax Tutorial"

         .. container:: card-header section-card

            CTI Syntax Tutorial

      .. container:: card-body

         .. container:: card-text

            This tutorial covers the details of the CTI format and its syntax
