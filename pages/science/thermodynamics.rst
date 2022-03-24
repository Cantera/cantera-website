.. slug: thermodynamics
.. has_math: true
.. title: Calculating phase and species thermodynamics

.. jumbotron::

   .. raw:: html

      <h1 class="display-3">Calculating thermodynamic properties in Cantera</h1>

   .. class:: lead

      Here, we describe how Cantera uses species and phase information to calculate thermodynamic properties. 
      
   Thermodynamic properties typically depend on information at both the species and phase levels. The user must specify thermodynamic models for both levels, and these selections must be compatible with one another. For instance: one cannot pair a non-ideal species thermodyamic model with an ideal phase model.

   - The user must specify a thermodynamic model for each species and provide inputs that inform how species-specific properties are calculated. For example, the user specifies how the reference enthalpy and entropy values for each species are calcualted, as a function of temperature.
   - The user also selects a phase model. This model describes how the species interact with one another to determine phase properties and species specific properties, for a given thermodynamic state. This includes general :math:`P-\hat{v}-T` behavior (for example, calculate the phase pressure for a given molar volume, temperature, and chemical composition), as well as how species-specific properties, such as internal energy, entropy, and others depend on the state variables

Example: The Ideal Gas Model
============================
For a simple example: in the Ideal Gas model, one might use 7-parameter NASA polynomials to specify the species thermodynamics.  These would be used to calculate the reference molar enthalpy :math:`\hat{h}_k^\circ(T)` and entropy :math:`\hat{s}_k^\circ(T)` for a given species :math:`k` as a function of temperature :math:`T`:

.. math::

   \frac{\hat{h}^\circ_k (T)}{\overline{R} T} = a_0 + \frac{a_1}{2} T + \frac{a_2}{3} T^2 +
                         \frac{a_3}{4} T^3 + \frac{a_4}{5} T^4 + \frac{a_5}{T}

   \frac{\hat{s}^\circ_k(T)}{\overline{R}} = a_0 \ln T + a_1 T + \frac{a_2}{2} T^2 + \frac{a_3}{3} T^3 +
                      \frac{a_4}{4} T^4 + a_6

At the phase level, the Ideal Gas Law determines the state, for example the pressure as a function of molar volume :math:`\hat{v}`, and temperature :math:`T`:

.. math::
   p = \frac{\overline{R}T}{v}

where :math:`\overline{R}` is the Universal Gas Constant. The phase model also dictates how the state variables influence the species thermodynamic quantities at a given state. For a species :math:`k`, for example, the Ideal Gas Model specifies that the specific molar internal energy :math:`\hat{u}_k` and entropy :math:`s_k` will be:

.. math::
   \hat{u}_k = \hat{h}^\circ_k(T) - p\hat{v}X_k

   \hat{s}_k = \hat{s}^\circ_k(T) - \overline{R}T\ln\left(\frac{pX_k}{p^\circ}\right)

where :math:`X_k` is the mole fraction of species :math:`k`, and where :math:`p^\circ` is the reference pressure at which the properties :math:`\hat{h}_k^\circ(T)` and :math:`\hat{s}_k^\circ(T)` are known.

Please click either of the cards below for details on specific species and phase models available in Cantera:

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

               The models and equations that Cantera uses to calculate species thermodynamic properties.

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

      