.. slug: phases
.. has_math: true
.. title: Modeling Phases

.. jumbotron::

   .. raw:: html

      <h1 class="display-3">Modeling Phases in Cantera</h1>

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

Ideal gas mixtures can be defined in the CTI format using the :cti:class:`ideal_gas` entry.

.. _sec-transport-models:

Transport Models
^^^^^^^^^^^^^^^^

Two transport models are available for use with ideal gas mixtures. The first is a multicomponent
transport model that is based on the model described by Dixon-Lewis [#dl68]_ (see also Kee et al.
[#Kee2017]_). The second is a model that uses the mixture-averaged rule.

Stoichiometric Solid
--------------------

A **stoichiometric solid** is one that is modeled as having a precise, fixed composition,
given by the composition of the one species present. A stoichiometric solid can be used to define a
condensed phase that can participate in heterogeneous reactions. (Of course, there cannot be
homogeneous reactions, since the composition is fixed.)

A stoichiometric solid can be defined in the CTI format using the
:cti:class:`stoichiometric_solid` entry.


Interfaces
##########

Cantera presently implements a simple model for an interface between phases that treats it as a
two-dimensional ideal solution of interfacial species. There is a fixed site density :math:`n^0`,
and each site may be occupied by one of several adsorbates, or may be empty. The chemical potential
of each species is computed using the expression for an ideal solution:

.. math::

   \mu_k = \mu^0_k + \hat{R}T \log \theta_k,

where :math:`\theta_k` is the coverage of species :math:`k` on the surface. The coverage is related
to the surface concentration :math:`C_k` by

.. math::

   \theta_k = \frac{C_k n_k}{n^0} ,

where :math:`n_k` is the number of sites covered or blocked by species :math:`k`.

An interface can be defined in the CTI format using the :cti:class:`ideal_interface` entry.


.. rubric:: References

.. [#Kee1989] R. J. Kee, F. M. Rupley, and J. A. Miller. Chemkin-II: A Fortran
   chemical kinetics package for the analysis of gasphase chemical
   kinetics. Technical Report SAND89-8009, Sandia National Laboratories, 1989.

.. [#dl68] G. Dixon-Lewis. Flame structure and flame reaction kinetics,
   II: Transport phenomena in multicomponent systems. *Proc. Roy. Soc. A*,
   307:111--135, 1968.

.. [#Kee2017] R. J. Kee, M. E. Coltrin, P. Glarborg, and H. Zhu. *Chemically Reacting Flow:
   Theory and Practice*. 2nd Ed. John Wiley and Sons, 2017.
