.. slug: reactions
.. title: Reactions
.. has_math: true

.. jumbotron::

   .. raw:: html

      <h1 class="display-3">Reactions</h1>

   .. class:: lead

      A description of how reactions are defined in CTI input files

Basic Reactions
===============

Cantera supports a number of different types of reactions, including several
types of homogeneous reactions, surface reactions, and electrochemical
reactions. For each, there is a corresponding entry type. The simplest entry
type is :cti:class:`reaction`, which can be used for any homogeneous reaction that
has a rate expression that obeys the law of mass action, with a rate coefficient
that depends only on temperature.

Common Attributes
=================

All of the entry types that define reactions share some common features. These
are described first, followed by descriptions of the individual reaction types
in the following sections.

The Reaction Equation
~~~~~~~~~~~~~~~~~~~~~

The reaction equation determines the reactant and product stoichiometry. A
relatively simple parsing strategy is currently used, which assumes that all
coefficient and species symbols on either side of the equation are delimited by
spaces:

.. code:: python

   2 CH2 <=> CH + CH3  # OK
   2 CH2<=>CH + CH3  # OK
   2CH2 <=> CH + CH3  # error
   CH2 + CH2 <=> CH + CH3  # OK
   2 CH2 <=> CH+CH3  # error

The incorrect versions here would generate "undeclared species" errors and would
halt processing of the input file. In the first case, the error would be that
the species ``2CH2`` is undeclared, and in the second case it would be species
``CH+CH3``.

Whether the reaction is reversible or not is determined by the form of the
equality sign in the reaction equation. If either ``<=>`` or ``=`` is found,
then the reaction is regarded as reversible, and the reverse rate will be
computed from detailed balance. If, on the other hand, ``=>`` is found, the
reaction will be treated as irreversible.

The rate coefficient is specified with an embedded entry corresponding to the
rate coefficient type. At present, the only implemented type is the modified
Arrhenius function

.. math::

   k_f(T) = A T^b \exp(-E/\bar{R}T)

which is defined with an :cti:class:`Arrhenius` entry:

.. code:: python

   rate_coeff=Arrhenius(A=1.0e13, b=0, E=(7.3, 'kcal/mol'))
   rate_coeff=Arrhenius(1.0e13, 0, (7.3, 'kcal/mol'))

As a shorthand, if the ``rate_coeff`` field is assigned a sequence of three
numbers, these are assumed to be :math:`(A, b, E)` in the modified Arrhenius
function:

.. code:: python

   rate_coeff=[1.0e13, 0, (7.3, 'kcal/mol')]  # equivalent to above

The units of the pre-exponential factor :math:`A` can be specified explicitly if desired. If not
specified, they will be constructed using the ``quantity``, ``length``, and ``time`` units specified
in the :cti:class:`units` directive. Since the units of :math:`A` depend on the reaction order, the
units of each reactant concentration (different for bulk species in solution, surface species, and
pure condensed-phase species), and the units of the rate of progress (different for homogeneous and
heterogeneous reactions), it is usually best not to specify units for :math:`A`, in which case they
will be computed taking all of these factors into account.

Note: if :math:`b \ne 0`, then the term :math:`T^b` should have units of
:math:`K^b`, which would change the units of :math:`A`. This is not done, however, so
the units associated with :math:`A` are really the units for :math:`k_f` . One way to
formally express this is to replace :math:`T^b` by the non-dimensional quantity
:math:`[T/(1 K)]^b`.

The ID String
-------------

An optional identifying string can be entered in the ``ID`` field, which can
then be used in the ``reactions`` field of a :cti:class:`phase` or interface entry
to identify this reaction. If omitted, the reactions are assigned ID strings as
they are read in, beginning with ``'0001'``, ``'0002'``, etc.

Note that the ID string is only used when selectively importing reactions. If
all reactions in the local file or in an external one are imported into a phase
or interface, then the reaction ``ID`` field is not used.

.. _sec-reaction-options:

Options
-------

Certain conditions are normally flagged as errors by Cantera. In some cases,
they may not be errors, and the options field can be used to specify how they
should be handled.

``skip``
    The ``'skip'`` option can be used to temporarily remove this reaction from
    the phase or interface that imports it, just as if the reaction entry were
    commented out. The advantage of using skip instead of commenting it out is
    that a warning message is printed each time a phase or interface definition
    tries to import it. This serves as a reminder that this reaction is not
    included, which can easily be forgotten when a reaction is "temporarily"
    commented out of an input file.

``duplicate``
    Normally, when a reaction is imported into a phase, it is checked to see
    that it is not a duplicate of another reaction already present in the phase,
    and an error results if a duplicate is found. But in some cases, it may be
    appropriate to include duplicate reactions, for example if a reaction can
    proceed through two distinctly different pathways, each with its own rate
    expression. Another case where duplicate reactions can be used is if it is
    desired to implement a reaction rate coefficient of the form:

    .. math::

       k_f(T) = \sum_{n=1}^{N} A_n T^{b_n} exp(-E_n/\hat{R}T)

    While Cantera does not provide such a form for reaction rates, it can be
    implemented by defining *N* duplicate reactions, and assigning one rate
    coefficient in the sum to each reaction. If the ``'duplicate'`` option is
    specified, then the reaction not only *may* have a duplicate, it *must*. Any
    reaction that specifies that it is a duplicate, but cannot be paired with
    another reaction in the phase that qualifies as its duplicate generates an
    error.

``negative_A``
    If some of the terms in the above sum have negative :math:`A_n`, this scheme
    fails, since Cantera normally does not allow negative pre-exponential
    factors. But if there are duplicate reactions such that the total rate is
    positive, then negative :math:`A` parameters are acceptable, as long as the
    ``'negative_A'`` option is specified.

``negative_orders``
    Reaction orders are normally required to be non-negative, since negative
    orders are non-physical and undefined at zero concentration. Cantera allows
    negative orders for a global reaction only if the ``negative_orders``
    override option is specified for the reaction.

Reaction Orders
---------------

Explicit reaction orders different from the stoichiometric coefficients are
sometimes used for non-elementary reactions. For example, consider the global
reaction:

.. math::

   \mathrm{C_8H_{18} + 12.5 O_2 \rightarrow 8 CO_2 + 9 H_2O}

the forward rate constant might be given as [#Westbrook1981]_:

.. math::

   k_f = 4.6 \times 10^{11} [\mathrm{C_8H_{18}}]^{0.25} [\mathrm{O_2}]^{1.5}
         \exp\left(\frac{30.0\,\mathrm{kcal/mol}}{RT}\right)

This reaction could be defined as:

.. code:: python

   reaction("C8H18 + 12.5 O2 => 8 CO2 + 9 H2O", [4.6e11, 0.0, 30.0],
            order="C8H18:0.25 O2:1.5")

Special care is required in this case since the units of the pre-exponential
factor depend on the sum of the reaction orders, which may not be an integer.

Note that you can change reaction orders only for irreversible reactions.

Normally, reaction orders are required to be positive. However, in some cases
negative reaction orders are found to be better fits for experimental data. In
these cases, the default behavior may be overridden by adding
``negative_orders`` to the reaction options, e.g.:

.. code:: python

   reaction("C8H18 + 12.5 O2 => 8 CO2 + 9 H2O", [4.6e11, 0.0, 30.0],
            order="C8H18:-0.25 O2:1.75", options=['negative_orders'])

Some global reactions could have reactions orders for non-reactant species. One
should add ``nonreactant_orders`` to the reaction options to use this feature:

.. code:: python

   reaction("C8H18 + 12.5 O2 => 8 CO2 + 9 H2O", [4.6e11, 0.0, 30.0],
            order="C8H18:-0.25 CO:0.15",
            options=['negative_orders', 'nonreactant_orders'])

.. container:: container

   .. container:: row

      .. container:: col-4 text-left

         .. container:: btn btn-primary
            :tagname: a
            :attributes: href=cti-species.html
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
            :attributes: href=cti-processing.html
                         title="Processing CTI Files"

            Next: Processing CTI Files

.. rubric:: References

.. [#Gilbert1983] R. G. Gilbert, K. Luther, and
   J. Troe. *Ber. Bunsenges. Phys. Chem.*, 87:169, 1983.

.. [#Lindemann1922] F. Lindemann. *Trans. Faraday Soc.*, 17:598, 1922.

.. [#Smith1997] Gregory P. Smith, David M. Golden, Michael Frenklach, Nigel
   W. Moriarty, Boris Eiteneer, Mikhail Goldenberg, C. Thomas Bowman, Ronald
   K. Hanson, Soonho Song, William C. Gardiner, Jr., Vitali V. Lissianski, , and
   Zhiwei Qin. GRI-Mech version 3.0, 1997. see
   http://www.me.berkeley.edu/gri_mech.

.. [#Stewart1989] P. H. Stewart, C. W. Larson, and D. Golden.
   *Combustion and Flame*, 75:25, 1989.

.. [#Kee1989] R. J. Kee, F. M. Rupley, and J. A. Miller. Chemkin-II: A Fortran
   chemical kinetics package for the analysis of gas-phase chemical
   kinetics. Technical Report SAND89-8009, Sandia National Laboratories, 1989.

.. [#Westbrook1981] C. K. Westbrook and F. L. Dryer. Simplified reaction
   mechanisms for the oxidation of hydrocarbon fuels in flames. *Combustion
   Science and Technology* **27**, pp. 31--43. 1981.
