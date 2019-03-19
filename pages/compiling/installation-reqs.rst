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

.. _sec-conda-reqs:

Conda Requirements
^^^^^^^^^^^^^^^^^^

* Install `Anaconda <https://www.anaconda.com/download/>`__ or
  `Miniconda <https://conda.io/miniconda.html>`__. We highly recommend using the Python 3 version
  unless you have a specific reason not to.

* On Windows, use the Anaconda Prompt to run the following steps (available from the Start Menu).
  On macOS and Linux, the installer should add the appropriate activation mechanism for your normal terminal by
  default. You can test this by running

  .. code:: bash

     conda --version

  in the terminal. If there's no output or an error appears, locate your Conda installation and run the
  following code in the terminal:

  .. code:: bash

     /path/to/conda/install/folder/bin/conda init [name of your shell]

  If you haven't changed any defaults for your terminal, the name of your shell is most likely ``bash``.
  Then restart your terminal or shell.

* Create an environment with the dependencies to build Cantera

  .. code:: bash

     conda create --name cantera python=3 scons cython boost numpy
     conda activate cantera

* (Optional) If you also want to build the documentation, after you've created the environment and
  activated it, you'll also need to install the following dependencies

  .. code:: bash

     conda install sphinx doxygen graphviz
     pip install sphinxcontrib-matlabdomain sphinxcontrib-katex sphinxcontrib-doxylink

* (Optional) If you also want to build the Python 2 interface (this is unlikely), create another
  environment for those dependencies:

  .. code:: bash

     conda create --name py2k python=2 numpy
     conda activate py2k
     pip install 3to2
     conda activate cantera

  and after you've :ref:`cloned the source code <sec-source-code>`, add the following lines to a
  file called ``cantera.conf``  in the root of the source directory (creating the file if it
  doesn't exist).

  On macOS and Linux, add the following code to your ``cantera.conf`` file:

  .. code:: python

     python2_package = 'full'
     python2_cmd = '/path/to/conda/install/folder/envs/py2k/bin/python'

  On Windows, add the following code to your ``cantera.conf`` file:

  .. code:: bash

     python2_package = 'full'
     python2_cmd = '/path/to/conda/install/folder/envs/py2k/python.exe

  Note that it is not possible to simultaneously install the Python 2 and Python 3 interfaces;
  you'll have to use separate builds if you want to install both (however, this is an unlikely
  scenario). In addition, note Cantera 2.4 is the last version that will support Python 2. If
  you checked out the most recent commit on the ``master`` branch of the git repository,
  support for Python 2 has already been dropped and you cannot use these options.

* After you've :ref:`cloned the source code <sec-source-code>`, configure the Cantera build by
  adding the following options to a file called ``cantera.conf`` in the root of the source directory
  (creating the file if it doesn't exist).

  On macOS and Linux, add the following code to your ``cantera.conf`` file:

  .. code:: python

     python3_package = 'full'
     boost_inc_dir = '/path/to/conda/install/folder/envs/cantera/include'

  On Windows, add the following code to your ``cantera.conf`` file:

  .. code:: python

     python3_package = 'full'
     boost_inc_dir = '/path/to/conda/install/folder/envs/cantera/Library/include'

  .. note::

     If you're using commits from the ``master`` branch of the git repository, Python 2 is no
     longer supported and the version-specific Python package options have been dropped. You
     should just use ``python_package`` instead of ``python3_package`` if you're compiling the
     ``master`` branch.

* Now you can build Cantera with

  .. code:: bash

     scons build

* To install Cantera, use the command

  .. code:: bash

     scons install prefix=$CONDA_PREFIX

  to make sure that the files end up in the right directory

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
  ``pip``.

* Users of other distributions should install the equivalent packages, which
  may have slightly different names.

* In addition to the operating systems below, Cantera should work on any
  Unix-like system where the necessary prerequisites are available, but some
  additional configuration may be required.

.. _sec-ubuntu-debian-reqs:

Ubuntu & Debian
^^^^^^^^^^^^^^^

* Ubuntu 14.04 LTS (Trusty Tahr) or newer is required; 18.04 LTS (Bionic Beaver)
  or newer is recommended

* Debian 7.0 (Wheezy) or newer; 9.0 (Stretch) or newer is recommended

* The following packages must be installed to build any of the Cantera modules using
  your choice of package manager::

      g++ python scons libboost-dev

* In addition to the general packages, building the Python 2 module also requires::

      cython python-dev python-numpy python-numpy-dev python-setuptools

* In addition to the general packages, building the Python 3 module also requires::

      cython python3 python3-dev python3-setuptools python3-numpy

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

* In addition to the general packages, building the Python 2 module also requires::

      python-setuptools python-devel Cython numpy

* In addition to the general packages, building the Python 3 module also requires::

      python3 python3-setuptools python3-devel Cython python3-numpy

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

* OpenSUSE 13.2 or newer; Leap 42.2 or newer recommended

* The following packages must be installed to build any of the Cantera modules using
  your choice of package manager::

      gcc-c++ python scons boost-devel

* In addition to the general packages, building the Python 2 module also requires::

      python-Cython python-devel python-numpy python-numpy-devel python-setuptools

* In addition to the general packages, building the Python 3 module also requires::

      python-Cython python3 python3-devel python3-setuptools python3-numpy python3-numpy-devel

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
  that you use a 64-bit version of Python to handle this automatically. Note
  that the default download from the Python website
  (https://www.python.org) is for a 32-bit installer, and you will
  need to select the 64-bit installer specifically.

* It is generally helpful to have SCons and Python in your ``PATH`` environment
  variable. This can be done by checking the appropriate box during the
  installation of Python or can be accomplished by adding the top-level Python
  directory and the ``Scripts`` subdirectory (e.g.,
  ``C:\Python36;C:\Python36\Scripts``) to your ``PATH``. The dialog to change
  the ``PATH`` is accessible from::

      Control Panel > System and Security > System > Advanced System Settings > Environment Variables

  Make sure that the installation of Python that has SCons comes first on your
  ``PATH``.

* In order to use SCons to install Cantera to a system folder (e.g. ``C:\Program
  Files\Cantera``) you must run the ``scons install`` command in a command
  prompt that has been launched by selecting the *Run as Administrator* option.

.. _sec-windows-reqs:

Windows Requirements
^^^^^^^^^^^^^^^^^^^^^^^

* Windows 7 or later; either 32-bit or 64-bit

* To build any of the Cantera modules, you will need to install

  * Python

    * https://www.python.org/downloads/

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

      * Known to work with Visual Studio 2013 (MSVC 12.0) and Visual Studio 2015
        (MSVC 14.0)

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

  * Pip

    * Most packages will be downloaded as Wheel (``*.whl``) files. To install
      these files, type::

          pip install C:\Path\to\downloaded\file\package-file-name.whl

  * Cython

    * http://www.lfd.uci.edu/~gohlke/pythonlibs/#cython

    * Download the ``*.whl`` file for your Python architecture (32-bit or 64-bit)
      and Python X.Y (indicated by ``cpXY`` in the file name), where X and Y are the
      major and minor versions of the Python where you installed SCons.

    * Cython must be installed in the version of Python that has SCons installed

  * NumPy

    * http://www.lfd.uci.edu/~gohlke/pythonlibs/#numpy

    * Download the ``*.whl`` file for your Python architecture (32-bit or 64-bit)
      and Python X.Y (indicated by ``cpXY`` in the file name), where X and Y are the
      major and minor versions of Python.

* In addition to the general software, building the Python 3 module also requires

  * Python 3

    * https://www.python.org/downloads/

    * Cantera supports Python 3.3 and higher

    * Be sure to choose the appropriate architecture for your system - either
      32-bit or 64-bit

    * Be careful that the installation of Python with SCons installed comes before the one without,
      if you have multiple versions of Python installed.

  * Pip

    * Most packages will be downloaded as Wheel (``*.whl``) files. To install
      these files, type::

          pip3 install C:\Path\to\downloaded\file\package-file-name.whl

   * Cython

     * http://www.lfd.uci.edu/~gohlke/pythonlibs/#cython

     * Download the ``*.whl`` file for your Python architecture (32-bit or 64-bit)
       and Python X.Y (indicated by ``cpXY`` in the file name), where X and Y are the
       major and minor versions of the Python where you installed SCons.

     * Cython must be installed in the version of Python that has SCons installed

   * NumPy

     * http://www.lfd.uci.edu/~gohlke/pythonlibs/#numpy

     * Download the ``*.whl`` file for your Python architecture (32-bit or 64-bit)
       and Python X.Y (indicated by ``cpXY`` in the file name), where X and Y are the
       major and minor versions of Python.

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

OS X & macOS
------------

General Notes
^^^^^^^^^^^^^

* It is not recommended to use the system-installed version of Python to build
  Cantera. Instead, the following instructions use Homebrew to install a
  separate copy of Python, independent from the system Python.

* To download the source code, installing ``git`` via HomeBrew is highly recommended.

* Cython is only required to be installed for the version of Python that also
  has SCons installed; following the instructions below will install Cython for
  the version of Python 2 installed in the system directories. The minimum
  compatible Cython version is 0.23.

.. _sec-mac-os-reqs:

OS X & macOS Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^

* OS X 10.9 (Mavericks) or newer required; 10.10 (Yosemite) or newer is recommended

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

         /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

  * Once Homebrew is installed, the rest of the dependencies can be installed with:

    .. code:: bash

       brew install python scons boost

    Note that brew installs Python 3 by default, but does not over-write the existing system Python.
    When you want to use the brew-installed Python, you should use ``python3``.

* In addition to the general software, building the Python 2 module also requires:

  .. code:: bash

     brew install python@2
     pip install numpy

* In addition to the general software, building the Python 3 module also requires:

  .. code:: bash

     pip3 install cython numpy

  Note that Cython should be installed into the version of Python that has SCons
  installed.

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
