.. slug: kinetics
.. has_math: true
.. title: Modeling Chemical Reactions

.. jumbotron::

   .. raw:: html

      <h1 class="display-3">Modeling Chemical Reactions in Cantera</h1>

   .. class:: lead

      Here, we describe how Cantera calculates chemical reaction rates for various
      reaction types.

Elementary Reactions
--------------------

The basic reaction type is a homogeneous reaction with a pressure-independent
rate coefficient and mass action kinetics. For example:

.. math::

   \mathrm{A + B \rightleftharpoons C + D}

with a forward rate constant :math:`k_f` defined as a modified Arrhenius function:

.. math::

   k_f = A T^b e^{-E_a / RT}

where :math:`A` is the pre-exponential factor, :math:`T` is the temperature,
:math:`b` is the temperature exponent, :math:`E_a` is the activation energy,
and :math:`R` is the gas constant. The forward reaction rate is then calculated
as:

.. math::

   R_f = [\mathrm{A}] [\mathrm{B}] k_f

An elementary reaction can be defined in the CTI format using the
:cti:class:`reaction` entry, or in the YAML format using the
:ref:`elementary <sec-yaml-elementary>` reaction ``type``.

In YAML, the reaction ``type`` entry can be omitted, as it represents the default. In
case the ``type`` entry is omitted and a species occurs on both sides, Cantera
infers that the reaction type is :ref:`three-body <sec-yaml-three-body>`.

Three-Body Reactions
--------------------

A three-body reaction is a gas-phase reaction of the form:

.. math::

   \mathrm{A + B + M \rightleftharpoons AB + M}

Here :math:`\mathrm{M}` is an unspecified collision partner that carries away excess energy to
stabilize the :math:`\mathrm{AB}` molecule (forward direction) or supplies energy to break the
:math:`\mathrm{AB}` bond (reverse direction). In addition to the generic collision partner
:math:`\mathrm{M}`, it is also possible to explicitly specify a colliding species. In this case,
the reaction type is automatically inferred by Cantera.

Different species may be more or less effective in acting as the collision partner. A species that
is much lighter than :math:`\mathrm{A}` and :math:`\mathrm{B}` may not be able to transfer much of
its kinetic energy, and so would be inefficient as a collision partner. On the other hand, a species
with a transition from its ground state that is nearly resonant with one in the
:math:`\mathrm{AB^*}` activated complex may be much more effective at exchanging energy than would
otherwise be expected.

These effects can be accounted for by defining a collision efficiency
:math:`\epsilon` for each species, defined such that the forward reaction rate is

.. math::

   R_f = [\mathrm{A}][\mathrm{B}][\mathrm{M}]k_f(T)

where

.. math::

   [\mathrm{M}] = \sum_{k} \epsilon_k C_k

where :math:`C_k` is the concentration of species :math:`k`. Since any constant
collision efficiency can be absorbed into the rate coefficient :math:`k_f(T)`, the default collision
efficiency is 1.0.

A three-body reaction may be defined in the CTI format using the
:cti:class:`three_body_reaction` entry, or in the YAML format using the
:ref:`three-body <sec-yaml-three-body>` reaction ``type``.

Falloff Reactions
-----------------

A falloff reaction is one that has a rate that is first-order in :math:`[\mathrm{M}]` at low
pressure, like a three-body reaction, but becomes zero-order in :math:`[\mathrm{M}]` as :math:`[\mathrm{M}]`
increases. Dissociation/association reactions of polyatomic molecules often
exhibit this behavior.

The simplest expression for the rate coefficient for a falloff reaction is the
Lindemann form [#Lindemann1922]_:

.. math::

   k_f(T, [{\mathrm{M}}]) = \frac{k_0[{ \mathrm{M}}]}{1 + \frac{k_0{ [\mathrm{M}]}}{k_\infty}}

In the low-pressure limit, this approaches :math:`k0{[\mathrm{M}]}`, and in the
high-pressure limit it approaches :math:`k_\infty`.

Defining the non-dimensional reduced pressure:

.. math::

   P_r = \frac{k_0 [\mathrm{M}]}{k_\infty}

The rate constant may be written as

.. math::

   k_f(T, P_r) = k_\infty \left(\frac{P_r}{1 + P_r}\right)

More accurate models for unimolecular processes lead to other, more complex,
forms for the dependence on reduced pressure. These can be accounted for by
multiplying the Lindemann expression by a function :math:`F(T, P_r)`:

.. math::

   k_f(T, P_r) = k_\infty \left(\frac{P_r}{1 + P_r}\right) F(T, P_r)

This expression is used to compute the rate coefficient for falloff
reactions. The function :math:`F(T, P_r)` is the falloff function, and is
specified by assigning an embedded entry to the ``falloff`` field.

A falloff reaction may be defined in the CTI format using the
:cti:class:`falloff_reaction` entry, or in the YAML format using the
:ref:`falloff <sec-yaml-falloff>` reaction ``type``.

The Troe Falloff Function
~~~~~~~~~~~~~~~~~~~~~~~~~

A widely-used falloff function is the one proposed by Gilbert et
al. [#Gilbert1983]_:

.. math::

   \log_{10} F(T, P_r) = \frac{\log_{10} F_{cent}(T)}{1 + f_1^2}

   F_{cent}(T) = (1-A) \exp(-T/T_3) + A \exp (-T/T_1) + \exp(-T_2/T)

   f_1 = (\log_{10} P_r + C) / (N - 0.14 (\log_{10} P_r + C))

   C = -0.4 - 0.67\; \log_{10} F_{cent}

   N = 0.75 - 1.27\; \log_{10} F_{cent}

A Troe falloff function may be specified in the CTI format using the
:cti:class:`Troe` directive, or in the YAML format using the
:ref:`Troe <sec-yaml-falloff>` field in the reaction entry. The first
three parameters, :math:`(A, T_3, T_1)`, are required. The fourth parameter,
:math:`T_2`, is optional; if omitted, the last term of the falloff function is
not used.

Tsang's Approximation to :math:`F_{cent}`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Wing Tsang presented approximations for the value of :math:`F_{cent}` for Troe
falloff in databases of reactions, for example, Tsang and Herron [#Tsang1991]_.
Tsang's approximations are linear in temperature:

.. math::
    F_{cent} = A + BT

where :math:`A` and :math:`B` are constants. The remaining equations for :math:`C`,
:math:`N`, :math:`f_1`, and :math:`F` from Troe falloff are not affected:

.. math::

   \log_{10} F(T, P_r) = \frac{\log_{10} F_{cent}(T)}{1 + f_1^2}

   f_1 = (\log_{10} P_r + C) / (N - 0.14 (\log_{10} P_r + C))

   C = -0.4 - 0.67\; \log_{10} F_{cent}

   N = 0.75 - 1.27\; \log_{10} F_{cent}

A Tsang falloff function may be specified in the YAML format using the
:ref:`Tsang <sec-yaml-falloff>` field in the reaction entry. *(New in Cantera 2.6)*

.. _sec-sri-falloff:

The SRI Falloff Function
~~~~~~~~~~~~~~~~~~~~~~~~

This falloff function is based on the one originally due to Stewart et al. [#Stewart1989]_, which
required three parameters :math:`a`, :math:`b`, and :math:`c`. Kee et al. [#Kee1989]_ generalized
this function slightly by adding two more parameters :math:`d` and :math:`e`. (The original form
corresponds to :math:`d = 1` and :math:`e = 0`.) Cantera supports the extended 5-parameter form,
given by:

.. math::

   F(T, P_r) = d \bigl[a \exp(-b/T) + \exp(-T/c)\bigr]^{1/(1+\log_{10}^2 P_r )} T^e

In keeping with the nomenclature of Kee et al. [#Kee1989]_, we will refer to this as
the **SRI falloff function**.

An SRI falloff function may be specified in the CTI format using the
:cti:class:`SRI` directive, or in the YAML format using the
:ref:`SRI <sec-yaml-falloff>` field in the entry.

Chemically-Activated Reactions
------------------------------

For these reactions, the rate falls off as the pressure increases, due to
collisional stabilization of a reaction intermediate. Example:

.. math::

   \mathrm{Si + SiH_4 (+M) \leftrightarrow Si_2H_2 + H_2 (+M)}

which competes with:

.. math::

   \mathrm{Si + SiH_4 (+M) \leftrightarrow Si_2H_4 (+M)}

Like falloff reactions, chemically-activated reactions are described by
blending between a low-pressure and a high-pressure rate expression. The
difference is that the forward rate constant is written as being proportional
to the *low-pressure* rate constant:

.. math::

   k_f(T, P_r) = k_0 \left(\frac{1}{1 + P_r}\right) F(T, P_r)

and the optional blending function :math:`F` may described by any of the
parameterizations allowed for falloff reactions.

Chemically-activated reactions can be defined in the CTI format using the
:cti:class:`chemically_activated_reaction` entry, or in the YAML format using
the :ref:`chemically-activated <sec-yaml-chemically-activated>` reaction ``type``.

Pressure-Dependent Arrhenius Rate Expressions (P-Log)
-----------------------------------------------------

This parameterization represents pressure-dependent reaction rates
by logarithmically interpolating between Arrhenius rate expressions at various
pressures. Given two rate expressions at two specific pressures:

.. math::

   P_1: k_1(T) = A_1 T^{b_1} e^{-E_1 / RT}

   P_2: k_2(T) = A_2 T^{b_2} e^{-E_2 / RT}

The rate at an intermediate pressure :math:`P_1 < P < P_2` is computed as

.. math::

   \log k(T,P) = \log k_1(T) + \bigl(\log k_2(T) - \log k_1(T)\bigr)
       \frac{\log P - \log P_1}{\log P_2 - \log P_1}

Multiple rate expressions may be given at the same pressure, in which case the
rate used in the interpolation formula is the sum of all the rates given at that
pressure. For pressures outside the given range, the rate expression at the nearest
pressure is used.

Negative A-factors can be used for any of the rate expressions at a given pressure.
However, the sum of all of the rates at a given pressure **must** be positive, due
to the logarithmic interpolation of the rate for intermediate pressures. When a
P-log type reaction is initialized, Cantera does a validation check for a range of
temperatures that the sum of the reaction rates at each pressure is positive. Unfortunately, if
these checks fail, the only options are to remove the reaction or contact the author
of the reaction/mechanism in question, because the reaction is mathematically unsound.

P-log reactions can be defined in the CTI format using the
:cti:class:`pdep_arrhenius` entry, or in the YAML format using the
:ref:`pressure-dependent-Arrhenius <sec-yaml-pressure-dependent-Arrhenius>`
reaction ``type``.

Chebyshev Reaction Rate Expressions
-----------------------------------

Chebyshev rate expressions represent a phenomenological rate coefficient
:math:`k(T,P)` in terms of a bivariate Chebyshev polynomial. The rate constant
can be written as:

.. math::

   \log k(T,P) = \sum_{t=1}^{N_T} \sum_{p=1}^{N_P} \alpha_{tp}
                            \phi_t(\tilde{T}) \phi_p(\tilde{P})

where :math:`\alpha_{tp}` are the constants defining the rate, :math:`\phi_n(x)`
is the Chebyshev polynomial of the first kind of degree :math:`n` evaluated at
:math:`x`, and

.. math::

   \tilde{T} \equiv \frac{2T^{-1} - T_\mathrm{min}^{-1} - T_\mathrm{max}^{-1}}
                          {T_\mathrm{max}^{-1} - T_\mathrm{min}^{-1}}

   \tilde{P} \equiv \frac{2 \log P - \log P_\mathrm{min} - \log P_\mathrm{max}}
                          {\log P_\mathrm{max} - \log P_\mathrm{min}}

are reduced temperatures and reduced pressures which map the ranges
:math:`(T_\mathrm{min}, T_\mathrm{max})` and :math:`(P_\mathrm{min},
P_\mathrm{max})` to :math:`(-1, 1)`.

A Chebyshev rate expression is specified in terms of the coefficient matrix
:math:`\alpha` and the temperature and pressure ranges.

Note that the Chebyshev polynomials are not defined outside the interval
:math:`(-1,1)`, and therefore extrapolation of rates outside the range of
temperatures and pressure for which they are defined is strongly discouraged.

Chebyshev reactions can be defined in the CTI format using the
:cti:class:`chebyshev_reaction` entry, or in the YAML format using the
:ref:`Chebyshev <sec-yaml-Chebyshev>` reaction ``type``.

.. _sec-Blowers-Masel:

Blowers-Masel Reactions
-----------------------

In some circumstances like thermodynamic sensitivity analysis, or
modeling heterogeneous reactions from one catalyst surface to another,
the enthalpy change of a reaction (:math:`\Delta H`) can be modified. Due to the change in :math:`\Delta H`,
the activation energy of the reaction must be adjusted accordingly to provide accurate simulation results. To
adjust the activation energy due to changes in the reaction enthalpy, the Blowers-Masel rate expression is
available. This approximation was proposed by Blowers and Masel [#BlowersMasel2000]_ to automatically
scale activation energy as the reaction enthalpy is changed.
The activation energy estimation can be written as:

.. math::

   E_a = \begin{cases}
      0 & \text{if } \Delta H \leq -4 E_a^0 \\
      \Delta H & \text{if } \Delta H \geq 4 E_a^0 \\
      \frac{\left( w + \frac{\Delta H }{2} \right)  (V_P - 2 w + \Delta H) ^2}
               {V_P^2 - 4 w^2 + \Delta H^2} & \text{Otherwise}
      \end{cases}

where

.. math::

   V_P = 2 w \frac{w + E_a^0}{w - E_a^0},

:math:`w` is the average of the bond dissociation energy of the bond breaking and that being formed,
:math:`E_a^0` is the intrinsic activation energy, and :math:`\Delta H` is the enthalpy change of the reaction.
Note that the expression is insensitive to :math:`w` as long as :math:`w \ge 2 E_a^0`, so we can use
an arbitrarily high value of :math:`w = 1000\text{ kJ/mol}`.

After :math:`E_a` is evaluated, the reaction rate can be calculated using the modified Arrhenius expression

.. math::

   k_f = A T^b e^{-E_a / RT}.

.. TODO: Update the link once version 2.6 is released

Blowers Masel reactions can be defined in the YAML format using the
`Blowers-Masel <https://cantera.org/documentation/dev/sphinx/html/yaml/reactions.html#sec-yaml-blowers-masel>`__ reaction ``type``.
*(New in Cantera 2.6)*

.. _sec-surface:

Surface Reactions
-----------------

Heterogeneous reactions on surfaces are represented by an extended Arrhenius-
like rate expression, which combines the modified Arrhenius rate expression with
further corrections dependent on the fractional surface coverages
:math:`\theta_{k}` of one or more surface species. The forward rate constant for a
reaction of this type is:

.. math::

   k_f = A T^b \exp \left( - \frac{E_a}{RT} \right)
      \prod_k 10^{a_k \theta_k}
      \theta_k^{m_k}
      \exp \left( \frac{- E_k \theta_k}{RT} \right)

where :math:`A`, :math:`b`, and :math:`E_a` are the modified Arrhenius
parameters and :math:`a_k`, :math:`m_k`, and :math:`E_k` are the coverage
dependencies from species :math:`k`.

Surface reactions can be defined in the CTI format using the
:cti:class:`surface_reaction` entry, with coverage information provided using
the ``coverage`` keyword argument supplied to the :cti:class:`Arrhenius`
directive. In the YAML format, surface reactions are identified by the presence
of surface species and support several
:ref:`additional options <sec-yaml-interface-reaction>`.

.. TODO: Update the link once version 2.6 is released

In YAML, the surface reaction ``type`` defaults to ``interface-Arrhenius``, where
the rate expression uses the
:ref:`Arrhenius <https://cantera.org/documentation/dev/sphinx/html/yaml/reactions.html#sec-yaml-interface-Arrhenius>`__
parameterization. As an alternative, Cantera also supports the
``interface-Blowers-Masel`` surface reaction ``type``, which uses the
:ref:`Blowers-Masel <https://cantera.org/documentation/dev/sphinx/html/yaml/reactions.html#sec-yaml-interface-Blowers-Masel>`__
parameterization *(New in Cantera 2.6)*. The prefix ``interface-`` is
not required as it is inferred automatically.

.. _sec-sticking:

Sticking Reactions
------------------

Sticking reactions represent a special case of surface reactions, where collisions
between gas-phase molecules and surfaces result in the gas-phase molecule sticking to
the surface. This process can be described as a reaction which is parameterized by a
sticking coefficient:

.. math::

   \gamma = a T^b e^{-c/RT}

where :math:`a`, :math:`b`, and :math:`c` are constants specific to the
reaction. The values of these constants must be specified so that the sticking
coefficient :math:`\gamma` is between 0 and 1 for all temperatures.

The sticking coefficient is related to the forward rate constant by the
formula:

.. math::

   k_f = \frac{\gamma}{\Gamma_\mathrm{tot}^m} \sqrt{\frac{RT}{2 \pi W}}

where :math:`\Gamma_\mathrm{tot}` is the total molar site density, :math:`m` is
the sum of all the surface reactant stoichiometric coefficients, and :math:`W`
is the molecular weight of the gas phase species.

.. TODO: Link to :cti:class:`stick` after 2.5.0 release adds that to the docs

Sticking reactions can be defined in the CTI format using the `stick` entry, or
in the YAML format by specifying the rate constant in the reaction's
:ref:`sticking-coefficient <sec-yaml-interface-reaction>` field.

In YAML, the sticking reaction ``type`` defaults to ``sticking-Arrhenius``, where
the rate expression uses the
:ref:`Arrhenius <https://cantera.org/documentation/dev/sphinx/html/yaml/reactions.html#sec-yaml-sticking-Arrhenius>`__
parameterization. As an alternative, Cantera also supports the
``sticking-Blowers-Masel`` surface reaction ``type``, which uses the
:ref:`Blowers-Masel <https://cantera.org/documentation/dev/sphinx/html/yaml/reactions.html#sec-yaml-sticking-Blowers-Masel>`__
parameterization *(New in Cantera 2.6)*. The prefix ``sticking-`` is
not required as it is inferred automatically.

.. _sec-plasma:

Two-Temperature-Plasma Reactions
--------------------------------

The two-temperature-plasma reaction is commonly used for non-equilibrium plasmas. The
reaction rate of a two-temperature-plasma reaction depends on both gas and electron
temperature [#Kossyi1992]_, and can be expressed as:

.. math::

   k_f = A T_e^b \exp \left( - \frac{E_{a,g}}{RT} \right)
      \exp \left(\frac{E_{a,e}(T_e - T)}{R T T_e}\right),

where :math:`A` is the pre-exponential factor, :math:`T` is the temperature, :math:`T_e`
is the electron temperature, :math:`b` is the electron temperature exponent,
:math:`E_{a,g}` is the activation energy for gas, :math:`E_{a,e}` is the activation
energy for electron and :math:`R` is the gas constant. *(New in Cantera 2.6)*

.. _sec-additional-options:

Additional Options
------------------

Reaction Orders
~~~~~~~~~~~~~~~

Explicit reaction orders different from the stoichiometric coefficients are
sometimes used for non-elementary reactions. For example, consider the global
reaction:

.. math::

   \mathrm{C_8H_{18} + 12.5 O_2 \rightarrow 8 CO_2 + 9 H_2O}

the forward rate constant might be given as [#Westbrook1981]_:

.. math::

   k_f = 4.6 \times 10^{11} [\mathrm{C_8H_{18}}]^{0.25} [\mathrm{O_2}]^{1.5}
          \exp\left(\frac{30.0\,\mathrm{kcal/mol}}{RT}\right)

Special care is required in this case since the units of the pre-exponential
factor depend on the sum of the reaction orders, which may not be an integer.

Note that you can change reaction orders only for irreversible reactions.

Normally, reaction orders are required to be positive. However, in some cases
negative reaction orders are found to be better fits for experimental data. In
these cases, the default behavior may be overridden in the input file.


.. rubric:: References

.. [#Lindemann1922] F. Lindemann. *Trans. Faraday Soc.*, 17:598, 1922.

.. [#Gilbert1983] R. G. Gilbert, K. Luther, and
   J. Troe. *Ber. Bunsenges. Phys. Chem.*, 87:169, 1983.

.. [#Tsang1991] W. Tsang and J. Herron. *Journal of Physical and Chemical Reference Data*, 20:4, 1991.

.. [#Stewart1989] P. H. Stewart, C. W. Larson, and D. Golden.
   *Combustion and Flame*, 75:25, 1989.

.. [#Kee1989] R. J. Kee, F. M. Rupley, and J. A. Miller. Chemkin-II: A Fortran
   chemical kinetics package for the analysis of gas-phase chemical
   kinetics. Technical Report SAND89-8009, Sandia National Laboratories, 1989.

.. [#BlowersMasel2000] Blowers, P., & Masel, R. (2000). Engineering approximations
   for activation energies in hydrogen transfer reactions. *AIChE Journal*, 46(10),
   2041-2052. https://doi.org/10.1002/aic.690461015

.. [#Westbrook1981] C. K. Westbrook and F. L. Dryer. Simplified reaction
   mechanisms for the oxidation of hydrocarbon fuels in flames. *Combustion
   Science and Technology* **27**, pp. 31--43. 1981.

.. [#Kossyi1992] I. A. Kossyi, A. Y. Kostinsky, A. A. Matveyev. and V. P.
   Kinetic scheme of the non-equilibrium discharge in nitrogen-oxygen mixtures.
   mechanisms for the oxidation of hydrocarbon fuels in flames.
   *Plasma Sources Science and Technology* **1**, no. 3, pp. 207. 1992.
   DOI: https://doi.org/10.1088/0963-0252/1/3/011
