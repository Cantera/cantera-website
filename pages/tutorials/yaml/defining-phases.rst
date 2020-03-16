.. slug: defining-phases
.. title: Defining Phases

.. jumbotron::

   .. raw:: html

      <h1 class="display-3">Defining Phases</h1>

   .. class:: lead

      A guide to Cantera's YAML input file format

Virtually every Cantera simulation involves one or more phases of matter.
Depending on the calculation being performed, it may be necessary to evaluate
thermodynamic properties, transport properties, and/or reaction rates for the
phase(s) present. Before the properties can be evaluated, each phase must be
defined, meaning that the models to use to compute its properties and reaction
rates must be specified, along with any parameters the models require.

Because the amount of data required can be quite large, this data is imported
from a YAML file that can be read by the application, so that a given phase
model can be re-used for other simulations.

This guide describes how to write such files to define phases and interfaces for
use in Cantera simulations. Each link below represents a standalone module -
while you certainly can read them in order, you can also jump to whichever
section addresses your current needs. If you need tips on troubleshooting the
YAML file syntax rules, please look at the :doc:`YAML Format Tutorial <yaml-format>`.

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

            For each phase that appears in a problem, a corresponding entry
            should be present in the input file(s). We'll start by describing
            the entries for phases of various types, and then look at how to
            define interfaces between phases.

   .. container:: card

      .. container::
         :tagname: a
         :attributes: href=yaml-species.html
                      title="Elements and Species"

         .. container:: card-header section-card

            Elements and Species

      .. container:: card-body

         .. container:: card-text

            For each species declared as part of a phase description, both the
            species and the elements that it is comprised of must be defined.
            Here, we describe how both are defined.

   .. container:: card

      .. container::
         :tagname: a
         :attributes: href=reactions.html
                      title="Reactions"

         .. container:: card-header section-card

            Reactions

      .. container:: card-body

         .. container:: card-text

            Cantera supports a number of different types of reactions, including
            several types of homogeneous reactions, surface reactions, and
            electrochemical reactions. For each, there is a corresponding entry
            type. Here, we describe how to declare each type of reaction and
            provide the necessary parameters to calculate the reaction rate for
            each.

Additional Information
======================

.. container:: card-deck

   .. container:: card

      .. container::
         :tagname: a
         :attributes: href=yaml-format.html
                      title="YAML Format Tutorial"

         .. container:: card-header section-card

            YAML Format Tutorial

      .. container:: card-body

         .. container:: card-text

            This module describes the basics of the YAML format as used by
            Cantera, how dimensional values are represented, and how to
            understand error messages that occur while reading input files.

   .. container:: card

      .. container::
         :tagname: a
         :attributes: href={{% ct_dev_docs sphinx/html/yaml/index.html %}}
                      title="YAML Format Reference"

         .. container:: card-header section-card

            YAML Format Reference

      .. container:: card-body

         .. container:: card-text

            The documentation of the YAML format, containing the specification
            for each of the entry types discussed previously, for when you
            require more detail.
