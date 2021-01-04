.. title: Cantera Science
.. slug: index
.. date: 2018-05-30 11:20:56 UTC-04:00
.. description: Cantera Science page
.. type: text

.. jumbotron::

   .. raw:: html

      <h1 class="display-3">Science & Theory</h1>

   .. class:: lead

      While Cantera's documentation gives insight into the various classes and functions that
      constitute Cantera's capabilities, software documentation does not always provide a great
      format for diving into scientific theory. This section describes the equations and models
      Cantera uses to represent the real world.

.. raw:: html

   <h2 class="display-4">Chemical Kinetic Theory</h2>

These sections describe some of the theory underpinning the various ways that Cantera models phases
of matter. This involves calculations for thermodynamic and transport properties and chemical
reaction rates. The above information gives some insight into the basic constitutive models
available in Cantera: capabilities for calculating the basic properties of
phases of matter, which can be extended to model a wide range of science and
technology applications.

.. container:: container
   :tagname: section

   .. container:: card-deck

      .. container:: card

         .. container::
            :tagname: a
            :attributes: href=phases.html
                         title=Phases

            .. container:: card-header section-card
               :tagname: div

               Phases

         .. container:: card-body

            .. container:: card-text

               The theory behind some of Cantera's phase models.

      .. container:: card

         .. container::
            :tagname: a
            :attributes: href=eos.html
                         title=EoS

            .. container:: card-header section-card
               :tagname: div

               Equations of State

         .. container:: card-body

            .. container:: card-text

               The theory behind ideal and non-ideal thermodynamic models used in Cantera.

      .. container:: card

         .. container::
            :tagname: a
            :attributes: href=science-species.html
                         title=Species

            .. container:: card-header section-card
               :tagname: div

               Species

         .. container:: card-body

            .. container:: card-text

               The models Cantera uses to calculate species properties (thermodynamic and
               transport).

      .. container:: card

         .. container::
            :tagname: a
            :attributes: href=reactions.html
                         title=Reactions

            .. container:: card-header section-card
               :tagname: div

               Reactions

         .. container:: card-body

            .. container:: card-text

               The models that Cantera uses to calculate chemical reaction rates.

.. raw:: html

   <h2 class="display-4">Cantera Reactor and Flame Models</h2>

Cantera comes with a number of zero- and one-dimensional models: reactor and flame models for a
number of well-defined and commonly encountered phenomena.  Below we give an overview of the theory
and and function of these models. You can also see the `Cantera examples </examples/index.html>`__
to see how these models might be used.

.. container:: container
   :tagname: section

   .. container:: card-deck

      .. container:: card

         .. container::
            :tagname: a
            :attributes: href=reactors.html
                         title=Reactors

            .. container:: card-header section-card

               Reactors

         .. container:: card-body

            .. container:: card-text

               Cantera provides a range of generalized zero-dimensional models that can be given a
               range of initial and boundary conditions and can also be linked to form reactor
               networks.

      .. container:: card

         .. container::
            :tagname: a
            :attributes: href=flames.html
                         title=Flames

            .. container:: card-header section-card

               Flames

         .. container:: card-body

            .. container:: card-text

               Cantera includes a set of models for representing steady-state, quasi-one-dimensional
               reacting flows, which can be used to simulate a number of common flames.


Note that this information is simply an overview. For a thorough, comprehensive description of
chemical kinetic theory and the associated governing equations for a variety of systems, a very
useful reference is R. J. Kee, M. E. Coltrin, P. Glarborg, and H. Zhu. *Chemically Reacting Flow:
Theory and Practice*. 2nd Ed. John Wiley and Sons, 2017.
