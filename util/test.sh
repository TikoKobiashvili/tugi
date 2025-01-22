#!/usr/bin/env bash

set -eu

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/.."
cd "$ROOT"

source util/venv.sh

print_header() {
    printf '\e[1;34m'
    printf '%s\n' "$1..."
    printf '\e[0m'
}

print_header "Running pytest"
python -m coverage run -m pytest . -s -v
python -m coverage report
python -m coverage html

