#! /usr/bin/env bash
set -e

source activate $PYTHONVENV
exec gunicorn run:server -b 0.0.0.0:8000