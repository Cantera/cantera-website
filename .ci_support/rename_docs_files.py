from collections import Counter
from pathlib import Path
import sys
import lxml.etree as ET
import lxml.html as HT

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


def fix_html(etree, dup):
    head = etree.find('head')
    for elem, type, loc, _ in head.iterlinks():
        if not loc.startswith('http'):
            elem.attrib[type] = '../' + loc

    body = etree.find('body')
    for elem, type, loc, _ in body.iterlinks():
        # If the location is one of the duplicate files or an absolute link,
        # we don't need to change it
        if not (loc in [d.name for d in dup]) and not loc.startswith('http'):
            elem.attrib[type] = '../' + loc

    return etree


def fix_svg(etree, dup):
    root = etree.getroot()
    href_attrib = '{' + root.nsmap['xlink'] + '}href'
    for link in root.xpath('//*[local-name() = "a"]'):
        href = link.attrib[href_attrib]
        if not href.startswith('http') and not (href in [d.name for d in dup]):
            link.attrib[href_attrib] = '../' + href

    return etree


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
    dup = [doxy_dir/c for c, v in Counter(files_case_ins).items() if v > 1]
    print(dir.name, [p.name for p in dup])
    for df in dup:
        for file_name, lines in file_contents.items():
            if lines is None or file_name == df.name:
                continue
            new_lines = []
            found = False
            for line in lines:
                if df.name in line:
                    found = True
                    line = line.replace(df.name, dupe_dir.name + '/' + df.name)
                new_lines.append(line)
            if found:
                with open(doxy_dir.joinpath(file_name), 'w') as file_obj:
                    file_obj.write(''.join(new_lines))
                # continue

        if df.suffix == '.html':
            etree = HT.parse(str(df))
            doc = fix_html(etree, dup)
            with open(dupe_dir/df.name, 'w') as file_obj:
                file_obj.write(HT.tostring(doc).decode('utf-8'))
            df.unlink()
        elif df.suffix == '.svg':
            etree = ET.parse(str(df))
            doc = fix_svg(etree, dup)
            with open(dupe_dir/df.name, 'w') as file_obj:
                file_obj.write(ET.tostring(doc).decode('utf-8'))
            df.unlink()
        else:
            raise Exception('Unknown suffix: {}'.format(df))
