#!/bin/bash
set -e
set -v

python -m flake8 --ignore=F403,F401 pantry --config=.flake8
