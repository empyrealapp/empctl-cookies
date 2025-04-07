export DEPLOYMENT_FILESYSTEM_PATH=.

# Run migrations
alembic revision --autogenerate -m "initial migration"
alembic upgrade head

# Install dependencies
poetry install
poetry lock

# Run the agent
echo "Starting {{ cookiecutter.project_name }}"
poetry run {{ cookiecutter.project_slug }}
