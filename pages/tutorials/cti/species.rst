.. slug: cti-species
.. title: Elements and Species
.. has_math: true

.. jumbotron::

   .. raw:: html

      <h1 class="display-3">Elements and Species</h1>

   .. class:: lead

      A description of how elements and species are defined in CTI input files

Elements
========

The :cti:class:`element` entry defines an element or an isotope of an element. Note
that these entries are not often needed, since the the database file
``elements.xml`` is searched for element definitions when importing phase and
interface definitions. An explicit element entry is needed only if an isotope
not in ``elements.xml`` is required:

.. code:: python

   element(symbol='C-13',
           atomic_mass=13.003354826)
   element("O-18", 17.9991603)

Species
=======

For each species, a :cti:class:`species` entry is required. Species are defined at
the top-level of the input file—their definitions are not embedded in a phase
or interface entry.

Species Name
~~~~~~~~~~~~

The name field may contain embedded parentheses, ``+`` or ``-`` signs to
indicate the charge, or just about anything else that is printable and not a
reserved character in XML. Some example name specifications:

.. code:: python

   name='CH4'
   name='methane'
   name='argon_2+'
   name='CH2(singlet)'

Elemental Composition
~~~~~~~~~~~~~~~~~~~~~

The elemental composition is specified in the atoms entry, as follows:

.. code:: python

   atoms="C:1, O:2"            # CO2 with optional comma
   atoms="Y:1 Ba:2 Cu:3 O:6.5" # stoichiometric YBCO
   atoms=""                    # a surface species representing an empty site
   atoms="Ar:1 E:-2"           # Ar++

For gaseous species, the elemental composition is well-defined, since the
species represent distinct molecules. For species in solid or liquid solutions,
or on surfaces, there may be several possible ways of defining the species. For
example, an aqueous species might be defined with or without including the water
molecules in the solvation cage surrounding it.

For surface species, it is possible to omit the ``atoms`` field entirely, in
which case it is composed of nothing, and represents an empty surface site. This
can also be done to represent vacancies in solids. A charged vacancy can be
defined to be composed solely of electrons:

.. code:: python

   species(name='ysz-oxygen-vacancy',
           atoms='O:0, E:2',
           # ...,
           )

Note that an atom number of zero may be given if desired, but is completely
equivalent to omitting that element.

The number of atoms of an element must be non-negative, except for the special
"element" ``E`` that represents an electron.

Thermodynamic Properties
~~~~~~~~~~~~~~~~~~~~~~~~

The :cti:class:`phase` and :cti:class:`ideal_interface` entries discussed previously implement
specific models for the thermodynamic properties appropriate for the type of phase or interface they
represent. Although each one may use different expressions to compute the properties, they all
require thermodynamic property information for the individual species. For the phase types
implemented at present, the properties needed are:

1. the molar heat capacity at constant pressure :math:`\hat{c}^0_p(T)` for a
   range of temperatures and a reference pressure :math:`P_0`;
2. the molar enthalpy :math:`\hat{h}(T_0, P_0)` at :math:`P_0` and a reference
   temperature :math:`T_0`;
3. the absolute molar entropy :math:`\hat{s}(T_0, P_0)` at :math:`(T_0, P_0)`.

See: :ref:`sec-thermo-models` for a listing of the available species
thermodynamic models available in Cantera.

7-Coefficient NASA Polynomials
------------------------------

A NASA parameterization is defined by an embedded :cti:class:`NASA` entry. Very
often, two NASA parameterizations are used for two contiguous temperature
ranges. This can be specified by assigning the ``thermo`` field of the
``species`` entry a sequence of two :cti:class:`NASA` entries:

.. code:: python

   # use one NASA parameterization for T < 1000 K, and another for T > 1000 K.
   species(name = "O2",
         atoms = " O:2 ",
         thermo = (
               NASA( [ 200.00, 1000.00], [ 3.782456360E+00, -2.996734160E-03,
                       9.847302010E-06, -9.681295090E-09, 3.243728370E-12,
                       -1.063943560E+03, 3.657675730E+00] ),
               NASA( [ 1000.00, 3500.00], [ 3.282537840E+00, 1.483087540E-03,
                       -7.579666690E-07, 2.094705550E-10, -2.167177940E-14,
                       -1.088457720E+03, 5.453231290E+00] ) ) )

9-Coefficient NASA polynomials
------------------------------

The following is an example of a species defined using the :cti:class:`NASA9`
parameterization in three different temperature regions:

.. code:: python

   species(name=u'CO2',
         atoms='C:1 O:2',
         thermo=(NASA9([200.00, 1000.00],
                         [ 4.943650540E+04, -6.264116010E+02,  5.301725240E+00,
                           2.503813816E-03, -2.127308728E-07, -7.689988780E-10,
                           2.849677801E-13, -4.528198460E+04, -7.048279440E+00]),
                   NASA9([1000.00, 6000.00],
                         [ 1.176962419E+05, -1.788791477E+03,  8.291523190E+00,
                          -9.223156780E-05,  4.863676880E-09, -1.891053312E-12,
                           6.330036590E-16, -3.908350590E+04, -2.652669281E+01]),
                   NASA9([6000.00, 20000.00],
                         [-1.544423287E+09,  1.016847056E+06, -2.561405230E+02,
                           3.369401080E-02, -2.181184337E-06,  6.991420840E-11,
                          -8.842351500E-16, -8.043214510E+06,  2.254177493E+03])),
           note='Gurvich,1991 pt1 p27 pt2 p24. [g 9/99]')

Thermodynamic data for a range of species can be obtained from the
`NASA ThermoBuild <http://cearun.grc.nasa.gov/cea/index_ds.html>`__ tool. Using the web
interface, an input file can be obtained for a set of species. This input file
should then be modified so that the first line reads "`thermo nasa9`", as in the
following example:

.. code::

   thermo nasa9
      200.000  1000.000  6000.000 20000.000   9/09/04
   CO                Gurvich,1979 pt1 p25 pt2 p29.
    3 tpis79 C   1.00O   1.00    0.00    0.00    0.00 0   28.0101000    -110535.196
       200.000   1000.0007 -2.0 -1.0  0.0  1.0  2.0  3.0  4.0  0.0         8671.104
    1.489045326D+04-2.922285939D+02 5.724527170D+00-8.176235030D-03 1.456903469D-05
   -1.087746302D-08 3.027941827D-12                -1.303131878D+04-7.859241350D+00
      1000.000   6000.0007 -2.0 -1.0  0.0  1.0  2.0  3.0  4.0  0.0         8671.104
    4.619197250D+05-1.944704863D+03 5.916714180D+00-5.664282830D-04 1.398814540D-07
   -1.787680361D-11 9.620935570D-16                -2.466261084D+03-1.387413108D+01
      6000.000  20000.0007 -2.0 -1.0  0.0  1.0  2.0  3.0  4.0  0.0         8671.104
    8.868662960D+08-7.500377840D+05 2.495474979D+02-3.956351100D-02 3.297772080D-06
   -1.318409933D-10 1.998937948D-15                 5.701421130D+06-2.060704786D+03
   CO2               Gurvich,1991 pt1 p27 pt2 p24.
    3 g 9/99 C   1.00O   2.00    0.00    0.00    0.00 0   44.0095000    -393510.000
       200.000   1000.0007 -2.0 -1.0  0.0  1.0  2.0  3.0  4.0  0.0         9365.469
    4.943650540D+04-6.264116010D+02 5.301725240D+00 2.503813816D-03-2.127308728D-07
   -7.689988780D-10 2.849677801D-13                -4.528198460D+04-7.048279440D+00
      1000.000   6000.0007 -2.0 -1.0  0.0  1.0  2.0  3.0  4.0  0.0         9365.469
    1.176962419D+05-1.788791477D+03 8.291523190D+00-9.223156780D-05 4.863676880D-09
   -1.891053312D-12 6.330036590D-16                -3.908350590D+04-2.652669281D+01
      6000.000  20000.0007 -2.0 -1.0  0.0  1.0  2.0  3.0  4.0  0.0         9365.469
   -1.544423287D+09 1.016847056D+06-2.561405230D+02 3.369401080D-02-2.181184337D-06
    6.991420840D-11-8.842351500D-16                -8.043214510D+06 2.254177493D+03
   END PRODUCTS
   END REACTANTS

This file (saved for example as ``nasathermo.dat``) can then be converted to the
CTI format using the ``ck2cti`` script:

.. code:: bash

   ck2cti --thermo=nasathermo.dat

To generate a full phase definition, create an input file defining the phase as
well, saved for example as ``nasa.inp``:

.. code::

   elements
   C O
   end

   species
   CO CO2
   end

The two input files can then be converted together by calling:

.. code:: bash

   ck2cti --input=nasa.inp --thermo=nasathermo.dat

Constant Heat Capacity
----------------------

Example:

.. code:: python

   thermo = const_cp(h0=(-393.51, 'kJ/mol'),
                     s0=(213.785, 'J/mol/K'),
                     cp0=(37.12, 'J/mol/K'))

Assuming that the :cti:func:`units` function has been used to set the default energy
units to Joules and the default quantity unit to kmol, this may be equivalently
written as:

.. code:: python

    thermo = const_cp(h0=-3.9351e8, s0=2.13785e5, cp0=3.712e4)


Species Transport Coefficients
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Transport property models in general require coefficients that express the
effect of each species on the transport properties of the phase. The
``transport`` field may be assigned an embedded entry that provides
species-specific coefficients.

Currently, the only entry type is :cti:class:`gas_transport`, which supplies
parameters needed by the ideal-gas transport property models. The field values
and their units of the :cti:class:`gas_transport` entry are compatible with the
transport database parameters described by Kee et al. [#Kee1986]_. Entries in
transport databases in the format described in their report can be used directly
in the fields of the :cti:class:`gas_transport` entry, without requiring any unit
conversion. The numeric field values should all be entered as pure numbers, with
no attached units string.

.. container:: container

   .. container:: row

      .. container:: col-4 text-left

         .. container:: btn btn-primary
            :tagname: a
            :attributes: href=phases.html
                         title="Phases and Interfaces"

            Previous: Phases and Interfaces

      .. container:: col-4 text-center

         .. container:: btn btn-primary
            :tagname: a
            :attributes: href=defining-phases.html
                         title="Defining Phases"

            Return: Defining Phases

      .. container:: col-4 text-right

         .. container:: btn btn-primary
            :tagname: a
            :attributes: href=reactions.html
                         title=Reactions

            Next: Reactions

.. rubric:: References

.. [#Kee1986] R. J. Kee, G. Dixon-Lewis, J. Warnatz, M. E. Coltrin, and J. A. Miller.
   A FORTRAN Computer Code Package for the Evaluation of Gas-Phase, Multicomponent
   Transport Properties. Technical Report SAND86-8246, Sandia National Laboratories, 1986.
