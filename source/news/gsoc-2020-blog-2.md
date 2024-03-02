---
date: 2020-06-29 14:00
tags: GSoC 2020
author: Paul Blum
---

# GSoC 2020: Developing a 0-D Steady-State Combustion Solver for Cantera

My work since last posting has been characterized by research and experimentation, and this blog post will highlight some of the findings that I've made. I have learned a lot about Cantera and combustion over the past two weeks, but more excitingly, I developed a working proof-of-concept 0-D steady-state solver, PSRv0.2!

## The Energy Equation

In my last blog post, I discussed the troubles I was having with reaching convergence in systems that included the energy equation, and introduced some ideas I had that might be potential remedies. After doing some research, I found a great resource that addressed these ideas and the numerical solution of perfectly-stirred reactors as a whole. The report provided a new version of the energy equation that considered time-dependent and heat release properties, derived from transient forms of the species conservation and energy balance equations; see the [full report](https://www.researchgate.net/publication/236418395_PSE_a_Fortran_program_for_modeling_well-stirred_reactors) for a detailed derivation. Building off of [PSR v0.1](https://github.com/paulblum/cantera/blob/0DSS/samples/cxx/psr/PSRv1.cpp) (introduced in the last blog post), I created a version of the solver that used the new energy equation in its solution attempt. Unfortunately, this too had trouble converging without a very good initial guess. Even after introducing time integration and solving the fixed-temperature problem first, the severe nonlinearities of the solution model almost always made convergence impossible.

## Time Integration

As just hinted at, the solvers that I developed and discussed in my last blog post hadn't been using time integration! I originally thought that this feature of the Cantera solver worked using only the residual function, but this wasn't the case. Time integration is actually done via the backward Euler method. In Cantera's application, the solution at the previous timestep is obtained using the solver's built-in `prevSoln()` method, and the timestep value *dt* is incorporated using its passed-in reciprocal, `rdt`. Each iteration of the backward Euler method needs to be subtracted from the result of the residual function at the corresponding solution vector—the Cantera solver is set up to extract the information that it needs from this difference. Further, modifying values in the `diag` pointer is also required at each iteration. `diag` can be thought of as a mask, and in order to activate time stepping for a specific solution component, its corresponding mask entry needs to be set to 1.

## PSR Solver v0.2

Although time integration didn't help convergence with the energy equation, it was exactly what I needed to get PSR v0.1 working! Adding time integration resulted in a capable and accurate PSR solver. I compared this new version of the solver to Cantera's `IdealGasReactor` based on the example code in {doc}`combustor.py <stable:examples/python/reactors/combustor>`, and the results were just about *exactly* the same:

```{image} /_static/images/gsoc-2020/v0-2-results.png
```

Check out the full code for [PSR v0.2 on GitHub](https://github.com/paulblum/cantera/blob/0DSS/samples/cxx/psr/PSRv2.cpp)! The energy equation and fixed-temperature versions of the solver are built in for reference, although they weren't used to produce the results above.

As always, I appreciate any suggestions or feedback you might have. Feel free to leave a comment on this project's page in the [Cantera enhancements repository](https://github.com/Cantera/enhancements/issues/31), or email me at <paul_d_blum@yahoo.com>.

Until next time,

[@paulblum](https://github.com/paulblum/)
