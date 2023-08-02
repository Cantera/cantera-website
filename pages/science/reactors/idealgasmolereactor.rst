.. title: Ideal Gas Mole Reactor
.. has_math: true

.. jumbotron::

   .. raw:: html

      <h1 class="display-3">Ideal Gas Mole Reactor</h1>
   .. class:: lead

      This page shows the derivation of the governing equations used in
      Cantera's Ideal Gas Mole Reactor model.

      More information on the Ideal Gas Mole Reactor class can be found `here.
      <{{% ct_docs doxygen/html/d0/d03/classCantera_1_1IdealGasMoleReactor.html %}}>`__

Ideal Gas Mole Reactor
**********************

An Ideal Gas Mole Reactor is defined by the three state variables:

- :math:`T`, the temperature (in K)

- :math:`V`, the reactor volume (in m\ :sup:`3`)

- :math:`n_k`, the number of moles for each species (in kmol)

The energy equation in terms of temperature is necessary as we replaced internal energy in the state vector with temperature.
We develop the equation for temperature by writing the total enthalpy in terms of the molar enthalpy and moles of each species.

.. math::

   U = \sum_k \bar{u}_k(T) n_k(T)

   \frac{dU}{dt} = \frac{dT}{dt}\sum_k n_k \bar{c_{v,k}} + \sum \bar{u}_k \dot{n}_k

After some manipulations yields an equation for the
temperature:

.. math::

   \frac{dT}{dt} = \frac{\dot{Q} - \sum \bar{u}_k \dot{n}_k}{\sum_k n_k \bar{c}_{p,k} }
  \tag{1}

The reactor volume changes as a function of time due to the motion of one or
more walls:

.. math::

   \frac{dV}{dt} = \sum_w f_w A_w v_w(t)
   \tag{2}

Where :math:`f_w = \pm 1` indicates the facing of the wall (whether moving the wall increases or decreases the volume of the reactor), :math:`A_w` is the surface area of the wall, and :math:`v_w(t)` is the velocity of the wall as a function of time.

Finally, the moles of each species in the reactor's contents changes as a result of flow through the reactor's inlets and outlets, and production of homogeneous gas phase species and reactions on the reactor :py:class:`Wall`.
The rate of moles of species :math:`k` generated through homogeneous phase
reactions is :math:`V \dot{\omega}_k`, and the total rate at which moles of species
:math:`k` is generated is:

.. math::

   \frac{dn_k}{dt} = V \dot{\omega}_k + \sum_{in} \dot{n}_{in} - \sum_{out} \dot{n}_{out} + \dot{n}_{wall}
   \tag{3}

Equations 1-3 are the governing equations for an Ideal Gas Mole Reactor.
