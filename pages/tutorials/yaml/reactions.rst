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

Cantera supports a number of different types of reactions, including several
types of homogeneous reactions, surface reactions, and electrochemical
reactions. The reaction entries for all reaction types some common features.
These general fields of a reaction entry are described first, followed by fields
used for specific reaction types.

The Reaction Equation
---------------------

The reaction equation, specified in the ``equation`` field of the reaction
entry, determines the reactant and product stoichiometry. All tokens (species
names, stoichiometric coefficients, `+`, and `<=>`) in the reaction equation
must be separated with spaces. Some examples of correctly and incorrectly
formatted reaction equations are shown below:

.. code:: yaml

   - equation: 2 CH2 <=> CH + CH3  # OK
   - equation: 2 CH2<=>CH + CH3  # error - spaces required around '<=>''
   - equation: 2CH2 <=> CH + CH3  # error - space required between '2' and 'CH2'
   - equation: CH2 + CH2 <=> CH + CH3  # OK
   - equation: 2 CH2 <=> CH+CH3  # error - spaces required around '+'

Whether the reaction is reversible or not is determined by the form of the
equality sign in the reaction equation. If either ``<=>`` or ``=`` is found,
then the reaction is regarded as reversible, and the reverse rate will be
computed based on the equilibrium constant. If, on the other hand, ``=>`` is
found, the reaction will be treated as irreversible.

Reaction type
-------------

The type of the rate coefficient parameterization may be specified in the
``type`` field of the ``reaction`` entry. Available reaction types are:

    - :ref:`elementary <sec-yaml-elementary>`
    - :ref:`three-body <sec-yaml-three-body>`
    - :ref:`falloff <sec-yaml-falloff>`
    - :ref:`chemically-activated <sec-yaml-chemically-activated>`
    - :ref:`pressure-dependent-Arrhenius <sec-yaml-pressure-dependent-Arrhenius>`
    - :ref:`Chebyshev <sec-yaml-Chebyshev>`

Additional parameters defining the rate constant for each of these reaction
types are described in the documentation linked above.

The default parameterization is ``elementary``. Reactions involving surface
species are automatically identified as :ref:`interface <sec-yaml-interface-reaction>`
reactions, and reactions involving charge transfer are
automatically identified as :ref:`electrochemical <sec-yaml-electrochemical-reaction>`
reactions.

Arrhenius Expressions
---------------------

Most reaction types in Cantera are parameterized by one or more modified
Arrhenius expressions, e.g.

.. math::

   k_f(T) = A T^b \exp(-E_a/\bar{R}T)

Rates in this form can be written as YAML mappings, e.g.

.. code:: yaml

    {A: 1.0e13, b: 0, E: 7.3 kcal/mol}

The units of the pre-exponential factor :math:`A` can be specified explicitly if
desired. If not specified, they will be determined based on the ``quantity``,
``length``, and ``time`` units specified in the governing ``units`` fields.
Since the units of :math:`A` depend on the reaction order, the units of each
reactant concentration (dependent on phase type and dimensionality), and the
units of the rate of progress (different for homogeneous and heterogeneous
reactions), it is usually best not to specify units for :math:`A`, in which case
they will be computed taking all of these factors into account.

Note: if :math:`b \ne 0`, then the term :math:`T^b` should have units of
:math:`K^b`, which would change the units of :math:`A`. This is not done,
however, so the units associated with :math:`A` are really the units for
:math:`k_f` . One way to formally express this is to replace :math:`T^b` by the
non-dimensional quantity :math:`[T/(1\;\mathrm{K})]^b`.

.. _sec-yaml-reaction-options:

Duplicate Reactions
-------------------

When a reaction is imported into a phase, it is checked to see that it is not a
duplicate of another reaction already present in the phase, and normally an
error results if a duplicate is found. But in some cases, it may be appropriate
to include duplicate reactions, for example if a reaction can proceed through
two distinctly different pathways, each with its own rate expression. Another
case where duplicate reactions can be used is if it is desired to implement a
reaction rate coefficient of the form:

.. math::

    k_f(T) = \sum_{n=1}^{N} A_n T^{b_n} \exp(-E_n/\hat{R}T)

While Cantera does not provide such a form for reaction rates, it can be
implemented by defining *N* duplicate reactions, and assigning one rate
coefficient in the sum to each reaction. By adding the field:

.. code:: yaml

    duplicate: true

to a reaction entry, then the reaction not only *may* have a duplicate, it
*must*. Any reaction that specifies that it is a duplicate, but cannot be paired
with another reaction in the phase that qualifies as its duplicate generates an
error.

Negative Pre-exponential Factors
--------------------------------

If some of the terms in the above sum have negative :math:`A_n`, this scheme
fails, since Cantera normally does not allow negative pre-exponential factors.
But if there are duplicate reactions such that the total rate is positive, then
the fact that negative :math:`A` parameters are acceptable can be indicated by
adding the field:

.. code:: yaml

    negative-A: true

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

.. code:: yaml

   - equation: C8H18 + 12.5 O2 => 8 CO2 + 9 H2O
     rate-constant: {A: 4.6e11, b: 0.0, Ea: 30.0 kcal/mol}
     orders: {C8H18: 0.25, O2: 1.5}

Special care is required in this case since the units of the pre-exponential
factor depend on the sum of the reaction orders, which may not be an integer.

Note that you can change reaction orders only for irreversible reactions.


Negative Reaction Orders
~~~~~~~~~~~~~~~~~~~~~~~~

Normally, reaction orders are required to be positive. However, in some cases
negative reaction orders provide better fits for experimental data. In these
cases, the default behavior may be overridden by adding the ``negative-orders``
field to the reaction entry, e.g.:

.. code:: yaml

   - equation: C8H18 + 12.5 O2 => 8 CO2 + 9 H2O
     rate-constant: {A: 4.6e11, b: 0.0, Ea: 30.0 kcal/mol}
     orders: {C8H18: -0.25, O2: 1.75}
     negative-orders: true


Non-reactant Orders
~~~~~~~~~~~~~~~~~~~

Some global reactions could have reactions orders for non-reactant species. In
this case, the ``nonreactant-orders`` field must be added to the reaction entry:

.. code:: yaml

   - equation: C8H18 + 12.5 O2 => 8 CO2 + 9 H2O
     rate-constant: {A: 4.6e11, b: 0.0, Ea: 30.0 kcal/mol}
     orders: {C8H18: -0.25, CO: 0.15}
     negative-orders: true
     nonreactant-orders: true


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
