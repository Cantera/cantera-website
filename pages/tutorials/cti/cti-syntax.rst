.. slug: cti-syntax
.. title: CTI File Syntax

.. jumbotron::

   .. raw:: html

      <h1 class="display-3">CTI File Syntax</h1>

   .. class:: lead

      CTI is the legacy human-readable input format for Cantera, and we describe it's syntax here

      Note that the legacy CTI input file format will be deprecated in Cantera 2.6
      and fully replaced by the YAML input file format in Cantera 3.0.

Input File Syntax
=================

An input file consists of *entries* and *directives*, both of which have a
syntax much like functions. An entry defines an object---for example, a
reaction, or a species, or a phase. A directive sets options that affect how the
entry parameters are interpreted, such as the default unit system, or how
certain errors should be handled.

Cantera's input files follow the syntax rules for Python, so if you're familiar
with Python syntax you already understand many of the details and can probably
skip ahead to `Dimensional Values`_.

Entries have fields that can be assigned values. A species entry is shown below
that has fields ``name`` and ``atoms``:

.. code:: python

   species(name='C60', atoms='C:60')

Most entries have some fields that are required; these must be assigned values,
or else processing of the file will abort and an error message will be
printed. Other fields may be optional, and take default values if not assigned.

An entry may be either a *top-level entry* or an *embedded entry*. Top-level
entries specify a phase, an interface, an element, a species, or a reaction, and
begin in the first (leftmost) column. Embedded entries specify a model, or a
group of parameters for a top-level entry, and are usually embedded in a field
of another entry.

The fields of an entry are specified in the form ``<field_name>=<value>``, and may
be listed on one line, or extend across several. For example, two entries for
graphite are shown below. The first is compact:

.. code:: python

   stoichiometric_solid(name='graphite', species='C(gr)', elements='C', density=(2.2, 'g/cm3'))

and the second is formatted to be easier to read:

.. code:: python

   stoichiometric_solid(
        name='graphite',
        elements='C',
        species='C(gr)',
        density=(2.2, 'g/cm3'),
   )

Both are completely equivalent.

The species ``C(gr)`` that appears in the definition of the graphite phase is
also defined by a top-level entry. If the heat capacity of graphite is
approximated as constant, then the following definition could be used:

.. code:: python

   species(name='C(gr)',
           atoms='C:1',
           thermo=const_cp(t0=298.15,
                           h0=0.0,
                           s0=(5.6, 'J/mol/K'),  # NIST
                           cp0=(8.43, 'J/mol/K')))  # Taylor and Groot (1980)

Note that the thermo field is assigned an embedded entry of type
:cti:class:`const_cp`. Entries are stored as they are encountered when the file is
read, and only processed once the end of the file has been reached. Therefore,
the order in which they appear is unimportant.

Comments
--------

The character ``#`` is the comment character. Everything to the right of this
character on a line is ignored:

.. code:: python

   # set the default units
   units(length='cm',  # use centimeters for length
         quantity='mol')  # use moles for quantity

Strings
-------

Strings may be enclosed in single quotes or double quotes, but they must
match. To create a string containing single quotes, enclose it in double quotes,
and vice versa. If you want to create a string to extend over multiple lines,
enclose it in triple quotes:

.. code:: python

   string1 = 'A string.'
   string2 = "Also a 'string'"
   string3 = """This is
   a
   string too."""

The multi-line form is useful when specifying a phase containing a large number
of species:

.. code:: python

   species = """ H2 H O O2 OH H2O HO2 H2O2 C CH
                 CH2 CH2(S) CH3 CH4 CO CO2 HCO CH2O CH2OH CH3O
                 CH3OH C2H C2H2 C2H3 C2H4 C2H5 C2H6 HCCO CH2CO HCCOH
                 N NH NH2 NH3 NNH NO NO2 N2O HNO CN
                 HCN H2CN HCNN HCNO HOCN HNCO NCO N2 AR C3H7
                 C3H8 CH2CHO CH3CHO """

Sequences
---------

A sequence of multiple items is specified by separating the items by commas and
enclosing them in square brackets or parentheses. The individual items can have
any type—strings, integers, floating-point numbers (or even entries or other
lists). Square brackets are often preferred, since parentheses are also used for
other purposes in the input file, but in many cases either can be used:

.. code:: python

   s0 = (3.5, 'J/mol/K')
   s0 = [3.5, 'J/mol/K']

Variables
---------

Another way to specify the species ``C(gr)`` is shown here:

.. code:: python

   graphite_thermo = const_cp(t0=298.15,
                              h0=0.0,
                              s0=(5.6, 'J/mol/K'),  # NIST
                              cp0=(8.43, 'J/mol/K'))  # Taylor and Groot (1980)

   species(name='C(gr)', atoms='C:1', thermo=graphite_thermo)

In this form, the ``const_cp`` entry is stored in a variable, instead of being
directly embedded within the species entry. The ``thermo`` field is assigned this
variable.

Variables can also be used for any other parameter type. For example, if you are
defining several phases in the file, and you want to set them all to the same
initial pressure, you could define a pressure variable:

.. code:: python

   P_initial = (2.0, 'atm')

and then set the pressure field in each embedded state entry to this variable.

Omitting Field Names
--------------------

Field names may be omitted if the values are entered in the order specified in
the entry declaration. (Entry declarations are the text printed on a colored
background in the following chapters.) It is also possible to omit only some of
the field names, as long as these fields are listed first, in order, before any
named fields.

For example, the first four entries below are equivalent, while the last two are
incorrect and would generate an error when processed:

.. code:: python

   element(symbol="Ar", atomic_mass=39.948) # OK
   element(atomic_mass=39.948, symbol='Ar') # OK
   element('Ar', atomic_mass=39.948)        # OK
   element("Ar", 39.948)                    # OK

   element(39.948, "Ar")                    # error
   element(symbol="Ar", 39.948)             # error

Validation
----------

Normally, Cantera will make some checks for errors in the definitions of species
and reactions, such as checking for duplicate reactions. To slightly speed up
processing (if a mechanism has previously been validated), or in case of
spurious validation errors, validation can be disabled using the
:cti:func:`validate` function. For example, to disable validation of reactions, add
the following to the CTI file:

.. code:: python

   validate(reactions='no')

Dimensional Values
==================

Many fields have numerical values that represent dimensional quantities—a
pressure, or a density, for example. If these are entered without specifying the
units, the default units (set by the :cti:class:`units` directive described in
`Setting the Default Units`_) will be used. However, it is also possible to
specify the units for each individual dimensional quantity (unless stated
otherwise). All that is required is to group the value in parentheses or square
brackets with a string specifying the units:

.. code:: python

   pressure = 1.0e5  # default is Pascals
   pressure = (1.0, 'bar')  # this is equivalent
   density = (4.0, 'g/cm3')
   density = 4000.0  # kg/m3

Compound unit strings may be used, as long as a few rules are followed:

1. Units in the denominator follow ``/``.
2. Units in the numerator follow ``-``, except for the first one.
3. Numerical exponents follow the unit string without a ``^`` character, and must
   be in the range 2–6. Negative values are not allowed.

Examples of compound units:

.. code:: python

   A = (1.0e20, 'cm6/mol2/s')  # OK
   h = (6.626e-34, 'J-s')      # OK
   density = (3.0, 'g/cm3')    # OK
   A = (1.0e20, 'cm^6/mol/s')  # error (^)
   A = (1.0e20, 'cm6/mol2-s')  # error ('s' should be in denominator)
   density = (3.0, 'g-cm-3')   # error (negative exponent)

Setting the Default Units
-------------------------

The default unit system may be set with the :cti:func:`units` directive. Note
that unit conversions are not done until the entire file has been read. Only one
units directive should be present in a file, and the defaults it specifies apply
to the entire file. If the file does not contain a units directive, the default
units are meters, kilograms, kilomoles, and seconds.

Shown below are two equivalent ways of specifying the site density for an
interface. In the first version, the site density is specified without a units
string, and so its units are constructed from the default units for quantity and
length, which are set with a units directive:

.. code:: python

   units(length='cm', quantity='molec')
   interface(name='Si-100',
             site_density=1.0e15,  # molecules/cm2 (default units)
             # ...
             )

The second version uses a different default unit system, but overrides the
default units by specifying an explicit units string for the site density:

.. code:: python

   units(length='cm', quantity='mol')
   interface(name='Si-100',
             site_density=(1.0e15, 'molec/cm2') # override default units
             # ...
             )

The second version is equivalent to the first, but would be very different if
the units of the site density were not specified!

The ``length``, ``quantity`` and ``time`` units are used to construct the units for
reaction pre-exponential factors. The ``energy`` units are used for molar
thermodynamic properties, in combination with the units for ``quantity``.

Since activation energies are often specified in units other than those used for
thermodynamic properties, a separate field is devoted to the default units for
activation energies:

.. code:: python

   units(length='cm', quantity='mol', act_energy='kcal/mol')
   kf = Arrhenius(A=1.0e14, b=0.0, E=54.0)  # E is 54 kcal/mol

See :cti:func:`units` for the declaration of the units directive.

Recognized Units
----------------

Cantera recognizes the following units in various contexts:

===========  ==============
field        allowed values
===========  ==============
length       ``'cm', 'm', 'mm'``
quantity     ``'mol', 'kmol', 'molec'``
time         ``'s', 'min', 'hr', 'ms'``
energy       ``'J', 'kJ', 'cal', 'kcal'``
act_energy   ``'kJ/mol', 'J/mol', 'J/kmol', 'kcal/mol', 'cal/mol', 'eV', 'K'``
pressure     ``'Pa', 'atm', 'bar'``
===========  ==============

.. container:: container

   .. container:: row

      .. container:: col-4 text-left

         .. container:: btn btn-primary
            :tagname: a
            :attributes: href=cti-processing.html
                         title="Processing CTI Files"

            Previous: Processing CTI Files

      .. container:: col-4 text-center

         .. container:: btn btn-primary
            :tagname: a
            :attributes: href=defining-phases-cti.html
                         title="Defining Phases"

            Return: Defining Phases

      .. container:: col-4 text-right

         .. container:: btn btn-primary
            :tagname: a
            :attributes: href={{% ct_docs sphinx/html/cti/classes.html %}}
                         title="CTI Class Reference"

            Next: CTI Class Reference
