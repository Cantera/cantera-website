.. slug: eos
.. has_math: true
.. title: Equations of state in Cantera

.. jumbotron::

   .. raw:: html

      <h1 class="display-3">Equations of state (EoS) </h1>

   .. class:: lead

      Here, we describe some of the most commonly-used ideal and non-ideal equations of state in Cantera.

Ideal Gas EoS
##############################

The most commonly-used thermodynamic phase model in Cantera is the **ideal gas** model.
The relationship between pressure :math:`p`, temperature :math:`T` and specific volume
:math:`v` for a pure gas-phase species is typically expressed using the ideal gas law as

.. math::

    p = \frac{RT}{v},

where :math:`R` is the universal gas constant. For a multicomponent mixture, the ideal gas equation is

.. math::

    p = \rho RT \sum \frac{Y_k}{W_k} = \frac{\rho RT}{\overline{W}}

where :math:`\rho` is the mass-density of the mixture, :math:`Y_k` and :math:`W_k` are the mass
fraction and molecular weight of species :math:`k` from the mixture. :math:`\overline{W}` is the mean
molecular weight calculates as:

.. math::

    \overline{W} = \frac{1}{\sum Y_k W_k} = \sum X_k W_k,

where :math:`X_k` is the mole fraction of species :math:`k`.

Ideal gas phase can be defined in the YAML format using the
:ref:`ideal-gas <sec-yaml-ideal-gas>` entry in the ``thermo`` field.

Non-Ideal EoS
##############################

Typically, all gases follow the ideal gas law at high temperatures and low pressures.
However ideal gas EoS departs significantly from the ideal behavior near the critical regime.
The deviation from ideal behavior is usually measured in terms of the compressibility factor
:math:`Z`, defined as

.. math::

    Z = \frac{pv}{RT} \overline{W}.

For an ideal gas, this compressibility factor is unity (i.e., :math:`Z = 1`).

Cantera implements two cubic EoS viz. Redlich-Kwong [#RK49]_ and Peng-Robinson [#PR76]_ EoS.
These cubic equations of state with 2-3 empirical parameters are widely used to model real-gas effects.

Thermodynamic properties for non-ideal EoS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In the case of cubic equations, consistent expressions can be derived for thermodynamic
properties that are accurate across a wide range of states and phases. The molar Helmholtz free
energy :math:`a` is calculated using its definition and integrating the equation of state.
The molar Helmholtz free energy for a species :math:`k` can be calculated as:

.. math::

    p \equiv -\left ( \frac{\partial a}{\partial v} \right)_{n_k, T}

where :math:`n_k` is the number of moles of species :math:`k`, :math:`p` is the pressure,
and :math:`v` is the molar volume of the mixture.

Once the non-ideal Helmholtz energy is obtained, the other thermodynamic properties
such as entropy (:math:`s`), internal energy (:math:`u`), enthalpy (:math:`h`) and
Gibb's free energy (:math:`g`) are evaluated using following relationships:

.. math::

    (s - s^\circ ) =  -  \left(\frac{\partial (a-a^\circ)}{\partial T}\right)_v

.. math::

    (u - u^\circ ) = (a-a^\circ) + T (s-s^\circ)

.. math::

    (h - h^\circ ) =  (a-a^\circ) + T (s-s^\circ) + RT(Z-1)

.. math::

    (g - g^\circ ) =  (a-a^\circ) + RT(Z-1)

Here :math:`s^\circ`, :math:`u^\circ`, :math:`h^\circ` and :math:`g^\circ`
denote standard-state entropy, internal energy, enthalpy and Gibb's free energy
respectively.

Mass-action kinetics and fugacities
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The real gas behavior also influences mass-action kinetics through species activities.
The species-specific activity concentrations :math:`[C_{ac,k}]` is defined as

.. math::

    [C_{ac,k}] = \alpha_k [X_k^\circ] = \gamma_k [X_k],

where :math:`\alpha_k` and :math:`\gamma_k` represent activity coefficients and
fugacity coefficients of species :math:`k`. For an ideal gas, :math:`\alpha_k = 1` and
:math:`\gamma_k = 1`. For real gas, the activities :math:`\alpha_k` are calculated
using adopted real gas equations of state (eg. R-K EoS, P-R EoS, etc) as

.. math::

    \alpha_k = \exp\left(\frac{\mu_k - \mu^\circ_k}{RT}\right).


Redlich-Kwong Equation of state (R-K EoS)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The cubic Redlich-Kwong formulation may be stated as

.. math::

    p=\frac{RT}{v-b^\ast}-\frac{a^\ast}{v\sqrt{T}(v+b^\ast)}

where, :math:`R` is the universal gas constant and :math:`v` is the molar volume.
The temperature-dependent Van der Waals attraction parameter :math:`a^\ast` and
volume correction parameter (repulsive parameter) :math:`b^\ast` represent molecular interactions.
The Redlich-Kwong equation of state has a critical compressibility :math:`Z_{\rm c} = 1/3`.

The mixture-average Van der Waals attraction parameter (:math:`a^\ast`) and volume correction
parameter (:math:`b^\ast`) for a multi-component mixture can be calculated using mixing rules
[#SPE03]_ as follows:

.. math::

    a^\ast_{\rm mix}=\sum_{i}\sum_{j} X_i X_j a^\ast_{ij}, \ \ \ \ b^\ast_{\rm mix}=\sum_{i} X_i b^\ast_i

where, :math:`X_k` is the mole fraction of species :math:`k`, :math:`a^\ast_{ij}` is the interaction parameter
calculated as the geometric average of the pure-species parameters [#RPP87]_ :

.. math::

    a^\ast_{ij}=\sqrt{a^\ast_i a^\ast_j}

where :math:`a_k^\ast` and :math:`b^\ast_k` are the pure-species parameters.

Peng-Robinson Equation of state (P-R EoS)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The cubic Peng-Robinson formulation may be stated as

.. math::

    p = \frac{RT}{v-b^\ast} - \frac{a^\ast \alpha}{v^2 + 2b^\ast v - b^{\ast2}}

where, :math:`R` is the universal gas constant and :math:`v` is the molar volume.
The temperature-dependent Van der Waals attraction parameter :math:`a^\ast` and
volume correction parameter (repulsive parameter) :math:`b^\ast` represent molecular interactions.
The Peng-Robinson equation of state has a critical compressibility :math:`Z_{\rm c} = 0.03074`.
A temperature dependent interaction parameter :math:`\alpha` is calculated as

.. math::

    \alpha(T) = \left[ 1 + \kappa \left(1- \sqrt{\frac{T}{T_\text{c}}} \right) \right]^2.

and the function :math:`\kappa` is calculated as

.. math::

    \kappa = 0.37464 + 1.54226 \omega - 0.26992 \omega^2  \qquad \qquad \qquad \qquad  \text{if}  \quad  \omega \leq 0.491

.. math::

    \kappa = 0.379642 + 1.487503 \omega - 0.164423 \omega^2 + 0.016666 \omega^3  \quad \text{if}  \quad  \omega > 0.491

Here :math:`\omega` is an acentric factor of a species.

The mixture-average Van der Waals attraction parameter (:math:`a^\ast`) and volume correction
parameter (:math:`b^\ast`) for a multi-component mixture can be calculated using mixing rules
[#SPE03]_ as follows:

.. math::

    a^\ast_{\text{mix}} = \sum_i \sum_j X_i X_j a^\ast_{ij}, \ \ \ \ (a \alpha)^\ast_{\text{mix}} = \sum_i \sum_j X_i X_j (a\alpha)^\ast_{ij}, \ \ \ \ b^\ast_{\rm mix}=\sum_{i} X_i b^\ast_i

where, :math:`X_k` is the mole fraction of species :math:`k`, :math:`a^\ast_{ij}` is the interaction parameter
calculated as the geometric average of the pure-species parameters [#RPP87]_ :

.. math::

    a^\ast_{ij}=\sqrt{a^\ast_i a^\ast_j}, \ \ \ \ (a\alpha)^\ast_{ij} = \sqrt{(a\alpha)^\ast_i (a\alpha)^\ast_j}

where :math:`a_k^\ast` and :math:`b^\ast_k` are the pure-species parameters.

.. rubric:: References

.. [#RK49] O. Redlich, J.N.S. Kwong. On the thermodynamics of solutions. V. An equation of state.
    Fugacities of gaseous solutions, Chem. Rev., 44:233--244, 1949.

.. [#PR76] D. Peng, D.B. Robinson. A New Two-Constant Equation of State,
    Industrial and engineering chemistry fundamentals, 15:59--64, 1976.

.. [#SPE03] N. Spycher, K. Pruess, J. Ennis-King. A simulation program for non-isothermal
    multiphase reactive geochemical transport in variably saturated geologic media:
    applications to geothermal injectivity and :math:`CO_2` geological sequestration,
    Geochimica et Cosmochimica Acta, 67:3015--3031, 2003.

.. [#RPP87] R.C. Reid, J.M. Prausnitz, B.E. Poling. Properties of Gases and Liquids,
    Mc.Graw-Hill Inc., 1987.
