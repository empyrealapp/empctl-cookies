# {{ cookiecutter.project_slug }}

This is a simple twitte agent, that respond to every person that tweets at them, and prints a tweet at noon every day.

## Setup

1. In order for this to run, you will need to create a twitter developer accound and get your API keys.
2. Create a `.env` file in the root of the project and add the following:

```
# you will need to provide the query that your agent will listen for
TWITTER_QUERY=@<TWITTER_USERNAME>

# also you need an OpenAI API key and a twitter bearer token to post
TWITTER_BEARER_TOKEN=...
OPENAI_API_KEY=...

# for a basic twitter developer account, you will also need:
TWITTER_CONSUMER_KEY=...
TWITTER_CONSUMER_SECRET=...
TWITTER_ACCESS_TOKEN=...
TWITTER_ACCESS_TOKEN_SECRET=...
```

## Deploying

We have integrated a github action that will automatically deploy the agent to the empyrealsdk cloud when you push to the `main` branch.


To deploy manually, you can use the following command:
NOTE: tag it with a release version

```
empctl build --tag <TAG> --push --deploy --service {{ cookiecutter.project_slug }}
```
