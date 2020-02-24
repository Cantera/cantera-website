.. slug: reactions
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

with a forward rate constant defined as a modified Arrhenius function:

.. math::

   k_f = A T^b e^{-E_a / RT}

and the forward reaction rate calculated as:

.. math::

   R_f = [\mathrm{A}] [\mathrm{B}] k_f

An elementary reaction can be defined in the CTI format using the
:cti:class:`reaction` entry, or in the YAML format using the
:ref:`elementary <sec-yaml-elementary>` reaction ``type``.

Three-Body Reactions
--------------------

A three-body reaction is a gas-phase reaction of the form:

.. math::

   \mathrm{A + B + M \rightleftharpoons AB + M}

Here :math:`\mathrm{M}` is an unspecified collision partner that carries away excess energy to
stabilize the :math:`\mathrm{AB}` molecule (forward direction) or supplies energy to break the
:math:`\mathrm{AB}` bond (reverse direction).

Different species may be more or less effective in acting as the collision partner. A species that
is much lighter than :math:`\mathrm{A}` and :math:`\mathrm{B}` may not be able to transfer much of
its kinetic energy, and so would be inefficient as a collision partner. On the other hand, a species
with a transition from its ground state that is nearly resonant with one in the
:math:`\mathrm{AB^*}` activated complex may be much more effective at exchanging energy than would
otherwise be expected.

These effects can be accounted for by defining a collision efficiency
:math:`\epsilon` for each species, defined such that the forward reaction rate is

.. math::

   k_f(T)[A][B][M]

where

.. math::

   [M] = \sum_{\mathrm{k}} \epsilon_{\mathrm{k}} C_{\mathrm{k}}

where :math:`C_{\mathrm{k}}` is the concentration of species :math:`\mathrm{k}`. Since any constant
collision efficiency can be absorbed into the rate coefficient :math:`k_f(T)`, the default collision
efficiency is 1.0.

A three-body reaction may be defined in the CTI format using the
:cti:class:`three_body_reaction` entry, or in the YAML format using the
:ref:`three-body <sec-yaml-three-body>` reaction ``type``.

Falloff Reactions
-----------------

A falloff reaction is one that has a rate that is first-order in :math:`[M]` at low
pressure, like a three-body reaction, but becomes zero-order in :math:`[M]` as :math:`[M]`
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
the "SRI" falloff function.

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
blending between a "low pressure" and a "high pressure" rate expression. The
difference is that the forward rate constant is written as being proportional
to the *low pressure* rate constant:

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

   P_1: k_1(T) = A_1 T^{b_1} e^{E_1 / RT}

   P_2: k_2(T) = A_2 T^{b_2} e^{E_2 / RT}

The rate at an intermediate pressure :math:`P_1 < P < P_2` is computed as

.. math::

   \log k(T,P) = \log k_1(T) + \bigl(\log k_2(T) - \log k_1(T)\bigr)
       \frac{\log P - \log P_1}{\log P_2 - \log P_1}

Multiple rate expressions may be given at the same pressure, in which case the
rate used in the interpolation formula is the sum of all the rates given at that
pressure. For pressures outside the given range, the rate expression at the nearest
pressure is used.

P-log reactions can be defined in the CTI format using the
:cti:class:`pdep_arrhenius` entry, or in the YAML format using the
:ref:`pressure-dependent-Arrhenius <sec-yaml-pressure-dependent-Arrhenius>`
reaction ``type``.

Chebyshev Reaction Rate Expressions
-----------------------------------

Chebyshev rate expressions represents a phenomenological rate coefficient
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

Surface Reactions
-----------------

Heterogeneous reactions on surfaces are represented by an extended Arrhenius-
like rate expression, which combines the modified Arrhenius rate expression with
further corrections dependent on the fractional surface coverages
:math:`\theta_{\mathrm{k}}` of one or more surface species. The forward rate constant for a
reaction of this type is:

.. math::

   k_f = A T^b \exp \left( - \frac{E_a}{RT} \right)
      \prod_{\mathrm{k}} 10^{a_{\mathrm{k}} \theta_{\mathrm{k}}}
      \theta_{\mathrm{k}}^{m_{\mathrm{k}}}
      \exp \left( \frac{- E_{\mathrm{k}} \theta_{\mathrm{k}}}{RT} \right)

where :math:`A`, :math:`b`, and :math:`E_a` are the modified Arrhenius
parameters and :math:`a_{\mathrm{k}}`, :math:`m_{\mathrm{k}}`, and :math:`E_{\mathrm{k}}` are the coverage
dependencies from species :math:`\mathrm{k}`.

Surface reactions can be defined in the CTI format using the
:cti:class:`surface_reaction` entry, with coverage information provided using
the ``coverage`` keyword argument supplied to the :cti:class:`Arrhenius`
directive. In the YAML format, surface reactions are identified by the presence
of surface species and support several
:ref:`additional options <sec-yaml-interface-reaction>`.

Sticking Coefficients
~~~~~~~~~~~~~~~~~~~~~

Collisions between gas-phase molecules and surfaces which result in the gas-
phase molecule sticking to the surface can be described as a reaction which is
parameterized by a sticking coefficient:

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
