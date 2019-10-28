"""Add release notes for the latest version of Cantera to the site.

This command plugin performs the following actions:

1. Creates a markdown page containing the body content of the latest Cantera release on
Github (other release versions can be manually specified via options). The page will be
created in 'pages/documentation/release_notes' as '{release tag_name}.md'.

2. Modifies 'pages/documentation/index.html' by adding an entry to the 'Release Notes'
card. The entry will be titled '{release name}' and will link to the markdown page
created in (1).
"""

import re
from git import Repo
from nikola.plugin_categories import Command
import requests
from datetime import datetime
from pathlib import Path
from nikola import utils
from lxml import etree, html


def expand_cantera_commits(text):
    """Replaces shorthand Cantera commit references with their full-length hashes"""
    cantera_repo = Repo(Path.cwd().parent / "cantera")
    commits = cantera_repo.iter_commits("master")
    commit_map = {c.hexsha[:7]: c.hexsha for c in commits}

    def expand_commits(string):
        match = re.search(r"(?<=\W)[a-z0-9]{7}(?=\W)", string)
        if match is None:
            return string
        key, start, end = match.group(), match.start(), match.end()
        if key in commit_map:
            return string[:start] + commit_map[key] + expand_commits(string[end:])
        return string[:end] + expand_commits(string[end:])

    return expand_commits(text)


class NewRelease(Command):
    name = "new_release"
    doc_usage = "[options]"

    cmd_options = [
        {
            "name": "tag_name",
            "short": "t",
            "long": "tag",
            "type": str,
            "default": None,
            "help": "Tag name of desired release",
        },
        {
            "name": "release_id",
            "short": "i",
            "long": "id",
            "type": str,
            "default": "latest",
            "help": "Release ID of desired release",
        },
    ]

    def _execute(self, options, args):
        if options["tag_name"] is not None:
            urlpath = "tags/{}".format(options["tag_name"])
        else:
            urlpath = options["release_id"]

        api_response = requests.get(
            "https://api.github.com/repos/Cantera/cantera/releases/{}".format(urlpath)
        )

        if api_response.status_code == 404:
            return "A release with the provided parameters could not be found."
        if api_response.status_code != 200:
            return "An error occurred while fetching the release."

        release_json = api_response.json()
        title = release_json["name"]
        slug = release_json["tag_name"]
        filename = "{}.md".format(slug)
        iso_date = release_json["published_at"]
        date = datetime.strptime(iso_date, "%Y-%m-%dT%H:%M:%S%z").strftime("%B %-d, %Y")
        content = expand_cantera_commits(release_json["body"])
        position = content.find("\n")
        content = (
            "{}\nPublished on {} | [Full release on Github]"
            "(https://github.com/Cantera/cantera/releases/tag/{}){}"
        ).format(content[:position], date, slug, content[position:])
        path = Path.cwd() / "pages" / "documentation" / "release_notes" / filename

        compiler_plugin = self.site.plugin_manager.getPluginByName(
            "markdown", "PageCompiler"
        ).plugin_object

        compiler_plugin.create_post(
            path,
            content=content,
            onefile=True,
            title=title,
            slug=slug,
            date=iso_date,
            is_page=True,
        )

        PAGELOGGER = utils.get_logger("new_page")
        PAGELOGGER.info("{} was created at {}".format(filename, path))

        indexhtml_file = Path.cwd() / "pages" / "documentation" / "index.html"
        indexhtml_content = indexhtml_file.read_text()
        indexhtml_sections = indexhtml_content.split("\n\n")

        for i in range(len(indexhtml_sections)):
            if "release-notes" in indexhtml_sections[i]:
                section_html = html.fragment_fromstring(indexhtml_sections[i])
                releasenotes_card = section_html.get_element_by_id("release-notes")
                new_entry = etree.Element(
                    "a",
                    {
                        "href": "/documentation/release_notes/{}.html".format(slug),
                        "class": "list-group-item release-notes",
                    },
                )
                new_entry.text = title
                new_entry.tail = "\n        "
                releasenotes_card.insert(0, new_entry)
                indexhtml_sections[i] = etree.tostring(section_html, encoding="unicode")

        indexhtml_content = "\n\n".join(indexhtml_sections)
        indexhtml_file.write_text(indexhtml_content)

        PAGELOGGER = utils.get_logger("modified_page")
        PAGELOGGER.info("{} was modified".format(indexhtml_file))