.. slug: yaml-species
.. title: Elements and Species
.. has_math: true

.. jumbotron::

   .. raw:: html

      <h1 class="display-3">Elements and Species</h1>

   .. class:: lead

      A description of how elements and species are defined in YAML input files

.. _sec-yaml-guide-elements:

Elements
========

Cantera provides built-in definitions for the chemical elements, including
values for their atomic weights taken from IUPAC / CIAAW. These elements can be
used by speciying the corresponding atomic symbols when specifying the
composition of species.

In order to give a name to a particular isotope or a virtual element
representing a surface site, a custom ``element`` entry can be used. The default
location for ``element`` entries is the ``elements`` section of the input file.
Elements defined in this section will automatically be considered for addition
to phases defined in the same file. Elements can be defined in other sections of
the input file if those sections are named explicitly in the ``elements`` field
of the phase definition.

An element entry has the following fields:

- ``symbol``: The symbol to be used for the element, for example when specifying
  the composition of a species.
- ``atomic-weight``: The atomic weight of the element, in unified atomic mass
  units (dalton)
- ``atomic-number``: The atomic number of the element. Optional.
- ``entropy298``: The standard molar entropy of the element at 298.15 K. Optional.

An example ``elements`` section:

.. code:: yaml

    elements:
    - symbol: C13
      atomic-weight: 13.003354826
      atomic-number: 12
    - symbol: O-18
      atomic-weight: 17.9991603

.. _sec-yaml-guide-species:

Species
=======

A species entry in Cantera is used to specify the name, composition,
thermodynamic, and transport properties of an individual species.

The default location for species entries is in the ``species`` section of the
input file. Species defined in this section will automatically be considered for
addition to phases defined in the same file. Species can be defined in other
sections of the input file (or in other input files), and these species
definitions can be used in phase definitions by explicitly referencing the
section name.

Species Name
------------

The name of a species is given in ``name`` field of a ``species`` entry. Names
may include almost all printable characters, with the exception of spaces. The
use of some characters such as ``[``, ``]``, and ``,`` may require that species
names be enclosed in quotes when written in YAML. Some valid species names given
in a YAML list include:

.. code:: yaml

    [CH4, methane, argon_2+, "C[CH2]", CH2(singlet), "H2O,l"]

Elemental Composition
---------------------

The elemental composition of a species is specified as a mapping in the
``composition`` entry.

For gaseous species, the elemental composition is well-defined, since the
species represent distinct molecules. For species in solid or liquid solutions,
or on surfaces, there may be several possible ways of defining the species. For
example, an aqueous species might be defined with or without including the water
molecules in the solvation cage surrounding it.

For surface species, it is possible for the ``composition`` mapping to be empty,
in which case the species is composed of nothing, and represents an empty
surface site. This can also be done to represent vacancies in solids. A charged
vacancy can be defined to be composed solely of electrons.

The number of atoms of an element must be non-negative, except for the special
"element" ``E`` that represents an electron.

Examples:

.. code:: yaml

    composition: {C: 1, O: 2}  # carbon dioxide
    composition: {Ar: 1, E: -2}  # Ar++
    composition: {Y: 1, Ba: 2, Cu: 3, O: 6.5}  # stoichiometric YBCO
    composition: {}  # A surface species representing an empty site

Thermodynamic Properties
------------------------

In addition to the thermodynamic model used at the phase level for computing
properties, parameterizations are usually required for the enthalpy, entropy,
and specific heat capacities of individual species under standard conditions.
These parameterizations are provided in the ``thermo`` field of each ``species``
entry.

The parameterization used to provide this information is specified by the
``model`` field of the ``thermo`` field. The models available are:

- :ref:`NASA7 <sec-yaml-nasa7>`: 7-coefficient NASA polynomials in one or two
  temperature regions
- :ref:`NASA9 <sec-yaml-nasa9>`: 9-coefficient NASA polynomials in one or more
  temperature regions
- :ref:`Shomate <sec-yaml-shomate>`: Shomate polynomials in one or two
  temperature regions
- :ref:`constant-cp <sec-yaml-constcp>`: Constant heat capacity
- :ref:`piecewise-Gibbs <sec-yaml-piecewise-gibbs>`: Interpolation between
  tabulated Gibbs free energies using a constant heat capacity in each
  temperature interval

The fields used by each model are described and examples provided in the linked
documentation.

Species Equation of State
-------------------------

For some phase thermodynamic models, additional equation of state
parameterizations are needed for each species. This information is provided in
the ``equation-of-state`` field of each ``species`` entry, with the type of
parameterization used specified by the ``model`` field of the
``equation-of-state`` field. The models available are:

- :ref:`constant-volume <sec-yaml-eos-constant-volume>`: A fixed value of mass
  density, molar density, or molar volume
- :ref:`density-temperature-polynomial <sec-yaml-eos-density-temperature-polynomial>`:
  Mass density parameterized using a cubic polynomial in temperature
- :ref:`HKFT <sec-yaml-eos-hkft>`: The Helgeson-Kirkham-Flowers-Tanger model for
  aqueous species
- :ref:`ideal-gas <sec-yaml-eos-ideal-gas>`: A species following the ideal gas
  law
- :ref:`ions-from-neutral-molecule <sec-yaml-eos-ions-from-neutral>`: Used with
  the `ions-from-neutral-molecule` phase model
- :ref:`liquid-water-IAPWS95 <sec-yaml-eos-liquid-water-iapws95>`: The IAPWS95
  equation of state for water, applied only in the liquid region
- :ref:`molar-volume-temperature-polynomial <sec-yaml-eos-molar-volume-temperature-polynomial>`:
  Molar volume parameterized using a cubic polynomial in temperature
- :ref:`Redlich-Kwong <sec-yaml-eos-redlich-kwong>`:
  A species which follows the Redlich-Kwong equation of state

The fields used by each model are described and examples provided in the linked
documentation.

.. _sec-yaml-guide-species-transport:

Species Transport Coefficients
------------------------------

Transport-related parameters for each species are needed in order to calculate
transport properties of a phase. These parameters are provided in the
``transport`` field of each ``species`` entry, with the type of the
parameterization used specified by the ``model`` field of the ``transport``
field. The only model type specifically handled is ``gas``. The parameters used
depend on the transport model specified at the phase level. The full set of
possible parameters is described in the :ref:`API documentation
<sec-yaml-species-transport>`.

An example of a ``transport`` entry:

.. code:: yaml

    transport:
      model: gas
      geometry: linear
      well-depth: 107.4
      diameter: 3.458
      polarizability: 1.6
      rotational-relaxation: 3.8


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
