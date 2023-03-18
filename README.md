# Cantera Website

This repository contains the source code for the [cantera.org](https://cantera.org) website. The
site is built using the [Sphinx](https://sphinx-doc.org) static site generator.

## To build the website

### Using pdm (Recommended)

1. Install [`pdm`](https://pdm.fming.dev/latest/). Recommended method is to use `pipx`.
2. Run `pdm install --no-self` to create the virtual environment
3. Run `pdm run build` to build the website, or run `pdm run rebuild` to automatically rebuild the website when a page changes.
4. Run a web server to view the website:

   ```shell
   python -m http.server 8080 --directory build/html
   ```

5. Open a browser to <http://localhost:8080>
6. Close the web server with `C-c` (`CTRL-c`)

### Using Conda (old instructions that aren't updated)

1. Create a virtual environment for Sphinx using `conda` and activate it. The environment must have Python 3.10 and the `conda-lock` package.
2. Clone the Cantera website source: `git clone https://github.com/Cantera/cantera-website.git`
3. Enter the website repo: `cd cantera-website`
4. Inside the website repo, install the required packages:

   ```shell
   conda-lock install continuous-integration/conda-lock.yml --name <name-of-your-environment>
   ```

5. Build the website and open in browser: `make html && python -m http.server --directory build/html` then navigate to `localhost:8000` in your browser
6. Press `C-c` (`CTRL-C`) to close the Python HTTP server
