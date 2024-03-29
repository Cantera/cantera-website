.. title: Downloading the Cantera source code

.. _sec-source-code:

.. jumbotron::

   .. raw:: html

      <h1 class="display-4">Downloading the Cantera source code</h1>


Stable Release
--------------

* **Option 1**: Check out the code using Git (recommended):

  .. code:: bash

      git clone --recursive https://github.com/Cantera/cantera.git
      cd cantera

  Then, check out the tag of the most recent stable version:

  .. code:: bash

      git checkout tags/v3.0.0
      git submodule update

  A list of all the tags can be shown by:

  .. code:: bash

     git tag --list

* **Option 2**: Download the most recent source ``.tar.gz`` or ``.zip`` file
  from `Github <https://github.com/Cantera/cantera/releases>`__ and extract the
  contents. In this case, several dependencies that are linked to the Cantera Git
  repository will not be available and will need to be installed elsewhere on your
  system.

Beta Release
------------

* Check out the code using Git:

  .. code:: bash

     git clone --recursive https://github.com/Cantera/cantera.git
     cd cantera

  Then pick either **Option 1** or **Option 2** below.

* **Option 1**: Check out the tag with the most recent beta release:

  .. code:: bash

     git checkout tags/v3.0.0b1
     git submodule update

  Note that the most recent beta version might be older than the most recent
  stable release. A list of all the tags, including stable and beta versions can
  be shown by:

  .. code:: bash

     git tag --list

* **Option 2**: Check out the branch with all the bug fixes leading to the
  next minor release of the stable version:

  .. code:: bash

     git checkout 3.0
     git submodule update

  This branch has all the work on the 3.0.x version of the software.

  If you've already checked out the 3.0 branch, you can get the latest updates from the
  main Cantera repository and synchronize your local repository by running:

  .. code:: bash

     git checkout 3.0
     git fetch --all
     git pull --ff-only

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

If you've previously checked out the repository, and haven't made any changes locally,
you can get the latest updates from the main Cantera repository and synchronize your
local repository by running:

.. code:: bash

   git checkout main
   git fetch --all
   git pull --ff-only

.. container:: container

   .. container:: row

      .. container:: col-6 text-left

         .. container:: btn btn-primary
            :tagname: a
            :attributes: href=compilation-reqs.html

            Previous: Compilation Requirements


      .. container:: col-6 text-right

         .. container:: btn btn-primary
            :tagname: a
            :attributes: href=configure-build.html

            Next: Configure & Build
