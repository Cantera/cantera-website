.. title: C++ Header Files

.. jumbotron::

   .. raw:: html

      <h1 class="display-3">C++ Header Files</h1>

   .. class:: lead

      Cantera provides some header files designed for use in C++ application
      programs. These are designed to include those portions of Cantera needed for
      particular types of calculations.

These headers are designed for use in C++ application programs, and are not
included by the Cantera core. The headers and their functions are:


``thermo.h``
    Base thermodynamic classes and functions for creating
    `ThermoPhase <{{% ct_docs doxygen/html/dc/d38/classCantera_1_1ThermoPhase.html %}}>`__
    objects from input files.

``kinetics.h``
    Base kinetics classes and functions for creating
    `Kinetics <{{% ct_docs doxygen/html/d4/dc4/classCantera_1_1Kinetics.html %}}>`__ objects from
    input files.

``transport.h``
    Base transport property classes and functions for creating
    `Transport <{{% ct_docs doxygen/html/d2/dfb/classCantera_1_1Transport.html %}}>`__
    objects from input files.

``zerodim.h``
    Zero-dimensional reactor networks.

``onedim.h``
    One-dimensional reacting flows.

``reactionpaths.h``
    Reaction path diagrams.


.. container:: container

   .. container:: row

      .. container:: col-4 text-left

         .. container:: btn btn-primary
            :tagname: a
            :attributes: href=compiling.html
                         title="Compiling Cantera C++ Applications"

            Previous: Compiling Cantera C++ Applications

      .. container:: col-4 text-center

         .. container:: btn btn-primary
            :tagname: a
            :attributes: href=index.html
                         title="C++ Interface Tutorial"

            Return: C++ Interface Tutorial

      .. container:: col-4 text-right

         .. container:: btn btn-primary
            :tagname: a
            :attributes: href=simple-example.html
                         title="A Very Simple C++ Program"

            Next: A Very Simple C++ Program
