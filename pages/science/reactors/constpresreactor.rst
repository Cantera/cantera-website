.. title: Constant Pressure Reactor
.. has_math: true

.. jumbotron::

   .. raw:: html

      <h1 class="display-4">Constant Pressure Reactor</h1>

   .. class:: lead

      This page shows the derivation of the governing equations used in
      Cantera's Constant Pressure Reactor model.
      
      More information on the Constant Pressure Reactor class can be found `here. 
      <{{% ct_docs doxygen/html/d5/dfb/classCantera_1_1ConstPressureReactor.html %}}>`__

Constant Pressure Reactor
*************************

For this reactor model, the pressure is held constant. The energy equation is 
defined by the total enthalpy.

A Constant Pressure Reactor is defined by the three state variables: 

- :math:`m`, the mass of the reactor's contents (in kg)

- :math:`H`, the total enthalpy of the reactor's contents (in J)

- :math:`Y_k`, the mass fractions for each species (dimensionless)

The total mass of the reactor's contents changes as a result of flow through
the reactor's inlets and outlets, and production of homogeneous phase species
on the reactor :py:class:`Wall`:

.. math::

   \frac{dm}{dt} = \sum_{in} \dot{m}_{in} - \sum_{out} \dot{m}_{out} +
                    \dot{m}_{wall}
                    \tag{1}

Where the subscripts *in* and *out* refer to the sum of the superscipted property
over all inlets and outlets respectively. A dot above a variable signifies a time 
derivative. A Reactor *wall* is defined `here.
<{{% ct_docs sphinx/html/cython/zerodim.html#cantera.Wall %}}>`__ 

Using the definition of the total enthalpy:

.. math::

   H = U + pV

   \frac{d H}{d t} = \frac{d U}{d t} + p \frac{dV}{dt} + V \frac{dp}{dt}

Noting that :math:`dp/dt = 0` and substituting into the energy equation yields:

.. math::

   \frac{dH}{dt} = \dot{Q} + \sum_{in} \dot{m}_{in} h_{in}
                   - h \sum_{out} \dot{m}_{out}
                   \tag{2}

Where the total specific enthalpy :math:`h` is defined as :math:`h = \sum_k{h_k Y_k}`.
The enthalpy terms in equation 2 appear due to enthalpy flowing in and out 
of the reactor. The rate of heat transfer :math:`\dot{Q}` can replace 
:math:`\frac{d U}{d t} + p \frac{dV}{dt}` in the above equation due to the first law 
of thermodynamics, which states :math:`\dot{Q} = \dot{H}` in a closed system where 
no work is done. Positive :math:`\dot{Q}` represents heat addition to the system.

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