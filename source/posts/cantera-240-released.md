---
title: Cantera 2.4.0
date: 2018-08-24 17:25:00 UTC-04:00
slug: cantera-240-released
tags: release
description: The new Cantera release is here!
type: text
author: Bryan Weber
---

# Cantera 2.4.0

We are pleased to announce the release of Cantera 2.4.0. Cantera 2.4.0 includes [more than 380
commits](https://github.com/Cantera/cantera/compare/v2.3.0...v2.4.0) to the code since 2.3.0, merges
more than [70 pull
requests](https://github.com/Cantera/cantera/pulls?utf8=%E2%9C%93&q=is%3Apr+is%3Aclosed+updated%3A%3E%3D2017-01-18+),
and [closes almost 60
issues](https://github.com/Cantera/cantera/issues?page=2&q=is%3Aissue+is%3Aclosed+updated%3A%3E%3D2017-01-18&utf8=%E2%9C%93).
In this release, we improved the maintainability of Cantera by removing [or
deprecating](https://cantera.org/documentation/docs-2.4/doxygen/html/da/d58/deprecated.html) old,
untested code, moving the website and Mixmaster to separate repositories, and automating more of the
build/testing process. We also added new features to the 1-D reactor code (among other areas),
including adding an ionized gas transport class and the `IonFlow` and `BurnerIonFlame` classes,
providing better accessing to callbacks during 1-D solutions, and automatically detecting certain
common failure conditions of the 1-D solver. This release of Cantera was made possible by
contributions from 14 developers: [@speth](https://github.com/speth),
[@bryanwweber](https://github.com/bryanwweber), [@BangShiuh](https://github.com/BangShiuh),
[@decaluwe](https://github.com/decaluwe), [@wandadars](https://github.com/wandadars),
[@jsantner](https://github.com/jsantner), [@arghdos](https://github.com/arghdos),
[@rwest](https://github.com/rwest), [@g3bk47](https://github.com/g3bk47),
[@awehrfritz](https://github.com/awehrfritz), [@band-a-prend](https://github.com/band-a-prend),
[@vdevgan](https://github.com/vdevgan), [@KyleLinevitchJr](https://github.com/KyleLinevitchJr), and
[@MarcDuQuesne](https://github.com/MarcDuQuesne).

<!-- TEASER_END -->

For installation and compilation instructions for Cantera 2.4.0, please see the directions on the
[Cantera website](https://cantera.org/install/index.html). In addition to Conda packages, Windows
installers, and Ubuntu packages, this release also features the addition of a pre-compiled Matlab
toolbox for macOS users, replacing Homebrew as the prefered method of installing Cantera for Matlab
on macOS.

Thanks to a small development grant from NumFOCUS (see more about NumFOCUS below),
[@bryanwweber](https://github.com/bryanwweber) and [@decaluwe](https://github.com/decaluwe)
reorganized and restyled the [Cantera website](https://cantera.org). The website has moved to a
[separate repository](https://github.com/Cantera/cantera-website), allowing the website content to
be updated without modifications to the main Cantera source code. We also tried to make it easy for
all of our users to find what they're looking for quickly, from installation instructions and
tutorials for beginners, to advanced examples and API documentation for experienced Cantera
programmers. The new website also redirects all traffic to HTTPS, ensuring a secure experience for
everyone.

Cantera is now officially part of NumFOCUS. NumFOCUS is a 501(c)3 nonprofit dedicated to supporting
the open source scientific computing community. If you are interested in learning more about
NumFOCUS, please visit their website at https://numfocus.org, or our website at
https://cantera.org/community.html#donations.

Cantera 2.4.0 is the last release that will be compatible with Python 2.7. Support for Python 2.7
from the Python Software Foundation will [end January 1,
2020](https://www.python.org/dev/peps/pep-0373/#maintenance-releases). Given the recent release
cadence of Cantera, the next major version of Cantera will probably be released very close to that
date, so we have made the decision to drop Python 2.7 support for Cantera 2.5.0 and higher.

One notable change to the build requirements for Cantera 2.4.0 is that SCons 3.0.0 or higher must be
used to compile the source code. This means that either Python 2 or Python 3 can be used to run
SCons. In addition, there are now three options to handle building the Python interface, depending
on whether the user wants to build for Python 2 or Python 3. Please check the documentation or run
`scons help` for more information.

## Summary of changes in Cantera 2.4.0

For a complete changelog, see the [Github release
page](https://github.com/Cantera/cantera/releases/tag/v2.4.0). Major changes are summarized below.

### Bugs fixed

- Fix inconstencies and bugs in several `ThermoPhase` derived classes, including `PDSS_IdealGas`, `IonsFromNeutralVPSSTP`, `PDSS_IonsFromNeutral`, `PDSS_HKFT`, `LatticePhase`, `PDSS_SSVol`, `ConstDensityThermo`, and `PureFluidPhase`
- Preserve constant property pair when multiplying `Quantity` objects
- Fix using pure fluids in reactors
- Add temperature dependence of rotational relaxation in transport calculations
- Disable linking to external SUNDIALS libraries when building the Matlab toolbox

### Changes to existing capabilities

- Allow instantiation of ThermoPhase derived classes without XML
- `set_equivalence_ratio` now supports sulfur oxidation
- Make all complex object types (ThermoPhase, Kinetics, Transport, Reactor, Domain1D, etc.) objects non-copyable
- Deprecate `FreeFlow` and `AxiStagnFlow` classes by moving the relevant functions into the `StFlow` class
- Allow `convertMech` function to be called multiple times
- Remove the requirement for users to have Boost headers installed when building against the Cantera library
- Change the options to build the Python interface, since SCons can be run by Python 3
- Update GTest, fmtlib, SUNDIALS, and Eigen submodule versions

### Additions

- Add ion gas transport model, and `IonFlow` and `BurnerIonFlame` flame classes
- Add C++ OpenMP, Non-Ideal Shock Tube, PSR/WSR, and time-dependent mass flow rate examples
- Add class `AnyMap`
- Allow negative reaction orders
- Add unity Lewis number transport model
- Add electron to the built-in elements
- Add `get_equivalence_ratio` function
