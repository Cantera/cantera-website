.. slug: thermodynamics
.. has_math: true
.. title: Calculating phase and species thermodynamics

.. jumbotron::

   .. raw:: html

      <h1 class="display-3">Calculating thermodynamic properties in Cantera</h1>

   .. class:: lead

      Here, we describe how Cantera uses species and phase information to calculate thermodynamic properties. Thermodynamic properties typically depend on information at both the species and phase levels.

      - The user must specify a thermodynamic model for each species and provide inputs that inform how species-specific properties are calculated (e.g. as a function of temperature).
      - The user also selects a phase model. This model describes how the species interact with one another to determine overall phase properties. This includes general :math:`P-v-T` behavior, as well as how species-specific properties are used to calculate phase-average properties such as internal energy, entropy, etc.  


.. container:: container
   :tagname: section

   .. container:: card-deck

      .. container:: card

         .. container::
            :tagname: a
            :attributes: href=species.html
                         title=Species

            .. container:: card-header section-card
               :tagname: div

               Species

         .. container:: card-body

            .. container:: card-text

               The models and equations that Cantera uses to calculate species thermdynamic properties.

      .. container:: card

         .. container::
            :tagname: a
            :attributes: href=phases.html
                         title=Phases

            .. container:: card-header section-card
               :tagname: div

               Phases

         .. container:: card-body

            .. container:: card-text

               The theory behind some of Cantera's phase models.

      