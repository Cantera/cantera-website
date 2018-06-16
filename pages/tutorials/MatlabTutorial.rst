
.. slug: matlab-tutorial
.. highlight:: matlab
.. hidetitle: true


Matlab Tutorial
===============

Getting Started
===============

When using Cantera, the first thing you usually need is an object representing
some phase of matter. Here, we'll create a gas mixture.  Start MATLAB, and at
the prompt type:

.. code:: matlab

    >> gas1 = GRI30

If you have successfully installed the Cantera toolbox, you should see something
like this:

.. code:: matlab

    gri30:

          temperature             300  K
             pressure          101325  Pa
              density       0.0818891  kg/m^3
     mean mol. weight         2.01588  amu

                             1 kg            1 kmol
                          -----------      ------------
             enthalpy         26470.1        5.336e+04     J
      internal energy    -1.21087e+06       -2.441e+06     J
              entropy         64913.9        1.309e+05     J/K
       Gibbs function    -1.94477e+07        -3.92e+07     J
    heat capacity c_p         14311.8        2.885e+04     J/K
    heat capacity c_v         10187.3        2.054e+04     J/K

                              X                 Y          Chem. Pot. / RT
                        -------------     ------------     ------------
                   H2              1                1         -15.7173
        [  +52 minor]              0                0



What you have just done is to create an object ("gas1") that
implements GRI-Mech 3.0, the 53-species, 325-reaction natural gas
combustion mechanism developed by Gregory P. Smith, David M. Golden,
Michael Frenklach, Nigel W. Moriarty, Boris Eiteneer, Mikhail
Goldenberg, C. Thomas Bowman, Ronald K. Hanson, Soonho Song, William
C. Gardiner, Jr., Vitali V. Lissianski, and Zhiwei Qin. (See
http://www.me.berkeley.edu/gri_mech/ for more information about
GRI-Mech 3.0.)

The `gas1` object has properties you would expect for a gas mixture - it has a
temperature, a pressure, species mole and mass fractions, etc. As we'll soon
see, it has many more properties.

The summary of the state of `gas1` printed above shows that new objects
created from the `gri30.cti` input file start out with a temperature of 300 K,
a pressure of 1 atm, and have a composition that consists of only one species,
in this case hydrogen. There is nothing special about H2 - it just happens to
be the first species listed in the input file defining GRI-Mech 3.0. In
general, whichever species is listed first will initially have a mole fraction
of 1.0, and all of the others will be zero.

Setting the State
~~~~~~~~~~~~~~~~~

The state of the object can easily be changed. For example:

.. code:: matlab

    >> setTemperature(gas1, 1200);

sets the temperature to 1200 K (Cantera always uses SI units). After this
statement, calling ``gas1`` results in:

.. code:: matlab

    gri30:

          temperature            1200  K
             pressure          405300  Pa
              density       0.0818891  kg/m^3
     mean mol. weight         2.01588  amu

                             1 kg            1 kmol
                          -----------      ------------
             enthalpy     1.32956e+07         2.68e+07     J
      internal energy     8.34619e+06        1.682e+07     J
              entropy         85227.6        1.718e+05     J/K
       Gibbs function    -8.89775e+07       -1.794e+08     J
    heat capacity c_p         15377.9          3.1e+04     J/K
    heat capacity c_v         11253.4        2.269e+04     J/K

                              X                 Y          Chem. Pot. / RT
                        -------------     ------------     ------------
                   H2              1                1         -17.9775
        [  +52 minor]              0                0


Notice that the temperature has been changed as requested, but the pressure has
changed too. The density and composition have not.

When setting properties individually, some convention needs to be
adopted to specify which other properties are held constant. This is
because thermodynamics requires that *two* properties (not one) in
addition to composition information be specified to fix the
intensive state of a substance (or mixture).

Cantera adopts the following convention: only one of the set
(temperature, density, mass fractions) is altered by setting any
single property. In particular:

- Setting the temperature is done holding density and composition  fixed.
  (The pressure changes.)
- Setting the pressure is done holding temperature and
  composition fixed. (The density changes.)
- Setting the composition is done holding temperature
  and density fixed. (The pressure changes).

If you want to set multiple properties at once, use the 'set' method. (Note: a
'method' is just the term for a function that acts on an object. In MATLAB,
methods take the object as the first argument.):

.. code:: matlab

    >> set(gas1, 'Temperature', 900.0, 'Pressure', 1.e5);

This statement sets both temperature and pressure at the same
time. Any number of property/value pairs can be specified in a
call to 'set'. For example, the following sets the mole fractions
too:

.. code:: matlab

    >> set(gas1, 'Temperature', 900.0, 'Pressure', 1.e5, 'MoleFractions',...
                                       'CH4:1,O2:2,N2:7.52');

The 'set' method also accepts abbreviated property names:

.. code:: matlab

    >> set(gas1,'T',900.0,'P',1.e5,'X','CH4:1,O2:2,N2:7.52')

Either version results in:

.. code:: matlab

    gri30:

          temperature             900  K
             pressure          100000  Pa
              density        0.369279  kg/m^3
     mean mol. weight         27.6332  amu

                             1 kg            1 kmol
                          -----------      ------------
             enthalpy         455660        1.259e+07     J
      internal energy         184862        5.108e+06     J
              entropy         8529.31        2.357e+05     J/K
       Gibbs function    -7.22072e+06       -1.995e+08     J
    heat capacity c_p          1304.4        3.604e+04     J/K
    heat capacity c_v         1003.52        2.773e+04     J/K

                              X                 Y          Chem. Pot. / RT
                        -------------     ------------     ------------
                   O2       0.190114         0.220149         -27.9596
                  CH4       0.095057        0.0551863         -37.0813
                   N2       0.714829         0.724665          -24.935
        [  +50 minor]              0                0

Other properties may also be set using 'set', including some that
can't be set individually. The following property pairs may be
set: (Enthalpy, Pressure), (IntEnergy, Volume), (Entropy,
Volume), (Entropy, Pressure). In each case, the values of the
extensive properties must be entered *per unit mass*.

Setting the enthalpy and pressure:

.. code:: matlab

    >> set(gas1, 'Enthalpy', 2*enthalpy_mass(gas1), 'Pressure', 2*oneatm);

The composition above was specified using a string. The format is a
comma-separated list of <species name>:<relative mole numbers>
pairs. The mole numbers will be normalized to produce the mole
fractions, and therefore they are 'relative' mole numbers.  Mass
fractions can be set in this way too by changing 'X' to 'Y' in the
above statement.

The composition can also be set using an array, which can be
either a column vector or a row vector but must have the same
size as the number of species. For example, to set all 53 mole
fractions to the same value, do this:

.. code:: matlab

    >> x = ones(53,1);   % a column vector of 53 ones
    >> set(gas1, 'X', x)

To set the mass fractions to equal values:

.. code:: matlab

    >> set(gas1, 'Y', x)

Importing multiple phases or interfaces
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A Cantera input file may contain more than one phase specification,
or may contain specifications of interfaces (surfaces). Here we
import definitions of two bulk phases and the interface between them
from file diamond.cti:

.. code:: matlab

    >> gas2 = Solution('diamond.cti', 'gas');        % a gas
    >> diamond = Solution('diamond.cti','diamond');  % bulk diamond
    >> diamonnd_surf = importInterface('diamond.cti','diamond_100',...
                                    gas2, diamond);

Note that the bulk (i.e., 3D) phases that participate in the surface
reactions must also be passed as arguments to importInterface.

The following command clears all Matlab objects created:

.. code:: matlab

    >> clear all

and this clears all Cantera objects created:

.. code:: matlab

    >> cleanup

Working with input files
========================

Previously, we used the function GRI30 to create an object that models an ideal
gas mixture with the species and reactions of GRI-Mech 3.0. Another way to do
this is shown here, with statements added to measure how long this takes:

.. code:: matlab

  >> t0 = cputime;
  >> gas1 = Solution('gri30.cti', 'gri30');
  >> msg = sprintf('time to create gas1: %f', cputime - t0)

Function 'Solution' constructs an object representing a phase of
matter by reading in attributes of the phase from a file, which in
this case is 'gri30.cti'. This file contains several phase
spcifications; the one we want here is 'gri30', which is specified
by the second argument.  This file contains a complete specification
of the GRI-Mech 3.0 reaction mechanism, including element data
(name, atomic weight), species data (name, elemental composition,
coefficients to compute thermodynamic and transport properties), and
reaction data (stoichiometry, rate coefficient parameters). The file
is written in a format understood by Cantera, which is described in
the document "Defining Phases and Interfaces."

On some systems, processing long CTI files like gri30.cti can be a
little slow. For example, using a typical laptop computer running
Windows 2000, the statement above takes more than 4 s, while on a
Mac Powerbook G4 of similar CPU speed it takes only 0.3 s. In any
case, running it again takes much less time, because Cantera
'remembers' files it has already processed and doesn't need to read
them in again:

.. code:: matlab

  >> t0 = cputime;
  >> gas1b = Solution('gri30.cti', 'gri30');
  >> msg = sprintf('time to create gas1b: %f', cputime - t0)

To learn more about the cti files already available with Cantera and how to
create new cti files, see :doc:`Working With Input Files <input-files>`

CTI files distributed with Cantera
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Several reaction mechanism files in this format are included in the
Cantera distribution, including ones that model high-temperature
air, a hydrogen/oxygen reaction mechanism, and a few surface
reaction mechanisms. Under Windows, these files may be located in
'C:\Program Files\Common Files\Cantera', or in 'C:\cantera\data',
depending on how you installed Cantera and the options you
specified.  On a unix/linux/Mac OSX machine, they are usually kept
in the 'data' subdirectory within the Cantera installation
directory.

If for some reason Cantera has difficulty finding where these files
are on your system, set environment variable CANTERA_DATA to the
directory where they are located. Alternatively, you can call function
adddir to add a directory to the Cantera search path:

.. code:: matlab

  >> adddir('/usr/local/cantera/my_data_files');


XML files
~~~~~~~~~

Note that when Cantera reads a .cti input file, wherever it is
located, it always writes a file of the same name but with extension
.xml *in the local directory*. If you happen to have some other file
by that name, it will be overwritten. Once the XML file is created,
you can use it instead of the .cti file, which will result in
somewhat faster startup:

.. code:: matlab

    >> gas4 = Solution('gri30.xml','gri30');

Interfaces can be imported from XML files too:

.. code:: matlab

   >> diamonnd_surf2 = importInterface('diamond.xml','diamond_100',...
                                     gas2, diamond);

Let's clear out all our Matlab and Cantera objects, before we move on:

.. code:: matlab

  >> clear all
  >> cleanup

Getting Help
============

Suppose you have created a Cantera object and want to know what
methods are available for it, and get help on using the methods.

.. code:: matlab

  >> g = GRI30

The first thing you need to know is the MATLAB class object g
belongs to. Type:

.. code:: matlab

  >> class(g)

This tells you that g belongs to a class called 'Solution'. To find
the methods for this class, type

.. code:: matlab

  >> methods Solution

This command returns only a few method names. These are the ones
directly defined in this class. But solution inherits many other
methods from base classes. To see all of its methods, type

.. code:: matlab

  >> methods Solution -full

Now a long list is printed, along with a specification of the class
the method is inherited from. For example, 'setPressure' is
inherited from a class 'ThermoPhase'. Don't be concerned at this
point about what these base classes are - we'll come back to them
later.

Now that you see what methods are available, you can type 'help
<method_name>' to print help text for any method. For example,

.. code:: matlab

  >> help setTemperature
  >> help setMassFractions
  >> help rop_net

For help on how to construct objects of a given class, type 'help
<classname>'

.. code:: matlab

  >> help Solution

Now that you know how to get help when you need it, you can
explore using the Cantera Toolbox on your own. But there are a
few more useful things to know, which are described in the next
few sections.



Chemical Equilibrium
====================

To set a gas mixture to a state of chemical equilibrium, use the
'equilibrate' method.

.. code:: matlab

  >> set(g,'T',1200.0,'P',oneatm,'X','CH4:0.95,O2:2,N2:7.52')
  >> equilibrate(g,'TP')

The above statement sets the state of object 'g' to the state of
chemical equilibrium holding temperature and pressure
fixed. Alternatively, the specific enthalpy and pressure can be held
fixed:

.. code:: matlab

  >> disp('fixed H and P:');
  >> set(g,'T',1200.0,'P',oneatm,'X','CH4:0.95,O2:2.0,N2:7.52');
  >> equilibrate(g,'HP')

Other options are:

  - 'UV'   fixed specific internal energy and specific volume
  - 'SV'   fixed specific entropy and specific volume
  - 'SP'   fixed specific entropy and pressure

.. code:: matlab

  >> disp('fixed U and V:');
  >> set(g,'T',1200.0,'P',oneatm,'X','CH4:0.95,O2:2,N2:7.52');
  >> equilibrate(g,'UV')

.. code:: matlab

  >> disp('fixed S and V:');
  >> set(g,'T',1200.0,'P',oneatm,'X','CH4:0.95,O2:2,N2:7.52');
  >> equilibrate(g,'SV')

.. code:: matlab

  >> disp('fixed S and P:');
  >> set(g,'T',1200.0,'P',oneatm,'X','CH4:0.95,O2:2,N2:7.52');
  >> equilibrate(g,'SP')

How can you tell if 'equilibrate' has correctly found the
chemical equilibrium state? One way is verify that the net rates of
progress of all reversible reactions are zero.

Here is the code to do this:

.. code:: matlab

  >> set(g,'T',2000.0,'P',oneatm,'X','CH4:0.95,O2:2,N2:7.52');
  >> equilibrate(g,'TP')
  >> rf = rop_f(g);
  >> rr = rop_r(g);
  >> format short e;
  >> for i = 1:nReactions(g)
  >>  if isReversible(g,i)
  >>    disp([i, rf(i), rr(i), (rf(i) - rr(i))/rf(i)]);
  >>    end
  >> end

You might be wondering how 'equilibrate' works. (Then again, you might
not, in which case you can go on to the next tutorial now.)  Method
'equilibrate' invokes Cantera's chemical equilibrium solver, which
uses an element potential method. The element potential method is
one of a class of equivalent 'nonstoichiometric' methods that all
have the characteristic that the problem reduces to solving a set of
M nonlinear algebraic equations, where M is the number of elements
(not species). The so-called 'stoichiometric' methods, on the other
hand, (including Gibbs minimization), require solving K nonlinear
equations, where K is the number of species (usually K >> M). See
Smith and Missen, "Chemical Reaction Equilibrium Analysis" for more
information on the various algorithms and their characteristics.

Cantera uses a damped Newton method to solve these equations, and
does a few other things to generate a good starting guess and to
produce a reasonably robust algorithm. If you want to know more
about the details, look at the on-line documented source code of
Cantera C++ class 'ChemEquil' at `<http://www.cantera.org>`_.

Reaction information and rates
==============================

Methods are provided that compute many quantities of interest for
kinetics. Some of these are:

Stoichiometric coefficients
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: matlab

  >> set(g,'T',1500,'P',oneatm,'X',ones(nSpecies(g),1));
  >> nu_r   = stoich_r(g)    % reactant stoichiometric coefficient mstix
  >> nu_p   = stoich_p(g)    % product stoichiometric coefficient mstix
  >> nu_net = stoich_net(g)  % net (product - reactant) stoichiometric
                             % coefficient mstix

For any of these, the (k,i) matrix element is the stoichiometric
coefficient of species k in reaction i. Since these coefficient
matrices are very sparse, they are implemented as MATLAB sparse
matrices.


Reaction rates of progress
~~~~~~~~~~~~~~~~~~~~~~~~~~

Methods rop_f, rop_r, and rop_net return column vectors containing
the forward, reverse, and net (forward - reverse) rates of
progress, respectively, for all reactions.

.. code:: matlab

  >> qf = rop_f(g);
  >> qr = rop_r(g);
  >> qn = rop_net(g);
  >> rop = [qf, qr, qn]

This plots the rates of progress

.. code:: matlab

  >> figure(1);
  >> bar(rop);
  >> legend('forward','reverse','net');

Species production rates
~~~~~~~~~~~~~~~~~~~~~~~~

Methods creationRates, destructionRates, and netProdRates return
column vectors containing the creation, destruction, and net
production (creation - destruction) rates, respectively, for all species.

.. code:: matlab

  >> cdot = creationRates(g);
  >> ddot = destructionRates(g);
  >> wdot = netProdRates(g);
  >> rates = [cdot, ddot, wdot]

This plots the production rates:

.. code:: matlab

  >> figure(2);
  >> bar(rates);
  >> legend('creation','destruction','net');

For comparison, the production rates may also be computed
directly from the rates of progress and stoichiometric
coefficients.

.. code:: matlab

  >> cdot2 = nu_p*qf + nu_r*qr;
  >> creation = [cdot, cdot2, cdot - cdot2]

.. code:: matlab

    >> ddot2 = nu_r*qf + nu_p*qr;
    >> destruction = [ddot, ddot2, ddot - ddot2]

.. code:: matlab

    >> wdot2 = nu_net * qn;
    >> net = [wdot, wdot2, wdot - wdot2]

Reaction equations
~~~~~~~~~~~~~~~~~~

.. code:: matlab

  >> e8    = reactionEqn(g,8)             % equation for reaction 8
  >> e1_10 = reactionEqn(g,1:10)          % equation for rxns 1 - 10
  >> eqs   = reactionEqn(g)               % all equations

Equilibrium constants
~~~~~~~~~~~~~~~~~~~~~

The equilibrium constants are computed in concentration units,
with concentrations in kmol/m^3.

.. code:: matlab

  >> kc = equil_Kc(g);
  >> for i = 1:nReactions(g)
  >>      disp(sprintf('%50s  %13.5g', eqs{i}, kc(i)))
  >> end

Multipliers
~~~~~~~~~~~

For each reaction, a multiplier may be specified that is applied
to the forward rate coefficient. By default, the multiplier is
1.0 for all reactions.

.. code:: matlab

  >> for i = 1:nReactions(g)
  >>      setMultiplier(g, i, 2*i);
  >>      m = multiplier(g, i);
  >> end

Let's clear out the Matlab and Cantera objects, before moving on:

.. code:: matlab

  >> clear all
  >> cleanup

Transport Properties
====================

Methods are provided to compute transport properties. By
default, calculation of transport properties is not enabled. If
transport properties are required, the transport model must be
specified when the gas mixture object is constructed.

Currently, two models are implemented. Both are based on kinetic
theory expressions, and follow the approach described in Dixon-Lewis
(1968) and Kee, Coltrin, and Glarborg (2003). The first is a full
multicomponent formulation, and the second is a simplification that
uses expressions derived for mixtures with a small number of species
(1 to 3), using approximate mixture rules to average over
composition.

To use the multicomponent model with GRI-Mech 3.0, call function
GRI30 as follows:

.. code:: matlab

  >> g1 = GRI30('Multi')

To use the mixture-averaged model:

.. code:: matlab

  >> g2 = GRI30('Mix')

Both models use a mixture-averaged formulation for the viscosity.

.. code:: matlab

  >> visc = [viscosity(g1), viscosity(g2)]

The thermal conductivity differs, however.

.. code:: matlab

  >> lambda = [thermalConductivity(g1), thermalConductivity(g2)]

Binary diffusion coefficients

.. code:: matlab

  >> bdiff1 = binDiffCoeffs(g1)
  >> bdiff2 = binDiffCoeffs(g2)

Mixture-averaged diffusion coefficients. For convenience, the
multicomponent model implements mixture-averaged diffusion
coefficients too.

.. code:: matlab

  >> dmix2 = mixDiffCoeffs(g1)
  >> dmix1 = mixDiffCoeffs(g2)

Multicomponent diffusion coefficients. These are only implemented
if the multicomponent model is used.

.. code:: matlab

  >> dmulti = multiDiffCoeffs(g1)

Thermal diffusion coefficients. These are only implemented with the
multicomponent model.  These will be very close to zero, since
the composition is pure H2.

.. code:: matlab

  >> dt = thermalDiffCoeffs(g1)

Now change the composition and re-evaluate

.. code:: matlab

  >> set(g1,'X',ones(nSpecies(g1),1));
  >> dt = thermalDiffCoeffs(g1)

Note that there are no singularities for pure gases. This is
because a very small positive value is added to all mole
fractions for the purpose of computing transport properties.


Let's clear out the Matlab and Cantera objects, before moving on:

.. code:: matlab

  >> clear all
  >> cleanup

Thermodynamic Properties
========================

A variety of thermodynamic property methods are provided.

.. code:: matlab

  >> gas = air
  >> set(gas,'T',800,'P',oneatm)

Temperature, pressure, density:

.. code:: matlab

  >> T = temperature(gas)
  >> P = pressure(gas)
  >> rho = density(gas)
  >> n = molarDensity(gas)

Species non-dimensional properties:

.. code:: matlab

  >> hrt = enthalpies_RT(gas)            % vector of h_k/RT

Mixture properties per mole:

.. code:: matlab

  >> hmole = enthalpy_mole(gas)
  >> umole = intEnergy_mole(gas)
  >> smole = entropy_mole(gas)
  >> gmole = gibbs_mole(gas)

Mixture properties per unit mass:

.. code:: matlab

  >> hmass = enthalpy_mass(gas)
  >> umass = intEnergy_mass(gas)
  >> smass = entropy_mass(gas)
  >> gmass = gibbs_mass(gas)

Le'ts do one final clearing of the workspace:

.. code:: matlab

  >> clear all
  >> cleanup

Congratulations -- Next Steps
=============================

Congratulations - you have finished the Cantera Matlab tutorial! You should now
be ready to begin using Cantera on your own.  Please see the Next Steps
section on the `Getting Started <index.html#cantera-next-steps>`_ page, for assistance with
intermediate and advanced Cantera functionality.  Good luck!
