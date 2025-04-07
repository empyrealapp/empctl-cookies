# Use Python 3.12 slim image as base
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:$PATH"

# Copy project files
COPY pyproject.toml ./
COPY {{ cookiecutter.project_slug }}/ ./{{ cookiecutter.project_slug }}/

# Configure Poetry
RUN poetry config virtualenvs.create false

# Install dependencies
RUN poetry install --no-interaction --no-ansi
RUN poetry lock

# Copy remaining files
COPY . .

# TODO: we want to make sure that the agent always syncs its db to the latest migration
#       but we need to inject the DEPLOYMENT_FILESYSTEM_PATH to the container so it knows
#       where to find the sqlite db file
ENV DEPLOYMENT_FILESYSTEM_PATH=.

# Run migrations
RUN poetry run alembic upgrade head

# Set the default command
CMD ["poetry", "run", "{{ cookiecutter.project_slug }}"]
