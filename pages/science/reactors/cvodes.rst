.. title: CVODES and Time Integration in Cantera
.. has_math: true

.. jumbotron::

   .. raw:: html

      <h1 class="display-3">CVODES and Time Integration in Cantera</h1>

   .. class:: lead

      This guide explains ways Cantera can solve the governing equations of 
      a transient Reactor Network problem. Additional insights 
      into Cantera's integrator (CVODES) are also provided.

Using Cantera to Advance a Reactor Network in Time
**************************************************

Starting off the current state of the system, it can be advanced in time by 
one of the following methods:

- ``step()``: The step method computes the state of the system at the a priori
  unspecified time :math:`t_{\mathrm{new}}`. The time :math:`t_{\mathrm{new}}`
  is internally computed so that all states of the system only change within a
  (specifiable) band of absolute and relative tolerances. Additionally, the time
  step must not be larger than a predefined maximum time step
  :math:`\Delta t_{\mathrm{max}}`. The new time :math:`t_{\mathrm{new}}` is
  returned by this function.

- ``advance(``\ :math:`t_{\mathrm{new}}`\ ``)``: This method computes the state of the
  system at time :math:`t_{\mathrm{new}}`. :math:`t_{\mathrm{new}}` describes
  the absolute time from the initial time of the system. By calling this method
  in a for loop for pre-defined times, the state of the system is obtained for
  exactly the times specified. Internally, several ``step()`` calls are
  typically performed to reach the accurate state at time
  :math:`t_{\mathrm{new}}`.

- ``advance_to_steady_state(max_steps, residual_threshold, atol,
  write_residuals)`` [Python interface only]: If the steady state solution of a
  reactor network is of interest, this method can be used. Internally, the
  steady state is approached by time stepping. The network is considered to be
  at steady state if the feature-scaled residual of the state vector is below a
  given threshold value (which by default is 10 times the time step ``rtol``).

The use of the ``advance`` method in a loop has the advantage that it produces
results corresponding to a predefined time series. These are associated with a
predefined memory consumption and well comparable between simulation runs with
different parameters. However, some detail (for example, a fast ignition process)
might not be resolved in the output data due to the typically large time steps.
To avoid losing this detail, the
`Reactor::setAdvanceLimit <{{% ct_docs doxygen/html/dc/d5e/classCantera_1_1Reactor.html#a9b630edc7d836e901886d7fd81134d9e %}}>`__
method (C++) or the :py:func:`Reactor.set_advance_limit` method (Python) can be
used to set the maximum amount that a specified solution component can change
between output times. For an example of this feature's use, see the example
`reactor1.py </examples/python/reactors/reactor1.py.html>`__.

The ``step`` method results in many more data points because of the small
timesteps needed. Additionally, the absolute time has to be kept track of
manually.

Even though Cantera comes pre-defined with typical parameters for tolerances
and the maximum internal time step, the solution sometimes diverges. To solve
this problem, three parameters can be tuned: The absolute time stepping
tolerances, the relative time stepping tolerances, and the maximum time step. A
reduction of the latter value is particularly useful when dealing with abrupt
changes in the boundary conditions (for example, opening/closing valves; see
also the `IC engine example </examples/python/reactors/ic_engine.py.html>`__).

How Does Cantera's Reactor Network Time Integration Feature Actually Work?
==========================================================================

There's a great description of the science behind Cantera's reactor network 
simulation capabilities available on the Cantera website, 
`here <https://cantera.org/science/reactors.html>`__. This section will go into more 
developer-oriented detail about how the last step, `ReactorNet`'s 
`time integration methods <https://cantera.org/science/reactors.html#time-
integration-for-reactor-networks>`__, actually work. A `ReactorNet` object doesn't 
perform time integration on its own. It generates a system of ODE's based on the 
combined governing equations of all contained `Reactor`s, which is then passed 
off to an `Integrator` object to find a solution.

Following integration from Reactor Network creation to solution
---------------------------------------------------------------

Step 1: Reactor(s) created in Reactor Network
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

First, let's take a look at a basic example to see how we might utilize Cantera's time integration 
functionality. We'll simulate an isolated reactor in Python that is homogeneously filled by a gas 
mixture (the gas state used in this example is arbitrary, but interesting because it's 
explosive). Then we'll advance the simulation in time to an (arbitrary) absolute time of 
1 second, noting the changes in the state of the gas.

.. code-block::

    >>> import cantera as ct                           #import Cantera's Python module
    >>> gas = ct.Solution('gri30.yaml')                #create a default GRI-Mech 3.0 gas mixture
    >>> gas.TPX = 1000.0, ct.one_atm, 'H2:2,O2:1,N2:4' #set gas to an interesting state
    >>> reac = ct.IdealGasReactor(gas)                 #create a reactor containing the gas
    >>> sim = ct.ReactorNet([reac])                    #add the reactor to a new ReactorNet simulator
    >>> gas()                #view the initial state of the mixture (state summary will be printed to console)
    >>> sim.advance(1)       #advance the simulation to the specified absolute time, t = 1 sec
    >>> gas()                #view the updated state of the mixture, reflecting properties at t = 1 sec

For a more advanced example that adds inlets and outlets to the reactor, see Cantera's combustor example 
(`Python <https://github.com/Cantera/cantera/blob/main/interfaces/cython/cantera/examples/reactors/combustor.py>`__ 
| `C++ <https://github.com/Cantera/cantera/blob/main/samples/cxx/combustor/combustor.cpp>`__). Additional examples 
can be found in the `Python Reactor Network Examples <https://cantera.org/examples/python/index.html#python-example-
reactors>`__ section of the Cantera website.

Step 2: `advance()` method called
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In any case, after properly configuring a reactor network and its components in Cantera, a call to the 
`ReactorNet`'s `advance()` method can be used to predict the state of the network at a specified time. 
`ReactorNet` is reinitialized after each timestep to update the initial conditions to match the 
steady state solution found by CVODES. The initial condition information is passed off to the 
`Integrator` when calling `advance()`.
Transient physical and chemical interactions are simulated by integrating the network's system of ODE 
governing equations through time, a process that's actually performed by an external `Integrator` object.

Step 3: Information about current gas state provided to an `Integrator`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The `Integrator` class is Cantera's interface for ODE system integrators.

`Integrator` is a `polymorphic base class <http://www.cplusplus.com/doc/tutorial/polymorphism/>`__; it 
defines a set of *virtual* functionalities that derived classes (the actual ODE system integrators) will 
provide implementations for.

**Integrator.h** creates a `newIntegrator()`, described below:

Factory Method `newIntegrator()`: Creates and returns a pointer to an `Integrator` instance of type `itype`.

- `Integrator* newIntegrator(const std::string& itype)`;
- Declared in Integrator.h, line 237 (see this on `GitHub <https://github.com/Cantera/cantera/blob/cf1c0816e7d535a1fc385063aebb8b8e93a85233/include/cantera/numerics/Integrator.h#L237>`__)
- Implemented in ODE_integrators.cpp, line 13 (see this on `GitHub <https://github.com/Cantera/cantera/blob/cf1c0816e7d535a1fc385063aebb8b8e93a85233/src/numerics/ODE_integrators.cpp#L13>`__)

The `newIntegrator()` instance will automatically have an `itype` of `CVODES`, which is installed with Cantera.
The `newIntegrator()` will be stored as variable `m_integ`.

Step 4: Communicate with CVODES using a wrapper function
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Because `CVODES` is written in C, the `CVodesIntegrator` C++ wrapper is used to access the solver:

- Class `CVodesIntegrator`: A C++ wrapper class for `CVODES`. (`Documentation <https://cantera.org/documentation/docs-2.4/doxygen/html/d9/d6b/classCantera_1_1CVodesIntegrator.html>`__)
- Declared in **CVodesIntegrator.h**, line 25 (see this on `GitHub <https://github.com/Cantera/cantera/blob/cf1c0816e7d535a1fc385063aebb8b8e93a85233/include/cantera/numerics/CVodesIntegrator.h#L25>`__)
- Implemented in **CVodesIntegrator.cpp**, line 79 (see this on `GitHub <https://github.com/Cantera/cantera/blob/cf1c0816e7d535a1fc385063aebb8b8e93a85233/src/numerics/CVodesIntegrator.cpp#L79>`__)
- Included in **ODE_integrators.cpp**, line 8 (see this on `GitHub <https://github.com/Cantera/cantera/blob/cf1c0816e7d535a1fc385063aebb8b8e93a85233/src/numerics/ODE_integrators.cpp#L8>`__)

The `CVodesIntegrator` wrapper class will then make the appropriate call to the `CVODES` driver function, `CVode()`.

Step 5: `Cvode()` driver function is called
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Method `CVode()`: Main driver of the `CVODES` package. Integrates over a time interval defined by the user, by calling `cvStep()` to do internal time steps. (*Documentation:* see `CVODES User Guide 
<https://sundials.readthedocs.io/en/latest/cvodes/index.html>`__)

- `int CVode(void *cvode_mem, realtype tout, N_Vector yout, realtype *tret, int itask)`;
- Implemented in **cvodes.c**, line 2771 (see this on `GitHub <https://github.com/LLNL/sundials/blob/887af4374af2271db9310d31eaa9b5aeff49e829/src/cvodes/cvodes.c#L2771>`__)

**CVodesIntegrator.cpp**, line 458 (see this on `GitHub <https://github.com/Cantera/cantera/blob/cf1c0816e7d535a1fc385063aebb8b8e93a85233/src/numerics/CVodesIntegrator.cpp#L458>`__)

.. code-block::

    int flag = CVode(m_cvode_mem, tout, m_y, &m_time, CV_NORMAL);

There are some interesting things to note about this call to `CVode()`:

- `m_cvode_mem` is a pointer to the block of memory that was allocated and configured during initialization.
- After execution, `m_y` will contain the computed solution vector, and will later be used to update the `ReactorNet` to its time-integrated state .
- The `CV_NORMAL` option tells the solver that it should continue taking internal timesteps until it has reached user-specified `tout` (or just passed it, in which case solutions are reached by interpolation). This provides the appropriate functionality for `ReactorNet::advance()`. The alternate option, `CV_ONE_STEP`, tells the solver to take a single internal step, and is used in `ReactorNet::step()`.

Step 6: `FuncEval` class describes ODEs to solve
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

How does `CVODES` know what ODE system it should be solving? 

The ODE system was actually already specified using `CVodeInit()`, one of the methods automatically invoked during the
`ReactorNet::initialize()` routine. `CVODES` requires that its user provide a C function that defines their ODE, 
able to compute the right-hand side of the ODE system (dy/dt) for a given value of the independent variable, `t`, 
and the state vector, `y`. For more information about ODE right-hand side function requirements, 
see `CVODES User Guide <https://sundials.readthedocs.io/en/latest/cvodes/index.html>`__, section 4.6.1.

The `CVodesIntegrator` wrapper class provides a useful C++ interface for configuring this C function by pairing with 
`FuncEval`, an abstract base class for ODE right-hand-side function evaluators. Classes derived from `FuncEval` will 
implement the evaluation of the provided ODE system.

- Class `FuncEval`: An abstract base class for ODE right-hand-side function evaluators. (`Documentation <https://cantera.org/documentation/docs-2.4/doxygen/html/d1/dd1/classCantera_1_1FuncEval.html>`__)
- Declared in **FuncEval.h**, line 26 (see this on `GitHub <https://github.com/Cantera/cantera/blob/cf1c0816e7d535a1fc385063aebb8b8e93a85233/include/cantera/numerics/FuncEval.h#L26>`__)
- Implemented in **FuncEval.cpp**, line 7 (see this on `GitHub <https://github.com/Cantera/cantera/blob/cf1c0816e7d535a1fc385063aebb8b8e93a85233/src/numerics/FuncEval.cpp#L7>`__)

An ODE right-hand-side evaluator is always needed in the ODE solution process (it's the only way to describe the system!), and for that reason a `FuncEval` object is a required parameter 
when initializing any type of `Integrator`.

Let's take a look at how `ReactorNet` implements this `FuncEval` object. `ReactorNet` actually points to itself when 
defining a `FuncEval` type, meaning it defines *itself* as a `FuncEval` derivative.

Then, `ReactorNet` initializes the `Integrator`, using a reference to itself (as a `FuncEval`) from the 
`this <https://www.geeksforgeeks.org/this-pointer-in-c/>`__ pointer.

To be a valid `FuncEval` object, a `ReactorNet` needs to provide implementations for all of `FuncEval`'s 
virtual functions, particularly the actual ODE right-hand-side computation 
function, `FuncEval::eval()`. Note that this is declared as a `pure virtual 
<https://www.geeksforgeeks.org/pure-virtual-functions-and-abstract-classes/>`__ function, which makes 
`FuncEval` an abstract class:

.. code-block::

    Evaluate the reactor governing equations. Called by ReactorNet::eval.
    
    @param[in] t time.
    @param[out] LHS pointer to start of vector of left-hand side 
    coefficients for governing equations, length m_nv, default values 1
    @param[out] RHS pointer to start of vector of right-hand side 
    coefficients for governing equations, length m_nv, default values 0
    
    virtual void eval(double t, double* LHS, double* RHS);

The above code shows the necessary inputs for solving the ODEs using the `eval()` function. `eval()` takes in the
value of each state variable derivative (`ydot`) at a time `t`, and will write the integrated values for each
state varaible to the solution vector (`y`).

Step 7: `eval()` is called to solve provided ODEs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Along with the rest of `FuncEval`'s virtual functions, an appropriate override is provided for `FuncEval::eval()` in 
`ReactorNet`:

**ReactorNet.cpp**, line 233 (see this on `GitHub <https://github.com/Cantera/cantera/blob/cf1c0816e7d535a1fc385063aebb8b8e93a85233/src/zeroD/ReactorNet.cpp#L233>`__)

.. code-block::

    void ReactorNet::eval(doublereal t, doublereal* y, doublereal* ydot, doublereal* p)
    {
        m_time = t; // This will be replaced at the end of the timestep
        updateState(y);
        for (size_t n = 0; n < m_reactors.size(); n++) {
            m_reactors[n]->evalEqs(t, y + m_start[n], ydot + m_start[n], p);
        }
        checkFinite("ydot", ydot, m_nv);
    }


`ReactorNet`'s `eval()` method invokes calls to `Reactor::evalEqs()`, to evaluate the governing equations of all 
`Reactors` contained in the network. This brings us right back to where we started; for more information see 
Cantera's `reactor network science page <https://cantera.org/science/reactors.html#governing-equations-for-single-reactors>`__. 

This documentation is based off @paulblum's `blog post <https://cantera.org/blog/gsoc-2020-blog-3.html>`__.