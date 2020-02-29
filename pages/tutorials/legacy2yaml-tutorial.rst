.. title: Converting CTI and XML input files to YAML
.. slug: legacy2yaml
.. has_math: true

.. jumbotron::

   .. raw:: html

      <h1 class="display-3">Converting CTI and XML input files to YAML</h1>

   .. class:: lead

      If you want to convert an existing, legacy CTI or XML input file to the
      YAML format, this section will help.

cti2yaml
--------

Cantera comes with a converter utility ``cti2yaml`` (or ``cti2yaml.py``) that
converts legacy CTI format mechanisms into the new YAML format introduced in
Cantera 2.5. This program can be run from the command line to convert files to
the YAML format. *(New in Cantera 2.5)*

Usage:

.. code:: bash

   cti2yaml [-h] input [output]

The ``input`` argument is required, and specifies the name of the input file to
be converted. The optional ``output`` argument specifies the name of the new
output file. If ``output`` is not specified, then the output file will have the
same name as the input file, with the extension replaced with ``.yaml``.

Example:

.. code:: bash

   cti2yaml mymech.cti

will generate the output file ``mymech.yaml``.

If the ``cti2yaml`` script is not on your path, but the Cantera Python module
is, ``cti2yaml`` can be used by running:

.. code:: bash

   python -m cantera.cti2yaml mymech.cti

It is not necessary to use ``cti2yaml`` to convert any of the CTI input files
included with Cantera. YAML versions of these files are already included with
Cantera.

For input files where you have both the CTI and XML versions, ``cti2yaml`` is
recommended over ``ctml2yaml``. In cases where the mechanism was originally
converted from a CK-format mechanism, it is recommended to use ``ck2yaml`` if
the original input files are available.

ctml2yaml
---------

Cantera comes with a converter utility ``ctml2yaml`` (or ``ctml2yaml.py``) that
converts legacy XML (CTML) format mechanisms into the new YAML format introduced
in Cantera 2.5. This program can be run from the command line to convert files
to the YAML format. *(New in Cantera 2.5)*

Usage:

.. code:: bash

   ctml2yaml [-h] input [output]

The ``input`` argument is required, and specifies the name of the input file to
be converted. The optional ``output`` argument specifies the name of the new
output file. If ``output`` is not specified, then the output file will have the
same name as the input file, with the extension replaced with ``.yaml``.

Example:

.. code:: bash

   ctml2yaml mymech.xml

will generate the output file ``mymech.yaml``.

If the ``ctml2yaml`` script is not on your path, but the Cantera Python module
is, ``ctml2yaml`` can be used by running:

.. code:: bash

   python -m cantera.cti2yaml mymech.xml

It is not necessary to use ``ctml2yaml`` to convert any of the XML input files
included with Cantera. YAML versions of these files are already included with
Cantera.
