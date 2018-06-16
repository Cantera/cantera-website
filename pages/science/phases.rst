.. slug: phases
.. hidetitle: true
.. has_math: true

Modeling Phases in Cantera
==========================

Here, we describe some of the most commonly-used phase models in Cantera.

Bulk, Three-Dimensional Phases
##############################

Ideal Gas Mixtures
------------------

Far and away, the most commonly-used phase model in Cnatera is the
:class:`ideal_gas` model. Many combustion and CVD simulations make use of
reacting ideal gas mixtures. These can be defined using the :class:`ideal_gas`
entry. The Cantera ideal gas model allows any number of species, and any number
of reactions among them. It supports all of the options in the widely-used model
described by Kee et al. [#Kee1989]_, plus some additional options for species
thermodynamic properties and reaction rate expressions.

An example of an ``ideal_gas`` entry is shown below:

.. code:: python

    ideal_gas(name='air8',
              elements='N O Ar',
              species='gri30: N2 O2 N O NO NO2 N2O AR',
              reactions='all',
              transport='Mix',
              initial_state=state(temperature=500.0,
                                  pressure=(1.0, 'atm'),
                                  mole_fractions='N2:0.78, O2:0.21, AR:0.01'))

This entry defines an ideal gas mixture that contains 8 species, the definitions
of which are imported from dataset gri30 (file ``gri30.xml``). All reactions
defined in the file are to be included, transport properties are to be computed
using mixture rules, and the state of the gas is to be set initially to 500 K, 1
atm, and a composition that corresponds to air.

Transport Models
^^^^^^^^^^^^^^^^

Two transport models are available for use with ideal gas mixtures. The first is
a multicomponent transport model that is based on the model described by
Dixon-Lewis [#dl68]_ (see also Kee et al. [#Kee2003]_). The second is a model
that uses mixture rules. To select the multicomponent model, set the transport
field to the string ``'Multi'``, and to select the mixture-averaged model, set
it to the string ``'Mix'``:

.. code:: python

    ideal_gas(name="gas1",
              # ...
              transport="Multi", # use multicomponent formulation
              # ...
              )

    ideal_gas(name="gas2",
              # ...
              transport="Mix", # use mixture-averaged formulation
              # ...
              )

Stoichiometric Solid
--------------------

A :class:`stoichiometric_solid` is one that is modeled as having a precise,
fixed composition, given by the composition of the one species present. A
stoichiometric solid can be used to define a condensed phase that can
participate in heterogeneous reactions. (Of course, there cannot be homogeneous
reactions, since the composition is fixed.) :

.. code:: python

    stoichiometric_solid(name='graphite',
                         elements='C',
                         species='C(gr)',
                         density=(2.2, 'g/cm3'),
                         initial_state=state(temperature=300.0,
                                             pressure=(1.0, 'atm')))

In the example above, the definition of the species ``'C(gr)'`` must appear
elsewhere in the input file.

Stoichiometric Liquid
---------------------

A stoichiometric liquid differs from a stoichiometric solid in only one respect:
the transport manager computes the viscosity as well as the thermal
conductivity.

Interfaces
##########

Now that we have seen how to define bulk, three-dimensional phases, we can
describe the procedure to define an interface between phases.

Cantera presently implements a simple model for an interface that treats it as a
two-dimensional ideal solution of interfacial species. There is a fixed site
density :math:`n^0`, and each site may be occupied by one of several adsorbates,
or may be empty. The chemical potential of each species is computed using the
expression for an ideal solution:

.. math::

    \mu_k = \mu^0_k + \hat{R}T \log \theta_k,

where :math:`\theta_k` is the coverage of species :math:`k` on the surface. The
coverage is related to the surface concentration :math:`C_k` by

.. math::

    \theta_k = \frac{C_k n_k}{n^0} ,

where :math:`n_k` is the number of sites covered or blocked by species
:math:`k`.

The entry type for this interface model is
:class:`ideal_interface`. (Additional interface models may be added to allow
non-ideal, coverage-dependent properties.)

Defining an interface is much like defining a phase. There are two new fields:
``phases`` and ``site_density``. The ``phases`` field specifies the bulk phases that
participate in the heterogeneous reactions. Although in most cases this string
will list one or two phases, no limit is placed on the number. This is
particularly useful in some electrochemical problems, where reactions take place
near the triple-phase boundary where a gas, an electrolyte, and a metal all meet.

The ``site_density`` field is the number of adsorption sites per unit area.

Another new aspect is in the embedded :class:`state` entry in the
``initial_state`` field. When specifying the initial state of an interface, the
:class:`state` entry has a field *coverages*, which can be assigned a string
specifying the initial surface species coverages:

.. code:: python

    ideal_interface(name='silicon_surface',
                    elements='Si H',
                    species='s* s-SiH3 s-H',
                    reactions='all',
                    phases='gas bulk-Si',
                    site_density=(1.0e15, 'molec/cm2'),
                    initial_state=state(temperature=1200.0,
                                        coverages='s-H:1'))


The State Entry
===============

The initial state of either a phase or an interface may be set using an embedded
:class:`state` entry. Note that only one of (``pressure``, ``density``) may be
specified, and only one of (``mole_fractions``, ``mass_fractions``, ``coverages``).


.. rubric:: References

.. [#Kee1989] R. J. Kee, F. M. Rupley, and J. A. Miller. Chemkin-II: A Fortran
   chemical kinetics package for the analysis of gasphase chemical
   kinetics. Technical Report SAND89-8009, Sandia National Laboratories, 1989.

.. [#dl68] G. Dixon-Lewis. Flame structure and flame reaction kinetics,
   II: Transport phenomena in multicomponent systems. *Proc. Roy. Soc. A*,
   307:111--135, 1968.

.. [#Kee2003] R. J. Kee, M. E. Coltrin, and P. Glarborg. *Chemically Reacting
   Flow: Theory and Practice*. John Wiley and Sons, 2003.
