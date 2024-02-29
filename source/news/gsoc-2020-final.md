---
title: GSoC 2020 Project Summary
date: 2020-08-31 16:20
slug: gsoc-2020-final
tags: GSoC 2020
description: A summary of the progress made during GSoC 2020 towards a Cantera 0-D steady-state combustion solver.
type: text
author: Paul Blum
---

# Google Summer of Code 2020: *Developing a 0-D Steady-State Combustion Solver for Cantera*

Combustion is a fundamental discipline of modern science, and understanding it has enabled the development of our technologies in electricity production, heating, transportation, and industry. Advancements in combustion science have been facilitated by our ability to simulate the phenomenon, made possible by computer software like Cantera. The goal of this project was to add a new solver to Cantera that would allow users to directly simulate zero-dimensional steady-state combustion, which can occur in reactors when internal chemical processes become perfectly balanced with one another. This type of idealized simulation can be used to quickly and accurately approximate the behavior of real combustion systems.
<!-- TEASER_END -->

- [Introductory Blog Post](gsoc-2020-intro)
- [Full Project Proposal](https://drive.google.com/file/d/1vaOjydm6wWKgF2M4J3iFwNZNKHX5laBY/view)
- [Official GSoC Project Link](https://summerofcode.withgoogle.com/projects/#4550970131873792)

As the project began, discussions with the Cantera community led me to make a few deviations from the project proposal, switching the development language to C++ and the numerical solver to Cantera’s built-in 1D multi-domain damped Newton solver. These changes allowed me to build upon existing Cantera C++ examples to create a simple constant-pressure perfectly-stirred reactor simulator, PSRv0.1. This initial version of the simulation tool could find solutions only to systems with simple reactions, but it was invaluable in helping me understand how the Cantera solver worked and how I would need to implement the governing equations in future versions.

- [Blog Post 1: Learning C++, Switching Solvers, and Initial Implementations](gsoc-2020-blog-1)
- [PSRv0.1 Code](https://github.com/paulblum/cantera/blob/0DSS/samples/cxx/psr/PSRv1.cpp)

Improving PSRv0.1 required extensive research on existing implementations of perfectly-stirred reactor solvers, and experimentation with different mathematical models of the governing equations. A simplification of these equations and the incorporation of time-stepping to improve convergence intervals led to the development of PSRv0.2, an accurate and broadly-capable version of the simulator.

- [Blog Post 2: Developing a Capable and Accurate PSR Solver](gsoc-2020-blog-2)
- [PSRv0.2 Code](https://github.com/paulblum/cantera/blob/0DSS/samples/cxx/psr/PSRv2.cpp)

With a working proof-of-concept simulator, the next step was to introduce compatibility with Cantera’s existing reactor network module, which would need to provide initial conditions and reactor-specific governing equations to the steady-state solver. Documentation at this implementation depth of Cantera’s source code was limited; becoming familiar with it required a detailed study of the code with line-by-line walkthroughs of a few example simulations. To better my own understanding and share what I had learned with the Cantera community, I wrote a developer-oriented overview of the module’s implementation, and created a new C++ example problem that uses the module’s fundamental solution tools to solve the governing equations that I had been working on. Based on the external-solver usage in Cantera’s reactor network module, I created a dedicated nonlinear algebraic solver interface, `Cantera_NonLinSol`, to be used by the reactor network module to simulate steady-state systems. Usage of this interface is demonstrated in PSRv0.3.

- [Blog Post 3: How Does Cantera’s Reactor Network Time Integration Feature Work?](gsoc-2020-blog-3)
- [New C++ Example: custom.cpp](https://github.com/Cantera/cantera/pull/922)
- [`Cantera_NonLinSol` Interface](https://github.com/paulblum/cantera/blob/ca36e253bd28c6d507eace5b6f1199cac64d8909/include/cantera/numerics/Cantera_NonLinSol.h)
- [PSRv0.3 Code](https://github.com/paulblum/cantera/blob/0DSS/samples/cxx/psr/PSRv0-3.cpp)

At this point, incorporating steady-state simulation into the reactor network module was relatively straightforward because most of the solution process took place in the external `Cantera_NonLinSol` interface. After including the interface appropriately and providing implementations for problem-specific system-defining pure virtual functions, the reactor network module was ready to simulate 0-D steady-state combustion at constant pressure. Usage of this feature is demonstrated in PSRv0.4, and more detailed information about its implementation and mathematical modeling are provided in my fourth GSoC blog post.

- [Blog Post 4: Steady-State Solution in `ReactorNet` Simulations](gsoc-2020-blog-4)
- [PSRv0.4 Code](https://github.com/paulblum/cantera/blob/0DSS/samples/cxx/psr/PSRv0-4.cpp)

The next step in this project’s development is to generalize the governing equations to allow steady-state simulation at variable or unknown reactor pressures. I’ve already begun working on adding this capability, and I’m expecting it to be operational very soon! Future updates will be posted to the Cantera [enhancements repository](https://github.com/Cantera/enhancements/issues/31) on GitHub, so be sure to stay tuned for the release of the finished steady-state solver.

This project has been one of the most challenging that I’ve ever worked on, but ultimately one of the most rewarding. I’ve learned an incredible amount about combustion and open-source programming, and I’m ready to continue using and advancing these skillsets to contribute even more code in the future. I’d like to extend a special thank you to my mentor [@bryanwweber](https://github.com/bryanwweber) for making this experience possible, and for all of the help he provided along the way.
