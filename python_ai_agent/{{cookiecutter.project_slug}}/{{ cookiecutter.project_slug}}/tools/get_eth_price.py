import os

from eth_rpc import set_alchemy_key
from eth_typeshed.chainlink.eth_usd_feed import ChainlinkPriceOracle, ETHUSDPriceFeed

set_alchemy_key(os.environ["ALCHEMY_API_KEY"])


async def get_eth_price():
    price_feed = ETHUSDPriceFeed(address=ChainlinkPriceOracle.Ethereum.ETH)
    price = await price_feed.latest_round_data().get()
    return f"The current price of ETH is ${price.answer / 10 ** 8}"
