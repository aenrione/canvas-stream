#!/bin/bash

# Defaults
URL="${URL:-https://to.canvas.com}"
ACCESS_TOKEN="${ACCESS_TOKEN:-default_access_token}"
OUTPUT_PATH="${OUTPUT_PATH:-canvas}"
EXCLUDED_FORMATS="${EXCLUDED_FORMATS:-[\"mp4\"]}"

# Slug config defaults
SLUG_PRESET="${SLUG_PRESET}"
SLUG_SEPARATOR="${SLUG_SEPARATOR:-_}"
SLUG_LOWER="${SLUG_LOWER:-false}"
SLUG_ASCII_ONLY="${SLUG_ASCII_ONLY:-true}"
SLUG_CAPITALIZE="${SLUG_CAPITALIZE:-false}"

cat <<EOF > config.toml
url = "${URL}"
access_token = "${ACCESS_TOKEN}"
output_path = "${OUTPUT_PATH}"
excluded_formats = ${EXCLUDED_FORMATS}

[slug]
preset = "${SLUG_PRESET}"
separator = "${SLUG_SEPARATOR}"
lower = ${SLUG_LOWER}
ascii_only = ${SLUG_ASCII_ONLY}
capitalize = ${SLUG_CAPITALIZE}
EOF

exec python -m canvas_stream

