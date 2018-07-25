import re
from collections import Counter
from pathlib import Path
import sys

if not sys.platform.startswith('linux'):
    # Actually, it can be run on any case-sensitive
    # file system, but practically this means Linux
    print('This script must be run on Linux!')
    sys.exit(1)


def get_contents(path):
    with path.open('r') as file_obj:
        try:
            return file_obj.readlines()
        except UnicodeDecodeError:
            return None

docs_dirs = Path('api-docs')
for dir in docs_dirs.iterdir():
    # if dir.name != 'docs-2.0':
    #     continue
    if not dir.is_dir():
        continue
    doxy_dir = dir/'doxygen'/'html'
    dupe_dir = doxy_dir/'dupe_files'
    if not dupe_dir.exists():
        dupe_dir.mkdir(parents=True)
    files = [p for p in doxy_dir.iterdir() if p.is_file()]
    file_contents = {p.name: get_contents(p) for p in files}
    files_case_ins = [p.name.lower() for p in files]
    dup = [doxy_dir.joinpath(c) for c, v in Counter(files_case_ins).items() if v > 1]
    print(dir.name, [p.name for p in dup])
    # dup_files = [files[i] for i, x in enumerate(files_case_ins) for d in dup if x == d]
    for df in dup:
        found_ever = False
        for file_name, lines in file_contents.items():
            if lines is None:
                continue
            new_lines = []
            found = False
            for line in lines:
                if df.name in line:
                    found = True
                    found_ever = True
                    line = line.replace(df.name, dupe_dir.name + '/' + df.name)
                new_lines.append(line)
            if found:
                if file_name in [p.name for p in dup]:
                    file_contents[file_name] = new_lines
                else:
                    with open(doxy_dir.joinpath(file_name), 'w') as file_obj:
                        file_obj.write(''.join(new_lines))

        if found_ever:
            with open(dupe_dir.joinpath(df.name), 'w') as file_obj:
                file_obj.write(''.join(file_contents[df.name]))
            doxy_dir.joinpath(df.name).unlink()
        else:
            new_file = dupe_dir.joinpath(df.name)
            df.replace(new_file)
