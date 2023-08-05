.. title: CVODES and Time Integration in Cantera
.. has_math: true

.. jumbotron::

   .. raw:: html

      <h1 class="display-4">Time Integration in Cantera using SUNDIALS</h1>

   .. class:: lead

      This guide explains ways Cantera can solve the governing equations of
      a transient Reactor Network problem. Additional insights
      into the integrator library SUNDIALS utilized by Cantera are also provided.

Using Cantera to Advance a Reactor Network in Time
**************************************************

A ``ReactorNet`` can be advanced in time by one of the following three
methods:

- ``step()``: The ``step()`` method computes the state of the system after one
  time step. The size of the step is determined by SUNDIALS when the method is called.
  SUNDIALS determines the step size by estimating the local error at every step, which
  must satisfy tolerance conditions. The step is redone with reduced step size whenever
  that error test fails. SUNDIALS also periodically checks if the maximum step size is
  being used. The time step must not be larger than a predefined maximum time step
  :math:`\Delta t_{\mathrm{max}}`. The new time :math:`t_{\mathrm{new}}` at the end
  of the single step is returned by this function. This method produces the highest time
  resolution in the output data of the methods implemented in Cantera.

- ``advance(t_new)``: This method computes the state of the system at the
  user-provided time :math:`t_{\mathrm{new}}`. :math:`t_{\mathrm{new}}` is the absolute
  time from the initial time of the system. Although the user specifies the time when
  integration should stop, SUNDIALS chooses the time step size as the network is integrated.
  Many of these internal SUNDIALS time steps are usually required to reach
  :math:`t_{\mathrm{new}}`. As such, ``advance(t_new)`` preserves the accuracy of using
  ``step()`` but allows consistent time step spacing in the output data.

- ``advance_to_steady_state(max_steps, residual_threshold, atol,
  write_residuals)`` [Python interface only]: If the steady state solution of a
  reactor network is of interest, this method can be used. Internally, the
  steady state is approached by time stepping. The network is considered to be
  at steady state if the feature-scaled residual of the state vector is below a
  given threshold value (which by default is 10 times the time step ``rtol``).

The ``advance(t_new)`` is typically used when consistent, regular, time steps are
required in the output data. This usually simplifies comparisons among many
simulation results at a single time point. However, some detail, for example, a
fast ignition process, might not be resolved in the output data if the user-provided
time step is not small enough.

To avoid losing this detail, the
`Reactor::setAdvanceLimit <{{% ct_docs doxygen/html/dc/d5e/classCantera_1_1Reactor.html#a9b630edc7d836e901886d7fd81134d9e %}}>`__
method (C++) or the :py:func:`Reactor.set_advance_limit` method (Python) can be
used to set the maximum amount that a specified solution component can change
between output times. For an example of this feature's use, see the example
`reactor1.py </examples/python/reactors/reactor1.py.html>`__. However, as a tradeoff,
the time step sizes in the output data are no longer guaranteed to be uniform.

Even though Cantera comes pre-defined with typical parameters for tolerances
and the maximum internal time step, the solver may not be correctly configured
for the specific system. In this case the internal timestep solutions may not
converge towards a single value. To solve this problem, three parameters can be
tuned: The absolute time stepping tolerances, the relative time stepping tolerances,
and the maximum time step. A reduction of the latter value is particularly useful
when dealing with abrupt changes in the boundary conditions (for example,
opening/closing valves; see also the `IC engine example </examples/python/reactors
/ic_engine.py.html>`__).

How Does Cantera's Reactor Network Time Integration Feature Actually Work?
==========================================================================

A description of the science behind Cantera's reactor network
simulation capabilities is available on the Cantera website,
`here <https://cantera.org/science/reactors/reactors.html>`__. This section will go into more
developer-oriented detail about how the last step, ``ReactorNet``'s
`time integration methods <https://cantera.org/science/reactors/reactors.html#time-
integration-for-reactor-networks>`__, actually work. A ``ReactorNet`` object doesn't
perform time integration on its own. Cantera generates a Jacobian array for the set
of ``Reactor`` objects contained in the ``ReactorNet``. This Jacobian, along with
functions to evaluate the residual of each ODE representing the system, is passed to
an ``Integrator``.

Following integration from Reactor Network creation to completion
-----------------------------------------------------------------

Step 1: Reactor(s) created in Reactor Network
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

First, let's take a look at a basic example to see how we might utilize Cantera's time integration
functionality. We'll simulate an isolated reactor in Python that is homogeneously filled by a gas
mixture (the gas state used in this example is arbitrary, but interesting because it's
explosive). Then we'll advance the simulation in time to an (arbitrary) absolute time of
1 second, noting the changes in the state of the gas.

.. code-block:: python

    import cantera as ct  # import Cantera's Python module

    gas = ct.Solution("gri30.yaml")  # create a default GRI-Mech 3.0 gas mixture
    gas.TPX = 1000.0, ct.one_atm, "H2:2,O2:1,N2:4"  # set gas to an interesting state
    reac = ct.IdealGasReactor(gas)  # create a reactor containing the gas
    sim = ct.ReactorNet([reac])  # add the reactor to a new ReactorNet simulator
    gas()  # view the initial state of the mixture (state summary will be printed to console)
    sim.advance(1)  # advance the simulation to the specified absolute time, t = 1 sec
    gas()  # view the updated state of the mixture, reflecting properties at t = 1 sec

For a more advanced example that adds inlets and outlets to the reactor, see Cantera's combustor example
(`Python </examples/python/reactors/combustor.py.html>`__
| `C++ </examples/cxx/combustor.html>`__). Additional examples can be found in the
`Python Reactor Network Examples <https://cantera.org/examples/python/index.html#python-example-
reactors>`__ section of the Cantera website.

Optional Preconditioning
^^^^^^^^^^^^^^^^^^^^^^^^

Some mole reactors are capable of leveraging preconditioning to accelerate integration of the system.
The former code can be modified as follows to use preconditioning.
The preconditioner can also be assigned to a python object and tunable parameters can adjusted.

.. code-block:: python

    import cantera as ct  # import Cantera's Python module

    gas = ct.Solution("gri30.yaml")  # create a default GRI-Mech 3.0 gas mixture
    gas.TPX = 1000.0, ct.one_atm, "H2:2,O2:1,N2:4"  # set gas to an interesting state
    reac = ct.IdealGasMoleReactor(gas)  # create a reactor containing the gas
    sim = ct.ReactorNet([reac])  # add the reactor to a new ReactorNet simulator
    sim.preconditioner = ct.AdaptivePreconditioner() # add preconditioner to the network
    gas()  # view the initial state of the mixture (state summary will be printed to console)
    sim.advance(1)  # advance the simulation to the specified absolute time, t = 1 sec
    gas()  # view the updated state of the mixture, reflecting properties at t = 1 sec

Step 2: ``advance()`` method called
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In any case, after properly configuring a reactor network and its components in Cantera, a call to the
``ReactorNet``'s ``advance()`` method can be used to predict the state of the network at a specified time.
The initial condition information is passed off to the `Integrator` when calling `advance()`.
Transient physical and chemical interactions are simulated by integrating the network's system of ODE
governing equations through time, a process that's actually performed by an external `Integrator` object.

Step 3: Information about current gas state provided to an `Integrator`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The ``Integrator`` class is Cantera's interface for ODE/DAE system integrators.

``Integrator`` is a `polymorphic base class <http://www.cplusplus.com/doc/tutorial/polymorphism/>`__; it
defines a set of *virtual* methods that derived classes (the actual system integrators) will
provide implementations for.

The ``newIntegrator()`` factory method creates and returns an ``Integrator`` object of
the specified type. Calling ``newIntegrator("CVODE")`` creates a new ``CVodesIntegrator``
object for integrating an ODE system, while calling ``newIntegrator("IDA")`` creates a
new ``IdasIntegrator`` object for integrating a DAE system. The appropriate integrator
type is determined by the ``ReactorNet`` class based on the types of the installed
reactors. Below, the implementation of ``CvodesIntegrator`` is described; the
``IdasIntegrator`` works in a similar way, though the function names are different.

Step 4: Communicate with SUNDIALS using a wrapper function
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Because SUNDIALS is written in C, the ``CVodesIntegrator`` C++ wrapper is used to access the solver.
The ``CVodesIntegrator`` class is a C++ wrapper class for ``CVODES``. (`Documentation
<{{% ct_docs doxygen/html/d9/d6b/classCantera_1_1CVodesIntegrator.html %}}>`__)
The ``CVodesIntegrator`` class makes the appropriate call to the ``CVODES`` driver function, ``CVode()``.

Step 5: ``Cvode()`` driver function is called
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Method ``CVode()`` is the main driver of the ``CVODES`` package. ``CVode()`` integrates over a time interval defined by
the user, by calling ``cvStep()`` to do internal time steps (not specified by the user). (*Documentation:*
see `CVODES User Guide <https://sundials.readthedocs.io/en/latest/cvodes/index.html>`__)

The arguments taken by the ``CVode()`` method is shown below:

.. code-block:: C++

    int CVode(void *cvode_mem, realtype tout, N_Vector yout, realtype *tret, int itask);

There are some interesting things to note about this call to ``CVode()``:

- ``m_cvode_mem`` is a pointer to the block of memory that was allocated and configured during initialization.
- After execution, ``m_y`` will contain the computed solution vector, and will later be used to update the ``ReactorNet``
  to its time-integrated state.
- The ``CV_NORMAL`` option tells the solver that it should continue taking internal timesteps until it has reached
  user-specified ``tout`` (or just passed it, in which case solutions are reached by interpolation). This provides the
  appropriate functionality for ``ReactorNet::advance()``. The alternate option, ``CV_ONE_STEP``, tells the solver to take
  a single internal step, and is used in ``ReactorNet::step()``.

The result of the ``CVode()`` method is assigned to the ``flag`` object. ``CVode()`` returns 1 or 0, corresponding to
a successful or unsuccessful integration, respectively.

.. code-block:: C++

    int flag = CVode(m_cvode_mem, tout, m_y, &m_time, CV_NORMAL);

Step 6: ``FuncEval`` class describes ODEs to solve
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

How does ``CVODES`` know what ODE system it should be solving?

The ODE system was actually already specified using ``CVodeInit()``, one of the methods automatically invoked during the
``ReactorNet::initialize()`` routine. ``CVODES`` requires that its user provide a C function that defines their ODE,
able to compute the right-hand side of the ODE system (dy/dt) for a given value of the independent variable, `t`,
and the state vector, ``y``. For more information about ODE right-hand side function requirements,
see `CVODES User Guide <https://sundials.readthedocs.io/en/latest/cvodes/Usage/SIM.html#user-supplied-functions>`__.

The ``CVodesIntegrator`` wrapper class provides a useful C++ interface for configuring this C function by pairing with
``FuncEval``, an abstract base class for ODE right-hand-side function evaluators (`Documentation
<{{% ct_docs doxygen/html/d1/dd1/classCantera_1_1FuncEval.html %}}>`__). Classes derived
from ``FuncEval`` will implement the evaluation of the provided ODE system.

An ODE right-hand-side evaluator is always needed in the ODE solution process (it's the only way to describe the system!), and for that reason a `FuncEval` object is a required parameter
when initializing any type of ``Integrator``.

Let's take a look at how ``ReactorNet`` implements this ``FuncEval`` object. ``ReactorNet`` actually points to itself when
defining a ``FuncEval`` type, meaning it defines *itself* as a ``FuncEval`` derivative.

Then, ``ReactorNet`` initializes the ``Integrator``, using a reference to itself (as a ``FuncEval``) from the
`this <https://en.cppreference.com/w/cpp/language/this>`__ pointer.

To be a valid ``FuncEval`` object, a ``ReactorNet`` needs to provide implementations for all of ``FuncEval``'s
virtual functions, particularly the actual ODE right-hand-side computation
function, ``FuncEval::eval()``. Note that this is declared as a `pure virtual
<https://en.cppreference.com/w/cpp/language/abstract_class>`__ function, which makes
``FuncEval`` an abstract class.

To evaluate the reactor governing equations the following parameters must be known:

#. ``t``: Current time in seconds.
#. ``LHS``: pointer to start of vector of left-hand side coefficients for governing equations.
    Has length m_nv, default values 1.
#. ``RHS``: pointer to start of vector of right-hand side coefficients for governing equations.
    Has length m_nv, default values 0.

.. code-block:: C++

    virtual void eval(double t, double* LHS, double* RHS);

``eval()`` is called by ``ReactorNet::eval``.

The above code shows the necessary inputs for solving the ODEs using the ``eval()`` function. ``eval()`` takes in the
value of each state variable derivative (``ydot``) at a time ``t``, and will write the integrated values for each
state variable to the solution vector (``y``).

Step 7: ``eval()`` is called to solve provided ODEs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Along with the rest of ``FuncEval``'s virtual functions, an appropriate override is provided for ``FuncEval::eval()`` in
``ReactorNet``

.. code-block:: C++

    void ReactorNet::eval(double t, double* y, double* ydot, double* p)
    {
        m_time = t;
        updateState(y);
        m_LHS.assign(m_nv, 1);
        m_RHS.assign(m_nv, 0);
        for (size_t n = 0; n < m_reactors.size(); n++) {
            m_reactors[n]->applySensitivity(p);
            m_reactors[n]->eval(t, m_LHS.data() + m_start[n], m_RHS.data() + m_start[n]);
            size_t yEnd = 0;
            if (n == m_reactors.size() - 1) {
                yEnd = m_RHS.size();
            } else {
                yEnd = m_start[n + 1];
            }
            for (size_t i = m_start[n]; i < yEnd; i++) {
                ydot[i] = m_RHS[i] / m_LHS[i];
            }
            m_reactors[n]->resetSensitivity(p);
        }
        checkFinite("ydot", ydot, m_nv);
    }


``ReactorNet``'s ``eval()`` method evaluates the governing equations of all ``Reactors``
contained in the network. This brings us right back to where we started. For more
information, see Cantera's `reactor network science page </science/reactors/reactors.html>`__.

This documentation is based off @paulblum's `blog post <https://cantera.org/blog/gsoc-2020-blog-3.html>`__.
