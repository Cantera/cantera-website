.. slug: phase-thermo
.. has_math: true
.. title: Modeling Phases

.. jumbotron::

   .. raw:: html

      <h1 class="display-4">Modeling Phase Thermodynamics in Cantera</h1>

   .. class:: lead

      Here, we describe some of the most commonly-used phase models in Cantera.

Bulk, Three-Dimensional Phases
##############################

Ideal Gas Mixtures
------------------

Far and away, the most commonly-used phase model in Cantera is the **ideal gas** model.
Many combustion and CVD simulations make use of reacting ideal gas mixtures. The Cantera
ideal gas model allows any number of species, and any number of reactions among them.
It supports all of the options in the widely-used model described by Kee et al.
[#Kee1989]_, plus some additional options for species thermodynamic properties
and reaction rate expressions.

Ideal gas mixtures can be defined in the YAML format by specifying
:ref:`ideal-gas <sec-yaml-ideal-gas>` in the ``thermo`` field.

Stoichiometric Solid
--------------------

A **stoichiometric solid** is one that is modeled as having a precise, fixed composition,
given by the composition of the one species present. A stoichiometric solid can be used to define a
condensed phase that can participate in heterogeneous reactions. (Of course, there cannot be
homogeneous reactions, since the composition is fixed.)

A stoichiometric solid can be defined in the YAML format by specifying
:ref:`fixed-stoichiometry <sec-yaml-fixed-stoichiometry>` in the ``thermo`` field.

Interfaces
##########

Cantera presently implements a simple model for an interface between phases that treats it as a
two-dimensional ideal solution of interfacial species. There is a fixed site density :math:`n^0`,
and each site may be occupied by one of several adsorbates, or may be empty. The chemical potential
of each species is computed using the expression for an ideal solution:

.. math::

   \mu_k = \mu^0_k + RT \log \theta_k,

where :math:`\theta_k` is the coverage of species :math:`k` on the surface. The coverage is related
to the surface concentration :math:`C_k` by

.. math::

   \theta_k = \frac{C_k n_k}{n^0} ,

where :math:`n_k` is the number of sites covered or blocked by species :math:`k`.

An interface can be defined in the YAML format by specifying
:ref:`ideal-surface <sec-yaml-ideal-surface>` in the ``thermo`` field.


.. rubric:: References

.. [#Kee1989] R. J. Kee, F. M. Rupley, and J. A. Miller. Chemkin-II: A Fortran
   chemical kinetics package for the analysis of gasphase chemical
   kinetics. Technical Report SAND89-8009, Sandia National Laboratories, 1989.
