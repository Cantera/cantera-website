---
date: 2020-07-26 16:20
tags: GSoC 2020
author: Paul Blum
---

# GSoC 2020: How Does Cantera's Reactor Network Time Integration Feature Work?

There's a great description of the science behind Cantera's reactor network simulation capabilities available on the Cantera website, {doc}`here <stable:reference/reactors/index>`. This post will go into more developer-oriented detail about how the last step, `ReactorNet`'s {doc}`time integration methods <stable:develop/reactor-integration>`, actually work. A `ReactorNet` object doesn't perform time integration on its own. It generates a system of ODE's based on the combined governing equations of all contained `Reactor`s, which is then passed off to an `Integrator` object for solution. What is an `Integrator`? How does this work?

## Reactor Network Time Integration, Explained

First, let's take a look at a basic example to see how we might utilize Cantera's time integration functionality. We'll simulate an isolated reactor that is homogeneously filled by a gas mixture (the gas state used in this example is arbitrary, but interesting because it's explosive). Then we'll advance the simulation in time to an (arbitrary) absolute time of 1 second, noting the changes in the state of the gas. Follow along by typing this code into an interactive Python interpreter (like [IPython](https://www.codecademy.com/articles/how-to-use-ipython)):

```pycon
>>> import cantera as ct                           #import Cantera's Python module
>>> gas = ct.Solution('gri30.yaml')                #create a default GRI-Mech 3.0 gas mixture
>>> gas.TPX = 1000.0, ct.one_atm, 'H2:2,O2:1,N2:4' #set gas to an interesting state
>>> reac = ct.IdealGasReactor(gas)                 #create a reactor containing the gas
>>> sim = ct.ReactorNet([reac])                    #add the reactor to a new ReactorNet simulator
>>> gas()                #view the initial state of the mixture (state summary will be printed to console)
>>> sim.advance(1)       #advance the simulation to the specified absolute time, t = 1 sec
>>> gas()                #view the updated state of the mixture, reflecting properties at t = 1 sec
```

Equivalently, the following can be compiled and run using Cantera's C++ interface:

```c++
#include "cantera/zerodim.h" //include Cantera's 0D reactor simulation module
using namespace Cantera;     //activate Cantera namespace to identify scope of class and method references
int main() {
    auto gas = newSolution("gri30.yaml"); //create a default GRI-Mech 3.0 gas mixture
    gas->thermo()->setState_TPX(1000.0, OneAtm, "H2:2,O2:1,N2:4"); //set gas to an interesting state
    Reactor reac;                         //create an empty Reactor
    reac.insert(gas);                     //fill the reactor with the specified gas
    ReactorNet sim;                       //create an empty ReactorNet simulator
    sim.addReactor(reac);                 //add the reactor to the ReactorNet
    std::cout << gas->thermo()->report(); //print the initial state of the mixture to the console
    sim.advance(1);                       //advance the simulation to absolute time t = 1 sec
    std::cout << gas->thermo()->report(); //print the updated state of the mixture to the console
    return 0;
}
```

For a more advanced example that adds inlets and outlets to the reactor, see Cantera's combustor example ({doc}`Python <stable:examples/python/reactors/combustor>` | {doc}`C++ <stable:examples/cxx/combustor>`). Additional examples can be found in the {doc}`Python Reactor Network Examples <stable:examples/python/reactors/index>` section of the Cantera website.

In any case, after properly configuring a reactor network and its components in Cantera, a call to the `ReactorNet`'s `advance()` method can be used to predict the state of the network at a specified time. Transient physical and chemical interactions are simulated by integrating the network's system of ODE governing equations through time, a process that's actually performed by an external `Integrator` object. What is an `Integrator`?

The `Integrator` class is Cantera's interface for ODE system integrators. This general-purpose ODE system integration tool can be accessed in any Cantera project by including the **Integrator.h** header file in your code:

- ***Class `Integrator`***: A base class interface for ODE system integrators. (<a href="/2.4/doxygen/html/d8/d6f/classCantera_1_1Integrator.html">Documentation</a>)
    - Declared and (virtually) implemented in **Integrator.h**, line 52 (see this on [GitHub](https://github.com/Cantera/cantera/blob/cf1c0816e7d535a1fc385063aebb8b8e93a85233/include/cantera/numerics/Integrator.h#L52))

`Integrator` is a *[polymorphic base class](http://www.cplusplus.com/doc/tutorial/polymorphism/)*; it defines a set of *virtual* functionalities that derived classes (the actual ODE system integrators) will provide implementations for. This is done so that different types of `Integrator`s can be used interchangeably, without having to modify their references in code. Method implementations in *different* `Integrator` subclasses can be executed using *the same* call to the `Integrator` base class's `virtual` function—the base class will refer the call to the appropriate subclass implementation, based on the `Integrator` object's type. How do you set the type of an `Integrator`?

Conveniently, **Integrator.h** provides `newIntegrator()`, a *[factory method](https://www.geeksforgeeks.org/design-patterns-set-2-factory-method/)* for creating `Integrator` instances of arbitrary type. This feature hides subclass implementation modules from users, who only know of the generic `Integrator` object that they received from the factory method:

- ***Factory Method `newIntegrator()`***: Creates and returns a pointer to an `Integrator` instance of type `itype`.
    - `Integrator* newIntegrator(const std::string& itype)`;
    - Declared in **Integrator.h**, line 237 (see this on [GitHub](https://github.com/Cantera/cantera/blob/cf1c0816e7d535a1fc385063aebb8b8e93a85233/include/cantera/numerics/Integrator.h#L237))
    - Implemented in **ODE_integrators.cpp**, line 13 (see this on [GitHub](https://github.com/Cantera/cantera/blob/cf1c0816e7d535a1fc385063aebb8b8e93a85233/src/numerics/ODE_integrators.cpp#L13))

The header files of different `Integrator` implementations are included near the top of **ODE_integrators.cpp** (see this on [GitHub](https://github.com/Cantera/cantera/blob/cf1c0816e7d535a1fc385063aebb8b8e93a85233/src/numerics/ODE_integrators.cpp#L8)). Cantera only includes one type of `Integrator` by default, the `CVODES` ODE solver, which automatically installs alongside Cantera. `CVODES` is an externally developed and maintained solver, a part of @LLNL's SUNDIALS library. If you're interested in learning more specific details about how `CVODES` actually solves an ODE system, I recommend that you read through the [`CVODES` User Guide](https://computing.llnl.gov/sites/default/files/cv_guide-5.7.0.pdf) for detailed documentation and explanation of the module. Note that `ReactorNet` configures `CVODES` to solve via Backward Differentiation Formulas (see [`CVODES` User Guide](https://computing.llnl.gov/sites/default/files/cv_guide-5.7.0.pdf), section 2.1), based on linear system solutions provided by the SUNDIALS `SUNLinSol_LapackDense` module (see [`CVODES` User Guide](https://computing.llnl.gov/sites/default/files/cv_guide-5.7.0.pdf), section 10.7).

Because `CVODES` is written in C, the `CVodesIntegrator` C++ wrapper is used to access the solver:

- ***Class `CVodesIntegrator`***: A C++ wrapper class for `CVODES`. (<a href="/2.4/doxygen/html/d9/d6b/classCantera_1_1CVodesIntegrator.html">Documentation</a>)
    - Declared in **CVodesIntegrator.h**, line 25 (see this on [GitHub](https://github.com/Cantera/cantera/blob/cf1c0816e7d535a1fc385063aebb8b8e93a85233/include/cantera/numerics/CVodesIntegrator.h#L25))
    - Implemented in **CVodesIntegrator.cpp**, line 79 (see this on [GitHub](https://github.com/Cantera/cantera/blob/cf1c0816e7d535a1fc385063aebb8b8e93a85233/src/numerics/CVodesIntegrator.cpp#L79))
    - Included in **ODE_integrators.cpp**, line 8 (see this on [GitHub](https://github.com/Cantera/cantera/blob/cf1c0816e7d535a1fc385063aebb8b8e93a85233/src/numerics/ODE_integrators.cpp#L8))

To create an instance of this `CVODES`-type `Integrator`, the factory method can be called with the "CVODE" keyword:

```c++
newIntegrator("CVODE")
```

This call returns a generic `Integrator` pointer, whose `virtual` functions are overridden by those of a `CVodesIntegrator`. This is exactly how a `ReactorNet` creates its `CVODES`-type `Integrator` object, before storing it locally as `m_integ` for future reference:

**ReactorNet.cpp**, line 18 (see this on [GitHub](https://github.com/Cantera/cantera/blob/cf1c0816e7d535a1fc385063aebb8b8e93a85233/src/zeroD/ReactorNet.cpp#L18))

```c++
m_integ(newIntegrator("CVODE"))
```

So, what actually happens when you call one of a `ReactorNet`'s time integration functions? Let's follow the execution of a call to `ReactorNet::advance()` through the source code. Consider this call to '`sim`', the `ReactorNet` object in Cantera's C++ combustor example:

**combustor.cpp**, line 122 (see this on [GitHub](https://github.com/Cantera/cantera/blob/cf1c0816e7d535a1fc385063aebb8b8e93a85233/samples/cxx/combustor/combustor.cpp#L122))

```c++
sim.advance(tnow);
```

The first thing that `ReactorNet::advance()` does is check for proper initialization, and initialize if needed: 

**ReactorNet.cpp**, line 128 (see this on [GitHub](https://github.com/Cantera/cantera/blob/cf1c0816e7d535a1fc385063aebb8b8e93a85233/src/zeroD/ReactorNet.cpp#L128))

```c++
void ReactorNet::advance(doublereal time)
{
    if (!m_init) {
        initialize();
    } else if (!m_integrator_init) {
        reinitialize();
```

A `ReactorNet` always needs to be initialized before solving a new reactor network configuration, or after making any changes to the `Integrator`'s settings. Initialization can be done with a call to `ReactorNet::initialize()`, which will allocate new memory, configure `Integrator` settings, initialize all substructures, and populate internal memory appropriately with required data and specifications about the current system.

After a certain `ReactorNet` configuration has been initialized, it can also be *reinitialized* to simulate the same network with modified initial conditions. This can be done by calling `ReactorNet::reinitialize()`, which updates the internal memory with the data and specifications of the modified system. `ReactorNet::reinitialize()` will be called automatically after changing the simulation's initial time with `ReactorNet::setInitialTime()`, or after modifying the contents of any contained reactor.

Once the `ReactorNet` has been properly initialized and its internal memory is up-to-date with the current network state, the problem is passed off to `m_integ`, the `Integrator` object, for solution:

**ReactorNet.cpp**, line 135 (see this on [GitHub](https://github.com/Cantera/cantera/blob/cf1c0816e7d535a1fc385063aebb8b8e93a85233/src/zeroD/ReactorNet.cpp#L135))

```c++
m_integ->integrate(time);
```

The `CVodesIntegrator` wrapper class will then make the appropriate call to the `CVODES` driver function, `CVode()`:

- ***Method `CVode()`***: Main driver of the `CVODES` package. Integrates over a time interval defined by the user, by calling `cvStep()` to do internal time steps. (*Documentation:* see [`CVODES` User Guide](https://computing.llnl.gov/sites/default/files/cv_guide-5.7.0.pdf), section 4.5.6)
    - `int CVode(void *cvode_mem, realtype tout, N_Vector yout, realtype *tret, int itask)`;
    - Implemented in **cvodes.c**, line 2771 (see this on [GitHub](https://github.com/LLNL/sundials/blob/887af4374af2271db9310d31eaa9b5aeff49e829/src/cvodes/cvodes.c#L2771))

**CVodesIntegrator.cpp**, line 458 (see this on [GitHub](https://github.com/Cantera/cantera/blob/cf1c0816e7d535a1fc385063aebb8b8e93a85233/src/numerics/CVodesIntegrator.cpp#L458))

```c++
int flag = CVode(m_cvode_mem, tout, m_y, &m_time, CV_NORMAL);
```

There are some interesting things to note about this call to `CVode()`:

- `m_cvode_mem` is a pointer to the block of memory that was allocated and configured during initialization.
- After execution, `m_y` will contain the computed solution vector, and will later be used to update the `ReactorNet` to its time-integrated state .
- The `CV_NORMAL` option tells the solver that it should continue taking internal timesteps until it has reached user-specified `tout` (or just passed it, in which case solutions are reached by interpolation). This provides the appropriate functionality for `ReactorNet::advance()`. The alternate option, `CV_ONE_STEP`, tells the solver to take a single internal step, and is used in `ReactorNet::step()`.

How does `CVODES` know what ODE system it should be solving? The ODE system was actually already specified using `CVodeInit()`, one of the methods automatically invoked during the `ReactorNet::initialize()` routine. `CVODES` requires that its user provide a C function that defines their ODE, able to compute the right-hand side of the ODE system (d`y`/d`t`) for a given value of the independent variable, `t`, and the state vector, `y`. For more information about ODE right-hand side function requirements, see [`CVODES` User Guide](https://computing.llnl.gov/sites/default/files/cv_guide-5.7.0.pdf), section 4.6.1.

The `CVodesIntegrator` wrapper class provides a useful C++ interface for configuring this C function by pairing with `FuncEval`, an abstract base class for ODE right-hand-side function evaluators. Like the `Integrator` base class, `FuncEval` defines virtual functions that derived classes will provide the implementations for. In this case, classes derived from `FuncEval` will implement the actual evaluation of their particular ODE system.

- ***Class `FuncEval`***: An abstract base class for ODE right-hand-side function evaluators. (<a href="/2.4/doxygen/html/d1/dd1/classCantera_1_1FuncEval.html">Documentation</a>)
    - Declared in **FuncEval.h**, line 26 (see this on [GitHub](https://github.com/Cantera/cantera/blob/cf1c0816e7d535a1fc385063aebb8b8e93a85233/include/cantera/numerics/FuncEval.h#L26))
    - Implemented in **FuncEval.cpp**, line 7 (see this on [GitHub](https://github.com/Cantera/cantera/blob/cf1c0816e7d535a1fc385063aebb8b8e93a85233/src/numerics/FuncEval.cpp#L7))

An ODE right-hand-side evaluator is always needed in the ODE solution process (it's the only way to describe the system!), and for that reason a `FuncEval` object is a required parameter when initializing any type of `Integrator`:

**Integrator.h**, line 99 (see this on [GitHub](https://github.com/Cantera/cantera/blob/cf1c0816e7d535a1fc385063aebb8b8e93a85233/include/cantera/numerics/Integrator.h#L99))

```c++
/**
 * Initialize the integrator for a new problem. Call after all options have
 * been set.
 * @param t0   initial time
 * @param func RHS evaluator object for system of equations.
 */
virtual void initialize(doublereal t0, FuncEval& func) {
```

Let's take a look at how `ReactorNet` implements this `FuncEval` object. Instead of creating an external `FuncEval` subclass object, it defines *itself* as a `FuncEval` derivative:

**ReactorNet.h**, line 23 (see this on [GitHub](https://github.com/Cantera/cantera/blob/cf1c0816e7d535a1fc385063aebb8b8e93a85233/include/cantera/zeroD/ReactorNet.h#L23))

```c++
class ReactorNet : public FuncEval
```

Then, it initializes the `Integrator`, using a reference to itself (as a `FuncEval`) from the *['this'](https://www.geeksforgeeks.org/this-pointer-in-c/)* pointer:

**ReactorNet.cpp**, line 112 (see this on [GitHub](https://github.com/Cantera/cantera/blob/cf1c0816e7d535a1fc385063aebb8b8e93a85233/src/zeroD/ReactorNet.cpp#L112))

```c++
m_integ->initialize(m_time, *this);
```

To be a valid `FuncEval` object, a `ReactorNet` needs to provide implementations for all of `FuncEval`'s virtual functions, particularly the actual ODE right-hand-side computation function, `FuncEval::eval()`. Note that this is declared as a *[pure virtual](https://www.geeksforgeeks.org/pure-virtual-functions-and-abstract-classes/)* function, which makes `FuncEval` an abstract class:

**FuncEval.h**, line 32 (see this on [GitHub](https://github.com/Cantera/cantera/blob/cf1c0816e7d535a1fc385063aebb8b8e93a85233/include/cantera/numerics/FuncEval.h#L32))

```c++
/**
 * Evaluate the right-hand-side function. Called by the integrator.
 * @param[in] t time.
 * @param[in] y solution vector, length neq()
 * @param[out] ydot rate of change of solution vector, length neq()
 * @param[in] p sensitivity parameter vector, length nparams()
 */
virtual void eval(double t, double* y, double* ydot, double* p)=0;
```

Along with the rest of `FuncEval`'s virtual functions, an appropriate override is provided for `FuncEval::eval()` in `ReactorNet`:

**ReactorNet.cpp**, line 233 (see this on [GitHub](https://github.com/Cantera/cantera/blob/cf1c0816e7d535a1fc385063aebb8b8e93a85233/src/zeroD/ReactorNet.cpp#L233))

```c++
void ReactorNet::eval(doublereal t, doublereal* y, doublereal* ydot, doublereal* p)
{
    m_time = t; // This will be replaced at the end of the timestep
    updateState(y);
    for (size_t n = 0; n < m_reactors.size(); n++) {
        m_reactors[n]->evalEqs(t, y + m_start[n], ydot + m_start[n], p);
    }
    checkFinite("ydot", ydot, m_nv);
}
```

`ReactorNet`'s `eval()` method invokes calls to `Reactor::evalEqs()`, to evaluate the governing equations of all `Reactor`s contained in the network. This brings us right back to where we started; for more information see Cantera's {doc}`reactor network science page <stable:reference/reactors/index>`.

Hope you enjoyed the post.

[@paulblum](https://github.com/paulblum/)
