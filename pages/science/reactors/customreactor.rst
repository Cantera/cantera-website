.. title: Custom Reactors
.. has_math: true

.. jumbotron::

   .. raw:: html

      <h1 class="display-3">Custom Reactors</h1>

   .. class:: lead

      This page defines and links to an example of a Custom Reactor.

Custom Reactors
***************

In some cases, Cantera's solver is insufficient to describe 
a certain configuration. In this situation, Cantera can 
still be used to provide chemical and thermodynamic computations, 
but external ODE solvers can be applied. The user may entirely bypass 
the provided governing equations, shown in the custom.py example 
linked below. This demonstrates an approach 
for solving problems where Cantera's reactor network model cannot 
be configured to describe the system in question, as in an `Extensible
Reactor </science/reactors/delegatedreactor.html>`__.

The process to bypass Cantera's existing governing equations can be
described in 7 steps:

#. Define your new class
   
   a. Create `_init_` function
   b. Specify the new custom ODEs

#. Create a new gas object and set initial conditions
#. Integrate custom equations over a single timestep
#. Set new gas state to the values obtained by the supplied ODE solver
#. Save the gas state
#. Repeat integration over all timesteps (steps 3-5)
#. The final state vector contains all gas properties obtained from Cantera for each timestep

A use case of a Custom Reactor where Cantera is used for evaluating 
thermodynamic properties and kinetic rates while an external ODE solver 
is used to integrate the resulting equations is linked here in the 
`custom.py example </examples/python/reactors/custom.py.html>`__.