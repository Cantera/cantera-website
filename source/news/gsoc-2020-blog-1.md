---
date: 2020-06-15 14:00
tags: GSoC 2020
author: Paul Blum
---

# GSoC 2020: Developing a 0-D Steady-State Combustion Solver for Cantera

## Learning C++ for Cantera Development

My original [project proposal](https://drive.google.com/file/d/1vaOjydm6wWKgF2M4J3iFwNZNKHX5laBY/view?usp=sharing) called for preliminary development in C and Python, primarily because I’ve worked with these languages in the past and would be able to start writing test code right away. However, I ultimately decided to learn and use  C++ instead, and I’m very glad that I did. Most of the Cantera source code is written in C++, and being able to easily read and reference it without guessing at the syntax has proven invaluable in development so far.

I learned C++ by following a free [Codecademy tutorial](https://www.codecademy.com/learn/learn-c-plus-plus), which I would definitely recommend to beginning and experienced coders alike. The tutorial was detailed and interactive, and only took me a day to complete. After that, I followed Cantera’s {doc}`C++ Interface Tutorial <stable:userguide/cxx-tutorial>`, another excellent resource that I’d say is essential for any beginning Cantera developer. It introduced Cantera-specific technical details needed for C++ development, and provided simple code examples that illustrated how to use Cantera’s functionality to perform some basic calculations.

## Switching Solvers

The heart of this project is a capable numerical solver that can quickly provide a solution to the [set of nonlinear equations](https://drive.google.com/file/d/1vxt3tW1wbvMLTaDygRmpqEJN6yNSO_Lv/view?usp=sharing) that characterize 0-D steady-state combustion systems. In my project proposal I suggested the use of KINSOL, an externally developed code module that uses a version of Newton’s method to solve nonlinear algebraic equations. Stemming from discussions with mentors, I found that Cantera has a built-in and similarly implemented damped Newton solver that should be able to provide the equivalent capability. In efforts not to duplicate existing functionality, as well as to maintain consistency with the rest of the source code, I decided it would be best to use Cantera’s solver in this application. The solver was developed for solving 1-D multi-domain problems, but after some quick testing, I determined that it’s also able to solve 0-D problems with ease. These tests were performed by modifying the residual functions and a few input parameters in the {doc}`Blasius sample program <stable:examples/cxx/blasius>` to find solutions to arbitrary sets of equations at a single point, rather than along a 1-D array of points.

## Implementing the Simple Solver

My first development objective was to create a basic standalone solver for the well-stirred reactor model. As mentioned previously, solutions for this type of problem are characterized by a [set of nonlinear equations](https://drive.google.com/file/d/1vxt3tW1wbvMLTaDygRmpqEJN6yNSO_Lv/view?usp=sharing) that are typically solved by some numerical analysis software, in this case the one that’s built in to Cantera. The Blasius sample code worked well for my initial tests, so I based the structure of my solver on this program, even directly using the simplified {doc}`boundary value problem interface <stable:examples/cxx/BoundaryValueProblem>` to Cantera’s solver. Unfortunately, I couldn’t get this to converge to an appropriate solution. Even given the true solution as an initial vector, the slightest of inaccuracies in inputted properties seemed to result in huge residual values of the energy equation, pushing the solver further from an acceptable solution with each iteration. After doing some research on why this might be, I found that it’s likely due to the exponential dependence of reaction rates on temperature, which makes convergence of the 0-D steady-state equation system quite difficult for a numerical solver. There are a few potential solutions to the issue, which I’m planning on studying in more detail in the coming weeks to get this version of the solver working:

- The energy equation in the model may need to be replaced with one that considers transient properties
- The system may need to be solved twice, first at a fixed temperature (without the energy equation) to obtain a “consistent” initial guess for a second run which will solve for the true solution
- Rates of heat release during the reaction may need to be incorporated into the system
- A more advanced, problem-specific version of the Cantera solver may need to be used rather than the simplified boundary value problem interface
- Something else?

## PSR Solver v0.1

After some brief experimentation with the ideas listed above, I noticed that the well-stirred reactor equations converged very quickly to the correct solution when simulated at arbitrarily fixed temperatures. This confirmed my suspicion that the addition of the energy equation to the system was causing the trouble. At its roots, the energy equation ensures energy conservation through the reactor by forcing the total enthalpy of the exhaust gas mixture at the reactor outlet to match the total enthalpy of the gas mixture at the inlet. The total enthalpy of the exhaust is directly correlated to reactor temperature, which is typically the property that a numerical solver will adjust in attempt to satisfy the energy equation.

I realized that Cantera may provide an alternate way to satisfy the conservation of energy, by keeping total enthalpy fixed via the `setState_HP()` method of the thermodynamics library. After specifying iteration mass fractions, exhaust enthalpy can be forced to match the inlet enthalpy simply by explicitly setting it this way with `setState_HP()`. This function will adjust any dependent properties, like temperature, as needed in order to satisfy the laws of thermodynamics. This idea evolved into [my first working version](https://github.com/paulblum/cantera/blob/0DSS/samples/cxx/psr/PSRv1.cpp) of a PSR solver! This experimental version of the solver converges quickly for simple reactions, but has trouble finding solutions to more complicated ones. At this point, I’m not entirely sure of the extent of v0.1’s capabilities, but it will be tested thoroughly in the coming weeks and used in the future as seen fit.
