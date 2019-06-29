.. slug: reactions
.. title: Reactions
.. has_math: true

.. jumbotron::

   .. raw:: html

      <h1 class="display-3">Reactions</h1>

   .. class:: lead

      A description of how reactions are defined in YAML input files

Common Attributes
=================

All of the entry types that define reactions share some common features. These
are described first, followed by descriptions of the individual reaction types
in the following sections.

The Reaction Equation
~~~~~~~~~~~~~~~~~~~~~

The reaction equation determines the reactant and product stoichiometry.

The ID String
-------------

.. _sec-reaction-options:

Options
-------

Certain conditions are normally flagged as errors by Cantera. In some cases,
they may not be errors, and the options field can be used to specify how they
should be handled.

Reaction Orders
---------------


.. container:: container

   .. container:: row

      .. container:: col-4 text-left

         .. container:: btn btn-primary
            :tagname: a
            :attributes: href=yaml-species.html
                         title="Elements and Species"

            Previous: Elements and Species

      .. container:: col-4 text-center

         .. container:: btn btn-primary
            :tagname: a
            :attributes: href=defining-phases.html
                         title="Defining Phases"

            Return: Defining Phases

      .. container:: col-4 text-right

         .. container:: btn btn-primary
            :tagname: a
            :attributes: href=yaml-format.html
                         title="YAML Format Tutorial"

            Next: YAML Format Tutorial

.. rubric:: References

.. [#Westbrook1981] C. K. Westbrook and F. L. Dryer. Simplified reaction
   mechanisms for the oxidation of hydrocarbon fuels in flames. *Combustion
   Science and Technology* **27**, pp. 31--43. 1981.
