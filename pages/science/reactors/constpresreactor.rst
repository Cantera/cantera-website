.. title: Deriving Constant Pressure Reactor Governing Equations
.. has_math: true

.. jumbotron::

   .. raw:: html

      <h1 class="display-3">Deriving Constant Pressure Reactor Governing 
      Equations</h1>

   .. class:: lead

      This guide shows you how to derive the governing equations used to define a 
      Constant Pressure Reactor

Constant Pressure Reactor
*************************

For this reactor model, the pressure is held constant. The volume is not a
state variable, but instead takes on whatever value is consistent with holding
the pressure constant. The total enthalpy replaces the total internal energy
as a state variable. 

A Constant Pressure Reactor is defined by the three state variables: 

- :math:`m`, the mass of the reactor's contents (in kg)

- :math:`H`, the total enthalpy of the reactors contents (in J)

- :math:`Y_k`, the mass fractions for each species (dimensionless)

The total mass of the reactor's contents changes as a result of flow through
the reactor's inlets and outlets, and production of homogeneous phase species
on the reactor :py:class:`Wall`:

.. math::

   \frac{dm}{dt} = \sum_{in} \dot{m}_{in} - \sum_{out} \dot{m}_{out} +
                    \dot{m}_{wall}
                    \tag{1}

Using the definition of the total enthalpy:

.. math::

   H = U + pV

   \frac{d H}{d t} = \frac{d U}{d t} + p \frac{dV}{dt} + V \frac{dp}{dt}

Noting that :math:`dp/dt = 0` and substituting into the energy equation yields:

.. math::

   \frac{dH}{dt} = - \dot{Q} + \sum_{in} \dot{m}_{in} h_{in}
                   - h \sum_{out} \dot{m}_{out}
                   - \tag{2}

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

Equations 1-3 are the governing equations for a Constant Pressure Reactor.