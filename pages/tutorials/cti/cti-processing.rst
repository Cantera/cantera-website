.. slug: cti-processing
.. has_math: true
.. title: Processing Input Files

.. jumbotron::

   .. raw:: html

      <h1 class="display-3">Processing Input Files</h1>

   .. class:: lead

      A description of how Cantera processes input files, to help with debugging any errors that
      occur.

Cantera Input Files
===================

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

.. _sec-two-file-formats:

Two File Formats
----------------

Why two file formats? There are several reasons. XML is a widely-used standard
for data files, and it is designed to be relatively easy to parse. This makes it
possible for other applications to use Cantera CTML data files, without
requiring the substantial chemical knowledge that would be required to use ``.cti``
files. For example, web services (small applications that run remotely over a
network) are often designed to accept XML input data over the network, perform a
calculation, and send the output in XML back across the network. Supporting an
XML-based data file format facilitates using Cantera in web services or other
network computing applications.

The difference between the high-level description in a ``.cti`` input file and the
lower-level description in the CTML file may be illustrated by how reactions are
handled. In the input file, the reaction stoichiometry and its reversibility or
irreversibility are determined from the reaction equation. For example:

.. code:: python

   O + HCCO <=> H + 2 CO

specifies a reversible reaction between an oxygen atom and the ketenyl radical
HCCO to produce one hydrogen atom and two carbon monoxide molecules. If ``<=>``
were replaced with ``=>``, then it would specify that the reaction should be
treated as irreversible.

Of course, this convention is not spelled out in the input file - the parser
simply has to know it, and has to also know that a "reactant" appears on the
left side of the equation, a "product" on the right, that the optional number in
front of a species name is its stoichiometric coefficient (but if missing the
value is one), etc. The preprocessor does know all this, but we cannot expect
the same level of knowledge of chemical conventions by a generic XML parser.

Therefore, in the CTML file, reactions are explicitly specified to be reversible
or irreversible, and the reactants and products are explicitly listed with their
stoichiometric coefficients. The XML file is, in a sense, a "dumbed-down"
version of the input file, spelling out explicitly things that are only implied
in the input file syntax, so that "dumb" (that is, easy to write) parsers can be
used to read the data with minimal risk of misinterpretation.

The reaction definition:

.. code:: python

   reaction("O + HCCO <=> H + 2 CO", [1.00000E+14, 0, 0])

in the input file is translated by the preprocessor to the following CTML text:

.. code:: xml

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
write a custom parser—virtually any standard XML parser, of which there are
many, can be used to read the CTML data.

So, in general, files that are easy for knowledgeable users (you) to write are more
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
start Python, and type:

.. code:: python

   >>> import cantera.ctml_writer
   >>> help(cantera.ctml_writer)

The ``ctml_writer.py`` module can also be run as a script to convert input ``.cti``
files to CTML. For example, if you have an input file ``phasedefs.cti``, then
simply type at the command line:

.. code:: bash

   python -m cantera.ctml_writer phasedefs.cti

to create CTML file ``phasedefs.xml``. On systems which support running Python
scripts directly, a script to run ``ctml_writer`` directly is also installed. If
the Cantera ``bin`` directory is on your ``PATH``, you can also do the
conversion by running:

.. code:: bash

   ctml_writer phasedefs.cti

This can be used to generate XML input files for use on systems where the
Cantera Python package is not installed. Of course, most of the time creation of
the CTML file will happen behind the scenes, and you will not need to be
concerned with CTML files at all.

Error Handling
==============

During processing of an input file, errors may be encountered. These could be
syntax errors, or could be ones that are flagged as errors by Cantera due to
some apparent inconsistency in the data—an unphysical value, a species that
contains an undeclared element, a reaction that contains an undeclared species,
missing species or element definitions, multiple definitions of elements,
species, or reactions, and so on.

Syntax Errors
-------------

Syntax errors are caught by the Python preprocessor, not by Cantera, and must be
corrected before proceeding further.  Python prints a "traceback" that allows
you to find the line that contains the error. For example, consider the
following input file, which is intended to create a gas with the species and
reactions of GRI-Mech 3.0, but has a misspelled the field name ``reactions``:

.. code:: python

   ideal_gas(name = 'gas',
             elements = 'H O',
             species = 'gri30: all',
             reactionss = 'gri30: all')

When this definition is imported into an application, an error message like the
following would be printed to the screen, and execution of the program or script
would terminate. :

.. code:: python

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
the part starting with the ``Cantera Error`` heading, and specifically the
contents of the ``converter log`` section. This message says that that on line 4
of ``gas.cti``, the the keyword argument ``reactionss`` was not
recognized. Seeing this message, it is clear that the problem is that
*reactions* is misspelled.

Cantera Errors
--------------

Now let's consider the other class of errors—ones that Cantera, not Python,
detects. Continuing the example above, suppose that the misspelling is
corrected, and the input file processed again. Again an error message results,
but this time it is from Cantera:

.. code:: python

   cantera.error:
   Procedure: installSpecies
   Error: species C contains undeclared element C

The problem is that the phase definition specifies that all species are to be
imported from dataset ``gri30``, but only the elements H and O are declared. The
``gri30`` dataset contains species composed of the elements H, O, C, N, and Ar. If
the definition is modified to declare these additional elements:

.. code:: python

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

.. container:: container

   .. container:: row

      .. container:: col-4 text-left

         .. container:: btn btn-primary
            :tagname: a
            :attributes: href=reactions.html

            Previous: Reactions

      .. container:: col-4 text-center

         .. container:: btn btn-primary
            :tagname: a
            :attributes: href=defining-phases.html

            Return: Defining Phases

      .. container:: col-4 text-right

         .. container:: btn btn-primary
            :tagname: a
            :attributes: href=cti-syntax.html

            Next: CTI Syntax Tutorial
