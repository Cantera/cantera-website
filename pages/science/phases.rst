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

Ideal gas mixtures can be defined in the CTI format using the
:cti:class:`ideal_gas` entry, or in the YAML format by specifying
:ref:`ideal-gas <sec-yaml-ideal-gas>` in the ``thermo`` field.

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
:cti:class:`stoichiometric_solid` entry, or in the YAML format by specifying
:ref:`fixed-stoichiometry <sec-yaml-fixed-stoichiometry>` in the ``thermo`` field.

Plasma
------

The **plasma** model support the features in **ideal gas** model. In addition, it calculate electron
energy distribution function (EEDF) and EEDF-dependent properties, which includes electron transport
properties and plasma reaction rate coefficients. The electron Boltzmann equation in an ionized gas is

.. math::

   \frac{\partial f}{\partial t} + \bm{v} \cdot \nabla f - \frac{e}{m}\bm{E} \cdot \nabla_\bm{v} f = C[f],

where :math:`f` is the electron distribution in six-dimensional phase space,
:math:`\bm{v}` are the velocity coordinates, :math:`e` is the elementary charge,
:math:`m` is the electron mass, :math:`\bm{E}` is the electric field,
:math:`\nabla_\bm{v}` is the velocity-gradient operator and
:math:`C` represents the rate of change in :math:`f` due to collisions.


Weakly-Ionized Gas Model
^^^^^^^^^^^^^^^^^^^^^^^^

This model assumes that the electron number density is low so that the collision between two electrons
is neglected. The EEDF can be calculated by the electron Boltzmann equation with two-term approximation
[#Hag2005]_,

.. math::

   \frac{d}{d \epsilon}\left(\tilde{W} F_0 - \tilde{D} \frac{d F_0}{d \epsilon}\right)
   = \tilde{S},

.. math::

   \tilde{W} = -\gamma\epsilon^2\sigma_{\epsilon},

.. math::

   \tilde{D} = \frac{\gamma}{3} \left(\frac{E}{N} \right)^2 \frac{\epsilon}{\tilde{\sigma}_m} +
                 \frac{\gamma k_B T}{e} \epsilon^2 \sigma_{\epsilon},

.. math::

   \tilde{S} = \sum_{k} \tilde{C}_{0,k} + G,

where :math:`\gamma = (\frac{2 e}{m})^{1/2}`, :math:`\epsilon` is the electron energy,
:math:`\sigma_{\epsilon}` is the total elastic collision cross section,
:math:`E` is electric field strength, :math:`N` is gas number density,
:math:`\tilde{\sigma}_m` is the effective total momentum-transfer cross section,
:math:`k_B` is Boltzmann constant, :math:`e` is the elementary charge,
:math:`\tilde{C}_{0,k}` represents the rate of change in EEDF due to collisions,
:math:`k` is the index of inelastic collision process, and :math:`F_0` is the normalized EEDF.

The inelastic collision terms are,

.. math::

   \tilde{C}_{0,k} = -\gamma X_k \epsilon \sigma_k F_0
                                \big|^{\epsilon=\epsilon}_{\epsilon=\epsilon + u_k},

.. math::

   \tilde{C}_{0,k} = -\gamma X_k \epsilon \sigma_k F_0
                                \big|^{\epsilon=\epsilon}_{\epsilon=2\epsilon + u_k},

.. math::

   \tilde{C}_{0,k} = -\gamma X_k \epsilon \sigma_k F_0,

respectively for excitation, ionization, and attchment collision processes. The exponential temporal growth
model is used to calculate :math:`G`.

.. math::

   G = \left[ \int_0^\infty \left(\sum_{k=ionization} X_k \sigma_k - \sum_{k=attachment} X_k \sigma_k \right)
       \epsilon F_0 d \epsilon \right] \epsilon^{1/2} F_0,

where :math:`X_k` is the mole fraction of the target species, and :math:`\sigma_k` is the cross section.

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

An interface can be defined in the CTI format using the
:cti:class:`ideal_interface` entry, or in the YAML format by specifying
:ref:`ideal-surface <sec-yaml-ideal-surface>` in the ``thermo``
field.


.. rubric:: References

.. [#Kee1989] R. J. Kee, F. M. Rupley, and J. A. Miller. Chemkin-II: A Fortran
   chemical kinetics package for the analysis of gasphase chemical
   kinetics. Technical Report SAND89-8009, Sandia National Laboratories, 1989.

.. [#dl68] G. Dixon-Lewis. Flame structure and flame reaction kinetics,
   II: Transport phenomena in multicomponent systems. *Proc. Roy. Soc. A*,
   307:111--135, 1968.

.. [#Kee2017] R. J. Kee, M. E. Coltrin, P. Glarborg, and H. Zhu. *Chemically Reacting Flow:
   Theory and Practice*. 2nd Ed. John Wiley and Sons, 2017.

.. [#Hag2005] G. J. M. Hagelaar and L. C. Pitchford. Solving the Boltzmann equation
   to obtain electron transport coefficients and rate coefficients for fluid models.
   *Plasma Sources Science and Technology* 14.4:722, 2005.