.. slug: species
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

.. [#Mcbride2002] B. J. McBride, M. J. Zehe, S. Gordon. "NASA Glenn Coefficients
   for Calculating Thermodynamic Properties of Individual Species,"
   NASA/TP-2002-211556, Sept. 2002.
