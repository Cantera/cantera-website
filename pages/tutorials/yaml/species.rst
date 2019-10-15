.. slug: yaml-species
.. title: Elements and Species
.. has_math: true

.. jumbotron::

   .. raw:: html

      <h1 class="display-3">Elements and Species</h1>

   .. class:: lead

      A description of how elements and species are defined in YAML input files

.. _sec-yaml-elements:

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

- ``symbol``: The symbol to be used for the element, e.g. when specifying the
  composition of a species.
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

.. _sec-yaml-species:

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

    - `NASA7 <{{% yaml_dev species sec-yaml-nasa7 %}}>`__
    - `NASA9 <{{% yaml_dev species nasa-9-coefficient-polynomials %}}>`__
    - `Shomate <{{% yaml_dev species shomate-polynomials %}}>`__
    - `constant-cp <{{% yaml_dev species constant-heat-capacity %}}>`__
    - `piecewise-Gibbs <{{% yaml_dev species piecewise-gibbs %}}>`__

The fields used by each model are described and examples provided in the linked
documentation.

Species Equation of State
-------------------------

For some phase thermodynamic models, additional equation of state
parameterizations are needed for each species. This information is provided in
the ``equation-of-state`` field of each ``species`` entry, with the type of
parameterization used specified by the ``model`` field of the
``equation-of-state`` field. The models available are:

    - `constant-volume <{{% yaml_dev species sec-yaml-eos-constant-volume %}}>`__
    - `density-temperature-polynomial <{{% yaml_dev species density-temperature-polynomial %}}>`__
    - `HKFT <{{% yaml_dev species hkft %}}>`__
    - `ideal-gas <{{% yaml_dev species sec-yaml-eos-ideal-gas %}}>`__
    - `ions-from-neutral-molecule <{{% yaml_dev species ions-from-neutral-molecule %}}>`__
    - `liquid-water-IAPWS95 <{{% yaml_dev species liquid-water-iapws95 %}}>`__
    - `molar-volume-temperature-polynomial <{{% yaml_dev species piecewise-gibbs %}}>`__
    - `Redlich-Kwong <{{% yaml_dev species redlich-kwong %}}>`__

The fields used by each model are described and examples provided in the linked
documentation.

.. _sec-yaml-species-transport:

Species Transport Coefficients
------------------------------

Transport-related parameters for each species are needed in order to calculate
transport properties of a phase. These parameters are provided in the
``transport`` field of each ``species`` entry, with the type of the
parameterization used specified by the ``model`` field of the ``transport``
field. The only model type specifically handled is ``gas``. The parameters used
depend on the transport model specified at the phase level. The full set of
possible parameters is described in the `API documentation
<{{% yaml_dev species gas-transport %}}>`__.

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
