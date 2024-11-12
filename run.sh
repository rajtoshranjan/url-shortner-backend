#!/bin/bash

# to stop on first error
set -e

# Run required migrations
export FLASK_APP=src/api.py


# Run server
gunicorn -c gunicorn_config.py src.api:app
