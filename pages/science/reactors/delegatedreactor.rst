.. title: Delegated Reactors in Cantera
.. has_math: true

.. jumbotron::

   .. raw:: html

      <h1 class="display-3">Delegated Reactors in Cantera</h1>

   .. class:: lead

      This guide defines and links to an example of a Delegated Reactor.

Delegating Reactors
*******************

In some cases, Cantera's solver is insufficient to describe 
a certain configuration. In this situation, Cantera can 
still be used to provide chemical and thermodynamic computations, 
but external ODE solvers can be applied. This demonstrates an approach 
for solving problems where Cantera's reactor network model cannot 
be configured to describe the system in question.

The Delegated Reactor type is defined by `governing equations 
</examples/python/reactors/surf_pfr.py.html>`__ 
modified or supplied by the user in Python. The user may entirely bypass 
the provided governing equations, shown in the example below, or modify 
Cantera's pre-existing Reactor governing equations. The state variables 
available for modification depend on the user provided ODE or the type 
of Reactor base class chosen. For example, choosing an `Ideal 
Gas Reactor </science/reactors/idealgasreactor.html>`__ 

add explaination top level for using gov and replacing
add explanation of how del react works (y(0), before, after functions etc, inputs req (dmdt ect))

A use case of a Delegated Reactor is where Cantera is used for evaluating 
thermodynamic properties and kinetic rates while an external ODE solver 
is used to integrate the resulting equations.

See this example of a `custom ODE solver </examples/python/reactors/custom.py.html>`__.