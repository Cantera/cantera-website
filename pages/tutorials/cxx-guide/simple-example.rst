.. title: A Very Simple C++ Program

.. _sec-cxx-simple-example:

.. jumbotron::

   .. raw:: html

      <h1 class="display-4">A Very Simple C++ Program</h1>

   .. class:: lead

      How to build a simple C++ program using Cantera objects

A short C++ program that uses Cantera is shown below. This program reads in a
specification of a gas mixture from an input file, and then builds a new object
representing the mixture. It then sets the thermodynamic state and composition
of the gas mixture, and prints out a summary of its properties.

.. include:: pages/tutorials/cxx-guide/demo1a.cpp
   :code: c++

Before you can run this program, it first needs to be compiled. On a Linux
system using the GCC compiler, a typical command line for compiling this program
might look like this:

.. code:: bash

   g++ combustor.cpp -o combustor -O3 $(pkg-config --cflags --libs cantera)

This example relies on the `pkg-config` tool to determine the appropriate compiler
flags, such as those specifying the Cantera header and library files. For more advanced
and flexible methods of compiling programs that use the Cantera C++ library, see
:doc:`compiling`.

This program produces the output below::

  ohmech:

       temperature   500 K
          pressure   2.0265e+05 Pa
           density   0.36118 kg/m^3
  mean mol. weight   7.4093 kg/kmol
   phase of matter   gas

                          1 kg             1 kmol
                     ---------------   ---------------
          enthalpy       -2.4772e+06       -1.8354e+07  J
   internal energy       -3.0382e+06       -2.2511e+07  J
           entropy             20699        1.5337e+05  J/K
    Gibbs function       -1.2827e+07       -9.5038e+07  J
 heat capacity c_p            3919.1             29038  J/K
 heat capacity c_v              2797             20724  J/K

                      mass frac. Y      mole frac. X     chem. pot. / RT
                     ---------------   ---------------   ---------------
                H2           0.21767               0.8           -15.644
                 H                 0                 0
                 O                 0                 0
                O2                 0                 0
                OH                 0                 0
               H2O           0.24314               0.1           -82.953
               HO2                 0                 0
              H2O2                 0                 0
                AR           0.53919               0.1           -20.503
                N2                 0                 0

As C++ programs go, this one is *very* short. It is the Cantera equivalent of
the "Hello, World" program most programming textbooks begin with. But it
illustrates some important points in writing Cantera C++ programs.

Catching ``CanteraError`` exceptions
====================================

The entire body of the program is put inside a function that is invoked within
a ``try`` block in the main program. In this way, exceptions thrown in the
function or in any procedure it calls may be caught. In this program, a
``catch`` block is defined for exceptions of type `CanteraError`_. Cantera
throws exceptions of this type, so it is always a good idea to catch them.

The ``report`` function
=======================

The `ThermoPhase.report`_ function generates a nicely-formatted report of the properties of
a phase, including its composition in both mole (X) and mass (Y) units. For
each species present, the non-dimensional chemical potential is also printed.
This is handy particularly when doing equilibrium calculations. This function
is very useful to see at a glance the state of some phase.

.. _CanteraError: {{% ct_docs doxygen/html/db/ddf/classCantera_1_1CanteraError.html %}}
.. _ThermoPhase.report: {{% ct_docs doxygen/html/dc/d38/classCantera_1_1ThermoPhase.html#a046799f2a038fddf13b5752cd0cc7117 %}}

.. container:: container

   .. container:: row

      .. container:: col-4 text-left

         .. container:: btn btn-primary
            :tagname: a
            :attributes: href=headers.html
                         title="C++ Header Files"

            Previous: C++ Header Files

      .. container:: col-4 text-center

         .. container:: btn btn-primary
            :tagname: a
            :attributes: href=index.html
                         title="C++ Interface Tutorial"

            Return: C++ Interface Tutorial

      .. container:: col-4 text-right

         .. container:: btn btn-primary
            :tagname: a
            :attributes: href=thermo.html
                         title="Computing Properties"

            Next: Computing Properties
