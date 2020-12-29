#!/bin/bash

set -e
set -v

gunicorn -b :"$PORT" pantry.wsgi
