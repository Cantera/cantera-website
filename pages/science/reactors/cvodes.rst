.. title: CVODES and Time Integration in Cantera
.. has_math: true

.. jumbotron::

   .. raw:: html

      <h1 class="display-3">CVODES and Time Integration in Cantera</h1>

   .. class:: lead

      This guide explains ways Cantera can solve governing equations of 
      a transient Reactor or Reactor Network problem. Additional insights 
      into CVODES's solver are also provided.

Advancing a Reactor Network in Time
***********************************

Starting off the current state of the system, it can be advanced in time by 
one of the following methods:

- ``step()``: The step method computes the state of the system at the a priori
  unspecified time :math:`t_{\mathrm{new}}`. The time :math:`t_{\mathrm{new}}`
  is internally computed so that all states of the system only change within a
  (specifiable) band of absolute and relative tolerances. Additionally, the time
  step must not be larger than a predefined maximum time step
  :math:`\Delta t_{\mathrm{max}}`. The new time :math:`t_{\mathrm{new}}` is
  returned by this function.

- ``advance(``\ :math:`t_{\mathrm{new}}`\ ``)``: This method computes the state of the
  system at time :math:`t_{\mathrm{new}}`. :math:`t_{\mathrm{new}}` describes
  the absolute time from the initial time of the system. By calling this method
  in a for loop for pre-defined times, the state of the system is obtained for
  exactly the times specified. Internally, several ``step()`` calls are
  typically performed to reach the accurate state at time
  :math:`t_{\mathrm{new}}`.

- ``advance_to_steady_state(max_steps, residual_threshold, atol,
  write_residuals)`` [Python interface only]: If the steady state solution of a
  reactor network is of interest, this method can be used. Internally, the
  steady state is approached by time stepping. The network is considered to be
  at steady state if the feature-scaled residual of the state vector is below a
  given threshold value (which by default is 10 times the time step ``rtol``).

The use of the ``advance`` method in a loop has the advantage that it produces
results corresponding to a predefined time series. These are associated with a
predefined memory consumption and well comparable between simulation runs with
different parameters. However, some detail (for example, a fast ignition process)
might not be resolved in the output data due to the typically large time steps.
To avoid losing this detail, the
`Reactor::setAdvanceLimit <{{% ct_docs doxygen/html/dc/d5e/classCantera_1_1Reactor.html#a9b630edc7d836e901886d7fd81134d9e %}}>`__
method (C++) or the :py:func:`Reactor.set_advance_limit` method (Python) can be
used to set the maximum amount that a specified solution component can change
between output times. For an example of this feature's use, see the example
`reactor1.py </examples/python/reactors/reactor1.py.html>`__.

The ``step`` method results in many more data points because of the small
timesteps needed. Additionally, the absolute time has to be kept track of
manually.

Even though Cantera comes pre-defined with typical parameters for tolerances
and the maximum internal time step, the solution sometimes diverges. To solve
this problem, three parameters can be tuned: The absolute time stepping
tolerances, the relative time stepping tolerances, and the maximum time step. A
reduction of the latter value is particularly useful when dealing with abrupt
changes in the boundary conditions (for example, opening/closing valves; see
also the `IC engine example </examples/python/reactors/ic_engine.py.html>`__).

