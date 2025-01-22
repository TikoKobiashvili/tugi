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

print_header "Running flake8"
python -m flake8 .
print_header "Running mypy"
python -m mypy --no-error-summary .
print_header "Running bandit"
bandit -c pyproject.toml -r -q -f custom .
