
.. slug: defining-phases
.. hidetitle: true


Defining Phases
===============
A guide to Cantera's input file format
=========================================

Virtually every Cantera simulation involves one or more phases of
matter. Depending on the calculation being performed, it may be necessary to
evaluate thermodynamic properties, transport properties, and/or homogeneous
reaction rates for the phase(s) present. Before the properties can be evaluated,
each phase must be defined, meaning that the models to use to compute its
properties and reaction rates must be specified, along with any parameters the
models require.

Because the amount of data required can be quite large, this data is imported
from a text file that can be read by the application, so that a given
phase model can be re-used for other simulations.  This is the Cantera
Input (CTI) file.

This guide describes how to write such files to define phases and interfaces for
use in Cantera simulations.  Each link below represents a standalone module -
while you certainly can read them in order, you can also jump to whichever
section addresses your current needs.  If you need tips on troubleshooting the
CTI file syntax rules, please go `here <cti-syntax.html>`_.

.....

`Phases and their Interfaces <phases.html>`_
********************************************

For each phase that appears in a problem, a corresponding entry should be
present in the input file(s). We'll start by describing the
entries for phases of various types, and the look at how to define interfaces
between phases.

.....

`Elements and Species <species.html>`_
**************************************

For each species declared as part of a phase description, both the species and
the elements that it is comprised of must be defined. Here, we describe how both
are defined.

.....

`<Reactions.html>`_
*******************

Cantera supports a number of different types of reactions, including several
types of homogeneous reactions, surface reactions, and electrochemical
reactions. For each, there is a corresponding entry type. Here, we describe how
to declare each type of reaction and provide the necessary parameters to
calculate the reaction rate for each.

`Processing Input Files <cti-processing.html>`_
***********************************************

This module describes how a CTI file is processed, and helps debug some errors
commonly encountered during input file processing.

.....

Additional Information
======================

`CTI Class Reference </sphinx/html/cti/classes.html>`_
******************************************************

Congratulations - you have finished the main CTI tutorials!  This last link
connects you to the documentation of the CTI class, which you can peruse if and
when you require additional details.
