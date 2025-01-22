#!/bin/bash

set -eu

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/.."
cd "$ROOT"

if [ -d "venv" ]; then
    source venv/bin/activate
else
    echo "No virtual environment found. Run util/dev-setup.sh to configure one."
    exit 1
fi
