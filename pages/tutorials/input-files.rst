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

The required input files can be provided via one of several methods:

- Use one of the pre-existing input files that are distributed with Cantera (note that
  these input files are provided for convenience, and may not be suited for research)
- Convert a pre-existing mechanism from Chemkin (CK) format to YAML format *(New
  in Cantera 2.5)*
- Create your own YAML file from scratch or by editing an existing file *(New in
  Cantera 2.5)*

The first option will suffice for tutorials and introductory work with thermodynamic
phases and reaction kinetics. Most modern reaction mechanisms are published in Chemkin
(CK) format, and can be converted to Cantera's YAML format using the ``ck2yaml``
conversion tool (option 2). Advanced users may, however, need to edit an existing input
file in order to define additional species, reactions, or entirely new phases. Even if
you need to create an entirely new input file, it is still advisable to start from an
existing file, to cut down on syntax errors.

Whenever you edit a Cantera input file, it is *highly advised* that you begin by copying the existing file and
saving it under a new name, before editing the new file. Editing a file under its original name can
easily lead to errors, if one forgets that this file does not represent the original mechanism.

Input files distributed with Cantera
====================================

Several reaction mechanism files are included in the Cantera distribution,
including ones that model natural gas combustion (``gri30.yaml``), high-temperature air
(``air.yaml``), a hydrogen/oxygen reaction mechanism (``h2o2.yaml``), some pure fluids in the
liquid-vapor region (``liquidvapor.yaml``), and a few surface reaction mechanisms (such as
``ptcombust.yaml``, ``diamond.yaml``, etc.), among others. Under Windows, these files may be located
in ``C:\Program Files\Cantera\data`` depending on how you installed Cantera and the options you
specified. On a Unix/Linux/macOS machine, they are usually kept in the ``data`` subdirectory
within the Cantera installation directory.

Please see the tutorials for :doc:`Python <python-tutorial>` and :doc:`Matlab <matlab-tutorial>`
for instructions on how to import from these pre-existing files.

Converting or Creating New Input Files
======================================

If you want to model a phase not available in the input files distributed with Cantera, you will need
to either procure a new input file (there are a limited number of input files available on the web), or
create a new one.

There are three primary options for creating a new Cantera input file:

.. container:: container

   .. row::

      .. container:: card-deck

         .. container:: card

            .. container::
               :tagname: a
               :attributes: href=ck2yaml-tutorial.html
                            title="Chemkin File Conversion"

               .. container:: card-header section-card

                  Conversion from Chemkin to YAML

            .. container:: card-body

               .. container:: card-text

                  Convert a Chemkin-formatted ('CK') file to the Cantera YAML
                  format. *(New in Cantera 2.5)*

         .. container:: card

            .. container::
               :tagname: a
               :attributes: href="yaml/defining-phases.html"
                            title="Defining Phases in YAML"

               .. container:: card-header section-card

                  Create a new YAML file

            .. container:: card-body

               .. container:: card-text

                  Create a completely new mechanism, by defining new species,
                  phases, and/or reactions, using the YAML format.
                  *(New in Cantera 2.5)*

   .. row::

      .. container:: card-deck

         .. container:: card

            .. container::
               :tagname: a
               :attributes: href="legacy2yaml.html"
                            title="Converting CTI and XML input files to YAML"

               .. container:: card-header section-card

                  Convert CTI and XML input files to YAML

            .. container:: card-body

               .. container:: card-text

                  Convert existing Cantera mechanisms in the legacy CTI or XML
                  formats to the YAML format. *(New in Cantera 2.5)*

         .. container:: card

            .. container::
               :tagname: a
               :attributes: href="thermobuild.html"
                            title="Importing data from NASA ThermoBuild"

               .. container:: card-header section-card

                  Importing data from NASA ThermoBuild

            .. container:: card-body

               .. container:: card-text

                  Import thermodynamic data for a range of species from this
                  web-based tool.

Understanding Input File Syntax
===============================

For any of these options (adapting an existing Cantera input file, converting from CK, or creating a new input
file), it can be helpful to understand the input file syntax requirements. Clearly, anyone writing directly
in the YAML formats must conform to these standards. However, even when importing an
externally-provided file or converting from CK format, understanding the input file syntax can
help diagnose and correct any errors (although many/most of the CK conversion errors will be related
to errors in the CK syntax formatting).

.. container:: card-deck

   .. container:: card

      .. container::
         :tagname: a
         :attributes: href="yaml/yaml-format.html"
                      title="YAML Format Tutorial"

         .. container:: card-header section-card

            YAML Format Tutorial

      .. container:: card-body

         .. container:: card-text

            This tutorial covers the details of the YAML format and its syntax.
            *(New in Cantera 2.5)*
