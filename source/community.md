# The Cantera Community

:::{admonition} Supporting Cantera
If you would like support the Cantera project, please check out our
{doc}`getting involved <getting-involved>` page. If you use Cantera in a publication,
we would appreciate if you {doc}`cited Cantera <citations>`. If you have found Cantera
to be useful to your research or company, please consider making a
[donation](sec-donations) to support our efforts.
:::

## About the Cantera Community

Cantera was originally developed by {doc}`Prof. David G. Goodwin <dave-goodwin>` at the
California Institute of Technology. Building on Prof. Goodwin's legacy, Cantera is
licensed under a [permissive 3-Clause BSD license](https://github.com/Cantera/cantera/blob/main/License.txt),
ensuring that the software will remain open source and available for all to use.

In this vein, Cantera software relies exclusively upon the volunteer contributions of
its users. These contributions range from diagnosing and reporting problems/bugs, to
helping others learn to use Cantera, to developing and implementing new software
capabilities. For a brief overview, see our {doc}`getting involved <getting-involved>`
page.

While Cantera provides some standalone models and applications, numerous external
packages exist that provide more specialized functionality and rely on Cantera. We
provide a non-exhaustive list of these {doc}`affiliated packages <affiliated>`.

### Governance

Cantera is governed by a Steering Committee; more information about our project's
governance policies can be found on the {doc}`governance <governance>` page.

### The Cantera Users' Group

The [Cantera Users’ Group](https://groups.google.com/g/cantera-users) on Google Groups
is the forum where most Cantera users have their questions asked and answered. If you
need help using Cantera and cannot find an answer in the tutorials or documentation at
Cantera's website, consider joining and asking a question there. A few notes:

- Please use the search feature before posting to see if your question has been answered
  before.
- If you are not running the current stable release of Cantera, please upgrade first,
  and see if the problem persists.
- This group is moderated, so it may take some time for your posts to appear if you are
  a new member.

For installation/compilation problems, please provide:

- The contents of the `cantera.conf` and `config.log` files, and the output of the
  `scons build` and `scons build dump` commands. You can direct this output to a file
  called `buildlog.txt` by running:

  ```
  scons build >buildlog.txt 2>&1
  ```

- The exact version of Cantera you are trying to compile, and how it was
  obtained (for example, downloaded source tarball or the specific Git commit).

- Your operating system, compiler versions, and the versions of any other relevant
  software.

For application problems (that is, not related to installation or compilation), please:

- Provide a minimal, complete, and verifiable example that demonstrates the problem when
  making your post; in short this means include a code example and input files.
- Please also provide information about your operating system and Cantera version. This
  will enable other members of the group to efficiently understand the problem and offer
  suggestions on how to fix it.
- *Please do not post screenshots of code or error messages!* They cannot be searched by
  anyone looking to solve a similar problem, and also cannot be read by text readers for
  visually impaired users. Instead, please copy and paste any relevant text directly
  into your message. Thanks!

## Interacting with the Cantera Community

### Code of Conduct

All online and in-person interactions and communications related to Cantera are governed
by the [Cantera Code of Conduct](https://github.com/Cantera/cantera/blob/main/CODE_OF_CONDUCT.md).
This code of conduct sets expectations for the community to ensure that users and
contributors are able to participate in a respectful and welcoming environment.

Please adhere to this code of conduct in any interactions you have in the Cantera
community. It is strictly enforced on all official Cantera repositories, websites,
users' group, and other resources. If you encounter someone violating these terms,
please [contact the code of conduct team](mailto:conduct@cantera.org)
([@speth](https://github.com/speth), [@bryanwweber](https://github.com/bryanwweber), and
[@kyleniemeyer](https://github.com/kyleniemeyer)) and we will address it as soon as
possible.

### Contributing Code

If there is a feature you would like to see added to Cantera, please consider becoming
part of the developer community and contributing code!
[Cantera's code repository](https://github.com/Cantera/cantera) is developed openly on
[GitHub](https://github.com/). Contributions are welcomed from anyone in the community;
please see the [Contributors' guide](https://github.com/Cantera/cantera/blob/main/CONTRIBUTING.md)
for assistance in getting started. There are also plenty of current contributors who are
happy to help, if you do not know how to get started.

(sec-bug-reporting)=
### Bug Reporting

**What should I do if I think I've found a bug in Cantera?**

- Check to see if you're using the most recent version of Cantera, and
  upgrade if not.
- Check the [Issue Tracker](https://github.com/Cantera/cantera/issues) to see if the
  issue has already been reported.
- Try to generate a [minimal, complete, and verifiable example](https://stackoverflow.com/help/mcve)
  that demonstrates the observed bug.
- Create a new issue on the tracker (the "New Issue" button is toward the upper
  right-hand corner, just above the list of open issues). Include as much information as
  possible about your system configuration (operating system, compiler versions, Python
  versions, installation method, etc.)

**What information should I include in my bug report?**

- The version of Cantera are you using, and how you installed it
- The operating system you are using
- If you compiled Cantera, what compiler you used, and what compilation options you
  specified
- The version of Python or Matlab are you using, if applicable
- The necessary *input* to generate the reported behavior
- The full text of any error message you receive

:::{toctree}
:maxdepth: 1
:hidden:

News <news-index>
Getting Involved <getting-involved>
Citing Cantera <citations>
Affiliated Packages <affiliated>
Governance <governance>
Dave Goodwin <dave-goodwin>
:::
