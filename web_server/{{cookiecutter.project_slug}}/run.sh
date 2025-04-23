#!/bin/bash

echo "Running the FastAPI server"
poetry run uvicorn {{ cookiecutter.project_slug}}.main:app --host 0.0.0.0 --port 8000
