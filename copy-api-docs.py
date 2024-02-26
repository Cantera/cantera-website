"""
Copy versioned documentation generated from the Cantera/cantera repository into the
output directory. In addition to copying from the 'api-docs' submodule, this script also
expects that 'dev-docs' is a symlink to the 'build/doc/html' subdirectory of the main
Cantera repository or otherwise contains the built docs for the latest development
version of Cantera.
"""

from pathlib import Path
import shutil

if not Path('source').exists():
    raise FileNotFoundError('Expected to be called from the root of the '
                            'cantera-website repository')

dest = Path('build/html')
dest.mkdir(parents=True, exist_ok=True)

for p in Path('api-docs').glob('docs-*'):
    version_string = p.name.split('-')[1]
    shutil.copytree(str(p), dest / version_string, dirs_exist_ok=True)

shutil.copytree('dev-docs', dest / 'dev', dirs_exist_ok=True)

# TODO: After the 3.1 release, this should be updated to copy from 'api-docs/docs-3.1'
shutil.copytree('dev-docs', dest / 'stable', dirs_exist_ok=True)
