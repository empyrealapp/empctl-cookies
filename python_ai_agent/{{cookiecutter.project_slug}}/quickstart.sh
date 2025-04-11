export DEPLOYMENT_FILESYSTEM_PATH=.

# Run migrations
alembic revision --autogenerate -m "initial migration"
alembic upgrade head

# Install dependencies
poetry install
poetry lock

# setup empctl
empctl services init --name {{ cookiecutter.service_name }}
