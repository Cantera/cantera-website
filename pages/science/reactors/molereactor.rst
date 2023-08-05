.. title: Mole Reactor
.. has_math: true

.. jumbotron::

   .. raw:: html

      <h1 class="display-4">Mole Reactor</h1>

   .. class:: lead

      This page shows the derivation of the governing equations used in
      Cantera's Mole Reactor model.

      More information on the Mole Reactor class can be found `here.
      <{{% ct_docs doxygen/html/da/d29/classCantera_1_1MoleReactor.html %}}>`__

Mole Reactor
************

A homogeneous zero-dimensional reactor. By default, they are closed (no inlets or outlets),
have fixed volume, and have adiabatic, chemically-inert walls. These properties may all be
changed by adding appropriate components such as :py:class:`Wall`, :py:class:`ReactorSurface`,
:py:class:`MassFlowController`, and :py:class:`Valve`.

A Mole Reactor is defined by the three state variables:

- :math:`U`, the total internal energy of the reactor's contents (in J)

- :math:`V`, the reactor volume (in m\ :sup:`3`)

- :math:`n_k`, the number of moles for each species (in kmol)

The equation for the total internal energy is found by writing the first law
for an open system:

.. math::

   \frac{dU}{dt} = - p \frac{dV}{dt} + \dot{Q} +
                    \sum_{in} \dot{n}_{in} \bar{h}_{in} - \bar{h} \sum_{out} \dot{n}_{out}
   \tag{1}

Where :math:`\dot{Q}` is the net rate of heat addition to the system.

The reactor volume changes as a function of time due to the motion of one or
more :py:class:`Wall`\ s:

.. math::

   \frac{dV}{dt} = \sum_w f_w A_w v_w(t)
   \tag{2}

where :math:`f_w = \pm 1` indicates the facing of the wall (whether moving the wall increases or
decreases the volume of the reactor), :math:`A_w` is the
surface area of the wall, and :math:`v_w(t)` is the velocity of the wall as a
function of time.

The moles of each species in the reactor's contents changes as a result of flow through
the reactor's inlets and outlets, and production of homogeneous gas phase species and reactions on the reactor :py:class:`Wall`.
The rate of moles of species :math:`k` generated through homogeneous phase
reactions is :math:`V \dot{\omega}_k`, and the total rate at which moles of species
:math:`k` changes is:

.. math::

   \frac{dn_k}{dt} = V \dot{\omega}_k + \sum_{in} \dot{n}_{k, in} - \sum_{out} \dot{n}_{k, out} + \dot{n}_{k, wall}
   \tag{3}

Where the subscripts *in* and *out* refer to the sum of the corresponding property
over all inlets and outlets respectively. A dot above a variable signifies a time
derivative.

Equations 1-3 are the governing equations for a Mole Reactor.
