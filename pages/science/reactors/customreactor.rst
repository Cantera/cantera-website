.. title: Custom Reactors
.. has_math: true

.. jumbotron::

   .. raw:: html

      <h1 class="display-3">Custom Reactors</h1>

   .. class:: lead

      This page defines and links to an example of a Custom Reactor.

Custom Reactors
***************

If using an external integrator (an integrator besides CVODES) is 
desired, a `Custom Reactor </science/reactors/customreactor.html>`__
may be the most appropriate Reactor class to use. In this situation, 
Cantera can still be used to provide chemical and thermodynamic computations, 
but external ODE solvers can be applied. The user may entirely bypass 
the provided governing equations, shown in the custom.py example 
linked below. This demonstrates an approach for solving problems where 
Cantera's reactor network model cannot be configured to describe the system 
in question. If the existing governing equations *can* be modified to suit 
the user's needs and the existing integrator is sufficient, an `Extensible
Reactor </science/reactors/extensiblereactor.html>`__ may be better
suited.

The process to bypass Cantera's existing governing equations can be
described in 7 steps:

#. Define your new class
   
   a. Create ``__init__`` function
   b. Specify the new custom ODEs

#. Create a new phase object(s) and set initial conditions
#. Integrate custom equations over a single timestep
#. Set new phase state to the values obtained by the supplied ODE solver
#. Save the phase state
#. Repeat integration over all timesteps (steps 3-5)
#. The final state vector contains all phase properties obtained from Cantera for each timestep

A use case of a Custom Reactor where Cantera is used for evaluating 
thermodynamic properties and kinetic rates while an external ODE solver 
is used to integrate the resulting equations is linked here in the 
`custom.py example </examples/python/reactors/custom.py.html>`__.