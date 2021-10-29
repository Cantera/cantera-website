.. slug: defining-phases-cti
.. title: Defining Phases

.. jumbotron::

   .. raw:: html

      <h1 class="display-3">Defining Phases</h1>

   .. class:: lead

      A guide to Cantera's legacy CTI input file format

      Note that the legacy CTI input file format will be deprecated in Cantera 2.6
      and fully replaced by the YAML input file format in Cantera 3.0.

Virtually every Cantera simulation involves one or more phases of
matter. Depending on the calculation being performed, it may be necessary to
evaluate thermodynamic properties, transport properties, and/or homogeneous
reaction rates for the phase(s) present. Before the properties can be evaluated,
each phase must be defined, meaning that the models to use to compute its
properties and reaction rates must be specified, along with any parameters the
models require.

Because the amount of data required can be quite large, this data is imported
from a text file that can be read by the application, so that a given
phase model can be re-used for other simulations. This is the Cantera
Input (CTI) file.

This guide describes how to write such files to define phases and interfaces for
use in Cantera simulations. Each link below represents a standalone module -
while you certainly can read them in order, you can also jump to whichever
section addresses your current needs. If you need tips on troubleshooting the
CTI file syntax rules, please look at the :doc:`CTI syntax tutorial <cti-syntax>`.

.. container:: card-deck

   .. container:: card

      .. container::
         :tagname: a
         :attributes: href=phases.html
                      title="Phases and their Interfaces"

         .. container:: card-header section-card

            Phases and their Interfaces

      .. container:: card-body

         .. container:: card-text

            For each phase that appears in a problem, a corresponding entry should be present in the
            input file(s). We'll start by describing the entries for phases of various types, and
            then look at how to define interfaces between phases.

   .. container:: card

      .. container::
         :tagname: a
         :attributes: href=cti-species.html
                      title="Elements and Species"

         .. container:: card-header section-card

            Elements and Species

      .. container:: card-body

         .. container:: card-text

            For each species declared as part of a phase description, both the species and the
            elements that it is comprised of must be defined. Here, we describe how both are
            defined.

   .. container:: card

      .. container::
         :tagname: a
         :attributes: href=reactions.html
                      title="Reactions"

         .. container:: card-header section-card

            Reactions

      .. container:: card-body

         .. container:: card-text

            Cantera supports a number of different types of reactions, including several types of
            homogeneous reactions, surface reactions, and electrochemical reactions. For each, there
            is a corresponding entry type. Here, we describe how to declare each type of reaction
            and provide the necessary parameters to calculate the reaction rate for each.

Additional Information
======================

.. container:: card-deck

   .. container:: card

      .. container::
         :tagname: a
         :attributes: href=cti-processing.html
                      title="Processing Input Files"

         .. container:: card-header section-card

            Processing Input Files

      .. container:: card-body

         .. container:: card-text

            This module describes how a CTI file is processed, and helps debug some errors commonly
            encountered during input file processing.

   .. container:: card

      .. container::
         :tagname: a
         :attributes: href=cti-syntax.html
                      title="CTI Syntax Tutorial"

         .. container:: card-header section-card

            CTI Syntax Tutorial

      .. container:: card-body

         .. container:: card-text

            This module gives an overview of the syntax of CTI files

   .. container:: card

      .. container::
         :tagname: a
         :attributes: href={{% ct_docs sphinx/html/cti/classes.html %}}
                      title="CTI Class Reference"

         .. container:: card-header section-card

            CTI Class Reference

      .. container:: card-body

         .. container:: card-text

            The documentation of the CTI class, containing the specification for each of the
            functions and classes discussed previously, for when you require more detail.
