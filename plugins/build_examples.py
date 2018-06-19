from pathlib import Path
import ast

from collections import OrderedDict
import io
import os
import lxml.html
import json

from nikola.plugins.task.listings import Listings
from nikola import utils

from pygments import highlight
from pygments.lexers import get_lexer_for_filename, guess_lexer, TextLexer, MatlabLexer
import natsort


class BuildExamples(Listings):
    """Build the Cantera examples into the documentation"""

    name = "build_examples"

    def gen_tasks(self):
        """Render pretty code listings."""
        # Things to ignore in listings
        self.ignored_extensions = (".pyc", ".pyo", ".cti", ".dat", ".ipynb_checkpoints")

        def render_listing_index(type, headers, input_folder, output_folder, output_file):
            def chunks(l, n):
                """Yield successive n-sized chunks from l.
                https://stackoverflow.com/a/312464"""
                for i in range(0, len(l), n):
                    yield l[i:i + n]

            for head, file_dict in headers.items():
                file_dict['files'] = list(chunks(file_dict['files'], 3))

            permalink = self.site.link(
                'listing',
                os.path.join(
                    input_folder,
                    os.path.relpath(
                        output_file[:-5],  # remove '.html'
                        os.path.join(
                            self.kw['output_folder'],
                            output_folder))))
            title = '{} Examples'.format(type).title()
            context = {
                'headers': headers,
                'lang': self.kw['default_lang'],
                'pagekind': ['listing'],
                'permalink': permalink,
                'title': title,
                'description': title,
            }
            self.site.render_template('{}-example-index.tmpl'.format(type), output_file, context)

        def render_listing(in_name, out_name, input_folder, output_folder):
            needs_ipython_css = False
            if in_name.endswith('.ipynb'):
                # Special handling: render ipynbs in listings (Issue #1900)
                ipynb_compiler = self.site.plugin_manager.getPluginByName("ipynb", "PageCompiler").plugin_object  # NOQA: E501
                with io.open(in_name, "r", encoding="utf8") as in_file:
                    nb_json = ipynb_compiler._nbformat_read(in_file)
                    ipynb_raw = ipynb_compiler._compile_string(nb_json)
                ipynb_html = lxml.html.fromstring(ipynb_raw)
                # The raw HTML contains garbage (scripts and styles), we can’t leave it in
                code = lxml.html.tostring(ipynb_html, encoding='unicode')
                title = os.path.basename(in_name)
                needs_ipython_css = True
            elif in_name.endswith('.m'):
                lexer = MatlabLexer()
                with open(in_name, 'r') as fd:
                    code = highlight(fd.read(), lexer, utils.NikolaPygmentsHTML(in_name))
                title = os.path.basename(in_name)
            else:
                with open(in_name, 'r') as fd:
                    try:
                        lexer = get_lexer_for_filename(in_name)
                    except Exception:
                        try:
                            lexer = guess_lexer(fd.read())
                        except Exception:
                            lexer = TextLexer()
                        fd.seek(0)
                    code = highlight(fd.read(), lexer, utils.NikolaPygmentsHTML(in_name))
                title = os.path.basename(in_name)

            permalink = self.site.link(
                'listing',
                os.path.join(
                    input_folder,
                    os.path.relpath(
                        out_name[:-5],  # remove '.html'
                        os.path.join(
                            self.kw['output_folder'],
                            output_folder))))
            source_link = permalink[:-5]  # remove '.html'
            context = {
                'code': code,
                'title': title,
                'permalink': permalink,
                'lang': self.kw['default_lang'],
                'description': title,
                'source_link': source_link,
                'pagekind': ['listing'],
            }
            if needs_ipython_css:
                # If someone does not have ipynb posts and only listings, we
                # need to enable ipynb CSS for ipynb listings.
                context['needs_ipython_css'] = True
            self.site.render_template('listing.tmpl', out_name, context)

        yield self.group_task()

        for input_folder, output_folder in self.kw['listings_folders'].items():

            #########################################################
            # Build the Python examples
            #########################################################
            if 'python' in output_folder:
                template_deps = self.site.template_system.template_deps('python-example-index.tmpl')
                headers = OrderedDict(
                    thermo={'name': 'Thermodynamics'}, kinetics={'name': 'Kinetics'},
                    transport={'name': 'Transport'}, reactors={'name': 'Reactor Networks'},
                    onedim={'name': 'One-Dimensional Flames'},
                    multiphase={'name': 'Multiphase Mixtures'},
                    surface_chemistry={'name': 'Surface Chemistry'})

                p = Path(input_folder)
                files = []
                for dir in p.iterdir():
                    if not dir.is_dir():
                        continue
                    summaries = {}
                    this_header_files = []
                    for f in dir.iterdir():
                        if f.suffix in self.ignored_extensions:
                            continue
                        files.append(f)
                        this_header_files.append(str(f))
                        with open(f, 'r') as pyfile:
                            try:
                                mod = ast.parse(pyfile.read())
                            except UnicodeDecodeError:
                                raise Exception('The file is {}'.format(f))
                            #mod = ast.parse(pyfile.read())
                        for node in mod.body:
                            if isinstance(node, ast.Expr) and isinstance(node.value, ast.Str):
                                doc = node.value.s.strip().split('\n\n')[0].strip()
                                if not doc.endswith('.'):
                                    doc += '.'
                                break
                        summaries[str(f).split('/')[-1]] = doc
                    headers[dir.stem]['summaries'] = summaries
                    this_header_files = natsort.natsorted(this_header_files, alg=natsort.IC)
                    headers[dir.stem]['files'] = this_header_files

                uptodate = {'c': self.site.GLOBAL_CONTEXT}

                for k, v in self.site.GLOBAL_CONTEXT['template_hooks'].items():
                    uptodate['||template_hooks|{0}||'.format(k)] = v.calculate_deps()

                for k in self.site._GLOBAL_CONTEXT_TRANSLATABLE:
                    uptodate[k] = self.site.GLOBAL_CONTEXT[k](self.kw['default_lang'])

                # save navigation links as dependencies
                uptodate['navigation_links'] = uptodate['c']['navigation_links'](self.kw['default_lang'])  # NOQA: E501

                uptodate['kw'] = self.kw

                uptodate2 = uptodate.copy()
                uptodate2['d'] = headers.keys()
                uptodate2['f'] = list(map(str, files))

                rel_output_name = os.path.join(output_folder, self.kw['index_file'])

                # Render Python examples index file
                out_name = os.path.join(self.kw['output_folder'], rel_output_name)
                yield utils.apply_filters({
                    'basename': self.name,
                    'name': out_name,
                    'file_dep': template_deps,
                    'targets': [out_name],
                    'actions': [(render_listing_index, ['python', headers, input_folder, output_folder, out_name])],
                    # This is necessary to reflect changes in blog title,
                    # sidebar links, etc.
                    'uptodate': [utils.config_changed(uptodate2, 'nikola.plugins.task.listings:folder')],  # NOQA: E501
                    'clean': True,
                }, self.kw["filters"])

                for f in files:
                    if str(f) == '.DS_Store':
                        continue
                    if f.suffix in self.ignored_extensions:
                        continue
                    in_name = str(f.resolve())
                    # Record file names
                    parent = str(f.parent.stem)
                    f_name = str(f.name)
                    rel_name = os.path.join(parent, f_name + '.html')
                    rel_output_name = os.path.join(output_folder, parent, f_name + '.html')
                    self.register_output_name(input_folder, rel_name, rel_output_name)
                    # Set up output name
                    out_name = os.path.join(self.kw['output_folder'], rel_output_name)
                    # Yield task
                    yield utils.apply_filters({
                        'basename': self.name,
                        'name': out_name,
                        'file_dep': template_deps + [in_name],
                        'targets': [out_name],
                        'actions': [(render_listing, [in_name, out_name, input_folder, output_folder])],  # NOQA: E501
                        # This is necessary to reflect changes in blog title,
                        # sidebar links, etc.
                        'uptodate': [utils.config_changed(uptodate, 'nikola.plugins.task.listings:source')],  # NOQA: E501
                        'clean': True,
                    }, self.kw["filters"])

                    rel_name = os.path.join(parent, f_name)
                    rel_output_name = os.path.join(output_folder, parent, f_name)
                    self.register_output_name(input_folder, rel_name, rel_output_name)
                    out_name = os.path.join(self.kw['output_folder'], rel_output_name)
                    yield utils.apply_filters({
                        'basename': self.name,
                        'name': out_name,
                        'file_dep': [in_name],
                        'targets': [out_name],
                        'actions': [(utils.copy_file, [in_name, out_name])],
                        'clean': True,
                    }, self.kw["filters"])

            #########################################################
            # Build the Matlab examples
            #########################################################
            elif 'matlab' in output_folder:
                template_deps = self.site.template_system.template_deps('matlab-example-index.tmpl')
                p = Path(input_folder)
                headers = {'examples': {'name': 'Examples'}}
                files = []
                summaries = {}
                for file in p.iterdir():
                    if 'tut' in file.name or file.name == 'README' or 'test' in file.name:
                        continue
                    if file.suffix in self.ignored_extensions:
                        continue
                    files.append(file)
                    doc = ''
                    with open(file) as mfile:
                        for line in mfile:
                            line = line.strip()
                            if line.startswith('%'):
                                doc = line.strip('%').strip()
                            if doc:
                                break
                    name = file.stem.replace('_', ' ')
                    if doc.lower().replace('_', ' ').startswith(name):
                        doc = doc[len(name):].strip()
                    summaries[file.name] = doc
                headers['examples']['summaries'] = summaries
                this_files = list(map(str, files))
                headers['examples']['files'] = natsort.natsorted(this_files, alg=natsort.IC)

                uptodate = {'c': self.site.GLOBAL_CONTEXT}

                for k, v in self.site.GLOBAL_CONTEXT['template_hooks'].items():
                    uptodate['||template_hooks|{0}||'.format(k)] = v.calculate_deps()

                for k in self.site._GLOBAL_CONTEXT_TRANSLATABLE:
                    uptodate[k] = self.site.GLOBAL_CONTEXT[k](self.kw['default_lang'])

                # save navigation links as dependencies
                uptodate['navigation_links'] = uptodate['c']['navigation_links'](self.kw['default_lang'])  # NOQA: E501

                uptodate['kw'] = self.kw

                uptodate2 = uptodate.copy()
                uptodate2['d'] = headers.keys()
                uptodate2['f'] = list(map(str, files))

                rel_output_name = os.path.join(output_folder, self.kw['index_file'])

                # Render Matlab examples index file
                out_name = os.path.join(self.kw['output_folder'], rel_output_name)
                yield utils.apply_filters({
                    'basename': self.name,
                    'name': out_name,
                    'file_dep': template_deps,
                    'targets': [out_name],
                    'actions': [(render_listing_index, ['matlab', headers, input_folder, output_folder, out_name])],
                    # This is necessary to reflect changes in blog title,
                    # sidebar links, etc.
                    'uptodate': [utils.config_changed(uptodate2, 'nikola.plugins.task.listings:folder')],  # NOQA: E501
                    'clean': True,
                }, self.kw["filters"])

                for f in files:
                    if str(f) == '.DS_Store':
                        continue
                    if f.suffix in self.ignored_extensions:
                        continue
                    in_name = str(f.resolve())
                    # Record file names
                    f_name = str(f.name)
                    rel_name = os.path.join(f_name + '.html')
                    rel_output_name = os.path.join(output_folder, f_name + '.html')
                    self.register_output_name(input_folder, rel_name, rel_output_name)
                    # Set up output name
                    out_name = os.path.join(self.kw['output_folder'], rel_output_name)
                    # Yield task
                    yield utils.apply_filters({
                        'basename': self.name,
                        'name': out_name,
                        'file_dep': template_deps + [in_name],
                        'targets': [out_name],
                        'actions': [(render_listing, [in_name, out_name, input_folder, output_folder])],  # NOQA: E501
                        # This is necessary to reflect changes in blog title,
                        # sidebar links, etc.
                        'uptodate': [utils.config_changed(uptodate, 'nikola.plugins.task.listings:source')],  # NOQA: E501
                        'clean': True,
                    }, self.kw["filters"])

                    rel_name = os.path.join(f_name)
                    rel_output_name = os.path.join(output_folder, f_name)
                    self.register_output_name(input_folder, rel_name, rel_output_name)
                    out_name = os.path.join(self.kw['output_folder'], rel_output_name)
                    yield utils.apply_filters({
                        'basename': self.name,
                        'name': out_name,
                        'file_dep': [in_name],
                        'targets': [out_name],
                        'actions': [(utils.copy_file, [in_name, out_name])],
                        'clean': True,
                    }, self.kw["filters"])

            elif 'jupyter' in output_folder:
                template_deps = self.site.template_system.template_deps('jupyter-example-index.tmpl')
                headers = OrderedDict(
                    thermo={'name': 'Thermodynamics'},
                    reactors={'name': 'Reactor Networks'},
                    flames={'name': 'One-Dimensional Flames'},
                )

                p = Path(input_folder)
                files = []
                for dir in p.iterdir():
                    if not dir.is_dir() or dir.name.startswith('.') or dir.suffix in self.ignored_extensions:
                        continue
                    summaries = {}
                    this_header_files = []
                    for f in dir.iterdir():
                        if f.suffix in self.ignored_extensions or f.is_dir() or f.name == '.ipynb_checkpoints':
                            continue
                        files.append(f)
                        this_header_files.append(str(f))
                        with open(f, 'r') as pyfile:
                            data = json.load(pyfile)
                        for cell in data['cells']:
                            if cell['cell_type'] != 'markdown':
                                continue
                            doc = cell['source'][0].replace('#', '').strip()
                            break
                        summaries[str(f).split('/')[-1]] = doc
                    headers[dir.stem]['summaries'] = summaries
                    this_header_files = natsort.natsorted(this_header_files, alg=natsort.IC)
                    headers[dir.stem]['files'] = this_header_files

                uptodate = {'c': self.site.GLOBAL_CONTEXT}

                for k, v in self.site.GLOBAL_CONTEXT['template_hooks'].items():
                    uptodate['||template_hooks|{0}||'.format(k)] = v.calculate_deps()

                for k in self.site._GLOBAL_CONTEXT_TRANSLATABLE:
                    uptodate[k] = self.site.GLOBAL_CONTEXT[k](self.kw['default_lang'])

                # save navigation links as dependencies
                uptodate['navigation_links'] = uptodate['c']['navigation_links'](self.kw['default_lang'])  # NOQA: E501

                uptodate['kw'] = self.kw

                uptodate2 = uptodate.copy()
                uptodate2['d'] = headers.keys()
                uptodate2['f'] = list(map(str, files))

                rel_output_name = os.path.join(output_folder, self.kw['index_file'])

                # Render Python examples index file
                out_name = os.path.join(self.kw['output_folder'], rel_output_name)
                yield utils.apply_filters({
                    'basename': self.name,
                    'name': out_name,
                    'file_dep': template_deps,
                    'targets': [out_name],
                    'actions': [(render_listing_index, ['jupyter', headers, input_folder, output_folder, out_name])],
                    # This is necessary to reflect changes in blog title,
                    # sidebar links, etc.
                    'uptodate': [utils.config_changed(uptodate2, 'nikola.plugins.task.listings:folder')],  # NOQA: E501
                    'clean': True,
                }, self.kw["filters"])

                for f in files:
                    if str(f) == '.DS_Store':
                        continue
                    if f.suffix in self.ignored_extensions:
                        continue
                    in_name = str(f.resolve())
                    # Record file names
                    parent = str(f.parent.stem)
                    f_name = str(f.name)
                    rel_name = os.path.join(parent, f_name + '.html')
                    rel_output_name = os.path.join(output_folder, parent, f_name + '.html')
                    self.register_output_name(input_folder, rel_name, rel_output_name)
                    # Set up output name
                    out_name = os.path.join(self.kw['output_folder'], rel_output_name)
                    # Yield task
                    yield utils.apply_filters({
                        'basename': self.name,
                        'name': out_name,
                        'file_dep': template_deps + [in_name],
                        'targets': [out_name],
                        'actions': [(render_listing, [in_name, out_name, input_folder, output_folder])],  # NOQA: E501
                        # This is necessary to reflect changes in blog title,
                        # sidebar links, etc.
                        'uptodate': [utils.config_changed(uptodate, 'nikola.plugins.task.listings:source')],  # NOQA: E501
                        'clean': True,
                    }, self.kw["filters"])

                    rel_name = os.path.join(parent, f_name)
                    rel_output_name = os.path.join(output_folder, parent, f_name)
                    self.register_output_name(input_folder, rel_name, rel_output_name)
                    out_name = os.path.join(self.kw['output_folder'], rel_output_name)
                    yield utils.apply_filters({
                        'basename': self.name,
                        'name': out_name,
                        'file_dep': [in_name],
                        'targets': [out_name],
                        'actions': [(utils.copy_file, [in_name, out_name])],
                        'clean': True,
                    }, self.kw["filters"])
