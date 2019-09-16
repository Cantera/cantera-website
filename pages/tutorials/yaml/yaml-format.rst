.. slug: yaml-format
.. title: YAML File Structure

.. jumbotron::

   .. raw:: html

      <h1 class="display-3">YAML Format Tutorial</h1>

   .. class:: lead

      Here we describe the syntax and structure of Cantera YAML files.

Syntax
======

Cantera YAML files use a subset of the `YAML 1.2
<https://yaml.org/spec/1.2/spec.html>`__ specification. Cantera YAML files
consist of individual values, which may be strings, numbers or booleans, that
are then composed as elements of nested mappings and sequences.

Strings
-------

Strings may be generally written without qoutes, but may be enclosed in single
quotes or double quotes if needed in order to avoid certain parsing ambiguties.

.. code:: yaml

   A string
   Another 'string'
   "A string: that requires quotes"

Numbers
-------

Numbers can be written as integers, decimal values, or using E-notation

.. code:: yaml

   3
   3.14
   6.022e23

Booleans
--------

Sequences
---------

A sequence of multiple items is specified by separating the items by commas and
enclosing them in square brackets. The individual items can have
any type -- strings, integers, floating-point numbers (or even entries or other
lists).

.. code:: yaml

   elements: [O, H, C, N, Ar]
   temperature-ranges: [200.0, 1000.0, 3500.0]

(block style, use of indentation)

Mappings
--------

(flow style and block style)
(main yaml file is actually a mapping)
(cantera requires all mapping keys to be strings)
(nested mappings)



Comments
--------

The character ``#`` is the comment character. Everything to the right of this
character on a line is ignored:

.. code:: yaml

   # set the default units
   units:
     length: cm  # use centimeters for length
     quantity: mol  # use moles for quantity

Top-level entries
-----------------

Entries have fields that can be assigned values. A species entry is shown below
that has fields ``name`` and ``composition``:

.. code:: yaml

   - name: H2O
     composition: {H: 2, O: 1}

Most entries have some fields that are required; these must be assigned values,
or else processing of the file will abort and an error message will be
printed. Other fields may be optional, and take default values if not assigned.

Dimensional Values
==================

Error Handling
==============

Syntax Errors
-------------

Cantera Errors
--------------


.. container:: container

   .. container:: row

      .. container:: col-4 text-left

         .. container:: btn btn-primary
            :tagname: a
            :attributes: href=reactions.html
                         title="Reactions"

            Previous: Reactions

      .. container:: col-4 text-center

         .. container:: btn btn-primary
            :tagname: a
            :attributes: href=defining-phases.html
                         title="Defining Phases"

            Return: Defining Phases

      .. container:: col-4 text-right

         .. container:: btn btn-primary
            :tagname: a
            :attributes: href={{% ct_dev_docs sphinx/html/yaml/index.html %}}
                         title="YAML Format Reference"

            Next: YAML Format Reference
