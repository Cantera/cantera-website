.. title: Ideal Gas Constant Pressure Mole Reactor
.. has_math: true

.. jumbotron::

   .. raw:: html

      <h1 class="display-4">Ideal Gas Constant Pressure
      Mole Reactor</h1>

   .. class:: lead

      This page shows the derivation of the governing equations used in
      Cantera's Ideal Gas Constant Pressure Mole Reactor model.

      More information on the Ideal Gas Constant Pressure Mole Reactor class can
      be found `here. <{{% ct_docs doxygen/html/de/daa/classCantera_1_1IdealGasConstPressureMoleReactor.html %}}>`__

Ideal Gas Constant Pressure Reactor
***********************************

An Ideal Gas Constant Pressure Mole Reactor is defined by the two state variables:

- :math:`T`, the temperature (in K)

- :math:`n_k`, the number of moles for each species (in kmol)

The energy equation in terms of temperature is necessary as we replaced enthalpy in the state vector with temperature.
We develop the equation for temperature by writing the total enthalpy in terms of the molar enthalpy and moles of each species.

.. math::

   H = \sum_k \bar{h}_k(T) n_k(T)

   \frac{dH}{dt} = \frac{dT}{dt}\sum_k n_k \bar{c_{p,k}} + \sum \bar{h}_k \dot{n}_k

After some manipulations yields an equation for the
temperature:

.. math::

   \sum_k n_k \bar{c}_{p,k} \frac{dT}{dt} = \dot{Q} - \sum \bar{h}_k \dot{n}_k
  \tag{1}

The moles of each species in the reactor's contents changes as a result of flow through
the reactor's inlets and outlets, and production of homogeneous gas phase species and reactions on the reactor :py:class:`Wall`.
The rate of moles of species :math:`k` generated through homogeneous phase
reactions is :math:`V \dot{\omega}_k`, and the total rate at which moles of species
:math:`k` changes is:

.. math::

   \frac{dn_k}{dt} = V \dot{\omega}_k + \sum_{in} \dot{n}_{k, in} - \sum_{out} \dot{n}_{k, out} + \dot{n}_{k, wall}
   \tag{2}

Where the subscripts *in* and *out* refer to the sum of the corresponding property
over all inlets and outlets respectively. A dot above a variable signifies a time
derivative. Reactor *Walls* are defined `here. <{{% ct_docs sphinx/html/cython/zerodim.html#cantera.Wall %}}>`__


Equations 1-2 are the governing equations for an Ideal Gas Constant Pressure
Mole Reactor.
