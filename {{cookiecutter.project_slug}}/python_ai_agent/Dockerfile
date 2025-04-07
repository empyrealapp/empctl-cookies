FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:$PATH"

COPY . .

RUN poetry config virtualenvs.create false

RUN poetry install --no-interaction --no-ansi
RUN poetry lock

# will be set automatically in emp cloud, but for local development, the user needs to set it
ENV DEPLOYMENT_FILESYSTEM_PATH=.

ENTRYPOINT ["poetry", "run"]
CMD ["{{ cookiecutter.project_slug }}"]
