.. title: Downloading the Cantera source code

.. _sec-source-code:

.. jumbotron::

   .. raw:: html

      <h1 class="display-3">Downloading the Cantera source code</h1>


Stable Release
--------------

* **Option 1**: Check out the code using Git:

  .. code:: bash

      git clone --recursive https://github.com/Cantera/cantera.git
      cd cantera

  Then, check out the tag of the most recent stable version:

  .. code:: bash

      git checkout tags/v2.4.0
      git submodule update

  A list of all the tags can be shown by:

  .. code:: bash

     git tag --list

* **Option 2**: Download the most recent source ``.tar.gz`` or ``.zip`` file
  from `Github <https://github.com/Cantera/cantera/releases>`__ and extract the
  contents.

Beta Release
------------

* Check out the code using Git:

  .. code:: bash

     git clone --recursive https://github.com/Cantera/cantera.git
     cd cantera

  Then pick either **Option 1** or **Option 2** below.

* **Option 1**: Check out the tag with the most recent beta release:

  .. code:: bash

     git checkout tags/v2.4.0b2
     git submodule update

  Note that the most recent beta version might be older than the most recent
  stable release. A list of all the tags, including stable and beta versions can
  be shown by:

  .. code:: bash

     git tag --list

* **Option 2**: Check out the branch with all the bug fixes leading to the
  next minor release of the stable version:

  .. code:: bash

     git checkout 2.4
     git submodule update

  This branch has all the work on the 2.4.x version of the software.

Development Version
-------------------

Check out the code using Git:

.. code:: bash

   git clone --recursive https://github.com/Cantera/cantera.git
   cd cantera

Note that by default, the ``main`` branch is checked out, containing all of
the feature updates and bug fixes to the code since the previous stable release.
The main branch is usually an alpha release, corresponding to the ``a`` in
the version number, and does not usually get a tag.

.. container:: container

   .. container:: row

      .. container:: col-6 text-left

         .. container:: btn btn-primary
            :tagname: a
            :attributes: href=installation-reqs.html

            Previous: Compilation Requirements


      .. container:: col-6 text-right

         .. container:: btn btn-primary
            :tagname: a
            :attributes: href=configure-build.html

            Next: Configure & Build
