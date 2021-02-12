.. slug: flames
.. title: One-dimensional Flames
.. has_math: true

.. jumbotron::

   .. raw:: html

      <h1 class="display-3">One-Dimensional Flames</h1>

   .. class:: lead

      Cantera includes a set of models for representing steady-state, quasi-one-
      dimensional reacting flows.

   These models can be used to simulate a number of common flames, such as:

   - freely-propagating premixed laminar flames
   - burner-stabilized premixed flames
   - counterflow diffusion flames
   - counterflow (strained) premixed flames

   Additional capabilities include simulation of surface reactions, which can be
   used to represent processes such as combustion on a catalytic surface or
   chemical vapor deposition processes.

   All of these configurations are simulated using a common set of governing
   equations within a 1D flow domain, with the differences between the models
   being represented by differences in the boundary conditions applied. Here, we
   describe the governing equations and the various boundary conditions which can
   be applied.

Stagnation Flow Governing Equations
===================================

Cantera models flames that are stabilized in an axisymmetric stagnation flow,
and computes the solution along the stagnation streamline (:math:`r=0`), using a
similarity solution to reduce the three-dimensional governing equations to a
single dimension.

The governing equations for a steady axisymmetric stagnation flow follow those
derived in Section 6.2 of [Kee2017]_:

*Continuity*:

.. math::

   \frac{\partial\rho u}{\partial z} + 2 \rho V = 0

*Radial momentum*:

.. math::

   \rho u \frac{\partial V}{\partial z} + \rho V^2 =
       - \Lambda
       + \frac{\partial}{\partial z}\left(\mu \frac{\partial V}{\partial z}\right)


*Energy*:

.. math::

   \rho c_p u \frac{\partial T}{\partial z} =
       \frac{\partial}{\partial z}\left(\lambda \frac{\partial T}{\partial z}\right)
       - \sum_k j_k c_{p,k} \frac{\partial T}{\partial z}
       - \sum_k h_k W_k \dot{\omega}_k

*Species*:

.. math::

   \rho u \frac{\partial Y_k}{\partial z} = - \frac{\partial j_k}{\partial z}
       + W_k \dot{\omega}_k

where :math:`\rho` is the density, :math:`u` is the axial velocity, :math:`v` is
the radial velocity, :math:`V = v/r` is the scaled radial velocity,
:math:`\Lambda` is the pressure eigenvalue (independent of :math:`z`),
:math:`\mu` is the dynamic viscosity, :math:`c_p` is the heat capacity at
constant pressure, :math:`T` is the temperature, :math:`\lambda` is the thermal
conductivity, :math:`Y_k` is the mass fraction of species :math:`k`, :math:`j_k`
is the diffusive mass flux of species :math:`k`, :math:`c_{p,k}` is the specific
heat capacity of species :math:`k`, :math:`h_k` is the enthalpy of species
:math:`k`, :math:`W_k` is the molecular weight of species :math:`k`, and
:math:`\dot{\omega}_k` is the molar production rate of species :math:`k`.

The tangential velocity :math:`w` has been assumed to be zero, and the fluid has
been assumed to behave as an ideal gas.

To help in the solution of the discretized problem, it is convenient to write a
differential equation for the scalar :math:`\Lambda`:

.. math::

   \frac{d\Lambda}{dz} = 0

Diffusive Fluxes
----------------

The species diffusive mass fluxes :math:`j_k` are computed according to either a
mixture-averaged or multicomponent formulation. If the mixture-averaged
formulation is used, the calculation performed is:

.. math::

   j_k^* = - \rho \frac{W_k}{\overline{W}} D_{km}^\prime \frac{\partial X_k}{\partial z}

   j_k = j_k^* - Y_k \sum_i j_i^*

where :math:`\overline{W}` is the mean molecular weight of the mixture, :math:`D_{km}^\prime` is the
mixture-averaged diffusion coefficient for species :math:`k`, and :math:`X_k` is the mole fraction
for species :math:`k`. The diffusion coefficients used here are those computed by the method
`GasTransport::getMixDiffCoeffs <{{% ct_docs doxygen/html/d8/d58/classCantera_1_1GasTransport.html#a699001499937e42f790551f01bce4424 %}}>`__.
The correction applied by the second equation ensures that the sum of the mass fluxes is zero, a
condition which is not inherently guaranteed by the mixture-averaged formulation.

When using the multicomponent formulation, the mass fluxes are computed
according to:

.. math::

   j_k = \frac{\rho W_k}{\overline{W}^2} \sum_i W_i D_{ki} \frac{\partial X_i}{\partial z}
         - \frac{D_k^T}{T} \frac{\partial T}{\partial z}

where :math:`D_{ki}` is the multicomponent diffusion coefficient and
:math:`D_k^T` is the Soret diffusion coefficient (used only if calculation of
this term is specifically enabled).

Boundary Conditions
===================

Inlet boundary
--------------

For a boundary located at a point :math:`z_0` where there is an inflow, values
are supplied for the temperature :math:`T_0`, the species mass fractions
:math:`Y_{k,0}` the scaled radial velocity :math:`V_0`, and the mass flow rate
:math:`\dot{m}_0` (except in the case of the freely-propagating flame).

The following equations are solved at the point :math:`z = z_0`:

.. math::

   T(z_0) = T_0

   V(z_0) = V_0

   \dot{m}_0 Y_{k,0} - j_k(z_0) - \rho(z_0) u(z_0) Y_k(z_0) = 0

If the mass flow rate is specified, we also solve:

.. math::

   \rho(z_0) u(z_0) = \dot{m}_0

Otherwise, we solve:

.. math::

   \Lambda(z_0) = 0

Outlet boundary
---------------

For a boundary located at a point :math:`z_0` where there is an outflow, we
solve:

.. math::

   \Lambda(z_0) = 0

   \left.\frac{\partial T}{\partial z}\right|_{z_0} = 0

   \left.\frac{\partial Y_k}{\partial z}\right|_{z_0} = 0

   V(z_0) = 0


Symmetry boundary
-----------------

For a symmetry boundary located at a point :math:`z_0`, we solve:

.. math::

   \rho(z_0) u(z_0) = 0

   \left.\frac{\partial V}{\partial z}\right|_{z_0} = 0

   \left.\frac{\partial T}{\partial z}\right|_{z_0} = 0

   j_k(z_0) = 0

Reacting surface
----------------

For a surface boundary located at a point :math:`z_0` on which reactions may
occur, the temperature :math:`T_0` is specified. We solve:

.. math::

   \rho(z_0) u(z_0) = 0

   V(z_0) = 0

   T(z_0) = T_0

   j_k(z_0) + \dot{s}_k W_k = 0

where :math:`\dot{s}_k` is the molar production rate of the gas-phase species
:math:`k` on the surface. In addition, the surface coverages :math:`\theta_i`
for each surface species :math:`i` are computed such that :math:`\dot{s}_i = 0`.

.. rubric:: References

.. [Kee2017] R. J. Kee, M. E. Coltrin, P. Glarborg, and H. Zhu. *Chemically Reacting Flow:
   Theory and Practice*. 2nd Ed. John Wiley and Sons, 2017.
