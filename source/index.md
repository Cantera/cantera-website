---
myst:
  html_meta:
    "description lang=en": |
      Cantera is an open-source suite of tools for problems involving chemical kinetics, thermodynamics, and transport processes.
html_theme.sidebar_secondary.remove: true
---

<!-- The following workaround is used to set the HTML page title -->
<div style="visibility: hidden; display: none;">

# Open-source chemical kinetics, thermodynamics, and transport

</div>

<p class="jumbotron-text">Cantera is an open-source suite of tools for problems involving chemical kinetics, thermodynamics, and transport processes.</p>

::::{grid} 1 2 2 4

:::{grid-item}

#### Automation

Cantera automates the chemical kinetic, thermodynamic, and transport calculations so that the users can efficiently incorporate detailed chemical thermo-kinetics and transport models into their calculations.
:::

:::{grid-item}

#### Object-Oriented

Cantera utilizes object-oriented concepts for robust yet flexible phase models, and algorithms are generalized so that users can explore different phase models with minimal changes to their overall code.
:::

:::{grid-item}

#### Multiple Interfaces

Cantera can be used from Python and Matlab, or in applications written in C/C++ and Fortran 90.
:::

:::{grid-item}

#### Broad Applications

Cantera is currently used for applications including combustion, detonations, electrochemical energy conversion and storage, fuel cells, batteries, aqueous electrolyte solutions, plasmas, and thin film deposition.
:::
::::

::::::{grid} 1

:::::{grid-item}

::::{grid} 1 1 3 3

:::{grid-item-card} <a href="stable/userguide/index.html#introductory-tutorials">Tutorials</a>

_Where do I get started?_ The tutorials linked below will get you started using Cantera
on your own machine.

{bdg-link-primary}`Python <stable/userguide/python-tutorial.html>`
{bdg-link-primary}`Convert Input Files <stable/userguide/ck2yaml-tutorial.html>`

:::

:::{grid-item-card} <a href="stable/examples/index.html">Examples</a>

_What can Cantera do?_ We have a number of examples demonstrating the use of Cantera in
some of our interfaces.

{bdg-link-primary}`Python <stable/examples/python/index.html>`
{bdg-link-primary}`Matlab (experimental)<stable/examples/matlab_experimental/index.html>`
{bdg-link-primary}`C++ <stable/examples/cxx/index.html>`
:::

:::{grid-item-card} <a href="stable/install/index.html">Install</a>

_How do I install Cantera?_ Instructions for installing pre-built Cantera binaries can
be found here.

{bdg-link-primary}`Conda <stable/install/conda.html>`
{bdg-link-primary}`Pip <stable/install/pip.html>`
{bdg-link-primary}`Ubuntu <stable/install/ubuntu.html>`
{bdg-link-primary}`Compile from source <stable/develop/index.html#compiling-cantera-from-source>`

:::
::::
:::::

:::::{grid-item}

::::{grid} 1 1 3 3

:::{grid-item-card} <a href="stable/reference/index.html#science-reference">Science Reference</a>

_What equations does Cantera solve?_ Descriptions of the models implemented by Cantera,
including equations of state, energy and mass conservation, and chemical kinetics.

{bdg-link-primary}`Thermodynamics <stable/reference/thermo/index.html>`
{bdg-link-primary}`Kinetics <stable/reference/kinetics/index.html>`
{bdg-link-primary}`Transport <stable/reference/transport/index.html>`
{bdg-link-primary}`Reactors <stable/reference/reactors/index.html>`
{bdg-link-primary}`1D Flames <stable/reference/onedim/index.html>`

:::

:::{grid-item-card} <a href="stable/reference/index.html#programming-reference">Programming Reference</a>

_How do I use Cantera's capabilities_? Documentation for the classes and functions that
make up Cantera.

{bdg-link-primary}`Python <stable/python/index.html>`
{bdg-link-primary}`C++ <stable/cxx/index.html>`
{bdg-link-primary}`Matlab <stable/matlab/index.html>`
{bdg-link-primary}`YAML <stable/yaml/index.html>`
:::

:::{grid-item-card} <a href="https://mybinder.org/v2/gh/Cantera/cantera-jupyter/main">Try Cantera in Your Browser!</a>

The Binder service allows you to try out Cantera in the cloud without installing it on
your computer. You'll see some of our examples and be able to run them yourself!

<a href="https://mybinder.org/v2/gh/Cantera/cantera-jupyter/main" rel="nofollow" class="card-link">
<img src="https://mybinder.org/badge_logo.svg" alt="Binder"
data-canonical-src="https://mybinder.org/badge_logo.svg" style="max-width:100%;">
</a>
:::
::::
:::::
::::::

::::::{grid} 1 1 2 2
:::::{grid-item}

<h2 class="text-center" style="magin-bottom: 20px">Connect With Cantera</h2>

::::{grid} 2
:::{grid-item}
:columns: 9
The <a href="https://groups.google.com/g/cantera-users">Cantera Users’ Group</a> on Google Groups is the forum where most Cantera users have their questions asked and answered. If you need help using Cantera and cannot find an answer in the tutorials or documentation at Cantera's website, consider joining and asking a question there. Find more information in our <a href="/community.html#the-cantera-users-group">Community section</a>.
:::
:::{grid-item}
:columns: 3
<a href="https://groups.google.com/g/cantera-users" rel="nofollow">
<img alt="Google Groups" class="align-center" src="/_static/img/Groups_Logo.png" style="width: 100px;">
</a>
:::
::::
::::{grid} 2
:::{grid-item}
:columns: 9
Cantera is developed by a team of volunteers, and we're always looking for new team members. If there is a feature you want added, a bug that needs to be fixed, or even just a typo in the documentation, changes from the community are always welcome. For more, see the section about <a href="/community.html#contributing-code" title="Contributing Code">contributing code</a> on our Community page.
:::
:::{grid-item}
:columns: 3

<a href="https://github.com/Cantera/cantera" rel="nofollow">
<img alt="GitHub" class="align-center" src="/_static/img/Git_Logo.png" style="width: 100px;">
</a>
:::
::::
:::::
:::::{grid-item}

<h2 class="text-center" style="magin-bottom: 20px">How is Cantera Supported?</h2>

Cantera is a Sponsored Project of NumFOCUS, a 501(c)(3) nonprofit charity in the United States. NumFOCUS provides Cantera with fiscal, legal, and administrative support to help ensure the health and sustainability of the project. Visit <a href="https://numfocus.org">numfocus.org</a> for more information.

Donations to Cantera are managed by NumFOCUS. For donors in the United States, your gift is tax-deductible to the extent provided by law. As with any donation, you should consult with your tax adviser about your particular tax situation.

If you have found Cantera to be useful to your research or company, please consider making a <a href="https://numfocus.org/donate-to-cantera" title="Donate to Cantera" rel="nofollow">donation</a> to support our efforts. All donations will be used exclusively to fund the development of Cantera's source code, documentation, or community.

```{image} /_static/img/SponsoredProject.png
:alt: Powered by NumFOCUS
:target: https://numfocus.org
:width: 250px
:align: center
```

&nbsp;

```{button-link} https://numfocus.org/donate-to-cantera
:align: center
:color: secondary
:shadow:
Donate to Cantera {octicon}`link-external`
```
:::::
::::::


:::{toctree}
:maxdepth: 1
:hidden:

Community <community>
:::
