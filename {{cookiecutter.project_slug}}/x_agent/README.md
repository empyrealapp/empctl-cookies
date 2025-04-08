# {{ cookiecutter.project_slug }}

This is a simple twitte agent, that respond to every person that tweets at them, and prints a tweet at noon every day.

## Setup

1. In order for this to run, you will need to create a twitter developer accound and get your API keys.
2. Create a `.env` file in the root of the project and add the following:

```
TWITTER_QUERY=@my_user_handle
TWITTER_BEARER_TOKEN=YOUR_TWITTER_BEARER_TOKEN
```

## Deploying

We have integrated a github action that will automatically deploy the agent to the empyrealsdk cloud when you push to the `main` branch.


To deploy manually, you can use the following command:
NOTE: tag it with a release version

```
empctl build --tag <TAG> --push --deploy --service {{ cookiecutter.project_slug }}
```
