.. title: Ideal Gas Reactor
.. has_math: true

.. jumbotron::

   .. raw:: html

      <h1 class="display-4">Ideal Gas Reactor</h1>
   .. class:: lead

      This page shows the derivation of the governing equations used in
      Cantera's Ideal Gas Reactor model.

      More information on the Ideal Gas Reactor class can be found `here. 
      <{{% ct_docs doxygen/html/dc/d06/classCantera_1_1IdealGasReactor.html %}}>`__

Ideal Gas Reactor
*****************

An Ideal Gas Reactor is defined by the four state variables: 

- :math:`m`, the mass of the reactor's contents (in kg)

- :math:`V`, the reactor volume (in m\ :sup:`3`)

- :math:`T`, the temperature (in K)

- :math:`Y_k`, the mass fractions for each species (dimensionless)

The total mass of the reactor's contents changes as a result of flow through
the reactor's inlets and outlets, and production of homogeneous phase species
on :py:class:`ReactorSurface` objects:

.. math::

   \frac{dm}{dt} = \sum_{in} \dot{m}_{in} - \sum_{out} \dot{m}_{out} +
                    \dot{m}_{wall}
                    \tag{1}

Where the subscripts *in* and *out* refer to the sum of the corresponding property
over all inlets and outlets respectively. A dot above a variable signifies a time 
derivative.

The reactor volume changes as a function of time due to the motion of one or
more :py:class:`Wall` objects:

.. math::

   \frac{dV}{dt} = \sum_w f_w A_w v_w(t)
   \tag{2}

Where :math:`f_w = \pm 1` indicates the facing of the wall (whether moving the wall increases or
decreases the volume of the reactor), :math:`A_w` is the
surface area of the wall, and :math:`v_w(t)` is the velocity of the wall as a
function of time.

In case of the Ideal Gas Reactor Model, the reactor temperature :math:`T` is
used instead of the total internal energy :math:`U` as a state variable. For an
ideal gas, we can rewrite the total internal energy in terms of the mass
fractions and temperature:

.. math::

   U = m \sum_k Y_k u_k(T)

   \frac{dU}{dt} = u \frac{dm}{dt}
                   + m c_v \frac{dT}{dt}
                   + m \sum_k u_k \frac{dY_k}{dt}

Substituting the corresponding derivatives yields an equation for the
temperature:

.. math::

   m c_v \frac{dT}{dt} = - p \frac{dV}{dt} + \dot{Q}
       + \sum_{in} \dot{m}_{in} \left( h_{in} - \sum_k u_k Y_{k,in} \right)
       - \frac{p V}{m} \sum_{out} \dot{m}_{out} - \sum_k \dot{m}_{k,gen} u_k
  \tag{3}

While this form of the energy equation is somewhat more complicated, it
significantly reduces the cost of evaluating the system Jacobian, since the
derivatives of the species equations are taken at constant temperature instead
of constant internal energy.

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
                      \tag{4}

Equations 1-4 are the governing equations for an Ideal Gas Reactor.