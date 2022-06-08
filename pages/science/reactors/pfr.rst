.. title: Plug Flow Reactor
.. has_math: true

.. jumbotron::

   .. raw:: html

      <h1 class="display-3">Plug Flow Reactor</h1>

   .. class:: lead

      This page shows the derivation of the governing equations used in
      Cantera's Plug Flow Reactor model.

Plug Flow Reactor
*****************

A Plug-Flow Reactor (PFR) represents a steady-state channel with a
cross-sectional area :math:`A`. Typically an ideal gas flows through it at a constant
mass flow rate :math:`\dot{m}`. Perpendicular to the flow direction, the gas is
considered to be completely homogeneous. In the axial direction :math:`z`, the states
of the gas is allowed to change. However, all diffusion processes are neglected.

Plug-Flow Reactors are often used to simulate ignition delay times, emission
formation, and catalytic processes.

A Plug Flow Reactor is defined by the three state variables: 

- :math:`m`, the mass of the reactor's contents (in kg)

- :math:`U`, the temperature (in K)

- :math:`Y_k`, the mass fractions for each species (dimensionless)

Mass conservation:

.. math::

   \frac{d(\rho u A)}{dz} =  P' \sum_k \dot{s}_k W_k
   \tag{1}

where :math:`u` is the axial velocity in (m/s) and :math:`P'` is the chemically active
channel perimeter in m (chemically active perimeter per unit length).

Energy conservation:

.. math::

  \rho u A c_p \frac{d T}{d z} =
  - A \sum_k h_k \dot{\omega}_k W_k
  - P' \sum_k h_k \dot{s}_k W_k
  + U P (T_w - T)
   \tag{2}

where :math:`U` is the heat transfer coefficient in W/m/K, :math:`P` is the perimeter of
the duct in m, and :math:`T_w` is the wall temperature in K. Kinetic and
potential energies are neglected.

Momentum conservation in the axial direction:

.. math::

  \rho u A \frac{d u}{d z} + u P' \sum_k \dot{s}_k W_k =
  - \frac{d (p A)}{dz} - \tau_w P
   \tag{3}

where :math:`\tau_w` is the wall friction coefficient (which might be computed from
Reynolds number based correlations).

Continuity equation of species :math:`k`:

.. math::

  \rho u \frac{d Y_k}{dz} + Y_k P' \sum_k \dot{s}_k W_k =
  \dot{\omega}_k W_k + P' \dot{s}_k W_k
  \tag{4}

Even though this problem extends geometrically in one direction, it can be
modeled via zero-dimensional reactors. Due to the neglecting of diffusion,
downstream parts of the reactor have no influence on upstream parts. Therefore,
PFRs can be modeled by marching from the beginning to the end of the reactor.

Cantera does not (yet) provide dedicated class to solve the PFR equations (The
``FlowReactor`` class is currently under development). However, there are two
ways to simulate a PFR with the reactor elements previously presented. Both
rely on the assumption that pressure is approximately constant throughout the
Plug-Flow Reactor and that there is no friction. The momentum conservation
equation is thus neglected.

PFR Modeling by Considering a Lagrangian Reactor
************************************************

A Plug-Flow Reactor can also be described from a Lagrangian point of view. An
unsteady fluid particle is considered which travels along the axial streamline
through the PFR. Since there is no information traveling upstream, the state
change of the fluid particle can be computed by a forward (upwind) integration
in time. Using the continuity equation, the speed of the particle can be
derived. By integrating the velocity in time, the temporal information can be
translated into the spatial resolution of the PFR.

An example for this procedure can be found in the `PFR example </examples/python/reactors/pfr.py.html>`__.

PFR Modeling as a Series of CSTRs
*********************************

The Plug-Flow Reactor is spatially discretized into a large number of axially
distributed volumes. These volumes are modeled to be steady-state CSTRs.

The only reason to use this approach as opposed to the Lagrangian one is if you
need to include surface reactions, because the system of equations ends up
being a DAE system instead of an ODE system.

In Cantera, it is sufficient to consider a single reactor and march it forward
in time, because there is no information traveling upstream. The mass flow rate
:math:`\dot{m}` through the PFR enters the reactor from an upstream reservoir. For
the first reactor, the reservoir conditions are the inflow boundary conditions
of the PFR. By performing a time integration as described in `Continuously
Stirred Tank Reactor </science/reactors.html>`__ until the state of the reactor is converged, the
steady-state CSTR solution is computed. The state of the CSTR is the inlet
boundary condition for the next CSTR downstream.

An example for this procedure can be found in the `PFR example
</examples/python/reactors/pfr.py.html>`__ and the `surface PFR example
</examples/python/reactors/surf_pfr.py.html>`__.