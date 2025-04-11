#!/bin/bash

echo "Creating DB File"
touch $DEPLOYMENT_FILESYSTEM_PATH/db.sqlite

echo "Making the deployment filesystem path writable"
chmod -R o+w $DEPLOYMENT_FILESYSTEM_PATH/db.sqlite

echo "Running migrations"
poetry run alembic upgrade head

echo "Running the agent"
poetry run ${cookiecutter.project_slug}
