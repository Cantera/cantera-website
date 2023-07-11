.. title: Control Volume Reactor
.. has_math: true

.. jumbotron::

   .. raw:: html

      <h1 class="display-4">Control Volume Reactor</h1>

   .. class:: lead

      This page shows the derivation of the governing equations used in
      Cantera's Control Volume Reactor model.

      More information on the Control Volume Reactor class can be found `here. 
      <{{% ct_docs doxygen/html/dc/d5e/classCantera_1_1Reactor.html %}}>`__

Control Volume Reactor
**********************

A homogeneous zero-dimensional reactor. By default, they are closed (no inlets or outlets), 
have fixed volume, and have adiabatic, chemically-inert walls. These properties may all be 
changed by adding appropriate components such as :py:class:`Wall`, :py:class:`MassFlowController` 
and :py:class:`Valve`.

A Control Volume Reactor is defined by the four state variables: 

- :math:`m`, the mass of the reactor's contents (in kg)

- :math:`V`, the reactor volume (in m\ :sup:`3`)

- :math:`U`, the total internal energy of the reactors contents (in J)

- :math:`Y_k`, the mass fractions for each species (dimensionless)

The total mass of the reactor's contents changes as a result of flow through
the reactor's inlets and outlets, and production of homogeneous phase species
on the reactor :py:class:`Wall`.

.. math::

   \frac{dm}{dt} = \sum_{in} \dot{m}_{in} - \sum_{out} \dot{m}_{out} +
                    \dot{m}_{wall}
                    \tag{1}

Where the subscripts *in* and *out* refer to the sum of the superscipted property
over all inlets and outlets respectively. A dot above a variable signifies a time 
derivative. A Reactor *wall* is defined `here.
<{{% ct_docs sphinx/html/cython/zerodim.html#cantera.Wall %}}>`__ 

The reactor volume changes as a function of time due to the motion of one or
more walls:

.. math::

   \frac{dV}{dt} = \sum_w f_w A_w v_w(t)
   \tag{2}

where :math:`f_w = \pm 1` indicates the facing of the wall (whether moving the wall increases or
decreases the volume of the reactor), :math:`A_w` is the
surface area of the wall, and :math:`v_w(t)` is the velocity of the wall as a
function of time.

The equation for the total internal energy is found by writing the first law
for an open system:

.. math::

   \frac{dU}{dt} = - p \frac{dV}{dt} + \dot{Q} +
                    \sum_{in} \dot{m}_{in} h_{in} - h \sum_{out} \dot{m}_{out}
   \tag{3}

Where :math:`\dot{Q}` is the net rate of heat addition to the system.

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

Equations 1-4 are the governing equations for a Control Volume Reactor.