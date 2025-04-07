export DEPLOYMENT_FILESYSTEM_PATH=.
alembic revision --autogenerate -m "initial migration"
alembic upgrade head
poetry install
poetry lock

echo "Starting {{ cookiecutter.project_name }}"
poetry run {{ cookiecutter.project_slug }}
