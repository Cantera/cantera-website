.. slug: phases
.. title: Phases and their Interfaces

.. jumbotron::

   .. raw:: html

      <h1 class="display-3">Phases and their Interfaces</h1>

   .. class:: lead

      A description of how phases and interfaces are defined in YAML input files

Phases
======

For each phase that appears in a problem, a corresponding entry should be
present in the input file(s). The phase entry specifies the elements and species
present in the phases, and the models to be used for computing thermodynamic,
kinetic, and transport properties.

Naming the Phase
----------------

The ``name`` entry is a string that identifies the phase. It must be unique
within the file among all phase definitions of any type. Phases are referenced
by name when importing them. The ``name`` is also used to identify the phase
within multiphase mixtures or at phase boundaries.

Setting the Thermodynamic Model
-------------------------------

The thermodynamic model used to represent a phase is specified in the ``thermo``
field. Supported models are:

- :ref:`binary-solution-tabulated <sec-yaml-binary-solution-tabulated>`: A
  binary mixture where the excess enthalpy and entropy are interpolated; *New in
  Cantera 2.5.0* between tabulated values as a function of mole fraction
- :ref:`compound-lattice <sec-yaml-compound-lattice>`: A phase that is comprised
  of a fixed additive combination of other lattice phases
- :ref:`constant-density <sec-yaml-constant-density>`: A phase with a fixed
  density, regardless of composition; *Deprecated in Cantera 2.5.0*
- :ref:`Debye-Huckel <sec-yaml-Debye-Huckel>`: A dilute liquid electrolyte which
  obeys the Debye-Hückel formulation for nonideality
- :ref:`edge <sec-yaml-edge>`: A one-dimensional edge between two surfaces
- :ref:`fixed-chemical-potential <sec-yaml-fixed-chemical-potential>`: An
  incompressible, single-species phase with a fixed value for the chemical
  potential
- :ref:`fixed-stoichiometry <sec-yaml-fixed-stoichiometry>`: An incompressible,
  single-species phase
- :ref:`HMW-electrolyte <sec-yaml-HMW-electrolyte>`: A dilute or concentrated
  liquid electrolyte which obeys the Pitzer formulation for nonideality
- :ref:`ideal-gas <sec-yaml-ideal-gas>`: A mixture which obeys the ideal gas law
- :ref:`ideal-gas-VPSS <sec-yaml-ideal-gas-VPSS>`: An ideal gas; Uses "variable
  pressure standard state" methods for calculating thermodynamic properties
- :ref:`ideal-molal-solution <sec-yaml-ideal-molal-solution>`: An ideal solution
  based on the mixing-rule assumption that all molality-based activity
  coefficients are equal to one
- :ref:`ideal-condensed <sec-yaml-ideal-condensed>`
- :ref:`ideal-solution-VPSS <sec-yaml-ideal-solution-VPSS>`: An ideal solution;
  Uses "variable pressure standard state" methods for calculating thermodynamic
  properties
- :ref:`ideal-surface <sec-yaml-ideal-surface>`: A surface between two bulk
  phases
- :ref:`ions-from-neutral-molecule <sec-yaml-ions-from-neutral-molecule>`: A
  phase for representing ionic species based on another phase where those ions
  are components of neutral molecules
- :ref:`lattice <sec-yaml-lattice>`: A simple model for an incompressible
  lattice of solid atoms
- :ref:`liquid-water-IAPWS95 <sec-yaml-liquid-water-IAPWS95>`: An implementation
  of the IAPWS95 equation of state for water, for the liquid region only
- :ref:`Margules <sec-yaml-Margules>`: A model that employs the Margules
  approximation for the excess Gibbs free energy
- :ref:`Maskell-solid-solution <sec-yaml-Maskell-solid-solution>`: A condensed,
  binary, non-ideal solution
- :ref:`electron-cloud <sec-yaml-electron-cloud>`: A phase representing free
  electrons in a metal
- :ref:`pure-fluid <sec-yaml-pure-fluid>`: A phase representing one of several
  pure substances including liquid, vapor, two-phase, and supercritical regions
- :ref:`Redlich-Kister <sec-yaml-Redlich-Kister>`: A model that employs the
  Redlich-Kister approximation for the excess Gibbs free energy
- :ref:`Redlich-Kwong <sec-yaml-Redlich-Kwong>`: A multi-species mixture obeying
  the Redlich-Kwong equation of state.

Some thermodynamic models use additional fields in the ``phase`` entry, which
are described in the linked documentation.

Declaring the Elements
----------------------

In most cases, it is not necessary to specify the elements present in a phase.
If no ``elements`` field is present, elements will be added automatically using
the definitions of the standard chemical elements based on the composition of
the species present in the phase.

If non-standard elements such as isotopes need to be represented, or the
ordering of elements within the phase is important, the elements in the phase
may be declared in the optional ``elements`` entry.

If all of the elements to be added are either standard chemical elements or
defined in the :ref:`elements <sec-yaml-guide-elements>` section of the current
input file, the elements can be specified as a list of element symbols, e.g.:

.. code:: yaml

    elements: [H, C, O, Ar]

To add elements from other top-level sections, from a different file, or from
multiple such sources, a list of single-key mappings can be used
where the key of each mapping specifies the source and the value is a list of
element names. The keys can be:

- The name of a section within the current file.
- The name of an input file and a section in that file, separated by a slash,
  e.g. ``myfile.yaml/my_elements``. If a relative path is specified, the
  directory containing the current file is searched first, followed by the
  Cantera data path.
- The name ``default`` to reference the standard chemical elements.

Example:

.. code:: yaml

    elements:
    - default: [C, H, Ar]
    - isotopes: [O18]
    - myelements.yaml/uranium: [U235, U238]

The order of the elements specified in the input file determines the order of
the elements in the phase when it is imported by Cantera.

Declaring the Species
---------------------

If the species present in the phase corresponds to those species defined in the
``species`` section of the input file, the ``species`` field may be omitted, and
those species will be added to the phase automatically. As a more explicit
alternative, the ``species`` field may be set to the string ``all``.

To include specific species from the ``species`` section of the input file, the
``species`` entry can be a list of species names from that section, e.g.:

.. code:: yaml

    species: [H2, O2, H2O]

If species are defined in multiple input file sections, the ``species`` entry
can be a list of single-key mappings, where the key of each mapping specifies
the source and the value is either the string ``all`` or a list of species
names. Each key can be either the name of a section within the current input
file or the name of a different file and a section in that file, separated by a
slash. If a relative path is specified, the directory containing the current
file is searched first, followed by the Cantera data path. Example:

.. code:: yaml

    species:
    - species: [O2, N2]
    - more_species: all
    - subdir/myfile.yaml/species: [NO2, N2O]

The order of species specified in the input file determines the order of the
species in the phase when it is imported by Cantera.

Species containing elements that are not declared within the phase may be
skipped by setting the ``skip-undeclared-elements`` field to ``true``. For
example, to add all species from the ``species`` section that contain only
hydrogen or oxygen, the phase definition could contain:

.. code:: yaml

    phases:
    - name: hydrogen-and-oxygen
      elements: [H, O]
      species: all
      skip-undeclared-elements: true

Setting the Kinetics Model
--------------------------

The kinetics model to be used, if any, is specified in the ``kinetics`` field.
Supported model strings are:

- `gas <{{% ct_docs doxygen/html/de/dae/classCantera_1_1GasKinetics.html#details %}}>`__
- `surface <{{% ct_docs doxygen/html/d1/d72/classCantera_1_1InterfaceKinetics.html#details %}}>`__
- `edge <{{% ct_docs doxygen/html/d0/df0/classCantera_1_1EdgeKinetics.html#details %}}>`__

If omitted, no kinetics model will be used.

Declaring the Reactions
-----------------------

If a kinetics model has been specified, reactions may be added to the phase. By
default, all reactions from the ``reactions`` section of the input file will be
added. Equivalently, the ``reactions`` entry may be specified as the string
``all``.

To disable automatic addition of reactions from the ``reactions`` section, the
``reactions`` entry may be set to ``none``. This may be useful if reactions will
be added programmatically after the phase is constructed. The ``reactions``
field must be set to ``none`` if a kinetics model has been specified but there
is no ``reactions`` section in the input file.

To include only those reactions from the ``reactions`` section where all of the
species involved are declared as being in the phase, the ``reactions`` entry
can be set to the string ``declared-species``.

To include reactions from multiple sections or other files, the ``reactions``
entry can be given as a list of section names, for example:

.. code:: yaml

    reactions:
    - OH_submechanism
    - otherfile.yaml/C1-reactions
    - otherfile.yaml/C2-reactions

To include reactions from multiple sections or other files while only including
reactions involving declared species, a list of single-key mappings can be used,
where the key is the section name (or file and section name) and the value is
either the string ``all`` or the string ``declared-species``. For example:

.. code:: yaml

    reactions:
    - OH_submechanism: all
    - otherfile.yaml/C1-reactions: all
    - otherfile.yaml/C2-reactions: declared-species

To permit reactions containing third-body efficiencies for species not present
in the phase, the additional field ``skip-undeclared-third-bodies`` may be added
to the phase entry with the value ``true``.

Setting the Transport Model
---------------------------

To enable transport property calculation, the transport model to be used can be
specified in the ``transport`` field. Supported models are:

- `high-pressure <{{% ct_docs doxygen/html/d9/d63/classCantera_1_1HighPressureGasTransport.html#details %}}>`__:
  A model for high-pressure gas transport properties based on a method of
  corresponding states
- `ionized-gas <{{% ct_docs doxygen/html/d4/d65/classCantera_1_1IonGasTransport.html#details %}}>`__:
  A model implementing the Stockmayer-(n,6,4) model for transport of ions in
  a gas
- `mixture-averaged <{{% ct_docs doxygen/html/d9/d17/classCantera_1_1MixTransport.html#details %}}>`__:
  The mixture-averaged transport model for ideal gases
- `mixture-averaged-CK <{{% ct_docs doxygen/html/d9/d17/classCantera_1_1MixTransport.html#details %}}>`__:
  The mixture-averaged transport model for ideal gases, using polynomial
  fits corresponding to Chemkin-II
- `multicomponent <{{% ct_docs doxygen/html/df/d7c/classCantera_1_1MultiTransport.html#details %}}>`__:
  The multicomponent transport model for ideal gases
- `multicomponent-CK <{{% ct_docs doxygen/html/df/d7c/classCantera_1_1MultiTransport.html#details %}}>`__:
  The multicomponent transport model for ideal gases, using polynomial fits
  corresponding to Chemkin-II
- `unity-Lewis-number <{{% ct_docs doxygen/html/d3/dd6/classCantera_1_1UnityLewisTransport.html#details %}}>`__:
  A transport model for ideal gases, where diffusion coefficients for all
  species are set so that the Lewis number is 1
- `water <{{% ct_docs doxygen/html/df/d1f/classCantera_1_1WaterTransport.html#details %}}>`__:
  A transport model for pure water applicable in both liquid and vapor phases

Setting the Initial State
-------------------------

The state of a phase can be set using two properties to set the thermodynamic
state, plus the composition. This state is specified as a mapping in the
``state`` field of ``phase`` entry.

The thermodynamic state can be set in terms of two of the following properties,
with the valid property pairs deplending on the phase model:

- ``temperature`` or ``T``
- ``pressure`` or ``P``
- ``enthalpy`` or ``H``
- ``entropy`` or ``S``
- ``int-energy``, ``internal-energy`` or ``U``
- ``specific-volume`` or ``V``
- ``density`` or ``D``
- ``vapor-fraction`` or ``Q``

The composition can be set using one of the following fields, depending on the
phase type. The composition is specified as a mapping of species names to
values. Where necessary, the values will be automatically normalized.

- ``mass-fractions`` or ``Y``
- ``mole-fractions`` or ``X``
- ``coverages``
- ``molalities`` or ``M``

Examples:

.. code:: yaml

    state:
      T: 300 K
      P: 101325 Pa
      X: {O2: 1.0, N2: 3.76}

    state:
      density: 100 kg/m^3
      T: 298
      Y:
        CH4: 0.2
        C3H8: 0.1
        CO2: 0.7

For pure fluid phases, the temperature, pressure, and vapor fraction may all be
specified if and only if they define a consistent state.

Examples
--------

The following input file defines two equivalent gas phases including all
reactions and species defined in the input file, (with species and reaction data
elided). In the second case, the phase definition is simplified by having the
elements added based on the species definitions, taking the species definitions
from the default `species` section, and reactions from the default `reactions`
section.

.. code:: yaml

    phases:
    - name: gas1
      thermo: ideal-gas
      elements: [O, H, N, Ar]
      species: [H2, H, O, O2, OH, H2O, HO2, H2O2, N2, AR]
      kinetics: gas
      reactions: all
      transport: mixture-averaged
      state:
        T: 300.0
        P: 1.01325e+05
    - name: gas2
      thermo: ideal-gas
      kinetics: gas
      transport: mixture-averaged
      state: {T: 300.0, 1 atm}

    species:
    - H2: ...
    - H: ...
    ...
    - AR: ...

    reactions:
    ...

An input file defining an interface and its adjacent bulk phases, with full
species data elided:

.. code:: yaml

    phases:
    - name: graphite
      thermo: lattice
      species:
      - graphite-species: all
      state: {T: 300, P: 101325, X: {C6: 1.0, LiC6: 1e-5}}
      density: 2.26 g/cm^3

    - name: electrolyte
      thermo: lattice
      species: [{electrolyte-species: all}]
      density: 1208.2 kg/m^3
      state:
        T: 300
        P: 101325
        X: {Li+(e): 0.08, PF6-(e): 0.08, EC(e): 0.28, EMC(e): 0.56}

    - name: anode-surface
      thermo: ideal-surface
      kinetics: surface
      reactions: [graphite-anode-reactions]
      species: [{anode-species: all}]
      site-density: 1.0 mol/cm^2
      state: {T: 300, P: 101325}

    graphite-species:
    - name: C6
      ...
    - name: LiC6
      ...

    electrolyte-species:
    - name: Li+(e)
      ...
    - name: PF6-(e)
      ...
    - name: EC(e)
      ...
    - name: EMC(e)
      ...

    anode-species:
    - name: (int)
      ...

    graphite-anode-reactions:
    - equation: LiC6 <=> Li+(e) + C6
      rate-constant: [5.74, 0.0, 0.0]
      beta: 0.4


.. container:: container

   .. container:: row

      .. container:: col-4 text-center offset-4

         .. container:: btn btn-primary
            :tagname: a
            :attributes: href=defining-phases.html

            Return: Defining Phases

      .. container:: col-4 text-right

         .. container:: btn btn-primary
            :tagname: a
            :attributes: href=yaml-species.html

            Next: Elements and Species
