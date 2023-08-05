.. title: Ideal Gas Constant Pressure Reactor
.. has_math: true

.. jumbotron::

   .. raw:: html

      <h1 class="display-4">Ideal Gas Constant Pressure Reactor</h1>

   .. class:: lead

      This page shows the derivation of the governing equations used in
      Cantera's Ideal Gas Constant Pressure Reactor model.

      More information on the Ideal Gas Constant Pressure Reactor class can
      be found `here. <{{% ct_docs doxygen/html/dc/d5d/classCantera_1_1IdealGasConstPressureReactor.html %}}>`__

Ideal Gas Constant Pressure Reactor
***********************************

An Ideal Gas Constant Pressure Reactor is defined by the three state variables: 

- :math:`m`, the mass of the reactor's contents (in kg)

- :math:`T`, the temperature (in K)

- :math:`Y_k`, the mass fractions for each species (dimensionless)

The total mass of the reactor's contents changes as a result of flow through
the reactor's inlets and outlets, and production of homogeneous phase species
on :py:class:`ReactorSurface` objects:

.. math::

   \frac{dm}{dt} = \sum_{in} \dot{m}_{in} - \sum_{out} \dot{m}_{out} +
                    \dot{m}_{wall}
                    \tag{1}

Where the subscripts *in* and *out* refer to the sum of the superscipted property
over all inlets and outlets respectively. A dot above a variable signifies a time 
derivative.

As for the Ideal Gas Reactor, we replace the total enthalpy as a state
variable with the temperature by writing the total enthalpy in terms of the
mass fractions and temperature:

.. math::

   H = m \sum_k Y_k h_k(T)

   \frac{dH}{dt} = h \frac{dm}{dt} + m c_p \frac{dT}{dt}
                   + m \sum_k h_k \frac{dY_k}{dt}

Substituting the corresponding derivatives yields an equation for the
temperature:

.. math::

   m c_p \frac{dT}{dt} = \dot{Q} - \sum_k h_k \dot{m}_{k,gen}
       + \sum_{in} \dot{m}_{in} \left(h_{in} - \sum_k h_k Y_{k,in} \right)
  \tag{2}

The rate at which species :math:`k` is generated through homogeneous phase
reactions is :math:`V \dot{\omega}_k W_k`, and the total rate at which species
:math:`k` is generated is:

.. math::

   \dot{m}_{k,gen} = V \dot{\omega}_k W_k + \dot{m}_{k,wall}

The rate of change in the mass of each species is:

.. math::

   \frac{d(mY_k)}{dt} = \sum_{in} \dot{m}_{in} Y_{k,in} -
                         \sum_{out} \dot{m}_{out} Y_k +
                         \dot{m}_{k,gen}

Expanding the derivative on the left hand side and substituting the equation
for :math:`dm/dt`, the equation for each homogeneous phase species is:

.. math::

   m \frac{dY_k}{dt} = \sum_{in} \dot{m}_{in} (Y_{k,in} - Y_k)+
                      \dot{m}_{k,gen} - Y_k \dot{m}_{wall}
                      \tag{3}

Equations 1-3 are the governing equations for an Ideal Gas Constant Pressure 
Reactor.