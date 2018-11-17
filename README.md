# Cantera Website

This repository contains the source code for the [cantera.org](https://cantera.org) website. The
site is built using the [Nikola](https://getnikola.com) static site generator.

## To build the website

0. Create a virtual environment for Nikola (i.e., using conda or virtualenv)
1. Clone the Cantera source: `git clone https://github.com/Cantera/cantera.git`
2. Clone the Cantera Jupyter examples: `git clone https://github.com/Cantera/cantera-jupyter.git`
3. Clone the Cantera website source: `git clone https://github.com/Cantera/cantera-website.git`
4. Enter the website repo: `cd cantera-website`
5. Inside the website repo, install the required packages: `pip install -r requirements.txt`
6. Build the website and open in browser: `nikola auto -b`
