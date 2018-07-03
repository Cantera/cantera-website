.. title: Computing Thermodynamic Properties
.. has_math: true

.. jumbotron::

   .. raw:: html

      <h1 class="display-3">Computing Thermodynamic Properties<h1>

   .. class:: lead

      Demonstration of how to use Cantera to compute thermodynamic properties of a phase

Class ThermoPhase
=================

Cantera can be used to compute thermodynamic properties of pure substances,
solutions, and mixtures of various types, including ones containing multiple
phases. The first step is to create an object that represents each phase. A
simple, complete program that creates an object representing a gas mixture and
prints its temperature is shown below:

.. code:: c++

   #include "cantera/thermo.h"
   #include <iostream>

   int main(int argc, char** argv)
   {
       std::unique_ptr<Cantera::ThermoPhase> gas(
           Cantera::newPhase("h2o2.cti", "ohmech"));
       std::cout << gas->temperature() << std::endl;
       return 0;
   }

Class `ThermoPhase`_ is the base class for Cantera classes that represent
phases of matter. It defines the public interface for all classes that represent
phases. For example, it specifies that they all have a method ``temperature``
that returns the current temperature, a method
``setTemperature(double T)`` that sets the
temperature, a method ``getChemPotentials(double* mu)`` that writes the species chemical potentials
into array ``mu``, and so on.

Class `ThermoPhase`_ can be used to represent the intensive state of any
single-phase solution of multiple species. The phase may be a bulk,
three-dimensional phase (a gas, a liquid, or a solid), or it may be a
two-dimensional surface phase, or even a one-dimensional "edge" phase. The
specific attributes of each type of phase are specified by deriving a class from
`ThermoPhase`_ and providing implementations for its virtual methods.

Cantera has a wide variety of models for bulk phases currently. Special attention
(in terms of the speed of execution) has been paid to an ideal gas phase
implementation, where the species thermodynamic polynomial representations
adhere to either the NASA polynomial form or the Shomate polynomial
form. This is widely used in combustion applications, the original application
that Cantera was designed for. Recently, a lot of effort has been placed into
constructing non-ideal liquid phase thermodynamics models that are used in
electrochemistry and battery applications. These models include a Pitzer
implementation for brines solutions and a Margules excess Gibbs free energy
implementation for molten salts.

The Intensive Thermodynamic State
---------------------------------

Class `ThermoPhase`_ and classes derived from it work only with the intensive
thermodynamic state. That is, all extensive properties (enthalpy, entropy,
internal energy, volume, etc.) are computed for a unit quantity (on a mass or
mole basis). For example, there is a method ``enthalpy_mole()`` that returns
the molar enthalpy (J/kmol), and a method ``enthalpy_mass()`` that returns the
specific enthalpy (J/kg), but no method *enthalpy()* that would return the total
enthalpy (J). This is because class `ThermoPhase`_ does not store the total amount
(mass or mole) of the phase.

The intensive state of a single-component phase in equilibrium is fully
specified by the values of any :math:`r+1` independent thermodynamic properties,
where :math:`r` is the number of reversible work modes. If the only reversible
work mode is compression (a "simple compressible substance"), then two
properties suffice to specify the intensive state. Class `ThermoPhase`_ stores
internally the values of the *temperature*, the *mass density*, and the *mass
fractions* of all species. These values are sufficient to fix the intensive
thermodynamic state of the phase, and to compute any other intensive properties.
This choice is arbitrary, and for most purposes you can't tell which properties
are stored and which are computed.

Derived Classes
---------------

Many of the methods of `ThermoPhase`_ are declared virtual, and are meant to be
overloaded in classes derived from ThermoPhase. For example, class
`IdealGasPhase`_ derives from `ThermoPhase`_, and represents ideal gas
mixtures.

Although class `ThermoPhase`_ defines the interface for all classes representing
phases, it only provides implementations for a few of the methods. This is
because `ThermoPhase`_ does not actually know the equation of state of any
phase—this information is provided by classes that derive from `ThermoPhase`_.
The methods implemented by `ThermoPhase`_ are ones that apply to all phases,
independent of the equation of state. For example, it implements methods
``temperature()`` and ``setTemperature()``, since the temperature value is
stored internally.

* `Classes that inherit from ThermoPhase <{{% ct_docs doxygen/html/group__thermoprops.html %}}>`__
* `Classes that handle standard states for species <{{% ct_docs doxygen/html/group__spthermo.html %}}>`__

Example Program
===============

In the program below, a gas mixture object is created, and a few thermodynamic
properties are computed and printed out:

.. include:: pages/tutorials/cxx-guide/thermodemo.cpp
   :code: c++

Note that the methods that compute the properties take no input parameters. The
properties are computed for the state that has been previously set and stored
internally within the object.

Naming Conventions
------------------

- methods that return *molar* properties have names that end in ``_mole``.
- methods that return properties *per unit mass* have names that end in
  ``_mass``.
- methods that write an array of values into a supplied output array have names
  that begin with ``get``. For example, the method
  ``getChemPotentials(double* mu)`` writes the species chemical
  potentials into the output array ``mu``.

The thermodynamic property methods are declared in class `ThermoPhase`_,
which is the base class from which all classes that represent any type of phase
of matter derive.

See `ThermoPhase`_ for the full list of available thermodynamic properties.

.. _ThermoPhase: {{% ct_docs doxygen/html/classCantera_1_1ThermoPhase.html %}}
.. _IdealGasPhase: {{% ct_docs doxygen/html/classCantera_1_1IdealGasPhase.html %}}

.. container:: container

   .. container:: row

      .. container:: col-4 text-left

         .. container:: btn btn-primary
            :tagname: a
            :attributes: href=simple-example.html
                         title="A Very Simple C++ Program"

            Previous: A Very Simple C++ Program

      .. container:: col-4 text-center

         .. container:: btn btn-primary
            :tagname: a
            :attributes: href=index.html
                         title="C++ Interface Tutorial"

            Return: C++ Interface Tutorial

      .. container:: col-4 text-right

         .. container:: btn btn-primary
            :tagname: a
            :attributes: href=equil-example.html
                         title="Equilibrium Example Program"

            Next: Equilibrium Example Program
