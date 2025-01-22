#!/usr/bin/env bash

set -eu

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/.."
cd $ROOT

if [ -d "venv" ]; then
    echo "Virtual environment found!"
    source venv/bin/activate
else
    echo "No virtual environment found. Attempting to create one..."
    python3.12 -m venv venv
    source venv/bin/activate
fi

pip install --upgrade pip
pip install -r requirements/dev.txt

