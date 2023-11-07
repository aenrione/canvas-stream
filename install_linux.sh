#!/bin/bash

# Create a virtual environment
python3 -m venv .venv

# Activate the virtual environment (Unix-like system)
source .venv/bin/activate

# Install Python packages from requirements.txt
python -m pip install -r requirements.txt

