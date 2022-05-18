.. title: Compilation Requirements

.. _sec-installation-reqs:

.. jumbotron::

   .. raw:: html

      <h1 class="display-3"> Compilation Requirements</h1>

   .. class:: lead

      Click the buttons below to see the required software that you must install to
      compile Cantera on your operating system.

   .. raw:: html

      <div class="container">
         <div class="row">
            <div class="col">
               <a class="btn btn-secondary btn-block" href="#sec-conda">Conda</a>
            </div>
            <div class="col">
               <a class="btn btn-secondary btn-block" href="#sec-ubuntu-debian-reqs">Ubuntu & Debian</a>
            </div>
            <div class="col">
               <a class="btn btn-secondary btn-block" href="#sec-fedora-reqs">Fedora & RHEL</a>
            </div>
            <div class="col">
               <a class="btn btn-secondary btn-block" href="#sec-opensuse-reqs">OpenSUSE & SLE</a>
            </div>
            <div class="col">
               <a class="btn btn-secondary btn-block" href="#sec-windows">Windows</a>
            </div>
            <div class="col">
               <a class="btn btn-secondary btn-block" href="#sec-macos">macOS</a>
            </div>
         </div>
      </div>


.. _sec-conda:

Conda & Anaconda
----------------

General Notes
^^^^^^^^^^^^^

* These instructions will set you up to build Cantera with the dependencies installed in a Conda
  environment

* You will need to install compilers for your system by following the instructions in the sections
  below to install the compiler for your operating system.

* By default, Cantera is installed into the active conda environment, where the
  layout of the directory structure corresponds to the
  `configuration option <https://cantera.org/compiling/configure-build.html>`__
  ``layout=conda``.

.. _sec-conda-reqs:

Conda Requirements
^^^^^^^^^^^^^^^^^^

* Install `Anaconda <https://www.anaconda.com/download/>`__ or
  `Miniconda <https://conda.io/miniconda.html>`__.

* Launch the command line interface:

  * On macOS and Linux, the installer should add the appropriate activation mechanism
    for your normal terminal by default. You can test this by running

    .. code:: bash

     conda --version

    in the terminal. If there is no output or an error appears, locate your Conda
    installation and run the following code in the terminal:

    .. code:: bash

      /path/to/conda/install/folder/bin/conda init -all

    Then restart your terminal or shell.

  * On Windows, use the Anaconda PowerShell to run the build process (available from
    the Start Menu). When using MSVC compilers, you also need to set environment
    variables for x64-native tools (see `Developer command file locations
    <https://docs.microsoft.com/en-us/cpp/build/building-on-the-command-line?view=msvc-170#developer_command_file_locations>`__)
    by running

    .. code:: bash

      . "C:\path\to\MSVC\Auxiliary\Build\vcvars64.bat"

    (note that the period ``'.'`` is part of the command). The path can be found as
    follows: locate the **x64 Native Tools Command Prompt** in the Start Menu,
    right-click, select **More > Open File Location**, right-click on the shortcut,
    select **Properties** and copy the **Target** command.

* Create an environment ``ct-build`` with the dependencies to build Cantera. Create a
  file called ``environment.yaml`` with the following content

  .. code:: yaml

     name: ct-build
     channels:
     - conda-forge
     dependencies:
     - python  # Cantera supports Python 3.7 and up
     - scons  # build system
     - boost-cpp  # C++ dependency
     # - sundials  # uncomment to override Cantera default
     # - fmt  # uncomment to override Cantera default
     # - eigen  # uncomment to override Cantera default
     # - yaml-cpp  # uncomment to override Cantera default
     # - libgomp  # optional (OpenMP implementation when using GCC)
     - cython  # needed to build Python package
     - numpy  # needed to build Python package
     - pytest  # needed for the Python test suite
     - ruamel.yaml  # needed for converter scripts
     # - h5py  # optional (needed for HDF/H5 output)
     # - pandas  # optional (needed for pandas interface)
     # - scipy  # optional (needed for some examples)
     # - matplotlib  # optional (needed for plots)
     # - python-graphviz  # optional (needed for reaction path diagrams)
     - ipython  # optional (needed for nicer interactive command line)
     # - jupyter  # optional (needed for Jupyter Notebook)
     # - sphinx  # optional (needed for documentation)
     # - doxygen  # optional (needed for documentation)
     # - graphviz  # optional (needed for documentation)
     # - pip  # optional (needed if PyPI managed packages are used)
     # - pip:  # optional (list of PyPI managed packages)
     #   - sphinxcontrib-matlabdomain  # optional (needed for documentation)
     #   - sphinxcontrib-katex  # optional (needed for documentation)
     #   - sphinxcontrib-doxylink  # optional (needed for documentation)

  The environment is then created and activated using

  .. code:: bash

     conda env create -f environment.yaml
     conda activate ct-build

  After creating the enviroment, it can be updated from within ``ct-build`` using

  .. code:: bash

     conda env update -f environment.yaml --prune

* (Optional) If you want to override external libraries packaged with Cantera
  (``sundials``, ``fmt``, ``eigen``, ``yaml-cpp``), simply uncomment corresponding
  lines in the file ``environment.yaml`` above. Note that specific versions can be
  forced by providing version numbers (example: replace ``sundials`` by
  ``sundials=5.8`` to install version ``5.8``).

* (Optional) If you want to build the documentation, make sure to uncomment lines
  containing ``sphinx``, ``doxygen``, ``graphviz``, ``pip`` as well as all relevant
  items listed for the ``pip:`` entry in ``environment.yaml``.

* (Cantera < 2.6 only) On previous Cantera versions, the build process requires
  configuration options ``boost_inc_dir`` and ``prefix`` (see
  `configuration options <https://cantera.org/compiling/configure-build.html>`__);
  starting with Cantera 2.6, these settings are detected automatically.

.. note::

   As the compiled code is based on the conda environment ``ct-build``, it is only
   usable from within that environment. This means that in order to use the compiled
   Cantera package, you have to activate your ``ct-build`` environment first.

.. container:: container

  .. container:: row

     .. container:: col-12 text-right

        .. container:: btn btn-primary
           :tagname: a
           :attributes: href=source-code.html

           Next: Download the Source Code

.. _sec-linux:

Linux
-----

General Notes
^^^^^^^^^^^^^

* To download the source code, installing ``git`` is highly recommended in addition
  to the requirements listed below.

* The following instructions use the system-installed versions of Python, but
  alternate installations such as the Anaconda distribution of Python can be
  used as well.

* Cython is only required to be installed for the version of Python that also
  has SCons installed; following the instructions below will install Cython for
  the version of Python installed in the system directories. The minimum
  compatible Cython version is 0.23. If your distribution does not contain a
  suitable version, you may be able to install a more recent version using
  Pip.

* Users of other distributions should install the equivalent packages, which
  may have slightly different names.

* In addition to the operating systems below, Cantera should work on any
  Unix-like system where the necessary prerequisites are available, but some
  additional configuration may be required.

.. _sec-ubuntu-debian-reqs:

Ubuntu & Debian
^^^^^^^^^^^^^^^

* Ubuntu 16.04 LTS (Xenial Xerus) or newer is required; 20.04 LTS (Focal Fossa)
  or newer is recommended

* Debian 9.0 (Stretch) or newer; 10.0 (Buster) or newer is recommended

* The following packages must be installed to build any of the Cantera modules using
  your choice of package manager::

      g++ python scons libboost-dev

* In addition to the general packages, building the Python 3 module also requires::

      cython python3 python3-dev python3-setuptools python3-numpy python3-ruamel.yaml

* In addition to the general packages, building the Fortran module also requires::

      gfortran

* In addition to the general packages, building the MATLAB toolbox also requires:

  * MATLAB version later than 2009a

    * Typically installed to::

        /opt/MATLAB/R20YYn

      where ``YY`` is a two digit year and ``n`` is either ``a`` or ``b``

.. container:: container

   .. container:: row

      .. container:: col-12 text-right

         .. container:: btn btn-primary
            :tagname: a
            :attributes: href=source-code.html

            Next: Download the Source Code

.. _sec-fedora-reqs:

Fedora & RHEL
^^^^^^^^^^^^^

* The following packages must be installed to build any of the Cantera modules using
  your choice of package manager::

      gcc-c++ python scons boost-devel

* In addition to the general packages, building the Python 3 module also requires::

      python3 python3-setuptools python3-devel Cython python3-numpy python3-ruamel-yaml

* In addition to the general packages, building the Fortran module also requires::

      gcc-gfortran

* In addition to the general packages, building the MATLAB toolbox also requires:

  * MATLAB version later than 2009a

    * Typically installed to::

        /opt/MATLAB/R20YYn

      where ``YY`` is a two digit year and ``n`` is either ``a`` or ``b``

.. container:: container

   .. container:: row

      .. container:: col-12 text-right

         .. container:: btn btn-primary
            :tagname: a
            :attributes: href=source-code.html

            Next: Download the Source Code

.. _sec-opensuse-reqs:

OpenSUSE & SUSE Linux Enterprise
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* OpenSUSE Leap 15.1 or newer recommended

* The following packages must be installed to build any of the Cantera modules using
  your choice of package manager::

      gcc-c++ python3 scons boost-devel

* In addition to the general packages, building the Python module also requires::

      python3-devel python3-setuptools python3-numpy python3-numpy-devel python3-ruamel.yaml

* In addition to the general packages, building the Fortran module also requires::

      gcc-fortran

* In addition to the general packages, building the MATLAB toolbox also requires:

  * MATLAB version later than 2009a

    * Typically installed to::

        /opt/MATLAB/R20YYn

      where ``YY`` is a two digit year and ``n`` is either ``a`` or ``b``

.. container:: container

   .. container:: row

      .. container:: col-12 text-right

         .. container:: btn btn-primary
            :tagname: a
            :attributes: href=source-code.html

            Next: Download the Source Code

.. _sec-windows:

Windows
-------

General Notes
^^^^^^^^^^^^^

* The build process will produce a Python module compatible with the version of
  Python used for the compilation. To generate different modules for other
  versions of Python, you will need to install those versions of Python and
  recompile.

* The following instructions use the versions of Python downloaded from
  https://www.python.org/downloads/, but alternate installations such as the
  Anaconda distribution of Python can be used as well.

* If you want to build the Matlab toolbox and you have a 64-bit copy of Windows,
  by default you will be using a 64-bit copy of Matlab, and therefore you need
  to compile Cantera in 64-bit mode. For simplicity, it is highly recommended
  that you use a 64-bit version of Python to handle this automatically.

* It is generally helpful to have SCons and Python in your ``PATH`` environment
  variable. This can be done by checking the appropriate box during the
  installation of Python or can be accomplished by adding the top-level Python
  directory and the ``Scripts`` subdirectory (for example,
  ``C:\Python36;C:\Python36\Scripts``) to your ``PATH``. The dialog to change
  the ``PATH`` is accessible from::

      Control Panel > System and Security > System > Advanced System Settings > Environment Variables

  Make sure that the installation of Python that has SCons comes first on your
  ``PATH``.

* In order to use SCons to install Cantera to a system folder (for example,
  ``C:\Program Files\Cantera``) you must run the ``scons install`` command in a
  command prompt that has been launched by selecting the *Run as Administrator*
  option.

.. _sec-windows-reqs:

Windows Requirements
^^^^^^^^^^^^^^^^^^^^^^^

* Windows 7 or later; either 32-bit or 64-bit

* To build any of the Cantera modules, you will need to install

  * Python

    * https://www.python.org/downloads/

    * Cantera supports Python 3.5 and higher

    * Be sure to choose the appropriate architecture for your system - either
      32-bit or 64-bit

    * When installing, make sure to choose the option to add to your ``PATH``

  * SCons

    * https://pypi.org/project/SCons/

    * Be sure to choose the appropriate architecture for your system - either
      32-bit or 64-bit

  * One of the following supported compilers

    * Microsoft compilers

      * https://visualstudio.microsoft.com/downloads/

      * Known to work with Visual Studio 2013 (MSVC 12.0), Visual Studio 2015
        (MSVC 14.0), Visual Studio 2017 (MSVC 14.1), and Visual Studio 2019
        (MSVC 14.2).

    * MinGW compilers

      * http://mingw-w64.org/

      * http://tdm-gcc.tdragon.net/

      * Known to work with Mingw-w64 3.0, which provides GCC 4.8. Expected to
        work with any version that provides a supported version of GCC and
        includes C++11 thread support.

      * The version of MinGW from http://www.mingw.org/ cannot be used to build
        Cantera. Users must use MinGW-w64 or TDM-GCC.

  * The Boost headers

    * https://www.boost.org/doc/libs/1_63_0/more/getting_started/windows.html#get-boost

    * It is not necessary to compile the Boost libraries since Cantera only uses
      the headers from Boost

* In addition to the general software, building the Python module also requires
  several Python packages: Cython, NumPy, and Ruamel.yaml. All of these can be
  installed using `pip`:

  .. code:: bash

     py -m pip install cython numpy ruamel.yaml

* In addition to the general software, building the MATLAB toolbox also requires:

  * MATLAB version later than 2009a

    * Typically installed to::

        C:\Program Files\MATLAB\R20YYn

      where ``YY`` is a two digit year and ``n`` is either ``a`` or ``b``

.. container:: container

   .. container:: row

      .. container:: col-12 text-right

         .. container:: btn btn-primary
            :tagname: a
            :attributes: href=source-code.html

            Next: Download the Source Code

.. _sec-macos:

macOS
-----

General Notes
^^^^^^^^^^^^^

* Cantera 2.5.0 and higher do not support Python 2, which may be installed by default
  on your computer. You must install Python 3 from another source to be able to build
  Cantera. The instructions below use Homebrew.

* To download the source code, installing ``git`` via HomeBrew is highly recommended.

.. _sec-mac-os-reqs:

macOS Requirements
^^^^^^^^^^^^^^^^^^

* macOS 10.14 (Mojave) or newer required to install Homebrew

* To build any of the Cantera modules, you will need to install

  * Xcode

    * Download and install from the App Store

    * From a Terminal, run:

      .. code:: bash

         sudo xcode-select --install

      and agree to the Xcode license agreement

  * Homebrew

    * https://brew.sh

    * From a Terminal, run:

      .. code:: bash

         /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

  * Once Homebrew is installed, the rest of the dependencies can be installed with:

    .. code:: bash

       brew install python scons boost git libomp

    Note that brew installs Python 3 by default, but does not over-write the existing system Python.
    When you want to use the brew-installed Python, you should use ``$(brew --prefix)/bin/python3``.

* In addition to the general software, building the Python module also requires:

  .. code:: bash

     $(brew --prefix)/bin/pip3 install cython numpy ruamel.yaml

* In addition to the general software, building the Fortran module also requires:

  .. code:: bash

     brew install gcc

* In addition to the general software, building the MATLAB toolbox also requires:

  * MATLAB version later than 2009a

    * Typically installed to::

        /Applications/MATLAB_R20YYn.app

      where ``YY`` is a two digit year and ``n`` is either ``a`` or ``b``

.. container:: container

   .. container:: row

      .. container:: col-12 text-right

         .. container:: btn btn-primary
            :tagname: a
            :attributes: href=source-code.html

            Next: Download the Source Code
