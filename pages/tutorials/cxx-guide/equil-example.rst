.. title: Chemical Equilibrium Example Program
.. has_math: true

.. jumbotron::

   .. raw:: html

      <h1 class="display-4">Chemical Equilibrium Example Program</h1>

   .. class:: lead

      Learn how to set a phase to a state of chemical equilibrium


In the program below, the ``equilibrate`` method is called to set the gas to a
state of chemical equilibrium, holding the temperature and pressure fixed.

.. include:: pages/tutorials/cxx-guide/demoequil.cpp
   :code: c++

The program output is::

  ohmech:

       temperature   1500 K
          pressure   2.0265e+05 Pa
           density   0.31683 kg/m^3
  mean mol. weight   19.499 kg/kmol
   phase of matter   gas

                          1 kg             1 kmol
                     ---------------   ---------------
          enthalpy       -4.1789e+06       -8.1485e+07  J
   internal energy       -4.8186e+06       -9.3957e+07  J
           entropy             11283        2.2001e+05  J/K
    Gibbs function       -2.1104e+07        -4.115e+08  J
 heat capacity c_p              1893             36912  J/K
 heat capacity c_v            1466.6             28597  J/K

                      mass frac. Y      mole frac. X     chem. pot. / RT
                     ---------------   ---------------   ---------------
                H2          0.025847              0.25           -19.295
                 H        3.2181e-07        6.2252e-06           -9.6477
                 O        6.2927e-12        7.6693e-12           -26.377
                O2        1.1747e-11        7.1586e-12           -52.753
                OH        3.0994e-07        3.5535e-07           -36.024
               H2O           0.46195               0.5           -45.672
               HO2        1.2362e-14        7.3034e-15           -62.401
              H2O2         6.904e-13        3.9578e-13           -72.049
                AR           0.51221              0.25           -21.339
                N2                 0                 0


How can we tell that this is really a state of chemical equilibrium? Well, by
applying the equation of reaction equilibrium to formation reactions from the
elements, it is straightforward to show that:

.. math::

   \mu_k = \sum_m \lambda_m a_{km}.

where :math:`\mu_k` is the chemical potential of species :math:`k`, :math:`a_{km}` is
the number of atoms of element :math:`m` in species :math:`k`, and :math:`\lambda_m` is the
chemical potential of the elemental species per atom (the so-called "element
potential"). In other words, the chemical potential of each species in an
equilibrium state is a linear sum of contributions from each atom. We see that
this is true in the output above—the chemical potential of H2 is exactly
twice that of H, the chemical potential for OH is the sum of the values for H
and O, the value for H2O2 is twice as large as the value for OH, and so on.

We'll see later how the ``equilibrate`` function really works.

.. container:: container

   .. container:: row

      .. container:: col-lg-4 text-left

         .. container:: btn btn-primary
            :tagname: a
            :attributes: href=thermo.html
                         title="Computing Properties"

            Previous: Computing Properties

      .. container:: col-lg-4 text-center

         .. container:: btn btn-primary
            :tagname: a
            :attributes: href=index.html
                         title="C++ Interface Tutorial"

            Return: C++ Interface Tutorial

      .. container:: col-lg-4 text-right

         .. container:: btn btn-primary
            :tagname: a
            :attributes: href=factories.html
                         title="Creating Cantera Phase objects"

            Next: Creating Cantera Phase objects
