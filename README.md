# Cantera Website

This repository contains the source code for the [cantera.org](https://cantera.org) website. The
site is built using the [Nikola](https://getnikola.com) static site generator.

## To build the website

1. Create a virtual environment for Nikola (i.e., using conda or virtualenv)
2. Clone the Cantera source: `git clone https://github.com/Cantera/cantera.git`
3. Clone the Cantera Jupyter examples: `git clone https://github.com/Cantera/cantera-jupyter.git`
4. Clone the Cantera website source: `git clone https://github.com/Cantera/cantera-website.git`
5. Enter the website repo: `cd cantera-website`
6. Inside the website repo, install the required packages: `pip install -r requirements.txt`
7. Build the website and open in browser: `nikola auto -b`

## To add a language of examples

1. Copy one of the existing `render_*_examples.py` and `render_*_examples.plugin`
2. Add the source folder as the key and destination folder to the `EXAMPLES_FOLDERS` dictionary in `conf.py`
3. Edit the `render_*_examples.py` file to build the examples
4. See [this blog post](https://bryanwweber.com/writing/personal/2018/12/22/writing-task-plugins-for-nikola/) for more information about building Nikola tasks

## To add an example category for Jupyter or Python

1. New example categories are stored in folders in the Jupyter and Python example repositories
2. If new categories (folders) are added to the examples, the appropriate renderer needs to be updated
3. In the Jupyter and Python examples, there's a dictionary called `*_headers`. Each folder of examples has a key in that dictionary. The values are a nested dictionary with three keys:
   1. `name`: The name used on the index page for that category
   2. `files`: An empty list that gets filled with the names of the examples in this category
   3. `summaries`: A empty dictionary that gets filled with keys that are the example filename and values that are the summary from that example
4. Add a new key to that dictionary with the folder name as the key and fill in the `name` key in the nested dictionary and set the `files` and `summaries` keys to the empty list and empty dictionary, respectively
