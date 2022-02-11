"""Add warning to old docs."""

import lxml.html as lh
from lxml import etree
from pathlib import Path

bquote = etree.Element("blockquote")
d = etree.SubElement(bquote, "div")
admonition = etree.SubElement(d, "div", {"class": "admonition warning"})
head = etree.SubElement(admonition, "p", {"class": "first admonition-title"})
head.text = "Warning"
last = etree.SubElement(admonition, "p", {"class": "last"})
last.text = "This documentation is for an old version of Cantera. You can find docs for newer versions "
link = etree.SubElement(
    last,
    "a",
    {"class": "reference external", "href": "https://cantera.org/documentation"},
)
link.text = "here"
link.tail = "."

folders = [Path(f"api-docs/docs-{x}") for x in (2.4,)]
for folder in folders:
    for html_file in folder.glob("sphinx/**/*.html"):
        print(html_file)

        doc = lh.parse(str(html_file))
        body = doc.xpath('//div[@class="body"]')[0]
        body.insert(0, bquote)

        head = doc.find("head")
        meta = etree.SubElement(head, "meta", {"name": "robots", "content": "noindex"})
        with open(html_file, "w", encoding="utf-8") as file_obj:
            file_obj.write(lh.tostring(doc).decode("utf-8"))
