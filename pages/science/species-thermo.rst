.. slug: species-thermo
.. has_math: true
.. title: Elements and Species

.. jumbotron::

   .. raw:: html

      <h1 class="display-3">Elements and Species Thermodynamics</h1>

   .. class:: lead

      All phases in Cantera are made up of one or more species, which in turn
      contain one or more elements.

Elements
========

In Cantera, an **element** may refer to a chemical element or an isotope. Note
that definitions of elements are not often needed, since Cantera has definitions
for the standard chemical elements. Explicit element definitions are usually
only needed for isotopes.

An element can be defined in the YAML format by adding entries to the :ref:`elements
<sec-yaml-elements>` section of the input file.

Species
=======

For each species, a species definition is required.

A species can be defined in the YAML format by adding an entry to the :ref:`species
<sec-yaml-species>` section of the input file.

Species Name
------------

The name of a species may contain letters, numbers, or just about anything else
that is a printable, non-whitespace character. Some example name specifications:

.. code::

   CH4
   methane
   argon_2+
   CH2(singlet)

Elemental Composition
---------------------

The elemental composition of each species must be specified.
For gaseous species, the elemental composition is well-defined, since the
species represent distinct molecules. For species in solid or liquid solutions,
or on surfaces, there may be several possible ways of defining the species. For
example, an aqueous species might be defined with or without including the water
molecules in the solvation cage surrounding it.

The special "element" ``E`` is used in representing charged species, where it
specifies the net number of electrons compared to the number needed to form a
neutral species. That is, negatively charged ions will have ``E`` > 0, while
positively charged ions will have ``E`` < 0.

The number of atoms of an element must be non-negative, with the exception of
electrons.

For surface species, it is possible to omit the elemental composition, in
which case it is composed of nothing, and represents an empty surface site. This
can also be done to represent vacancies in solids. A charged vacancy can be
defined to be composed solely of electrons.

Thermodynamic Properties
------------------------

The phase models discussed in the `Phases section </science/phases-thermo.html>`__
implement specific models for the thermodynamic properties appropriate for the
type of phase or interface they represent. Although each one may use different
expressions to compute the properties, they all require thermodynamic property
information for the individual species. For the phase types implemented at
present, the properties needed are:

1. the molar heat capacity at constant pressure :math:`\hat{c}^\circ_p(T)` for a
   range of temperatures and a reference pressure :math:`p^\circ`;
2. the molar enthalpy :math:`\hat{h}(T^\circ, p^\circ)` at :math:`p^\circ` and a reference
   temperature :math:`T^\circ`;
3. the absolute molar entropy :math:`\hat{s}(T^\circ, p^\circ)` at :math:`(T^\circ, p^\circ)`.

The superscript :math:`^\circ` here represents the *reference state*--a specified state (i.e. set of conditions :math:`T^\circ` and :math:`p^\circ` and fixed chemical composition) at which thermodynamic properties are known.

.. _sec-thermo-models:

Thermodynamic Property Models
=============================

The models described in this section can be used to provide thermodynamic data
for each species in a phase. Each model implements a different
**parameterization** (functional form) for the heat capacity. Note that there is
no requirement that all species in a phase use the same parameterization; each
species can use the one most appropriate to represent how the heat capacity
depends on temperature.

Currently, several types are implemented that provide species properties
appropriate for models of ideal gas mixtures, ideal solutions, and pure
compounds.

The NASA 7-Coefficient Polynomial Parameterization
--------------------------------------------------

The NASA 7-coefficient polynomial parameterization is used to compute the
species reference-state thermodynamic properties :math:`\hat{c}^\circ_p(T)`,
:math:`\hat{h}^\circ(T)`, and :math:`\hat{s}^\circ(T)`.

The NASA parameterization represents :math:`\hat{c}^\circ_p(T)` with a fourth-order
polynomial:

.. math::

   \frac{\hat{c}_p^\circ(T)}{\overline{R}} = a_0 + a_1 T + a_2 T^2 + a_3 T^3 + a_4 T^4
   
   \frac{\hat{h}^\circ (T)}{\overline{R} T} = a_0 + \frac{a_1}{2} T + \frac{a_2}{3} T^2 +
                         \frac{a_3}{4} T^3 + \frac{a_4}{5} T^4 + \frac{a_5}{T}

   \frac{\hat{s}^\circ(T)}{\overline{R}} = a_0 \ln T + a_1 T + \frac{a_2}{2} T^2 + \frac{a_3}{3} T^3 +
                      \frac{a_4}{4} T^4 + a_6

Note that this is the "old" NASA polynomial form, used in the original NASA
equilibrium program and in Chemkin, which uses 7 coefficients in each of two
temperature regions. It is not compatible with the form used in the most recent
version of the NASA equilibrium program, which uses 9 coefficients for each
temperature region.

A NASA-7 parameterization can be defined in the YAML format by specifying
:ref:`NASA7 <sec-yaml-nasa7>` as the ``model`` in the species ``thermo`` field.

.. _sec-thermo-nasa9:

The NASA 9-Coefficient Polynomial Parameterization
--------------------------------------------------

The NASA 9-coefficient polynomial parameterization [#McBride2002]_ ("NASA9" for
short) is an extension of the NASA 7-coefficient polynomial parameterization
which includes two additional terms in each temperature region, as well as
supporting an arbitrary number of temperature regions.

The NASA9 parameterization represents the species thermodynamic properties with
the following equations:

.. math::

   \frac{\hat{c}_p^\circ(T)}{\overline{R}} = a_0 T^{-2} + a_1 T^{-1} + a_2 + a_3 T
                  + a_4 T^2 + a_5 T^3 + a_6 T^4

   \frac{\hat{h}^\circ(T)}{\overline{R} T} = - a_0 T^{-2} + a_1 \frac{\ln T}{T} + a_2
       + \frac{a_3}{2} T + \frac{a_4}{3} T^2  + \frac{a_5}{4} T^3 +
       \frac{a_6}{5} T^4 + \frac{a_7}{T}

   \frac{\hat{s}^\circ(T)}{\overline{R}} = - \frac{a_0}{2} T^{-2} - a_1 T^{-1} + a_2 \ln T
      + a_3 T + \frac{a_4}{2} T^2 + \frac{a_5}{3} T^3  + \frac{a_6}{4} T^4 + a_8

A common source for species data in the NASA9 format is the
:ref:`NASA ThermoBuild <sec-thermobuild>` tool.

A NASA-9 parameterization can be defined in the YAML format by specifying
:ref:`NASA9 <sec-yaml-nasa9>` as the ``model`` in the species ``thermo`` field.

The Shomate Parameterization
----------------------------

The Shomate parameterization is:

.. math::

   \hat{c}_p^\circ(T) = A + Bt + Ct^2 + Dt^3 + \frac{E}{t^2}

   \hat{h}^\circ(T) = At + \frac{Bt^2}{2} + \frac{Ct^3}{3} + \frac{Dt^4}{4} -
                  \frac{E}{t} + F

   \hat{s}^\circ(T) = A \ln t + B t + \frac{Ct^2}{2} + \frac{Dt^3}{3} -
                  \frac{E}{2t^2} + G

where :math:`t = T / 1000 K`. It requires 7 coefficients :math:`A`, :math:`B`, :math:`C`, :math:`D`,
:math:`E`, :math:`F`, and :math:`G`. This parameterization is used to represent reference-state
properties in the `NIST Chemistry WebBook <http://webbook.nist.gov/chemistry>`__. The values of the
coefficients :math:`A` through :math:`G` should be entered precisely as shown there, with no units
attached. Unit conversions to SI will be handled internally.

A Shomate parameterization can be defined in the YAML format by specifying
:ref:`Shomate <sec-yaml-shomate>` as the ``model`` in the species
``thermo`` field.

Constant Heat Capacity
----------------------

In some cases, species properties may only be required at a single temperature
or over a narrow temperature range. In such cases, the heat capacity can be
approximated as constant, and simple expressions can be used for the
thermodynamic properties:

.. math::

   \hat{c}_p^\circ(T) = \hat{c}_p^\circ(T^\circ)

   \hat{h}^\circ(T) = \hat{h}^\circ\left(T_0\right) + \hat{c}_p^\circ \left(T-T^\circ\right)

   \hat{s}^\circ(T) = \hat{s}^\circ(T_0) + \hat{c}_p^\circ \ln{\left(\frac{T}{T^\circ}\right)}

The parameterization uses four constants: :math:`T^\circ, \hat{c}_p^\circ(T^\circ),
\hat{h}^\circ(T^\circ), and \hat{s}^\circ(T)`. The default value of :math:`T^\circ` is 298.15 K; the
default value for the other parameters is 0.0.

A constant heat capacity parameterization can be defined in the YAML format by specifying
:ref:`constant-cp <sec-yaml-constcp>` as the ``model`` in the species ``thermo`` field.


.. rubric:: References

.. [#Kee1986] R. J. Kee, G. Dixon-Lewis, J. Warnatz, M. E. Coltrin, and J. A. Miller.
   A FORTRAN Computer Code Package for the Evaluation of Gas-Phase, Multicomponent
   Transport Properties. Technical Report SAND86-8246, Sandia National Laboratories, 1986.

.. [#Mcbride2002] B. J. McBride, M. J. Zehe, S. Gordon. "NASA Glenn Coefficients
   for Calculating Thermodynamic Properties of Individual Species,"
   NASA/TP-2002-211556, Sept. 2002.
