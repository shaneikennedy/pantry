#!/bin/bash
set -e
set -v

python -m flake8 pantry --config=.flake8
