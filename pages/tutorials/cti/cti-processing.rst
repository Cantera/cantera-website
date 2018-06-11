.. slug: cti-processing


Processing Input Files
======================

A Two-step Process
------------------

From the point of view of the user, it appears that a Cantera application that
imports a phase definition reads the input file, and uses the information there
to construct the object representing the phase or interface in the
application. While this is the net effect, it is actually a two-step
process. When a constructor like ``Solution`` is called to import a phase definition
from a file, a preprocessor runs automatically to read the input file and create
a string that contains the same information but in an XML-based format called
CTML. After the preprocessor finishes, Cantera imports the phase definition from
this CTML data.

Two File Formats
----------------

Why two file formats? There are several reasons. XML is a widely-used standard
for data files, and it is designed to be relatively easy to parse. This makes it
possible for other applications to use Cantera CTML data files, without
requiring the substantial chemical knowledge that would be required to use .cti
files. For example, "web services" (small applications that run remotely over a
network) are often designed to accept XML input data over the network, perform a
calculation, and send the output in XML back across the network. Supporting an
XML-based data file format facilitates using Cantera in web services or other
network computing applications.

The difference between the high-level description in a .cti input file and the
lower-level description in the CTML file may be illustrated by how reactions are
handled. In the input file, the reaction stoichiometry and its reversibility or
irreversibility are determined from the reaction equation. For example:

.. code:: python

  O + HCCO <=> H + 2 CO

specifies a reversible reaction between an oxygen atom and the ketenyl radical
HCCO to produce one hydrogen atom and two carbon monoxide molecules. If ``<=>``
were replaced with ``=>``, then it would specify that the reaction should be
treated as irreversible.

Of course, this convention is not spelled out in the input file---the parser
simply has to know it, and has to also know that a "reactant" appears on the
left side of the equation, a "product" on the right, that the optional number in
front of a species name is its stoichiometric coefficient (but if missing the
value is one), etc. The preprocessor does know all this, but we cannot expect
the same level of knowledge of chemical conventions by a generic XML parser.

Therefore, in the CTML file, reactions are explicitly specified to be reversible
or irreversible, and the reactants and products are explicitly listed with their
stoichiometric coefficients. The XML file is, in a sense, a "dumbed-down"
version of the input file, spelling out explicitly things that are only implied
in the input file syntax, so that "dumb" (i.e., easy to write) parsers can be
used to read the data with minimal risk of misinterpretation.

The reaction definition::

    reaction( "O + HCCO <=> H + 2 CO", [1.00000E+14, 0, 0])

in the input file is translated by the preprocessor to the following CTML text:

.. code-block:: xml

    <reaction id="0028" reversible="yes">
      <equation>O + HCCO [=] H + 2 CO</equation>
      <rateCoeff>
        <Arrhenius>
          <A units="cm3/mol/s"> 1.000000E+14</A>
          <b>0</b>
          <E units="cal/mol">0.000000</E>
        </Arrhenius>
      </rateCoeff>
      <reactants>HCCO:1 O:1</reactants>
      <products>H:1 CO:2</products>
    </reaction>

The CTML version is much more verbose, and would be much more tedious to write
by hand, but is much easier to parse, particularly since it is not necessary to
write a custom parser---virtually any standard XML parser, of which there are
many, can be used to read the CTML data.

So in general files that are easy for knowledgeable users (you) to write are more
difficult for machines to parse, because they make use of high-level
application-specific knowledge and conventions to simplify the
notation. Conversely, files that are designed to be easily parsed are tedious to
write because so much has to be spelled out explicitly. A natural solution is to
use two formats, one designed for writing by humans, the other for reading by
machines, and provide a preprocessor to convert the human-friendly format to the
machine-friendly one.

Preprocessor Internals: the ``ctml_writer`` Module
--------------------------------------------------

If you are interested in seeing the internals of how the preprocessing works,
take a look at file ``ctml_writer.py`` in the Cantera Python package. Or simply
start Python, and type::

    >>> import cantera.ctml_writer
    >>> help(cantera.ctml_writer)

The ``ctml_writer.py`` module can also be run as a script to convert input .cti
files to CTML. For example, if you have an input file ``phasedefs.cti``, then
simply type at the command line::

    python -m cantera.ctml_writer phasedefs.cti

to create CTML file ``phasedefs.xml``. On systems which support running Python
scripts directly, a script to run ``ctml_writer`` directly is also installed. If
the Cantera ``bin`` directory is on your ``PATH``, you can also do the
conversion by running::

    ctml_writer phasedefs.cti

This can be used to generate XML input files for use on systems where the
Cantera Python package is not installed. Of course, most of the time creation of
the CTML file will happen behind the scenes, and you will not need to be
concerned with CTML files at all.

Error Handling
==============

During processing of an input file, errors may be encountered. These could be
syntax errors, or could be ones that are flagged as errors by Cantera due to
some apparent inconsistency in the data---an unphysical value, a species that
contains an undeclared element, a reaction that contains an undeclared species,
missing species or element definitions, multiple definitions of elements,
species, or reactions, and so on.

Syntax Errors
-------------

Syntax errors are caught by the Python preprocessor, not by Cantera, and must be
corrected before proceeding further.  Python prints a "traceback" that allows
you to find the line that contains the error. For example, consider the
following input file, which is intended to create a gas with the species and
reactions of GRI-Mech 3.0, but has a misspelled the field name ``reactions``::

    ideal_gas(name = 'gas',
              elements = 'H O',
              species = 'gri30: all',
              reactionss = 'gri30: all')

When this definition is imported into an application, an error message like the
following would be printed to the screen, and execution of the program or script
would terminate. ::

    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "/some/path/Cantera/importFromFile.py", line 18, in importPhase
        return importPhases(file, [name], loglevel, debug)[0]
      File "/some/path/Cantera/importFromFile.py", line 25, in importPhases
        s.append(solution.Solution(src=file,id=nm,loglevel=loglevel,debug=debug))
      File "/some/path/solution.py", line 39, in __init__
        preprocess = 1, debug = debug)
      File "/some/path/Cantera/XML.py", line 35, in __init__
        self._xml_id = _cantera.xml_get_XML_File(src, debug)
    cantera.error:

    ************************************************
                    Cantera Error!
    ************************************************

    Procedure: ct2ctml
    Error:   Error converting input file "./gas.cti" to CTML.
    Python command was: '/usr/bin/python'
    The exit code was: 4
    -------------- start of converter log --------------
    TypeError on line 4 of './gas.cti':
    __init__() got an unexpected keyword argument 'reactionss'

    | Line |
    |    1 | ideal_gas(name = 'gas',
    |    2 |           elements = 'H O',
    |    3 |           species = 'gri30: all',
    >    4 >           reactionss = 'gri30: all')
    |    5 |
    --------------- end of converter log ---------------

The top part of the error message shows the chain of functions that were called
before the error was encountered. For the most part, these are internal Cantera
functions not of direct concern here. The relevant part of this error message is
the part starting with the "Cantera Error" heading, and specifically the
contents of the *converter log* section. This message says that that on line 4
of ``gas.cti``, the the keyword argument ``reactionss`` was not
recognized. Seeing this message, it is clear that the problem is that
*reactions* is misspelled.

Cantera Errors
--------------

Now let's consider the other class of errors---ones that Cantera, not Python,
detects. Continuing the example above, suppose that the misspelling is
corrected, and the input file processed again. Again an error message results,
but this time it is from Cantera::

    cantera.error:
    Procedure: installSpecies
    Error: species C contains undeclared element C

The problem is that the phase definition specifies that all species are to be
imported from dataset gri30, but only the elements H and O are declared. The
gri30 datset contains species composed of the elements H, O, C, N, and Ar. If
the definition is modified to declare these additional elements::

    ideal_gas(name = 'gas',
              elements = 'H O C N Ar',
              species = 'gri30: all',
              reactions = 'gri30: all')

it may be imported successfully.

Errors of this type do not have to be fatal, as long as you tell Cantera how you
want to handle them. You can, for example, instruct Cantera to quietly skip
importing any species that contain undeclared elements, instead of flagging them
as errors. You can also specify that reactions containing undeclared species
(also usually an error) should be skipped. This allows you to very easily
extract a portion of a large reaction mechanism, as described in :ref:`sec-phase-options`.

.. _sec-ck-format-conversion:

Converting CK-format files
==========================

Many existing reaction mechanism files are in "CK format," by which we mean
the input file format developed for use with the Chemkin-II software package
as specified in the report describing the Chemkin software [SAND89]_.

Cantera comes with a converter utility program ``ck2cti`` (or ``ck2cti.py``)
that converts CK format into Cantera format. This program should be run from
the command line first to convert any CK files you plan to use into Cantera
format (CTI format).

Usage::

    ck2cti [--input=<filename>]
           [--thermo=<filename>]
           [--transport=<filename>]
           [--surface=<filename>]
           [--id=<phase-id>]
           [--output=<filename>]
           [--permissive]
           [-d | --debug]

Each of the terms in square brackets is an option that can be passed on the
command line to ``ck2cti``. ``--input`` is the chemistry input file, containing
a list of all the element names that are used, a list of all the species names,
and a list of all the reactions to be considered between the species. This file
can also optionally contain thermodynamic information for the species. If the
``--input`` file does not contain the thermodynamic data, a separate file
containing this information must be specified to the `--thermo`` option. Finally,
the ``--input`` file can also optionally contain transport information for the
species. If it does not, and the user wishes to use a part of Cantera that relies
on some transport properties, the ``--transport`` option must be used to specify
the file containing all the transport data for the species.

For the case of a surface mechanism, the gas phase input file should be
specified as ``--input`` and the surface phase input file should be specified as
``--surface``.

Example::

    ck2cti --input=chem.inp --thermo=therm.dat --transport=tran.dat

If the output file name is not given, an output file with the same name as the
input file, with the extension changed to '.cti'.

If the ck2cti script is not on your path but the Cantera Python module is,
ck2cti can also be used by running::

    python -m cantera.ck2cti --input=chem.inp --thermo=therm.dat --transport=tran.dat

An input file containing only species definitions (which can be referenced from
phase definitions in other input files) can be created by specifying only a
thermo file.

Many existing CK format files cause errors in ``ck2cti`` when they are
processed. Some of these errors may be avoided by specifying the
``--permissive`` option. This option allows certain recoverable parsing errors
(e.g. duplicate transport or thermodynamic data) to be ignored. Other errors
may be caused by incorrect formatting of lines in one or more of the input files.

Debugging common errors in CK files
-----------------------------------

When ``ck2cti`` encounters an error, it attempts to print the surrounding
information to help you to locate the error. Many of the most common errors
are due to an inconsistency of the input files from their standard, as defined
in the report for Chemkin referenced above. These errors include:

  * Each section of the input files must be started with a keyword representing that
    section and ending with the keyword ``END``. Keywords that may begin a section
    include:

    - ``ELEMENTS`` or ``ELEM``
    - ``SPECIES`` or ``SPEC``
    - ``THERMO`` or ``THERMO ALL``
    - ``REACTIONS`` or ``REAC``
    - ``TRANSPORT``

  * The thermodynamic data is read in a fixed format. This means that each
    column of the input has a particular meaning. *Many common errors are
    generated because information is missing or in the wrong column. Check
    thoroughly for extraneous or missing spaces.* The format for each
    thermodynamic entry should be as follows::

        N2                      N 2                 G200.000   6000.000  1000.00       1
         2.95258000E+00 1.39690000E-03-4.92632000E-07 7.86010000E-11-4.60755000E-15    2
        -9.23949000E+02 5.87189000E+00 3.53101000E+00-1.23661000E-04-5.02999000E-07    3
         2.43531000E-09-1.40881000E-12-1.04698000E+03 2.96747000E+00                   4

    The following table is adapted from the Chemkin manual [SAND89]_ to describe the
    column positioning of each required part of the entry. Empty columns should be
    filled with spaces.

    +---------+-------------------------------------+--------+
    |Line No. | Contents                            | Column |
    +=========+=====================================+========+
    | 1       | Species Name                        | 1--18  |
    +---------+-------------------------------------+--------+
    | 1       | Date (Optional)                     | 19--24 |
    +---------+-------------------------------------+--------+
    | 1       | Atomic Symbols and formula          | 25--44 |
    +---------+-------------------------------------+--------+
    | 1       | Phase of species (S, L, G)          | 45     |
    +---------+-------------------------------------+--------+
    | 1       | Low temperature                     | 46--55 |
    +---------+-------------------------------------+--------+
    | 1       | High temperature                    | 56--65 |
    +---------+-------------------------------------+--------+
    | 1       | Common temperature                  | 66--73 |
    +---------+-------------------------------------+--------+
    | 1       | Additional Atomic Symbols           | 74--78 |
    +---------+-------------------------------------+--------+
    | 1       | The integer ``1``                   | 80     |
    +---------+-------------------------------------+--------+
    | 2       | Coefficients :math:`a_1`            | 1--75  |
    |         | to :math:`a_5` for the upper        |        |
    |         | temperature interval                |        |
    +---------+-------------------------------------+--------+
    | 2       | The integer ``2``                   | 80     |
    +---------+-------------------------------------+--------+
    | 3       | Coefficients :math:`a_6,\ a_7`      | 1--75  |
    |         | for the upper temperature interval, |        |
    |         | and :math:`a_1,\ a_2,\ a_3` for     |        |
    |         | the lower temperature interval      |        |
    +---------+-------------------------------------+--------+
    | 3       | The integer ``3``                   | 80     |
    +---------+-------------------------------------+--------+
    | 4       | Coefficients :math:`a_4` through    | 1--60  |
    |         | :math:`a_7` for the lower           |        |
    |         | temperature interval                |        |
    +---------+-------------------------------------+--------+
    | 4       | The integer ``4``                   | 80     |
    +---------+-------------------------------------+--------+

    The first 18 columns are reserved for the species name. The name assigned
    to the species in the thermodynamic data must be the same as the species
    name defined in the ``SPECIES`` section. If the species name is shorter
    than 18 characters, the rest of the characters should be filled by spaces.
    The next six columns (columns 19--24) are typically used to write a date;
    they are not used further. The next 20 columns (25--44) are used to
    specify the elemental composition of the species. In column 45, the phase
    of the species (``S``, ``L``, or ``G`` for solid, liquid, or gas
    respectively) should be specified. The next 28 columns are reserved for
    the temperatures that delimit the ranges of the polynomials specified on
    the next several lines. The first two temperatures have a width of 10
    columns each (46--55 and 56--65), and represent the lowest temperature and
    highest temperature for which the polynomials are valid. The last
    temperature has a width of 8 columns (66--73) and is the "common"
    temperature, where the switch from low to high occurs. The next 5 columns
    (74--78) are reserved for atomic symbols and are usually left blank for
    the default behavior. Column 79 is blank and finally, the row is ended in
    column 80 with the integer ``1``.

    The next three lines of the thermodynamic entry have a similar format.
    They contain the coefficients of the polynomial described in
    :ref:`sec-thermo-models` for the NASA 7-coefficient polynomial formulation.
    The second row of the thermo entry (the first after the information row)
    contains the first five coefficients that apply the the temperature range
    between the midpoint and the upper limit. 15 columns are alloted for each
    coefficient (for a total of 75 columns), with no spaces between them.
    Although the entry above shows spaces between positive coefficients, it is
    to be noted that this is done only for formatting consistency with other
    lines that contain negative numbers. After the coefficients, four spaces
    in columns 76--79 are followed by the integer ``2`` in column 80. On the
    next line, the last two coefficients for the upper temperature range and
    the first three coefficients for the lower temperature range are
    specified. Once again, this takes up the first 75 columns, columns 76--79
    are blank, and the integer ``3`` is in column 80. Finally, on the last
    line of a particular entry, the last four coefficients of the lower
    temperature range are specified in columns 1--60, 19 blank spaces are
    present, and the integer ``4`` is in column 80. The 19 blank spaces in the
    last line are part of the standard. However, since the original Chemkin
    interpreter ignored those spaces, researchers began using that space to
    store additional information that was not necessary for the input file.
    Although these numbers create an error in ``ck2cti`` if present, they are
    harmless and can be ignored by using the ``--permissive`` option.

  * It may be the case that scientific formatted numbers are missing the ``E``.
    In this case, numbers often show up as ``1.1+01``, when they should be
    ``1.1E+01``. You can fix this with a simple Regular Expression find and
    replace::

        Find: (\d+\.\d+)([+-]\d+)
        Replace: \1E\2

  * The transport data file also has a specified format, as described in
    [SAND98]_, although the format is not as strict as for the thermodynamic
    entries. In particular, the first 15 columns of a line are reserved for
    the species name. *One common source of errors is a species that is present
    in the transport data file, but not in the thermodynamic data or in
    the species list; or a species that is present in the species list but
    not the transport data file.* The rest of the columns on a given line have
    no particular format, but must be present in the following order:

    +------------------+------------------------------------------------------+
    | Parameter Number | Parameter Name                                       |
    +==================+======================================================+
    | 1                | An integer with value 0, 1, or 2 indicating          |
    |                  | monatomic, linear, or non-linear molecular geometry. |
    +------------------+------------------------------------------------------+
    | 2                | The Lennard-Jones potential well depth               |
    |                  | :math:`\varepsilon/k_B` in Kelvin                    |
    +------------------+------------------------------------------------------+
    | 3                | The Lennard-Jones collision diameter :math:`\sigma`  |
    |                  | in Angstrom                                          |
    +------------------+------------------------------------------------------+
    | 4                | The dipole moment :math:`\mu` in Debye               |
    +------------------+------------------------------------------------------+
    | 5                | The polarizability :math:`\alpha` in Angstrom        |
    +------------------+------------------------------------------------------+
    | 6                | The rotational relaxation collision number           |
    |                  | :math:`Z_{rot}` at 298 K                             |
    +------------------+------------------------------------------------------+

    Another common error is if all 6 of these numbers are not present for every
    species.

.. [SAND89] See R. J. Kee, F. M. Rupley, and J. A. Miller, Sandia National
   Laboratories Report SAND89-8009 (1989).
   http://www.osti.gov/scitech/biblio/5681118

.. [SAND98] See R. J. Kee, G. Dixon-Lewis, J. Warnatz, M. E. Coltrin, J. A. Miller,
   H. K. Moffat, Sandia National Laboratories Report SAND86-8246B (1998).
