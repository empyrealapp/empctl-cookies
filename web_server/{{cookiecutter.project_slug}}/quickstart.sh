#!/bin/bash

# Install dependencies
poetry install
poetry lock

empctl services init --name {{ cookiecutter.service_name }} --ignore-exists
empctl services update --ingress-port 8000 --name {{ cookiecutter.service_name }}

# Run the server
poetry run uvicorn {{ cookiecutter.project_slug }}.main:app --host 0.0.0.0 --port 8000
