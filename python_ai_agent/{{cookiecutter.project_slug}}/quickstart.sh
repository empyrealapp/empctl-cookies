export DEPLOYMENT_FILESYSTEM_PATH=.

# Install dependencies
poetry install
poetry lock

# Run migrations
alembic revision --autogenerate -m "initial migration"
alembic upgrade head
