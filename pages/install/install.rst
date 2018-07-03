.. title: Installing Cantera
.. slug: index
.. date: 2018-06-15 11:20:56 UTC-04:00
.. description: Installation instructions for Cantera
.. type: text

.. _sec-install:

.. jumbotron::

    .. raw:: html

        <h1 class="display-3">Installing Cantera</h1>

    .. class:: lead

        The following instructions detail how to install Cantera on a variety
        of platforms. We highly recommend that if you want to use only the
        Python interface, you install via the Conda option. We also highly
        recommend that new users use the Python interface. If you want to use
        one of the other interfaces, please select the installation instructions
        for your platform.

.. container:: accordion

   .. container:: card

      .. container:: card-header btn btn-link text-left
         :attributes: id=heading-conda
                      data-toggle=collapse
                      href=#collapse-conda
                      aria-expanded=false
                      aria-controls=collapse-conda
         :tagname: a

         Conda Install Instructions (Highly recommended for all users)

      .. container:: collapse
         :attributes: id=collapse-conda
                      aria-labelledby=heading-conda
                      data-parents=#accordion

         .. container:: card-body

            .. _sec-install-conda:

            **Conda**

            `Anaconda <https://www.anaconda.com/downloads>`_ and `Miniconda
            <https://conda.io/miniconda.html>`_ are Python distributions for which
            Cantera is available through the ``conda`` package manager. Both distributions are
            available for Linux, macOS, and Windows. The base Anaconda distribution includes
            a large number of Python packages that are widely used in scientific
            applications. Miniconda is a minimal distribution, where all of the packages
            available in Anaconda can be installed using the package manager. Note that
            installing Cantera using conda will only provide the Cantera Python module. If
            you want to use the other Cantera interfaces, see the OS-specific installation
            options below.

            For more details on how to use conda, see the `conda documentation
            <https://conda.io/docs/intro.html>`_.

            **Option 1: Create a new environment for Cantera**

            If you have just installed Anaconda or Miniconda, the following instructions
            will create a conda environment where you can use Cantera. For this example, the
            environment is named ``spam``. From the command line (or the Anaconda Prompt
            on Windows), run::

                conda create -n spam -c cantera cantera ipython matplotlib

            This will create an environment with Cantera, IPython, Matplotlib, and all their
            dependencies installed. Although conda can install a large set of packages by
            default, it is also possible to install packages such as Cantera that are
            maintained independently. These additional channels from which packages may be
            obtained are specified by adding the ``-c`` option in the ``install`` or
            ``create`` commands. In this case, we want to install Cantera from the
            ``cantera`` channel, so we add ``-c cantera`` and to tell conda to look at the
            ``cantera`` channel in addition to the default channels.

            You can activate this environment to use the scripts and modules installed in
            it by running::

                conda activate spam

            **Option 2: Install Cantera in an existing environment**

            First, activate your environment (assumed to be named ``baked_beans``; if you've
            forgotten the name of the conda environment you wanted to use, the command
            ``conda env list`` can help). This is done by running::

                conda activate baked_beans

            Then, install Cantera by running::

                conda install -c cantera cantera

            **Option 3: Install the development version of Cantera**

            To install a recent development snapshot (i.e., an alpha or beta version) of
            Cantera in an existing environment, run::

                conda install -c cantera/label/dev cantera

            If you later want to revert back to the stable version, first remove and then
            reinstall Cantera::

                conda remove cantera
                conda install -c cantera cantera

   .. container:: card

      .. container:: card-header btn btn-link text-left
         :attributes: id=heading-windows
                      data-toggle=collapse
                      href=#collapse-windows
                      aria-expanded=false
                      aria-controls=collapse-windows
         :tagname: a

         Windows Install Instructions

      .. container:: collapse
         :attributes: id=collapse-windows
                      aria-labelledby=heading-windows
                      data-parents=#accordion

         .. container:: card-body

            .. _sec-install-windows:

            **Windows**

            Windows installers are provided for stable versions of Cantera. These
            installation instructions are for Cantera 2.4.0. Use these installers if you
            want to work with a copy of Python downloaded from `Python.org
            <https://www.python.org/>`__. If you are using Anaconda / Miniconda, see the
            directions :ref:`above <sec-install-conda>`.

            1. **Choose your Python version and architecture**

               - On Windows, Installers are provided for Python 2.7, Python 3.4, Python 3.5,
                 and Python 3.6. Python 3.6 is recommended unless you need to use legacy
                 code that does not work with Python 3. You can install multiple Cantera
                 Python modules simultaneously. Note that Cantera 2.4 will be the last
                 version to support Python 2.7.

               - Cantera supports both 32- and 64- bit Python installations.

               - You need choose the matching Cantera installer for your Python version and
                 machine architecture.

               - The rest of these instructions will refer to your chosen version of Python
                 as *X.Y*.

               - If you are using Matlab, you must use the same architecture for Cantera and
                 Matlab. Matlab defaults to 64-bit if you are running a 64-bit operating
                 system.

            2. **Install Python**

               - Go to `python.org <https://www.python.org/>`__.

                 - *64-bit*: Download the most recent "Windows X86-64 MSI Installer" for
                   Python *X.Y*.
                 - *32-bit*: Download the most recent "Windows x86 MSI Installer" for
                    Python *X.Y*.

               - Run the installer. The default installation options should be fine.

               - Python is required in order to work with ``.cti`` input files even if you are
                 not using the Python interface to Cantera.

               - Cantera can also be used with alternative Python distributions such as the
                 Enthought `Canopy <https://www.enthought.com/product/canopy/>`_
                 distribution. These distributions will generally be based on the 64-bit
                 version of Python 2.7, and will include Numpy as well as many other
                 packages useful for scientific users.

            3. **Install the Visual C++ Redistributable for Visual Studio 2015**

               - If you are using Python 3.5 or Python 3.6 you can skip this step as this
                 will have already been installed when you installed Python.

               - Go to the `Microsoft Visual C++ Redistributable Download Page
                 <https://www.microsoft.com/en-us/download/details.aspx?id=48145>`__.

                 - *64-bit*: Download ``vc_redist.x64.exe``

                 - *32-bit*: Download ``vc_redist.x86.exe``

               - Run the installer.

               - If this package is not installed, you will encounter the following error
                 when importing the ``cantera`` module::

                    ImportError: DLL load failed: The specified module could not be found.

            4. **Install Numpy and optional Python packages**

               - Go to the `Unofficial Windows Binaries for Python Extension Packages page
                 <http://www.lfd.uci.edu/~gohlke/pythonlibs/#numpy>`_.

               - Download the most recent release (distributed as a "wheel" archive) of the
                 1.x series for Python *X.Y* that matches your Python architecture. In the
                 filename, the digits after "cp" indicate the Python version, e.g.
                 ``numpy‑1.11.2+mkl‑cp35‑none‑win_amd64.whl`` is the installer for 64-bit
                 Python 3.5. The Windows installers for Cantera 2.4.0 require Numpy 1.10 or
                 newer.

               - From an administrative command prompt, install the downloaded wheel using
                 pip, e.g.,::

                     c:\python35\scripts\pip.exe install "%USERPROFILE%\Downloads\numpy‑1.11.2+mkl‑cp35‑none‑win_amd64.whl"

               - If you plan on using Cantera from Python, note that we highly recommend
                 installing the conda package. If you plan to continue using this Python
                 installation, you may also want to install IPython (an advanced
                 interactive Python interpreter) and Matplotlib (a plotting library), which
                 are also available from the above link (note that you may also need to
                 download additional dependencies for each of these packages). Matplotlib
                 is required to run some of the Python examples.

            5. **Remove old versions of Cantera**

               - Use The Windows "Add/Remove Programs" interface

               - Remove both the main Cantera package and the Python module.

               - The Python module will be listed as "Python *X.Y* Cantera ..."

            6. **Install Cantera**

               - Go to the `Cantera Releases <https://github.com/Cantera/cantera/releases>`_
                 page.

                 - *64-bit*: Download **Cantera-2.4.0-x64.msi** and
                   **Cantera-Python-2.4.0-x64-pyX.Y.msi**.
                 - *32-bit*: Download **Cantera-2.4.0-x86.msi** and
                   **Cantera-Python-2.4.0-x86-pyX.Y.msi**.

               - If you are only using the Python module, you do not need to download and
                 install the base package (the one without Python in the name).

               - Run the installer(s).

            7. **Configure Matlab** (optional)

               - Set the environment variable ``PYTHON_CMD``

                 - From the *Start* screen or menu type "edit environment" and select
                   "Edit environment variables for your account".
                 - Add a *New* variable with ``PYTHON_CMD`` as the *name* and the full path
                   to the Python executable (e.g. ``C:\python35\python.exe``) as the
                   *value*.
                 - Setting ``PYTHON_CMD`` is not necessary if the path to ``python.exe`` is
                   in your ``PATH`` (which can be set from the same configuration dialog).

               - Launch Matlab

               - Go to *File->Set Path...*

               - Select *Add with Subfolders*

               - Browse to the folder ``C:\Program Files\Cantera\matlab\toolbox``

               - Select *Save*, then *Close*.

            8. **Test the installation**

               - Python:

                 .. code-block:: python

                    import cantera
                    gas = cantera.Solution('gri30.cti')
                    h2o = cantera.PureFluid('liquidvapor.cti', 'water')

               - Matlab:

                 .. code-block:: matlab

                    gas = IdealGasMix('gri30.cti')
                    h2o = Solution('liquidvapor.cti','water')

   .. container:: card

      .. container:: card-header btn btn-link text-left
         :attributes: id=heading-macos
                      data-toggle=collapse
                      href=#collapse-macos
                      aria-expanded=false
                      aria-controls=collapse-macos
         :tagname: a

         macOS Install Instructions

      .. container:: collapse
         :attributes: id=collapse-macos
                      aria-labelledby=heading-macos
                      data-parents=#accordion

         .. container:: card-body

            .. _sec-install-macos:

            **macOS**

            Cantera can be installed on macOS using either Homebrew or Anaconda / Miniconda.
            If you are using Anaconda / Miniconda (which we recommend if you will only use
            the Python interface), see the directions :ref:`above <sec-install-conda>`. With
            Homebrew, the current stable or development version of Cantera can be installed,
            and both the Python 2.7 and Python 3.x modules are available, as well as the
            Matlab toolbox.

            These instructions have been tested on macOS 10.13 (High Sierra) with XCode
            9.4.1. If you've used Homebrew before, you can skip any steps which have already
            been completed.

            1. **Install Xcode and Homebrew**

               - Install Xcode from the App Store

               - From a Terminal, run::

                   sudo xcode-select --install
                   sudo xcodebuild -license

                 and agree to the Xcode license agreement.

               - Install `Homebrew <https://brew.sh/>`_ by running the following command in a
                 Terminal::

                   ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

            2. **Set up the environment**

               - Verify that your ``PATH`` is set up to use Homebrew's version of Python by
                 running::

                     echo $PATH

                 If this command does not print ``/usr/local/bin`` somewhere in it, run the
                 following command in the Terminal::

                     echo "export PATH=/usr/local/bin:$PATH" >> ~/.bash_profile

                 and then run::

                     source ~/.bash_profile

                 You only have to run these commands once.

            3. **Compile and install Cantera**

               - To compile and install Cantera using the default configuration, run::

                     brew install cantera

               - The following options are supported:

                 ``--HEAD``
                     Installs the current development version of Cantera.

                 ``--with-python@2``
                     Install the Python 2 module.

                 ``--with-matlab=/Applications/MATLAB_R2014a.app/``
                     Installs the Matlab toolbox (with the path modified to match your
                     installed Matlab version)

                 ``--with-minimal``
                     Install only the minimal Python 3 interface needed to process input
                     files. Recommended if the Matlab interface will be the only one used.

                 ``--with-graphviz``
                     Install the Graphviz library to be able to produce reaction path diagrams

                 ``--without-test``
                     NOT RECOMMENDED! Disable automatic testing of Cantera during the
                     installation process.

               - These options are specified as additional arguments to the ``brew install``
                 command, e.g.::

                     brew install cantera --HEAD --with-python@2

               - If you are installing the Matlab toolbox, the recommended command is::

                     brew install cantera --with-matlab=/Applications/MATLAB_R2014a.app/ --with-minimal

               - If something goes wrong with the Homebrew install, re-run the command with
                 the ``-v`` flag to get more verbose output that may help identify the
                 source of the problem::

                     brew install -v cantera

               - If Homebrew claims that it can't find a formula named ``cantera``, you may
                 be able to fix it by running the command::

                     brew doctor

            4. **Test Cantera Installation (Python)**

               - The Python examples will be installed in::

                     /usr/local/lib/pythonX.Y/site-packages/cantera/examples/

                 where ``X.Y`` is your Python version, e.g. ``3.6``.

               - You may find it convenient to copy the examples to your Desktop::

                     cp -r /usr/local/lib/python3.6/site-packages/cantera/examples ~/Desktop/cantera_examples

               - To run an example::

                     cd cantera_examples/reactors
                     python3 reactor1.py

               - Note that Homebrew installs Python 3 by default, but does not install an
                 unversioned ``python`` executable onto the ``PATH``. Therefore, you should
                 always specify ``python3`` whenever you want to run a command.

               - You can install additional Python packages (e.g., IPython, Matplotlib,
                 etc.) using the command::

                     pip3 install package

                 Matplotlib is required to run some of the Python examples.

            5. **Test Cantera Installation (Matlab)**

               - The Matlab toolbox, if enabled, will be installed in::

                     /usr/local/lib/cantera/matlab

               - To use the Cantera Matlab toolbox, run the following commands in Matlab
                 (each time you start Matlab), or add them to a ``startup.m`` file located
                 in ``~/Documents/MATLAB``::

                     addpath(genpath('/usr/local/lib/cantera/matlab'))
                     setenv('PYTHON_CMD', '/usr/local/bin/python3')

               - The Matlab examples will be installed in::

                     /usr/local/share/cantera/samples/matlab

               - You may find it convenient to copy the examples to your user directory::

                     cp -r /usr/local/share/cantera/samples/matlab ~/Documents/MATLAB/cantera_examples

   .. container:: card

      .. container:: card-header btn btn-link text-left
         :attributes: id=heading-ubuntu
                      data-toggle=collapse
                      href=#collapse-ubuntu
                      aria-expanded=false
                      aria-controls=collapse-ubuntu
         :tagname: a

         Ubuntu Install Instructions

      .. container:: collapse
         :attributes: id=collapse-ubuntu
                      aria-labelledby=heading-ubuntu
                      data-parents=#accordion

         .. container:: card-body

            .. _sec-install-ubuntu:

            **Ubuntu**

            Ubuntu packages are provided for recent versions of Ubuntu using a Personal
            Package Archive (PPA). As of Cantera 2.4.0, packages are available for Ubuntu
            Ubuntu 16.04 (Xenial Xerus) and Ubuntu 17.10 (Artful Aardvark). To see which
            Ubuntu releases and Cantera versions are currently available, visit
            https://launchpad.net/~speth/+archive/ubuntu/cantera

            The available packages are:

            - ``cantera-python`` - The Cantera Python module for Python 2.

            - ``cantera-python3`` - The Cantera Python module for Python 3.

            - ``cantera-dev`` - Libraries and header files for compiling your own C++ and
              Fortran 90 programs that use Cantera.

            To add the Cantera PPA::

                sudo aptitude install python-software-properties
                sudo apt-add-repository ppa:speth/cantera
                sudo aptitude update

            To install all of the Cantera packages::

                sudo aptitude install cantera-python cantera-python3 cantera-dev

            or install whichever subset you need by adjusting the above command.

            If you plan on using Cantera from Python, you may also want to install IPython
            (an advanced interactive Python interpreter) and Matplotlib (a plotting
            library). Matplotlib is required to run some of the Python examples. For Python
            2, these packages can be installed with::

                pip2 install ipython matplotlib

            And for Python 3, these packages can be installed with::

                pip3 install ipython matplotlib

            You may need to install ``pip`` first; instructions can be found on the `pip
            installation instructions.
            <https://pip.pypa.io/en/latest/installing/index.html#install-pip>`_ You may need to
            have superuser access to install packages into the system directories.
            Alternatively, you can add ``--user`` after ``pip install`` but before the
            package names to install into your local user directory.

   .. container:: card

      .. container:: card-header btn btn-link text-left
         :attributes: id=heading-other-linux
                      data-toggle=collapse
                      href=#collapse-other-linux
                      aria-expanded=false
                      aria-controls=collapse-other-linux
         :tagname: a

         Other Linux Distributions Install Instructions

      .. container:: collapse
         :attributes: id=collapse-other-linux
                      aria-labelledby=heading-other-linux
                      data-parents=#accordion

         .. container:: card-body

            .. _sec-install-other-linux:

            **Other Linux Distributions**

            On Linux distributions other than Ubuntu, we recommend that you use the conda
            package, described :ref:`above <sec-install-conda>`. However, due to the
            limitations of distributing binary packages, the conda package will not work on
            all Linux distributions (for instance, RHEL 6 is not supported). For these
            platforms, or if you want to use an interface other than the Python interface,
            you'll have to compile and install Cantera yourself. Instructions for that are
            in the :html:`<a href=#collapse-compiling data-toggle=collapse>Compiling section</a>`
            below.

   .. container:: card

      .. container:: card-header btn btn-link text-left
         :attributes: id=heading-compiling
                      data-toggle=collapse
                      href=#collapse-compiling
                      aria-expanded=false
                      aria-controls=collapse-compiling
         :tagname: a

         Compiling Cantera from Source

      .. container:: collapse
         :attributes: id=collapse-compiling
                      aria-labelledby=heading-compiling
                      data-parents=#accordion

         .. container:: card-body

            **Compiling Cantera from Source: Quickstart**

            Compiling Cantera from source code uses the SCons build system and a C/C++ compiler. If
            you also want to build the Python, Matlab, or Fortran interfaces, you'll need Cython +
            Numpy, Matlab, or a Fortran compiler installed, respectively. Specific instructions to
            install these things are platform-dependent, and more detail is provided in the sections
            linked below.

            The recommended way to obtain a copy of the source code is directly from the main
            version control repository on GitHub via the command

            .. code:: bash

               git clone https://github.com/Cantera/cantera.git
               cd cantera

            which clones the code into a folder called ``cantera`` and changes into that directory.
            At this point, you can run

            .. code:: bash

               scons help

            to see a list of all of the configuration options, including their defaults. On
            \*nix-type systems, the defaults will usually pick up the appropriate compilers and
            Python versions. The command

            .. code:: bash

               scons build

            will build Cantera using all the default options; additional options can be specified
            by

            .. code:: bash

               scons build option=value option=value

            Installing Cantera into the default directories is done by

            .. code:: bash

               scons install

            which may require super-user permissions if the installation directory is protected.

            **Compiling Cantera from Source: The Detailed Way**

            If you want or need more detail, the following sections go into depth on all of the
            options and requirements to build Cantera from source.

            * :ref:`Installation Requirements <sec-installation-reqs>`
            * :ref:`Getting the Source Code <sec-source-code>`
            * :ref:`Determine Configuration Options <sec-determine-config>`
            * :ref:`Cantera's Dependencies <sec-dependencies>`
            * :ref:`Special Compiling Cases <sec-special-compiling-cases>`
            * :ref:`Show me all of the configuration options <scons-config>`
