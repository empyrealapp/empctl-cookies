import os
from datetime import datetime, timezone

from emp_agents import AgentBase
from emp_agents.providers import OpenAIModelType, OpenAIProvider
from emp_hooks import log, manager, scheduler
from emp_hooks.handlers import twitter
from tweepy import Tweet
from tweepy.client import Client

from .prompts import MAIN_PROMPT

agent = AgentBase(
    provider=OpenAIProvider(default_model=OpenAIModelType.gpt4o),
    prompt=MAIN_PROMPT,
    sync_tools=True,
)


@twitter.on_tweet(os.environ["TWITTER_QUERY"])
async def on_simmi_tweet(tweet: Tweet) -> bool:
    """Reply to every tweet that mentions the twtiter query"""

    log.info(f"Received tweet: {tweet.id} - {tweet.text}")
    tweet_id = tweet.id

    # If you have the consumer key set, assume you have the full set of keys
    if os.environ.get("TWITTER_CONSUMER_KEY"):
        client = Client(
            bearer_token=os.environ["TWITTER_BEARER_TOKEN"],
            consumer_key=os.environ["TWITTER_CONSUMER_KEY"],
            consumer_secret=os.environ["TWITTER_CONSUMER_SECRET"],
            access_token=os.environ["TWITTER_ACCESS_TOKEN"],
            access_token_secret=os.environ["TWITTER_ACCESS_TOKEN_SECRET"],
        )
    else:
        client = Client(bearer_token=os.environ["TWITTER_BEARER_TOKEN"])

    response = await agent.answer(tweet.text)

    client.create_tweet(
        text=response,
        in_reply_to_tweet_id=tweet_id,
    )

    return True


@scheduler.on_schedule("0 12 * * *")
def print_at_noon_every_day():
    """Print a tweet at noon every day"""

    now = datetime.now(timezone.utc)
    client = Client(bearer_token=os.environ["TWITTER_BEARER_TOKEN"])
    client.create_tweet(
        text=f"It's {now.strftime('%m/%d %H:%M')} UTC! ",
    )


def main():
    manager.hooks.run_forever()
