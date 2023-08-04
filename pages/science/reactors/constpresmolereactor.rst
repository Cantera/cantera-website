.. title: Constant Pressure Reactor
.. has_math: true

.. jumbotron::

   .. raw:: html

      <h1 class="display-3">Constant Pressure Mole Reactor</h1>

   .. class:: lead

      This page shows the derivation of the governing equations used in
      Cantera's Constant Pressure Mole Reactor model.

      More information on the Constant Pressure Mole Reactor class can be found `here.
      <{{% ct_docs doxygen/html/d5/d7d/classCantera_1_1ConstPressureMoleReactor.html %}}>`__

Constant Pressure Mole Reactor
******************************

For this reactor model, the pressure is held constant. The energy equation is
defined by the total enthalpy.

A Constant Pressure Mole Reactor is defined by the two state variables:

- :math:`H`, the total enthalpy of the reactor's contents (in J)

- :math:`n_k`, the number of moles for each species (in kmol)

Using the definition of the total enthalpy:

.. math::

   H = U + pV

   \frac{d H}{d t} = \frac{d U}{d t} + p \frac{dV}{dt} + V \frac{dp}{dt}

Noting that :math:`dp/dt = 0` and substituting into the energy equation yields:

.. math::

   \frac{dH}{dt} = \dot{Q} + \sum_{in} \dot{n}_{in} \bar{h}_{in}
                   - \bar{h} \sum_{out} \dot{n}_{out}
                   \tag{1}

Where the total specific enthalpy :math:`h` is defined as :math:`h = \sum_k{\bar{h}_k n_k}`.
The enthalpy terms in equation 2 appear due to enthalpy flowing in and out
of the reactor.
The rate of heat transfer :math:`\dot{Q}` can replace :math:`\frac{d U}{d t} + p \frac{dV}{dt}` in the above equation due to the first law
of thermodynamics, which states :math:`\dot{Q} = \dot{H}` in a closed system where
no work is done.
Positive :math:`\dot{Q}` represents heat addition to the system.

The moles of each species in the reactor's contents changes as a result of flow through
the reactor's inlets and outlets, and production of homogeneous gas phase species and reactions on the reactor :py:class:`Wall`.
The rate of moles of species :math:`k` generated through homogeneous phase
reactions is :math:`V \dot{\omega}_k`, and the total rate at which moles of species
:math:`k` changes is:

.. math::

   \frac{dn_k}{dt} = V \dot{\omega}_k + \sum_{in} \dot{n}_{k, in} - \sum_{out} \dot{n}_{k, out} + \dot{n}_{k, wall}
   \tag{2}

Where the subscripts *in* and *out* refer to the sum of the superscripted property
over all inlets and outlets respectively. A dot above a variable signifies a time
derivative. Reactor *Walls* are defined `here. <{{% ct_docs sphinx/html/cython/zerodim.html#cantera.Wall %}}>`__

Equations 1-2 are the governing equations for a Constant Pressure Mole Reactor.
