.. slug: transport
.. has_math: true
.. title: Calculating phase and species transport properties and rates

.. jumbotron::

   .. raw:: html

      <h1 class="display-3">Calculating transport properties and rates in Cantera</h1>

   .. class:: lead

      Here, we describe how Cantera uses species and phase information to calculate transport properties and rates.

   Similar to Cantera's approach to `thermodynamic properties </science/thermodynamics.html>`__, transport property calculations in Cantera depend on information at both the species and phase levels. The user must specify transport models for both levels, and these selections must be compatible with one another. 
   
   - The user must specify a transport model for each species and provide inputs that inform how species properties are calculated. For example, the user provides inputs that allow Cantera to calculate species collision integrals based on species-specific Lennard-Jones parameters.
   - The user also selects a phase model. This model describes how the species interact with one another to determine phase-averaged properties (such viscosity or thermal conductivity) and species specific properties (such as diffusion coefficients), for a given thermodynamic state.
  
Species Transport Coefficients
------------------------------

Transport property models in general require coefficients that express the
effect of each species on the transport properties of the phase. Currently,
ideal-gas transport property models are implemented.

Transport properties can be defined in the YAML format using the
:ref:`transport <sec-yaml-species-transport>` field of a ``species`` entry.

.. _sec-phase-transport-models:

Phase Transport Models
----------------------

Two transport models are available for use with ideal gas mixtures. The first is a multicomponent
transport model that is based on the model described by Dixon-Lewis [#dl68]_ (see also Kee et al.
[#Kee2017]_). The second is a model that uses the mixture-averaged rule.



.. rubric:: References

.. [#dl68] G. Dixon-Lewis. Flame structure and flame reaction kinetics,
   II: Transport phenomena in multicomponent systems. *Proc. Roy. Soc. A*,
   307:111--135, 1968.

.. [#Kee2017] R. J. Kee, M. E. Coltrin, P. Glarborg, and H. Zhu. *Chemically Reacting Flow:
   Theory and Practice*. 2nd Ed. John Wiley and Sons, 2017.