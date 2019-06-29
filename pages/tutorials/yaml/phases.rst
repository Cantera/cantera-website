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
present in the input file(s).

Phase Attributes
----------------

Phase Name
^^^^^^^^^^

Declaring the Elements
^^^^^^^^^^^^^^^^^^^^^^

Defining the Species
^^^^^^^^^^^^^^^^^^^^

Declaring the Reactions
^^^^^^^^^^^^^^^^^^^^^^^

The Kinetics Model
^^^^^^^^^^^^^^^^^^

The Transport Model
^^^^^^^^^^^^^^^^^^^

The Initial State
^^^^^^^^^^^^^^^^^

Interfaces
==========

Now that we have seen how to define bulk, three-dimensional phases, we can
describe the procedure to define an interface between phases. Cantera presently
implements a simple model for an interface that treats it as a two-dimensional
ideal solution of interfacial species.

.. _sec-phase-options:

Special Processing Options
==========================

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
