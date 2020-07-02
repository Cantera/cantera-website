import lxml.html as lh
from pathlib import Path

for f in Path("api-docs/docs-2.4/sphinx/html").glob("**/*.html"):
    print(f)
    doc = lh.parse(str(f))
    head = doc.find("head")
    for l in head.findall("link"):
        if "jsdelivr" not in l.get("href", ""):
            continue
        l.set("href", "https://cdn.jsdelivr.net/npm/katex@0.11.1/dist/katex.min.css")
        l.set(
            "integrity",
            "sha384-zB1R0rpPzHqg7Kpt0Aljp8JPLqbXI3bhnPWROx27a9N0Ll6ZP/+DiW/UqRcLbRjq",
        )
        l.set("crossorigin", "anonymous")

    for l in head.findall("script"):
        if "jsdelivr" not in l.get("src", ""):
            continue
        if "katex.min.js" in l.get("src"):
            l.set("src", "https://cdn.jsdelivr.net/npm/katex@0.11.1/dist/katex.min.js")
            l.set(
                "integrity",
                "sha384-y23I5Q6l+B6vatafAwxRu/0oK/79VlbSz7Q9aiSZUvyWYIYsd+qj+o24G5ZU2zJz",
            )
        elif "auto-render.min.js" in l.get("src"):
            l.set(
                "src",
                "https://cdn.jsdelivr.net/npm/katex@0.11.1/dist/contrib/auto-render.min.js",
            )
            l.set(
                "integrity",
                "sha384-kWPLUVMOks5AQFrykwIup5lo0m3iMkkHrD0uJ4H5cjeGihAutqP0yW0J6dpFiVkI",
            )

        l.set("defer", None)
        l.set("crossorigin", "anonymous")

    with open(f, "w") as file_obj:
        file_obj.write(lh.tostring(doc).decode("utf-8"))
