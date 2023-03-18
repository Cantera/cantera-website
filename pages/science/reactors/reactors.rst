.. slug: reactors
.. title: Reactor Models in Cantera
.. has_math: true

.. jumbotron::

   .. raw:: html

      <h1 class="display-3">Reactors and Reactor Networks</h1>

   .. class:: lead

      Cantera Reactors and Reactor Networks model zero-dimensional reactors and their
      interactions with the surroundings.

Reactors
========

A Cantera :py:class:`Reactor` represents the simplest form of a chemically reacting system. It
corresponds to an extensive thermodynamic control volume :math:`V`, in which all state variables are
homogeneously distributed. The system is generally unsteady -- that is, all states are functions of time.
In particular, transient state changes due to chemical reactions are possible. However,
thermodynamic (but not chemical) equilibrium is assumed to be present throughout the reactor at all
instants of time.

Reactors can interact with the surrounding environment in multiple ways:

- Expansion/compression work: By moving the walls of the reactor, its volume can be changed and
  expansion or compression work can be done by or on the reactor.

- Heat transfer: An arbitrary heat transfer rate can be defined to cross the boundaries of the
  reactor.

- Mass transfer: The reactor can have multiple inlets and outlets. For the inlets, arbitrary states
  can be defined. Fluid with the current state of the reactor exits the reactor at the outlets.

- Surface interaction: One or multiple walls can influence the chemical reactions in the reactor.
  This is not just restricted to catalytic reactions, but mass transfer between the surface and the
  fluid can also be modeled.

All of these interactions do not have to be constant, but can vary as a function of time or state.
For example, heat transfer can be described as a function of the temperature difference between the
reactor and the environment, or the wall movement can be modeled depending on the pressure
difference. Interactions of the reactor with the environment are defined on one or more *walls*,
*inlets*, and *outlets*.

In addition to single reactors, Cantera is also able to interconnect reactors into a Reactor
Network. Each reactor in a network may be connected so that the contents of one reactor flow into
another. Reactors may also be in contact with one another or the environment via walls that conduct
heat or move to do work.

Reactor Types and Governing Equations
=====================================

All reactor types are modelled using combinations of Cantera's governing equations of state. 
The specific governing equations defining Cantera's supported reactor models are derived and described below.

.. container:: container

   .. row:: 

      .. container:: col-12

         .. container:: card-deck

            .. container:: card

               .. container::
                  :tagname: a
                  :attributes: href="controlreactor.html"
                              title="Control Volume Reactor"

                  .. container:: card-header section-card

                     Control Volume Reactor
                     
                     ..


               .. container:: card-body

                  .. container:: card-text

                     Derivations of governing equations for a Control Volume Reactor.
                     A reactor where the volume is prescribed by the motion of the 
                     reactor's walls.
            .. container:: card

               .. container::
                  :tagname: a
                  :attributes: href="constpresreactor.html"
                              title="Constant Pressure Reactor"

                  .. container:: card-header section-card

                     Constant Pressure Reactor

               .. container:: card-body

                  .. container:: card-text

                     Derivations of governing equations for a Constant Pressure Reactor.
                     A reactor where the pressure is held constant by varying the volume.

            .. container:: card

               .. container::
                  :tagname: a
                  :attributes: href="idealgasreactor.html"
                              title="Ideal Gas Reactor"

                  .. container:: card-header section-card

                     Ideal Gas Reactor

               .. container:: card-body

                  .. container:: card-text

                     Derivations of governing equations for an Ideal Gas
                     Control Volume Reactor.
                     A reactor where all gasses follow the ideal gas law,
                     volume is prescribed by the motion of the reactor's walls, 
                     and temperature is the energy equation state variable.
                     
.. container:: container

   .. row:: 

      .. container:: col-12

         .. container:: card-deck
            
            .. container:: card

               .. container::
                  :tagname: a
                  :attributes: href="idealgasconstpresreactor.html"
                              title="Ideal Gas Constant Pressure Reactor"

                  .. container:: card-header section-card

                     Ideal Gas Constant Pressure Reactor

               .. container:: card-body

                  .. container:: card-text

                     Derivations of governing equations for an Ideal Gas Constant Pressure Reactor.
                     A reactor where all gasses follow the ideal gas law, pressure is held
                     constant, and temperature is the energy equation state variable.
               
            .. container:: card
               
               .. container::
                  :tagname: a
                  :attributes: href="pfr.html"
                              title="Plug Flow Reactor"

                  .. container:: card-header section-card

                     Plug Flow Reactor
                     
                     ..


               .. container:: card-body

                  .. container:: card-text

                     Derivations of governing equations for a Plug Flow Reactor.
                     A steady-state reactor channel where typically an ideal gas 
                     flows through it at a constant mass flow rate.

In some cases, Cantera's solver is insufficient to describe 
a certain configuration. In this situation, there are two options for customizing
a reactor in Cantera. These two approaches are described below: Extensible Reactor and
Custom Reactor.

.. container:: container

   .. row:: 

      .. container:: col-12

         .. container:: card-deck

            .. container:: card

               .. container::
                  :tagname: a
                  :attributes: href="extensiblereactor.html"
                              title="Extensible Reactor"

                  .. container:: card-header section-card

                     Extensible Reactor
                     
                     ..


               .. container:: card-body

                  .. container:: card-text

                     Documentation for reactor type where the user can modify existing
                     governing equations of a chosen reactor.
               
            .. container:: card

               .. container::
                  :tagname: a
                  :attributes: href="customreactor.html"
                              title="Custom Reactor"

                  .. container:: card-header section-card

                     Custom Reactor

               .. container:: card-body

                  .. container:: card-text

                     Documentation for reactor type where Cantera provides chemical and 
                     thermodynamic computations, but external ODE solvers can be applied 
                     to solve user supplied governing equation(s).
               

Reactor Networks
================

While reactors by themselves just define the above governing equations of the
reactor, the time integration is performed in reactor networks. In other words
defining a reactor without assigning it to a reactor network prevents Cantera
from performing time integration to solve the governing equations. A reactor
network is therefore necessary to define even if only a single reactor is considered. 
An example of a single reactor network can be found `here
</examples/python/reactors/combustor.py.html>`__.

.. container:: container

   .. row:: 

      .. container:: col-12

         .. container:: card-deck

            .. container:: card

               .. container::
                  :tagname: a
                  :attributes: href="cvodes.html"
                              title="CVODES"

                  .. container:: card-header section-card

                     Time Integration for Reactor Networks: CVODES
                     
                     ..


               .. container:: card-body

                  .. container:: card-text

                     Cantera uses the CVODES solver from the `SUNDIALS 
                     <https://computing.llnl.gov/projects/sundials>`__ 
                     package to integrate the stiff ODEs of reacting systems. These stiff ODEs are referring to
                     the governing equations defining the reactors above.
                     More in-depth information on the CVODES solver can be found here.

Reactor Peripherals
===================

Reactor networks are also how Cantera interconnects multiple reactors. Not 
only mass flow from one reactor into another can be incorporated, but also heat 
can be transferred, or the wall between reactors can move. Documentation 
on the different ways to connect reactors is explained here.

To set up a network, the following components can be defined in addition
to the reactors previously mentioned:

- :py:class:`Reservoir`: A reservoir can be thought of as an infinitely large volume, in
  which all states are predefined and never change from their initial values.
  Typically, it represents a vessel to define temperature and composition of a
  stream of mass flowing into a reactor, or the ambient fluid surrounding the
  reactor network. Besides, the fluid flow finally exiting a reactor
  network has to flow into a reservoir. In the latter case, the state of the
  reservoir (except pressure) is irrelevant.

- :py:class:`Wall`: A wall separates two reactors, or a reactor and a reservoir. A wall
  has a finite area, may conduct or radiate heat between the two reactors on
  either side, and may move like a piston. See the `Wall Interactions`_ section below for
  detail of how the wall affects the connected reactors.

- :py:class:`Valve`: A valve is a flow devices with mass flow rate that is a function of
  the pressure drop across it. The mass flow rate is computed as:

  .. math::

     \dot m = K_v g(t) f(P_1 - P_2)

  with :math:`K_v` being a proportionality constant that is set using the class
  property :py:func:`Valve.valve_coeff`. Further, :math:`g` and :math:`f`
  are functions of time and pressure drop that are set by class methods
  :py:func:`Valve.set_time_function` and :py:func:`Valve.set_pressure_function`,
  respectively. If no functions are specified, the mass flow rate defaults to:

  .. math::

     \dot m = K_v (P_1 - P_2)

  The pressure difference between upstream (*1*) and downstream (*2*) reservoir
  is defined as :math:`P_1 - P_2`. It is never possible for the flow to reverse
  and go from the downstream to the upstream reactor/reservoir through a line
  containing a :py:class:`Valve` object, which means that the flow rate is set to zero if
  :math:`P_1 < P_2`.

  :py:class:`Valve` objects are often used between an upstream reactor and a downstream
  reactor or reservoir to maintain them both at nearly the same pressure. By
  setting the constant :math:`K_v` to a sufficiently large value, very small
  pressure differences will result in flow between the reactors that counteracts
  the pressure difference.

- :py:class:`MassFlowController`: A mass flow controller maintains a specified mass
  flow rate independent of upstream and downstream conditions. The equation used
  to compute the mass flow rate is

  .. math::

     \dot m = m_0 g(t)

  where :math:`m_0` is a mass flow coefficient and :math:`g` is a function of time
  which are set by class property :py:func:`MassFlowController.mass_flow_coeff`
  and method :py:func:`MassFlowController.set_time_function`, respectively. If no
  function is specified, the mass flow rate defaults to:

  .. math::

     \dot m = m_0

  Note that if :math:`\dot m < 0`, the mass flow rate will be set to zero,
  since a reversal of the flow direction is not allowed.

  Unlike a real mass flow controller, a :py:class:`MassFlowController` object will maintain
  the flow even if the downstream pressure is greater than the upstream
  pressure. This allows simple implementation of loops, in which exhaust gas
  from a reactor is fed back into it through an inlet. But note that this
  capability should be used with caution, since no account is taken of the work
  required to do this.

- :py:class:`PressureController`: A pressure controller is designed to be used in
  conjunction with another 'master' flow controller, typically a
  :py:class:`MassFlowController`. The master flow controller is installed on the inlet of
  the reactor, and the corresponding :py:class:`PressureController` is installed on on
  outlet of the reactor. The :py:class:`PressureController` mass flow rate is equal to the
  master mass flow rate, plus a small correction dependent on the pressure
  difference:

  .. math::

     \dot m = \dot m_{\text{master}} + K_v f(P_1 - P_2)

  where :math:`K_v` is a proportionality constant and :math:`f` is a function of
  pressure drop :math:`P_1 - P_2` that are set by class property
  :py:func:`PressureController.pressure_coeff` and method
  :py:func:`PressureController.set_pressure_function`, respectively. If no
  function is specified, the mass flow rate defaults to:

  .. math::

     \dot m = \dot m_{\text{master}} + K_v (P_1 - P_2)

  Note that if :math:`\dot m < 0`, the mass flow rate will be set to zero,
  since a reversal of the flow direction is not allowed.

  Cantera comes with a broad variety of well-commented example scrips for reactor
  networks. Please see the `Cantera Examples </examples/index.html>`__ for further 
  information.

Wall Interactions
-----------------

Walls are stateless objects in Cantera, meaning that no differential equation
is integrated to determine any wall property. Since it is the wall (piston)
velocity that enters the energy equation, this means that it is the velocity,
not the acceleration or displacement, that is specified. The wall velocity is
computed from

.. math::

   v = K(P_{\mathrm{left}} - P_{\mathrm{right}}) + v_0(t),

where :math:`K` is a non-negative constant, and :math:`v_0(t)` is a specified
function of time. The velocity is positive if the wall is moving to the right.

The total rate of heat transfer through all walls is:

.. math::

   \dot{Q} = \sum_w f_w \dot{Q}_w

where :math:`f_w = \pm 1` indicates the facing of the wall (-1 for the reactor
on the left, +1 for the reactor on the right). The heat flux :math:`\dot{Q}_w`
through a wall :math:`w` connecting reactors "left" and "right" is computed as:

.. math::

   \dot{Q}_w = U A (T_{\mathrm{left}} - T_{\mathrm{right}})
             + \epsilon\sigma A (T_{\mathrm{left}}^4 - T_{\mathrm{right}}^4)
             + A q_0(t)

where :math:`U` is a user-specified heat transfer coefficient (W/m\ :sup:`2`-K),
:math:`A` is the wall area (m\ :sup:`2`), :math:`\epsilon` is the user-specified
emissivity, :math:`\sigma` is the Stefan-Boltzmann radiation constant, and
:math:`q_0(t)` is a user-specified, time-dependent heat flux (W/m\ :sup:`2`).
This definition is such that positive :math:`q_0(t)` implies heat transfer from
the "left" reactor to the "right" reactor. Each of the user-specified terms
defaults to 0.

In case of surface reactions, there can be a net generation (or destruction) of
homogeneous (gas) phase species at the wall. The molar rate of production for
each homogeneous phase species :math:`k` on wall :math:`w` is
:math:`\dot{s}_{k,w}` (in kmol/s/m\ :sup:`2`). The total (mass) production rate
for homogeneous phase species :math:`k` on all walls is:

.. math::

   \dot{m}_{k,wall} = W_k \sum_w A_w \dot{s}_{k,w}

where :math:`W_k` is the molecular weight of species :math:`k` and :math:`A_w`
is the area of each wall. The net mass flux from all walls is then:

.. math::

   \dot{m}_{wall} = \sum_k \dot{m}_{k,wall}

For each surface species :math:`i`, the rate of change of the site fraction
:math:`\theta_{i,w}` on each wall :math:`w` is integrated with time:

.. math::

   \frac{d\theta_{i,w}}{dt} = \frac{\dot{s}_{i,w} n_i}{\Gamma_w}

where :math:`\Gamma_w` is the total surface site density on wall :math:`w` and
:math:`n_i` is the number of surface sites occupied by a molecule of species
:math:`i` (sometimes referred to within Cantera as the molecule's "size").

Common Reactor Types and their Implementation in Cantera
========================================================

Batch Reactor at Constant Volume or at Constant Pressure
--------------------------------------------------------

If you are interested in how a homogeneous chemical composition changes in time
when it is left to its own devices, a simple batch reactor can be used. Two versions
are commonly considered: A rigid vessel with fixed volume but variable
pressure, or a system idealized at constant pressure but varying volume.

In Cantera, such a simulation can be performed very easily. The initial state
of the solution can be specified by composition and a set of thermodynamic
parameters (like temperature and pressure) as a standard Cantera solution
object. Upon its base, a general (Ideal Gas) Reactor or an (Ideal Gas) Constant
Pressure Reactor can be created, depending on if a constant volume or constant
pressure batch reactor should be considered, respectively. The behavior of the
solution in time can be simulated as a very simple Reactor Network containing
only the formerly created reactor.

An example for such a Batch Reactor is given in the `examples
</examples/python/reactors/reactor1.py.html>`__.

Continuously Stirred Tank Reactor
---------------------------------

A Continuously Stirred Tank Reactor (CSTR), also often referred to as
Well-Stirred Reactor (WSR), Perfectly Stirred Reactor (PSR), or Longwell
Reactor, is essentially a single Cantera reactor with an inlet, an outlet, and
constant volume. Therefore, the governing equations for single reactors
defined above apply accordingly.

Steady state solutions to CSTRs are often of interest. In this case, the mass
flow rate :math:`\dot{m}` is constant and equal at inlet and outlet. The mass
contained in the confinement :math:`m` divided by :math:`\dot{m}` defines the mean
residence time of the fluid in the confinement.

At steady state, the time derivatives in the governing equations become zero,
and the system of ordinary differential equations can be reduced to a set of
coupled nonlinear algebraic equations. A Newton solver could be used to solve
this system of equations. However, a sophisticated implementation might be
required to account for the strong nonlinearities and the presence of multiple
solutions.

Cantera does not have such a Newton solver implemented. Instead, steady CSTRs
are simulated by considering a time-dependent constant volume reactor with
specified in- and outflow conditions. Starting off at an initial solution, the
reactor network containing this reactor is advanced in time until the state of
the solution is converged. An example for this procedure is
`the combustor example </examples/python/reactors/combustor.py.html>`__.

A problem can be the ignition of a CSTR: If the reactants are not reactive
enough, the simulation can result in the trivial solution that inflow and
outflow states are identical. To solve this problem, the reactor can be
initialized with a high temperature and/or radical concentration. A good
approach is to use the equilibrium composition of the reactants (which can be
computed using Cantera's ``equilibrate`` function) as an initial guess.

*Cantera always solves a transient problem. If you are interested in steady-state
conditions, you can run your simulation for a long time until the states are converged (see the* 
`surface reactor example </examples/python/reactors/surf_pfr.py.html>`__ *and the* `combustor example
</examples/python/reactors/combustor.html>`__ *).*

.. rubric:: For even more information on reactor equations, check out this reference:

.. [Kee2017] R. J. Kee, M. E. Coltrin, P. Glarborg, and H. Zhu. *Chemically Reacting Flow:
   Theory and Practice*. 2nd Ed. John Wiley and Sons, 2017.

.. rubric:: Footnotes

.. [1] Prior to Cantera 2.6, the sense of the net heat flow was reversed, with positive
   :math:`\dot{Q}` representing heat removal from the system. However, the sense of heat
   flow through a wall between two reactors was the same, with a positive value
   representing heat flow from the left reactor to the right reactor.
