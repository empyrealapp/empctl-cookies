#!/bin/bash

echo "Running the FastAPI server"
poetry run mcp run {{ cookiecutter.project_slug }}/main.py --transport=sse
