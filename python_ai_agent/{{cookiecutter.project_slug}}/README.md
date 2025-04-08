# {{ cookiecutter.project_name }}

Description: Python AI agent

### Quickstart 

This will migrate your sqlite models, install dependencies, and run the agent.

```bash
chmod +x quickstart.sh && ./quickstart.sh
```

### Environment

For production, you will need to set your empctl environment variables in the github repo secrets.

You will also need to set a few environment variables for local testing.

You will need the `DEPLOYMENT_FILESYSTEM_PATH` to be set.  When deployed in emp cloud, this will be set automatically, but for testing, this will say where your sqlite database will be stored.  You can export this into your local shell, or set it directly in your `.env` file.

```bash
export DEPLOYMENT_FILESYSTEM_PATH=.
```

### Create a new migration
```bash
alembic revision --autogenerate -m "message"
```

### Apply the migrations
```bash
alembic upgrade head
```

### Run the example
```bash
# include the DEPLOYMENT_FILESYSTEM_PATH to avoid using the default
DEPLOYMENT_FILESYSTEM_PATH=. poetry run agent
```

# NOTE: to run locally, you need to set the DEPLOYMENT_FILESYSTEM_PATH to a temporary directory.
#       this is where you will store the database files.
```bash
export DEPLOYMENT_FILESYSTEM_PATH=/tmp
```
