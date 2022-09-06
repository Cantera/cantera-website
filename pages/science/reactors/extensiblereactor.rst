.. title: Extensible Reactors in Cantera
.. has_math: true

.. jumbotron::

   .. raw:: html

      <h1 class="display-3">Extensible Reactor</h1>

   .. class:: lead

      This page defines and links to an example of an Extensible Reactor.

Extensible Reactors
*******************

In some cases, Cantera's existing governing equations are insufficient 
in describing a certain configuration, but the internal integrator is 
still well suited to solve the desired system. In this situation, Cantera 
Reactors' governing equations can be modified to the user's specific 
needs while still using the CVODES integrator. An Extensible Reactor allows 
for modifications of a Reactor class' 
`governing equations </science/reactors/reactors.html>`__. 
An Extensible Reactor is also known as a Delegated Reactor. If using an integrator 
besides CVODES is desired, a `Custom Reactor </science/reactors/
customreactor.html>`__ may be a more appropriate Reactor class to use.

The variables in the governing equations that are differentiated with 
respect to time are known as the state variables.
The state variables depend on the type of Reactor base class chosen. 
For example, choosing an `Ideal Gas Constant Pressure Reactor 
<idealgasconstpresreactor.html#ideal-gas-constant-pressure-reactor>`__ 
allows the user to modify the governing equations corresponding to 
the following state variables:

- :math:`m`, the mass of the reactor's contents (in kg)

- :math:`T`, the temperature (in K)

- :math:`Y_k`, the mass fractions for each species (dimensionless)

As shown in the derivations of the governing equations for an Ideal Gas 
Constant Pressure Reactor, the user may modify the 3 equations below:

.. math::

   \frac{dm}{dt} = \sum_{in} \dot{m}_{in} - \sum_{out} \dot{m}_{out} +
                    \dot{m}_{wall}
                    \tag{1}

.. math::

   m c_p \frac{dT}{dt} = - \dot{Q} - \sum_k h_k \dot{m}_{k,gen}
       + \sum_{in} \dot{m}_{in} \left(h_{in} - \sum_k h_k Y_{k,in} \right)
  \tag{2}

.. math::

   m \frac{dY_k}{dt} = \sum_{in} \dot{m}_{in} (Y_{k,in} - Y_k)+
                      \dot{m}_{k,gen} - Y_k \dot{m}_{wall}
                      \tag{3}

There are two "sides" to each of these equations: the terms left of the equals
sign and the terms to the right of the equals sign. This is the format
in which the user will be editing the governing equations. For example,
if the user wishes to add a term for a large mass (say a rock) inside
the reactor to see the effects on reaction temperature:

.. math::

   m c_p \frac{dT}{dt} = - \dot{Q} - \sum_k h_k \dot{m}_{k,gen}
       + \sum_{in} \dot{m}_{in} \left(h_{in} - \sum_k h_k Y_{k,in} \right)
  \tag{2}

Will change to:

.. math::

   m c_p \frac{dT}{dt} + m_{rock} c_{p,rock} \frac{dT}{dt} = - \dot{Q} - \sum_k h_k \dot{m}_{k,gen}
       + \sum_{in} \dot{m}_{in} \left(h_{in} - \sum_k h_k Y_{k,in} \right)

A simple example is shown below to illustrate the process for implementing
changes in Cantera's existing governing equations.
We will be replacing the right-hand side (RHS) and left-hand side (LHS) of 
the temperature governing equation for an Ideal Gas Constant Pressure Reactor.
All other governing equations defining an Ideal Gas Constant Pressure Reactor
will remain as the default.

In this example

.. math::

   m c_p \frac{dT}{dt} = - \dot{Q} - \sum_k h_k \dot{m}_{k,gen}
       + \sum_{in} \dot{m}_{in} \left(h_{in} - \sum_k h_k Y_{k,in} \right)
  \tag{2}

Will change to:

.. math::

   m_{rock} c_{p,rock}\frac{dT}{dt} + m_{gas}\frac{dT}{dt} = - \dot{Q}

The governing equations will be modified through the user created Python class' methods.
For each method, the name should be prefixed with ``before_``, ``after_``, or 
``replace_``, indicating whether the this method should be called before, after, 
or instead of the corresponding method from the base class.

.. code-block:: python

  #1 Define objects, properties, and initial conditions.

   #create gas object
   gas = ct.Solution('h2o2.yaml')
   gas.TPX = 500, ct.one_atm, 'H2:2,O2:1,N2:4'

   #define properties of gas and solid
   mass_gas = 20 #[kg]
   Q = 100 #[J/s]
   mass_rock = 10 #[kg]
   cp_rock = 1.0 #[J/kgK]

   #initialize time at zero
   time = 0 #[s]
   n_steps = 300

  #2 Define a new custom Reactor class. Here we named it "DummyReactor" and 
   #chose the Ideal Gas Constant Pressure Reactor as the base class to inheret
   #governing equations from. 

   #define a class representing reactor with a solid mass and gas inside of it
   class RockReactor(ct.DelegatedIdealGasConstPressureReactor):

      #modify energy equation to include solid mass in reactor
      
      #after the initial solution for time t is computed ask Cantera to solve the modified 
      #equation. The index 1 refers to modification of governing equation 2 in the reactor
      #documentation (recall that indexing begins at 0).

      def after_eval(self, t, LHS, RHS):
      #although the time variable t is not used directly in the method definition it is a 
      #required argument for the internal solver.
         self.m_mass = mass_gas

         #as the arguments for after_eval are positional arguments, you may name them as you wish
         #rather than use the default RHS and LHS nomenclature.
         LHS[1] = mass_rock * cp_rock + self.m_mass * self.thermo.cp_mass

         RHS[1] = -Q

   #Initialize the new Reactor class and Reactor Network.
   r1 = RockReactor(gas)
   r1_net = ct.ReactorNet([r1])

   #3 Integrate custom equations over desired time.
   for n in range(n_steps):
      time += 4.e-4
      r1_net.advance(time)

The final state vector for your reactor network contains the final gas 
properties obtained from Cantera using the modified equation(s).

Details on functions in addition to ``eval()`` 
that are able to be modified with ``before_``, ``after_``, or 
``replace_`` can be found `here 
<{{% ct_docs sphinx/html/cython/zerodim.html#extensiblereactor %}}>`__.

An Extensible Reactor is also known as a Delegated Reactor.

More in-depth documentation on the different ways to modify equations using
an Extensible Reactor can be found `here <{{% ct_docs doxygen/html/de/d7e/classCantera_1_1ReactorDelegator.html %}}>`__ and `here 
<{{% ct_docs sphinx/html/cython/zerodim.html#extensiblereactor %}}>`__.