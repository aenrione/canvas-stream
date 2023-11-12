"Helpers funcitions"

from __future__ import annotations

import unicodedata
import re
from datetime import datetime
from string import Template
from urllib.parse import urlsplit, parse_qs
import os


def naive_datetime(dt_str: str):
    "Transfors a datetime string to a naive datetime string"
    return datetime.fromisoformat(dt_str.strip("Z")).replace(tzinfo=None).isoformat()


def slugify(value: str, lower=True, capitalize=True) -> str:
    "Makes a string a valid file path"
    # TODO: find a better way to do this (python-slugify?)
    # Normalize and encode to ASCII
    value = unicodedata.normalize('NFKD', value).encode(
        'ascii', 'ignore').decode('ascii')

    # Single regex to replace invalid characters (including spaces) with '-'
    # This regex covers: <, >, :, ", /, \, |, ?, *, and any whitespace character
    value = re.sub(r'[<>:"/\\|?*\s]+', '-', value)

    # Remove leading/trailing hyphens or dots, and condense repeated hyphens
    value = re.sub(r'^[-.]+|[-.]+$', '', value)
    value = re.sub(r'[-]+', '-', value)

    # Other replacements
    value = value.lower() if lower else value
    value = value.capitalize() if capitalize else value
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
