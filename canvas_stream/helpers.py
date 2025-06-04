"Helpers funcitions"

from __future__ import annotations

import unicodedata
import re
from datetime import datetime
from string import Template
from urllib.parse import urlsplit, parse_qs, unquote_plus
import os


def naive_datetime(dt_str: str):
    "Transfors a datetime string to a naive datetime string"
    return datetime.fromisoformat(dt_str.strip("Z")).replace(tzinfo=None).isoformat()


def slugify(
    value: str,
    *,
    lower=False,
    separator="_",
    ascii_only=True,
    capitalize=False,
    preset=None
) -> str:
    """Make a string safe for filenames, with flexible formatting and presets."""
    value = unquote_plus(value.strip())

    if preset:
        presets = {
            "snake_case":      {"lower": True,  "separator": "_", "ascii_only": True,  "capitalize": False},
            "kebab-case":      {"lower": True,  "separator": "-", "ascii_only": True,  "capitalize": False},
            "PascalCase":      {"lower": False, "separator": "",  "ascii_only": True,  "capitalize": True},
        }
        if preset in presets:
            preset_cfg = presets[preset]
            lower = preset_cfg["lower"]
            separator = preset_cfg["separator"]
            ascii_only = preset_cfg["ascii_only"]
            capitalize = preset_cfg["capitalize"]

    if ascii_only:
        value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("ascii")
    else:
        value = unicodedata.normalize("NFKC", value)

    value = re.sub(r'[<>:"/\\|?*\s]+', separator, value)
    value = re.sub(f'{re.escape(separator)}+', separator, value).strip(separator)

    if lower:
        value = value.lower()
    if capitalize:
        value = value.capitalize()

    return value

HTML_HYPERLINK_DOCUMENT_TEMPLATE = Template(
    """
<html>
    <head>
        <meta http-equiv="refresh" content="0; url=${url}" />
    </head>
</html>
"""
)


def html_hyperlink_document(url: str):
    """OS-independent solution to make .url like files"""
    return HTML_HYPERLINK_DOCUMENT_TEMPLATE.substitute({"url": url})


def userfull_download_url_or_empty_str(url: str):
    "Verifies if the `verifier` key is in the url parameters"

    if "verifier" in parse_qs(urlsplit(url).query):
        return url
    return ""


def is_format_excluded(file_name, excluded_formats):
    # Extract the file extension and convert it to lowercase
    _, file_ext = os.path.splitext(file_name)
    file_ext = file_ext.lower()

    # Check if the file extension is in the list of excluded formats
    return file_ext in excluded_formats or file_ext.lstrip('.') in excluded_formats
