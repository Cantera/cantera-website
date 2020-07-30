---
title: GSoC 2020 Blog Post 3
date: 2020-07-26 16:20:00 UTC-04:00
slug: gsoc-2020-blog-3
tags: GSoC 2020
description: Developer-oriented detail about how ReactorNet's time integration methods actually work.
type: text
author: Paul Blum
---

## _How Does Cantera's Reactor Network Time Integration Feature Work?_

There's a great description of the science behind Cantera's reactor network simulation capabilities available on the Cantera website, [here](https://cantera.org/science/reactors.html). You can see these tools in action in Cantera's combustor example, where a reactor network is created from its components and then advanced in time:

- ***C++ Combustor Example:* combustor.cpp** (see this on [GitHub](https://github.com/Cantera/cantera/blob/main/samples/cxx/combustor/combustor.cpp))
    - Create and fill the inlet `Reservoir`s ([lines 19-41](https://github.com/Cantera/cantera/blob/ba13c652b45e74acac1daa929f66a3b6b3f92a63/samples/cxx/combustor/combustor.cpp#L19))
    - Create and fill a `Reactor` ([lines 44-48](https://github.com/Cantera/cantera/blob/ba13c652b45e74acac1daa929f66a3b6b3f92a63/samples/cxx/combustor/combustor.cpp#L44))
    - Create and fill the exhaust `Reservior` ([lines 51-54](https://github.com/Cantera/cantera/blob/ba13c652b45e74acac1daa929f66a3b6b3f92a63/samples/cxx/combustor/combustor.cpp#L51))
    - Create and install `MassFlowController`s to connect the inlets to the combustor ([lines 65-90](https://github.com/Cantera/cantera/blob/ba13c652b45e74acac1daa929f66a3b6b3f92a63/samples/cxx/combustor/combustor.cpp#L65))
    - Create and install a `Valve` to connect the combustor to the outlet and regulate pressure ([lines 92-96](https://github.com/Cantera/cantera/blob/ba13c652b45e74acac1daa929f66a3b6b3f92a63/samples/cxx/combustor/combustor.cpp#L92))
    - Create a `ReactorNet` simulator for the `Reactor` ([lines 98-100](https://github.com/Cantera/cantera/blob/ba13c652b45e74acac1daa929f66a3b6b3f92a63/samples/cxx/combustor/combustor.cpp#L98))
    - Advance the simulation in time ([line 122](https://github.com/Cantera/cantera/blob/ba13c652b45e74acac1daa929f66a3b6b3f92a63/samples/cxx/combustor/combustor.cpp#L122))
- ***Python Combustor Example:* combustor.py** (see this on [GitHub](https://github.com/Cantera/cantera/blob/main/interfaces/cython/cantera/examples/reactors/combustor.py))
    - Create and fill the inlet `Reservoir` ([lines 24-29](https://github.com/Cantera/cantera/blob/ba13c652b45e74acac1daa929f66a3b6b3f92a63/interfaces/cython/cantera/examples/reactors/combustor.py#L24))
    - Create and fill an `IdealGasReactor` ([lines 31-38](https://github.com/Cantera/cantera/blob/ba13c652b45e74acac1daa929f66a3b6b3f92a63/interfaces/cython/cantera/examples/reactors/combustor.py#L31))
    - Create and fill the exhaust `Reservior` ([lines 40-41](https://github.com/Cantera/cantera/blob/ba13c652b45e74acac1daa929f66a3b6b3f92a63/interfaces/cython/cantera/examples/reactors/combustor.py#L40))
    - Create and install a `MassFlowController` to connect the inlet to the combustor ([line 53](https://github.com/Cantera/cantera/blob/ba13c652b45e74acac1daa929f66a3b6b3f92a63/interfaces/cython/cantera/examples/reactors/combustor.py#L53))
    - Create and install a `PressureController` to connect the combustor to the outlet and regulate pressure ([lines 55-59](https://github.com/Cantera/cantera/blob/ba13c652b45e74acac1daa929f66a3b6b3f92a63/interfaces/cython/cantera/examples/reactors/combustor.py#L55))
    - Create a `ReactorNet` simulator for the `Reactor` ([lines 61-62](https://github.com/Cantera/cantera/blob/ba13c652b45e74acac1daa929f66a3b6b3f92a63/interfaces/cython/cantera/examples/reactors/combustor.py#L61))
    - Advance the simulation to steady state ([line 71](https://github.com/Cantera/cantera/blob/ba13c652b45e74acac1daa929f66a3b6b3f92a63/interfaces/cython/cantera/examples/reactors/combustor.py#L71))


This post will go into more developer-oriented detail about how the last step, `ReactorNet`'s [time integration methods](https://cantera.org/science/reactors.html#time-integration), actually work. A `ReactorNet` object doesn't perform time integration on its own. It generates a system of ODE's based on the combined governing equations of all contained `Reactor`s, which is then passed off to an `Integrator` object for solution. What is an `Integrator`?

<!-- TEASER_END -->

The `Integrator` class is Cantera's interface for ODE system integrators. This general-purpose ODE system integration tool can be accessed in any Cantera project by including the **Integrator.h** header file in your code:

- ***Class `Integrator`***: A base class interface for ODE system integrators. ([Documentation](https://cantera.org/documentation/docs-2.4/doxygen/html/d8/d6f/classCantera_1_1Integrator.html))
    - Declared and (virtually) implemented in **Integrator.h**, line 52 (see this on [GitHub](https://github.com/Cantera/cantera/blob/cf1c0816e7d535a1fc385063aebb8b8e93a85233/include/cantera/numerics/Integrator.h#L52))

`Integrator` is a *[polymorphic base class](http://www.cplusplus.com/doc/tutorial/polymorphism/)*; it defines a set of *virtual* functionalities that derived classes (the actual ODE system integrators) will provide implementations for. This is done so that different types of `Integrator`s can be used interchangeably, without having to modify their references in code. Method implementations in *different* `Integrator` subclasses can be executed using *the same* call to the `Integrator` base class's `virtual` function—the base class will refer the call to the appropriate subclass implementation, based on the `Integrator` object's type. How do you set the type of an `Integrator`?

Conveniently, **Integrator.h** provides `newIntegrator()`, a *[factory method](https://www.geeksforgeeks.org/design-patterns-set-2-factory-method/)* for creating `Integrator` instances of arbitrary type. This feature hides subclass implementation modules from users, who only know of the generic `Integrator` object that they received from the factory method:

- ***Factory Method `newIntegrator()`***: Creates and returns a pointer to an `Integrator` instance of type `itype`.
    - `Integrator* newIntegrator(const std::string& itype)`;
    - Declared in **Integrator.h**, line 237 (see this on [GitHub](https://github.com/Cantera/cantera/blob/cf1c0816e7d535a1fc385063aebb8b8e93a85233/include/cantera/numerics/Integrator.h#L237))
    - Implemented in **ODE_integrators.cpp**, line 13 (see this on [GitHub](https://github.com/Cantera/cantera/blob/cf1c0816e7d535a1fc385063aebb8b8e93a85233/src/numerics/ODE_integrators.cpp#L13))

The header files of different `Integrator` implementations are included near the top of **ODE_integrators.cpp** (see this on [GitHub](https://github.com/Cantera/cantera/blob/cf1c0816e7d535a1fc385063aebb8b8e93a85233/src/numerics/ODE_integrators.cpp#L8)). Cantera only includes one type of `Integrator` by default, the `CVODES` ODE solver, which automatically installs alongside Cantera. `CVODES` is an externally developed and maintained solver, a part of @LLNL's SUNDIALS library. If you're interested in learning more specific details about how `CVODES` actually solves an ODE system, I recommend that you read through the [`CVODES` User Guide](https://computing.llnl.gov/sites/default/files/public/cvs_guide.pdf) for detailed documentation and explanation of the module. Note that `ReactorNet` configures `CVODES` to solve via Backward Differentiation Formulas (see [`CVODES` User Guide](https://computing.llnl.gov/sites/default/files/public/cvs_guide.pdf), section 2.1), based on linear system solutions provided by the SUNDIALS `SUNLinSol_LapackDense` module (see [`CVODES` User Guide](https://computing.llnl.gov/sites/default/files/public/cvs_guide.pdf), section 10.7). 

Because `CVODES` is written in C, the `CVodesIntegrator` C++ wrapper is used to access the solver:

- ***Class `CVodesIntegrator`***: A C++ wrapper class for `CVODES`. ([Documentation](https://cantera.org/documentation/docs-2.4/doxygen/html/d9/d6b/classCantera_1_1CVodesIntegrator.html))
    - Declared in **CVodesIntegrator.h**, line 25 (see this on [GitHub](https://github.com/Cantera/cantera/blob/cf1c0816e7d535a1fc385063aebb8b8e93a85233/include/cantera/numerics/CVodesIntegrator.h#L25))
    - Implemented in **CVodesIntegrator.cpp**, line 79 (see this on [GitHub](https://github.com/Cantera/cantera/blob/cf1c0816e7d535a1fc385063aebb8b8e93a85233/src/numerics/CVodesIntegrator.cpp#L79))
    - Included in **ODE_integrators.cpp**, line 8 (see this on [GitHub](https://github.com/Cantera/cantera/blob/cf1c0816e7d535a1fc385063aebb8b8e93a85233/src/numerics/ODE_integrators.cpp#L8))

To create an instance of this `CVODES`-type `Integrator`, the factory method can be called with the "CVODE" keyword:

    newIntegrator("CVODE")

This call returns a generic `Integrator` pointer, whose `virtual` functions are overridden by those of a `CVodesIntegrator`. This is exactly how a `ReactorNet` creates its `CVODES`-type `Integrator` object, before storing it locally as `m_integ` for future reference:

**ReactorNet.cpp**, line 18 (see this on [GitHub](https://github.com/Cantera/cantera/blob/cf1c0816e7d535a1fc385063aebb8b8e93a85233/src/zeroD/ReactorNet.cpp#L18))

    m_integ(newIntegrator("CVODE"))

So, what actually happens when you call one of a `ReactorNet`'s time integration functions? Let's follow a call to `ReactorNet::advance()`, like this one to '`sim`', the `ReactorNet` object in Cantera's C++ combustor example:

**combustor.cpp**, line 122 (see this on [GitHub](https://github.com/Cantera/cantera/blob/cf1c0816e7d535a1fc385063aebb8b8e93a85233/samples/cxx/combustor/combustor.cpp#L122))

    sim.advance(tnow);

The first thing that `ReactorNet::advance()` does is check for proper initialization, and initialize if needed: 

**ReactorNet.cpp**, line 128 (see this on [GitHub](https://github.com/Cantera/cantera/blob/cf1c0816e7d535a1fc385063aebb8b8e93a85233/src/zeroD/ReactorNet.cpp#L128))

    void ReactorNet::advance(doublereal time)
    {
        if (!m_init) {
            initialize();
        } else if (!m_integrator_init) {
            reinitialize();

A `ReactorNet` always needs to be initialized before solving a new reactor network configuration, or after making any changes to the `Integrator`'s settings. Initialization can be done with a call to `ReactorNet::initialize()`, which will allocate new memory, configure `Integrator` settings, initialize all substructures, and populate internal memory appropriately with required data and specifications about the current system.

After a certain `ReactorNet` configuration has been initialized, it can also be *reinitialized* to simulate the same network with modified initial conditions. This can be done by calling `ReactorNet::reinitialize()`, which updates the internal memory with the data and specifications of the modified system. `ReactorNet::reinitialize()` will be called automatically after changing the simulation's initial time with `ReactorNet::setInitialTime()`, or after modifying the contents of any contained reactor.

Once the `ReactorNet` has been properly initialized and its internal memory is up-to-date with the current network state, the problem is passed off to `m_integ`, the `Integrator` object, for solution:

**ReactorNet.cpp**, line 135 (see this on [GitHub](https://github.com/Cantera/cantera/blob/cf1c0816e7d535a1fc385063aebb8b8e93a85233/src/zeroD/ReactorNet.cpp#L135))

    m_integ->integrate(time);

The `CVodesIntegrator` wrapper class will then make the appropriate call to the `CVODES` driver function, `CVode()`:

- ***Method `CVode()`***: Main driver of the `CVODES` package. Integrates over a time interval defined by the user, by calling `cvStep()` to do internal time steps. (*Documentation:* see [`CVODES` User Guide](https://computing.llnl.gov/sites/default/files/public/cvs_guide.pdf), section 4.5.6)
    - `int CVode(void *cvode_mem, realtype tout, N_Vector yout, realtype *tret, int itask)`;
    - Implemented in **cvodes.c**, line 2771 (see this on [GitHub](https://github.com/LLNL/sundials/blob/887af4374af2271db9310d31eaa9b5aeff49e829/src/cvodes/cvodes.c#L2771))

**CVodesIntegrator.cpp**, line 458 (see this on [GitHub](https://github.com/Cantera/cantera/blob/cf1c0816e7d535a1fc385063aebb8b8e93a85233/src/numerics/CVodesIntegrator.cpp#L458))

    int flag = CVode(m_cvode_mem, tout, m_y, &m_time, CV_NORMAL);

There are some interesting things to note about this call to `CVode()`:

- `m_cvode_mem` is a pointer to the block of memory that was allocated and configured during initialization.
- After execution, `m_y` will contain the computed solution vector, and will later be used to update the `ReactorNet` to its time-integrated state .
- The `CV_NORMAL` option tells the solver that it should continue taking internal timesteps until it has reached user-specified `tout` (or just passed it, in which case solutions are reached by interpolation). This provides the appropriate functionality for `ReactorNet::advance()`. The alternate option, `CV_ONE_STEP`, tells the solver to take a single internal step, and is used in `ReactorNet::step()`.

How does `CVODES` know what ODE system it should be solving? The ODE system was actually already specified using `CVodeInit()`, one of the methods automatically invoked during the `ReactorNet::initialize()` routine. `CVODES` requires that its user provide a C function that defines their ODE, able to compute the right-hand side of the ODE system (d`y`/d`t`) for a given value of the independent variable, `t`, and the state vector, `y`. For more information about ODE right-hand side function requirements, see [`CVODES` User Guide](https://computing.llnl.gov/sites/default/files/public/cvs_guide.pdf), section 4.6.1.

The `CVodesIntegrator` wrapper class provides a useful C++ interface for configuring this C function by pairing with `FuncEval`, an abstract base class for ODE right-hand-side function evaluators. Like the `Integrator` base class, `FuncEval` defines virtual functions that derived classes will provide the implementations for. In this case, classes derived from `FuncEval` will implement the actual evaluation of their particular ODE system.

- ***Class `FuncEval`***: An abstract base class for ODE right-hand-side function evaluators. ([Documentation](https://cantera.org/documentation/docs-2.4/doxygen/html/d1/dd1/classCantera_1_1FuncEval.html))
    - Declared in **FuncEval.h**, line 26 (see this on [GitHub](https://github.com/Cantera/cantera/blob/cf1c0816e7d535a1fc385063aebb8b8e93a85233/include/cantera/numerics/FuncEval.h#L26))
    - Implemented in **FuncEval.cpp**, line 7 (see this on [GitHub](https://github.com/Cantera/cantera/blob/cf1c0816e7d535a1fc385063aebb8b8e93a85233/src/numerics/FuncEval.cpp#L7))

An ODE right-hand-side evaluator is always needed in the ODE solution process (it's the only way to describe the system!), and for that reason a `FuncEval` object is a required parameter when initializing any type of `Integrator`:

**Integrator.h**, line 99 (see this on [GitHub](https://github.com/Cantera/cantera/blob/cf1c0816e7d535a1fc385063aebb8b8e93a85233/include/cantera/numerics/Integrator.h#L99))

    /**
     * Initialize the integrator for a new problem. Call after all options have
     * been set.
     * @param t0   initial time
     * @param func RHS evaluator object for system of equations.
     */
    virtual void initialize(doublereal t0, FuncEval& func) {

Let's take a look at how `ReactorNet` implements this `FuncEval` object. Instead of creating an external `FuncEval` subclass object, it defines *itself* as a `FuncEval` derivative:

**ReactorNet.h**, line 23 (see this on [GitHub](https://github.com/Cantera/cantera/blob/cf1c0816e7d535a1fc385063aebb8b8e93a85233/include/cantera/zeroD/ReactorNet.h#L23))

    class ReactorNet : public FuncEval

Then, it initializes the `Integrator`, using a reference to itself (as a `FuncEval`) from the *['this'](https://www.geeksforgeeks.org/this-pointer-in-c/)* pointer:

**ReactorNet.cpp**, line 112 (see this on [GitHub](https://github.com/Cantera/cantera/blob/cf1c0816e7d535a1fc385063aebb8b8e93a85233/src/zeroD/ReactorNet.cpp#L112))

    m_integ->initialize(m_time, *this);

To be a valid `FuncEval` object, a `ReactorNet` needs to provide implementations for all of `FuncEval`'s virtual functions, particularly the actual ODE right-hand-side computation function, `FuncEval::eval()`. Note that this is declared as a *[pure virtual](https://www.geeksforgeeks.org/pure-virtual-functions-and-abstract-classes/)* function, which makes `FuncEval` an abstract class:

**FuncEval.h**, line 32 (see this on [GitHub](https://github.com/Cantera/cantera/blob/cf1c0816e7d535a1fc385063aebb8b8e93a85233/include/cantera/numerics/FuncEval.h#L32))

    /**
     * Evaluate the right-hand-side function. Called by the integrator.
     * @param[in] t time.
     * @param[in] y solution vector, length neq()
     * @param[out] ydot rate of change of solution vector, length neq()
     * @param[in] p sensitivity parameter vector, length nparams()
     */
    virtual void eval(double t, double* y, double* ydot, double* p)=0;

Along with the rest of `FuncEval`'s virtual functions, an appropriate override is provided for `FuncEval::eval()` in `ReactorNet`:

**ReactorNet.cpp**, line 233 (see this on [GitHub](https://github.com/Cantera/cantera/blob/cf1c0816e7d535a1fc385063aebb8b8e93a85233/src/zeroD/ReactorNet.cpp#L233))

    void ReactorNet::eval(doublereal t, doublereal* y, doublereal* ydot, doublereal* p)
    {
        m_time = t; // This will be replaced at the end of the timestep
        updateState(y);
        for (size_t n = 0; n < m_reactors.size(); n++) {
            m_reactors[n]->evalEqs(t, y + m_start[n], ydot + m_start[n], p);
        }
        checkFinite("ydot", ydot, m_nv);
    }

`ReactorNet`'s `eval()` method invokes calls to `Reactor::evalEqs()`, to evaluate the governing equations of all `Reactor`s contained in the network. This brings us right back to where we started; for more information see Cantera's [reactor network science page](https://cantera.org/science/reactors.html#governing-equations-for-single-reactors).

Hope you enjoyed the post. 

@paulblum

### Keep Reading:

Previous Post - [GSoC 2020 Blog Post 2](https://cantera.org/blog/gsoc-2020-blog-2)

Start from the Beginning - [Introduction](https://cantera.org/blog/gsoc-2020-intro)
