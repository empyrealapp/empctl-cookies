from .get_eth_price import get_eth_price

"""
This is where you will add all the tools you would like to be made available to your agent.
"""

TOOLS = [
    get_eth_price,
]

__all__ = ["TOOLS"]
