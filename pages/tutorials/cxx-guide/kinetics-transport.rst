.. title: Computing Reaction Rates and Transport Properties in C++

.. jumbotron::

   .. raw:: html

      <h1 class="display-4">Computing Reaction Rates and Transport Properties in C++</h1>

   .. class:: lead

      Learn how to use ``Kinetics`` and ``Transport`` objects to calculate reaction
      rates and transport properties for a phase.

The following program demonstrates the general method for accessing the following
object types from a ``Solution`` object:

- ``ThermoPhase``: Represents the thermodynamic properties of mixtures containing one or
  more species. Accessed using the ``thermo()`` method on the ``Solution`` object.
- ``Kinetics``: Represents a kinetic mechanism involving one or more phases. Accessed
  using the ``kinetics()`` method on the ``Solution`` object.
- ``Transport``: Computes transport properties for a ``ThermoPhase``. Accessed using the
  ``transport()`` method on the ``Solution`` object.

.. include:: pages/tutorials/cxx-guide/kinetics_transport.cpp
   :code: c++

This program produces the output below::

    Net reaction rates for reactions involving CO2
     11  CO + O (+M) <=> CO2 (+M)         3.54150687e-08
     13  HCO + O <=> CO2 + H              1.95679990e-11
     29  CH2CO + O <=> CH2 + CO2          3.45366954e-17
     30  CO + O2 <=> CO2 + O              2.70102741e-13
     98  CO + OH <=> CO2 + H              6.46935827e-03
    119  CO + HO2 <=> CO2 + OH            1.86807592e-10
    131  CH + CO2 <=> CO + HCO            9.41365868e-14
    151  CH2(S) + CO2 <=> CH2 + CO2       3.11161343e-12
    152  CH2(S) + CO2 <=> CH2O + CO       2.85339294e-11
    225  NCO + O2 <=> CO2 + NO            3.74127381e-19
    228  NCO + NO <=> CO2 + N2            6.25672710e-14
    261  HNCO + O <=> CO2 + NH            6.84524918e-13
    267  HNCO + OH <=> CO2 + NH2          7.78871222e-10
    279  CO2 + NH <=> CO + HNO           -3.30333709e-09
    281  NCO + NO2 <=> CO2 + N2O          2.14286657e-20
    282  CO2 + N <=> CO + NO              6.42658345e-10
    289  CH2 + O2 => CO2 + 2 H            1.51032305e-18
    304  CH2CHO + O => CH2 + CO2 + H      1.00331721e-19

    T        viscosity     thermal conductivity
    ------   -----------   --------------------
    300.0    1.6701e-05    4.2143e-02
    400.0    2.0896e-05    5.2797e-02
    500.0    2.4704e-05    6.2827e-02
    600.0    2.8230e-05    7.2625e-02
    700.0    3.1536e-05    8.2311e-02

.. container:: container

   .. container:: row

      .. container:: col-4 text-left

         .. container:: btn btn-primary
            :tagname: a
            :attributes: href=equil-example.html
                         title="Equilibrium Example Program"

            Previous: Equilibrium Example Program

      .. container:: col-4 text-center

         .. container:: btn btn-primary
            :tagname: a
            :attributes: href=index.html
                         title="C++ Interface Tutorial"

            Return: C++ Interface Tutorial
