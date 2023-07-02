Options List
^^^^^^^^^^^^

.. _msvc-version:

*  ``msvc_version``: [ ``string`` ]
   Version of Visual Studio to use. The default is the newest installed version.
   Note that since multiple MSVC toolsets can be installed for a single version of
   Visual Studio, you probably want to use ``msvc_toolset_version`` unless you
   specifically installed multiple versions of Visual Studio. Windows MSVC only.

   -  default: ``''``

.. _msvc-toolset-version:

*  ``msvc_toolset_version``: [ ``string`` ]
   Version of the MSVC toolset to use. The default is the default version for
   the given ``msvc_version``. Note that the toolset selected here must be
   installed in the MSVC version selected by ``msvc_version``. The default
   toolsets associated with various Visual Studio versions are:
   
   * ``14.1`` (``14.1x``): Visual Studio 2017
   * ``14.2`` (``14.2x``): Visual Studio 2019
   * ``14.3`` (``14.3x``): Visual Studio 2022.
   
   For version numbers in parentheses, ``x`` is a placeholder for a minor version
   number. Windows MSVC only.

   -  default: ``''``

.. _target-arch:

*  ``target_arch``: [ ``'amd64'`` | ``'x86'`` ]
   Target architecture. The default is the same architecture as the
   installed version of Python. Windows only.

   -  default: platform dependent

      -  Windows: ``'amd64'``

.. _toolchain:

*  ``toolchain``: [ ``'msvc'`` | ``'mingw'`` | ``'intel'`` ]
   The preferred compiler toolchain. If MSVC is not on the path but
   ``g++`` is on the path, ``mingw`` is used as a backup. Windows only.

   -  default: platform dependent

      -  Windows: ``'msvc'``

.. _ar:

*  ``AR``: [ ``string`` ]
   The archiver to use.

   -  default: ``'${AR}'``

.. _cxx:

*  ``CXX``: [ ``string`` ]
   The C++ compiler to use.

   -  default: ``'${CXX}'``

.. _cxx-flags:

*  ``cxx_flags``: [ ``string`` ]
   Compiler flags passed to the C++ compiler only. Separate multiple
   options with spaces, for example, ``"cxx_flags='-g -Wextra -O3 --std=c++14'"``

   -  default: compiler dependent

      -  If using ``MSVC``: ``'/EHsc /std:c++17'``
      -  Otherwise: ``'-std=c++17'``

.. _cc:

*  ``CC``: [ ``string`` ]
   The C compiler to use. This is only used to compile CVODE.

   -  default: ``'${CC}'``

.. _cc-flags:

*  ``cc_flags``: [ ``string`` ]
   Compiler flags passed to both the C and C++ compilers, regardless of
   optimization level.

   -  default: compiler dependent

      -  If using ``MSVC``: ``'/MD /nologo /D_SCL_SECURE_NO_WARNINGS /D_CRT_SECURE_NO_WARNINGS'``
      -  If using ``Clang``: ``'-fcolor-diagnostics'``
      -  Otherwise: ``''``

.. _prefix:

*  ``prefix``: [ ``path/to/prefix`` ]
   Set this to the directory where Cantera should be installed. If the Python
   executable found during compilation is managed by ``conda``, the installation
   ``prefix`` defaults to the corresponding environment and the ``conda`` layout
   will be used for installation (specifying any of the options ``prefix``,
   ``python_prefix``, ``python_cmd``, or ``layout`` will override this default). On
   Windows systems, ``$ProgramFiles`` typically refers to ``"C:\Program Files"``.

   -  default: platform dependent

      -  Windows: ``'$ProgramFiles\Cantera'``
      -  Otherwise: ``'/usr/local'``

.. _libdirname:

*  ``libdirname``: [ ``path/to/libdirname`` ]
   Set this to the directory where Cantera libraries should be installed.
   Some distributions (for example, Fedora/RHEL) use ``lib64`` instead of ``lib``
   on 64-bit systems or could use some other library directory name instead of
   ``lib``, depending on architecture and profile (for example, Gentoo ``libx32``
   on x32 profile). If the user didn't set the ``libdirname`` configuration
   variable, set it to the default value ``lib``

   -  default: ``'lib'``

.. _python-package:

*  ``python_package``: [ ``'n'`` | ``'y'`` | ``'full'`` | ``'minimal'`` | ``'none'`` | ``'default'`` ]
   If you plan to work in Python, then you need the ``full`` Cantera Python
   package. If, on the other hand, you will only use Cantera from some
   other language (for example, MATLAB or Fortran 90/95) and only need Python
   to process YAML files, then you only need a ``minimal`` subset of the
   package and Cython and NumPy are not necessary. The ``none`` option
   doesn't install any components of the Python interface. The default
   behavior is to build the full Python module for whichever version of
   Python is running SCons if the required prerequisites (NumPy and
   Cython) are installed. Note: ``y`` is a synonym for ``full`` and ``n``
   is a synonym for ``none``.

   -  default: ``'default'``

.. _python-sdist:

*  ``python_sdist``: [ ``'yes'`` | ``'no'`` ]
   Setting this option to True builds the Python sdist.

   -  default: ``'no'``

.. _python-cmd:

*  ``python_cmd``: [ ``path/to/python_cmd`` ]
   Cantera needs to know where to find the Python interpreter. If
   ``PYTHON_CMD`` is not set, then the configuration process will use the
   same Python interpreter being used by SCons.

   -  default: ``'${PYTHON_CMD}'``

.. _python-prefix:

*  ``python_prefix``: [ ``path/to/python_prefix`` ]
   Use this option if you want to install the Cantera Python package to
   an alternate location. On Unix-like systems, the default is the same
   as the ``prefix`` option. If the ``python_prefix`` option is set to
   the empty string or the ``prefix`` option is not set, then the package
   will be installed to the system default ``site-packages`` directory.
   To install to the current user's ``site-packages`` directory, use
   ``python_prefix=USER``.

   -  default: platform dependent

      -  Otherwise: ``''``

.. _matlab-toolbox:

*  ``matlab_toolbox``: [ ``'n'`` | ``'y'`` | ``'default'`` ]
   This variable controls whether the MATLAB toolbox will be built. If
   set to ``y``, you will also need to set the value of the ``matlab_path``
   variable. If set to ``default``, the MATLAB toolbox will be built if
   ``matlab_path`` is set.

   -  default: ``'default'``

.. _matlab-path:

*  ``matlab_path``: [ ``path/to/matlab_path`` ]
   Path to the MATLAB install directory. This should be the directory
   containing the ``extern``, ``bin``, etc. subdirectories. Typical values
   are: ``"C:\Program Files\MATLAB\R2021a"`` on Windows,
   ``"/Applications/MATLAB_R2021a.app"`` on macOS, or
   ``"/opt/MATLAB/R2021a"`` on Linux.

   -  default: ``''``

.. _f90-interface:

*  ``f90_interface``: [ ``'n'`` | ``'y'`` | ``'default'`` ]
   This variable controls whether the Fortran 90/95 interface will be
   built. If set to ``default``, the builder will look for a compatible
   Fortran compiler in the ``PATH`` environment variable, and compile
   the Fortran 90 interface if one is found.

   -  default: ``'default'``

.. _fortran:

*  ``FORTRAN``: [ ``path/to/FORTRAN`` ]
   The Fortran (90) compiler. If unspecified, the builder will look for a
   compatible compiler (pgfortran, gfortran, ifort, ifx, g95) in the ``PATH``
   environment variable. Used only for compiling the Fortran 90 interface.

   -  default: ``''``

.. _fortranflags:

*  ``FORTRANFLAGS``: [ ``string`` ]
   Compilation options for the Fortran (90) compiler.

   -  default: ``'-O3'``

.. _coverage:

*  ``coverage``: [ ``'yes'`` | ``'no'`` ]
   Enable collection of code coverage information with gcov.
   Available only when compiling with gcc.

   -  default: ``'no'``

.. _doxygen-docs:

*  ``doxygen_docs``: [ ``'yes'`` | ``'no'`` ]
   Build HTML documentation for the C++ interface using Doxygen.

   -  default: ``'no'``

.. _sphinx-docs:

*  ``sphinx_docs``: [ ``'yes'`` | ``'no'`` ]
   Build HTML documentation for Cantera using Sphinx.

   -  default: ``'no'``

.. _sphinx-cmd:

*  ``sphinx_cmd``: [ ``path/to/sphinx_cmd`` ]
   Command to use for building the Sphinx documentation.

   -  default: ``'sphinx-build'``

.. _sphinx-options:

*  ``sphinx_options``: [ ``string`` ]
   Options passed to the ``sphinx_cmd`` command line. Separate multiple
   options with spaces, for example, ``"-W --keep-going"``.

   -  default: ``'-W --keep-going'``

.. _system-eigen:

*  ``system_eigen``: [ ``'n'`` | ``'y'`` | ``'default'`` ]
   Select whether to use Eigen from a system installation (``y``), from a
   Git submodule (``n``), or to decide automatically (``default``). If Eigen
   is not installed directly into a system include directory, for example, it
   is installed in ``/opt/include/eigen3/Eigen``, then you will need to add
   ``/opt/include/eigen3`` to ``extra_inc_dirs``.

   -  default: ``'default'``

.. _system-fmt:

*  ``system_fmt``: [ ``'n'`` | ``'y'`` | ``'default'`` ]
   Select whether to use the fmt library from a system installation
   (``y``), from a Git submodule (``n``), or to decide automatically
   (``default``). If you do not want to use the Git submodule and fmt
   is not installed directly into system include and library
   directories, then you will need to add those directories to
   ``extra_inc_dirs`` and ``extra_lib_dirs``. This installation of fmt
   must include the shared version of the library, for example,
   ``libfmt.so``.

   -  default: ``'default'``

.. _hdf-support:

*  ``hdf_support``: [ ``'n'`` | ``'y'`` | ``'default'`` ]
   Select whether to support HDF5 container files natively (``y``), disable HDF5
   support (``n``), or to decide automatically based on the system configuration
   (``default``). Native HDF5 support uses the HDF5 library as well as the
   header-only HighFive C++ wrapper (see option ``system_highfive``). Specifying
   ``hdf_include`` or ``hdf_libdir`` changes the default to ``y``.

   -  default: ``'default'``

.. _hdf-include:

*  ``hdf_include``: [ ``path/to/hdf_include`` ]
   The directory where the HDF5 header files are installed. This should be the
   directory that contains files ``H5Version.h`` and ``H5Public.h``, amongst others.
   Not needed if the headers are installed in a standard location, for example,
   ``/usr/include``.

   -  default: ``''``

.. _hdf-libdir:

*  ``hdf_libdir``: [ ``path/to/hdf_libdir`` ]
   The directory where the HDF5 libraries are installed. Not needed if the
   libraries are installed in a standard location, for example, ``/usr/lib``.

   -  default: ``''``

.. _system-highfive:

*  ``system_highfive``: [ ``'n'`` | ``'y'`` | ``'default'`` ]
   Select whether to use HighFive from a system installation (``y``), from a
   Git submodule (``n``), or to decide automatically (``default``). If HighFive
   is not installed directly into a system include directory, for example, it
   is installed in ``/opt/include/HighFive``, then you will need to add
   ``/opt/include/HighFive`` to ``extra_inc_dirs``.

   -  default: ``'default'``

.. _system-yamlcpp:

*  ``system_yamlcpp``: [ ``'n'`` | ``'y'`` | ``'default'`` ]
   Select whether to use the yaml-cpp library from a system installation
   (``y``), from a Git submodule (``n``), or to decide automatically
   (``default``). If yaml-cpp is not installed directly into system
   include and library directories, then you will need to add those
   directories to ``extra_inc_dirs`` and ``extra_lib_dirs``.

   -  default: ``'default'``

.. _system-sundials:

*  ``system_sundials``: [ ``'n'`` | ``'y'`` | ``'default'`` ]
   Select whether to use SUNDIALS from a system installation (``y``), from
   a Git submodule (``n``), or to decide automatically (``default``).
   Specifying ``sundials_include`` or ``sundials_libdir`` changes the
   default to ``y``.

   -  default: ``'default'``

.. _sundials-include:

*  ``sundials_include``: [ ``path/to/sundials_include`` ]
   The directory where the SUNDIALS header files are installed. This
   should be the directory that contains the ``"cvodes"``, ``"nvector"``, etc.
   subdirectories. Not needed if the headers are installed in a
   standard location, for example, ``/usr/include``.

   -  default: ``''``

.. _sundials-libdir:

*  ``sundials_libdir``: [ ``path/to/sundials_libdir`` ]
   The directory where the SUNDIALS static libraries are installed.
   Not needed if the libraries are installed in a standard location,
   for example, ``/usr/lib``.

   -  default: ``''``

.. _system-blas-lapack:

*  ``system_blas_lapack``: [ ``'n'`` | ``'y'`` | ``'default'`` ]
   Select whether to use BLAS/LAPACK from a system installation (``y``), use
   Eigen linear algebra support (``n``), or to decide automatically based on
   libraries detected on the system (``default``). Specifying ``blas_lapack_libs``
   or ``blas_lapack_dir`` changes the default to ``y``, whereas installing the
   Matlab toolbox changes the default to ``n``. On macOS, the ``default`` option
   uses the Accelerate framework, whereas on other operating systems the
   preferred option depends on the CPU manufacturer. In general, OpenBLAS
   (``openblas``) is prioritized over standard libraries (``lapack,blas``), with
   Eigen being used if no suitable BLAS/LAPACK libraries are detected. On Intel
   CPU's, MKL (Windows: ``mkl_rt`` / Linux: ``mkl_rt,dl``) has the highest priority,
   followed by the other options. Note that Eigen is required whether or not
   BLAS/LAPACK libraries are used.

   -  default: ``'default'``

.. _blas-lapack-libs:

*  ``blas_lapack_libs``: [ ``string`` ]
   Cantera can use BLAS and LAPACK libraries installed on your system if you
   have optimized versions available (see option ``system_blas_lapack``). To use
   specific versions of BLAS and LAPACK, set ``blas_lapack_libs`` to the the list
   of libraries that should be passed to the linker, separated by commas, for
   example, ``"lapack,blas"`` or ``"lapack,f77blas,cblas,atlas"``.

   -  default: ``''``

.. _blas-lapack-dir:

*  ``blas_lapack_dir``: [ ``path/to/blas_lapack_dir`` ]
   Directory containing the libraries specified by ``blas_lapack_libs``. Not
   needed if the libraries are installed in a standard location, for example,
   ``/usr/lib``.

   -  default: ``''``

.. _lapack-ftn-trailing-underscore:

*  ``lapack_ftn_trailing_underscore``: [ ``'yes'`` | ``'no'`` ]
   Controls whether the LAPACK functions have a trailing underscore
   in the Fortran libraries.

   -  default: ``'yes'``

.. _lapack-ftn-string-len-at-end:

*  ``lapack_ftn_string_len_at_end``: [ ``'yes'`` | ``'no'`` ]
   Controls whether the LAPACK functions have the string length
   argument at the end of the argument list (``yes``) or after
   each argument (``no``) in the Fortran libraries.

   -  default: ``'yes'``

.. _googletest:

*  ``googletest``: [ ``'default'`` | ``'system'`` | ``'submodule'`` | ``'none'`` ]
   Select whether to use gtest/gmock from system
   installation (``system``), from a Git submodule (``submodule``), to decide
   automatically (``default``) or don't look for gtest/gmock (``none``)
   and don't run tests that depend on gtest/gmock.

   -  default: ``'default'``

.. _env-vars:

*  ``env_vars``: [ ``string`` ]
   Environment variables to propagate through to SCons. Either the
   string ``all`` or a comma separated list of variable names, for example,
   ``LD_LIBRARY_PATH,HOME``.

   -  default: ``'PATH,LD_LIBRARY_PATH,DYLD_LIBRARY_PATH,PYTHONPATH,USERPROFILE'``

.. _use-pch:

*  ``use_pch``: [ ``'yes'`` | ``'no'`` ]
   Use a precompiled-header to speed up compilation

   -  default: compiler dependent

      -  If using ``ICC``: ``'no'``
      -  Otherwise: ``'yes'``

.. _pch-flags:

*  ``pch_flags``: [ ``string`` ]
   Compiler flags when using precompiled-header.

   -  default: compiler dependent

      -  If using ``MSVC``: ``'/FIpch/system.h'``
      -  If using ``GCC``: ``'-include src/pch/system.h'``
      -  If using ``icx``: ``'-include-pch src/pch/system.h.gch'``
      -  If using ``Clang``: ``'-include-pch src/pch/system.h.gch'``
      -  Otherwise: ``''``

.. _thread-flags:

*  ``thread_flags``: [ ``string`` ]
   Compiler and linker flags for POSIX multithreading support.

   -  default: platform dependent

      -  Windows: ``''``
      -  macOS: ``''``
      -  Otherwise: ``'-pthread'``

.. _optimize:

*  ``optimize``: [ ``'yes'`` | ``'no'`` ]
   Enable extra compiler optimizations specified by the
   ``optimize_flags`` variable, instead of the flags specified by the
   ``no_optimize_flags`` variable.

   -  default: ``'yes'``

.. _optimize-flags:

*  ``optimize_flags``: [ ``string`` ]
   Additional compiler flags passed to the C/C++ compiler when ``optimize=yes``.

   -  default: compiler dependent

      -  If using ``MSVC``: ``'/O2'``
      -  If using ``ICC``: ``'-O3 -fp-model precise'``
      -  If using ``icx``: ``'-O3 -fp-model precise'``
      -  If using ``GCC``: ``'-O3 -Wno-inline'``
      -  Otherwise: ``'-O3'``

.. _no-optimize-flags:

*  ``no_optimize_flags``: [ ``string`` ]
   Additional compiler flags passed to the C/C++ compiler when ``optimize=no``.

   -  default: compiler dependent

      -  If using ``MSVC``: ``'/Od /Ob0'``
      -  Otherwise: ``'-O0'``

.. _debug:

*  ``debug``: [ ``'yes'`` | ``'no'`` ]
   Enable compiler debugging symbols.

   -  default: ``'yes'``

.. _debug-flags:

*  ``debug_flags``: [ ``string`` ]
   Additional compiler flags passed to the C/C++ compiler when ``debug=yes``.

   -  default: compiler dependent

      -  If using ``MSVC``: ``'/Zi /Fd${TARGET}.pdb'``
      -  Otherwise: ``'-g'``

.. _no-debug-flags:

*  ``no_debug_flags``: [ ``string`` ]
   Additional compiler flags passed to the C/C++ compiler when ``debug=no``.

   -  default: ``''``

.. _debug-linker-flags:

*  ``debug_linker_flags``: [ ``string`` ]
   Additional options passed to the linker when ``debug=yes``.

   -  default: compiler dependent

      -  If using ``MSVC``: ``'/DEBUG'``
      -  Otherwise: ``''``

.. _no-debug-linker-flags:

*  ``no_debug_linker_flags``: [ ``string`` ]
   Additional options passed to the linker when ``debug=no``.

   -  default: ``''``

.. _warning-flags:

*  ``warning_flags``: [ ``string`` ]
   Additional compiler flags passed to the C/C++ compiler to enable
   extra warnings. Used only when compiling source code that is part
   of Cantera (for example, excluding code in the ``ext`` directory).

   -  default: compiler dependent

      -  If using ``MSVC``: ``'/W3'``
      -  Otherwise: ``'-Wall'``

.. _extra-inc-dirs:

*  ``extra_inc_dirs``: [ ``string`` ]
   Additional directories to search for header files, with multiple
   directories separated by colons (\*nix, macOS) or semicolons (Windows).
   If an active ``conda`` environment is detected, the corresponding include
   path is automatically added.

   -  default: ``''``

.. _extra-lib-dirs:

*  ``extra_lib_dirs``: [ ``string`` ]
   Additional directories to search for libraries, with multiple
   directories separated by colons (\*nix, macOS) or semicolons (Windows).
   If an active ``conda`` environment is detected, the corresponding library
   path is automatically added.

   -  default: ``''``

.. _boost-inc-dir:

*  ``boost_inc_dir``: [ ``path/to/boost_inc_dir`` ]
   Location of the Boost header files. Not needed if the headers are
   installed in a standard location, for example, ``/usr/include``.

   -  default: ``''``

.. _stage-dir:

*  ``stage_dir``: [ ``path/to/stage_dir`` ]
   Directory relative to the Cantera source directory to be
   used as a staging area for building for example, a Debian
   package. If specified, 'scons install' will install files
   to ``stage_dir/prefix/...``.

   -  default: ``''``

.. _verbose:

*  ``VERBOSE``: [ ``'yes'`` | ``'no'`` ]
   Create verbose output about what SCons is doing. Deprecated in Cantera 3.0
   and to be removed thereafter; replaceable by ``logging=debug``.

   -  default: ``'no'``

.. _logging:

*  ``logging``: [ ``'debug'`` | ``'info'`` | ``'warning'`` | ``'error'`` | ``'default'`` ]
   Select logging level for SCons output. By default, logging messages use
   the ``info`` level for 'scons build' and the ``warning`` level for all other
   commands. In case the SCons option ``--silent`` is passed, all messages below
   the ``error`` level are suppressed.

   -  default: ``'default'``

.. _gtest-flags:

*  ``gtest_flags``: [ ``string`` ]
   Additional options passed to each GTest test suite, for example,
   ``--gtest_filter=*pattern*``. Separate multiple options with spaces.

   -  default: ``''``

.. _renamed-shared-libraries:

*  ``renamed_shared_libraries``: [ ``'yes'`` | ``'no'`` ]
   If this option is turned on, the shared libraries that are created
   will be renamed to have a ``_shared`` extension added to their base name.
   If not, the base names will be the same as the static libraries.
   In some cases this simplifies subsequent linking environments with
   static libraries and avoids a bug with using valgrind with
   the ``-static`` linking flag.

   -  default: ``'yes'``

.. _versioned-shared-library:

*  ``versioned_shared_library``: [ ``'yes'`` | ``'no'`` ]
   If enabled, create a versioned shared library, with symlinks to the
   more generic library name, for example, ``libcantera_shared.so.2.5.0`` as the
   actual library and ``libcantera_shared.so`` and ``libcantera_shared.so.2``
   as symlinks.

   -  default: compiler dependent

      -  If using ``mingw``: ``'no'``
      -  If using ``MSVC``: ``'no'``
      -  Otherwise: ``'yes'``

.. _use-rpath-linkage:

*  ``use_rpath_linkage``: [ ``'yes'`` | ``'no'`` ]
   If enabled, link to all shared libraries using ``rpath``, that is, a fixed
   run-time search path for dynamic library loading.

   -  default: ``'yes'``

.. _openmp-flag:

*  ``openmp_flag``: [ ``string`` ]
   Compiler flags used for multiprocessing (only used to generate sample build
   scripts).

   -  default: compiler dependent

      -  If using ``MSVC``: ``'/openmp'``
      -  If using ``ICC``: ``'-qopenmp'``
      -  If using ``icx``: ``'-qopenmp'``
      -  If using ``apple-clang``: ``'-Xpreprocessor -fopenmp'``
      -  Otherwise: ``'-fopenmp'``

.. _layout:

*  ``layout``: [ ``'standard'`` | ``'compact'`` | ``'conda'`` ]
   The layout of the directory structure. ``standard`` installs files to
   several subdirectories under 'prefix', for example, ``prefix/bin``,
   ``prefix/include/cantera``, ``prefix/lib`` etc. This layout is best used in
   conjunction with ``"prefix='/usr/local'"``. ``compact`` puts all installed files
   in the subdirectory defined by 'prefix'. This layout is best with a prefix
   like ``/opt/cantera``. If the Python executable found during compilation is
   managed by ``conda``, the layout will default to ``conda`` irrespective of
   operating system. For the ``conda`` layout, the Python package as well as all
   libraries and header files are installed into the active ``conda`` environment.
   Input data, samples, and other files are installed in the ``shared/cantera``
   subdirectory of the active ``conda`` environment.

   -  default: platform dependent

      -  Windows: ``'compact'``
      -  Otherwise: ``'standard'``

.. _package-build:

*  ``package_build``: [ ``'yes'`` | ``'no'`` ]
   Used in combination with packaging tools (example: ``conda-build``). If
   enabled, the installed package will be independent from host and build
   environments, with all external library and include paths removed. Packaged
   C++ and Fortran samples assume that users will compile with local SDKs, which
   should be backwards compatible with the tools used for the build process.

   -  default: ``'no'``

.. _fast-fail-tests:

*  ``fast_fail_tests``: [ ``'yes'`` | ``'no'`` ]
   If enabled, tests will exit at the first failure.

   -  default: ``'no'``

.. _skip-slow-tests:

*  ``skip_slow_tests``: [ ``'yes'`` | ``'no'`` ]
   If enabled, skip a subset of tests that are known to have long runtimes.
   Skipping these may be desirable when running with options that cause tests
   to run slowly, like disabling optimization or activating code profiling.

   -  default: ``'no'``

.. _show-long-tests:

*  ``show_long_tests``: [ ``'yes'`` | ``'no'`` ]
   If enabled, duration of slowest tests will be shown.

   -  default: ``'no'``

.. _verbose-tests:

*  ``verbose_tests``: [ ``'yes'`` | ``'no'`` ]
   If enabled, verbose test output will be shown.

   -  default: ``'no'``
