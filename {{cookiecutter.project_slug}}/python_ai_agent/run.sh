# Run migrations
poetry run alembic upgrade head

# Run the agent
poetry run {{ cookiecutter.project_slug }}
