# encoding: utf-8

from server import pyrin_client


async def get_coinsupply():
    """
    Get $PYI coin supply information
    """
    resp = await pyrin_client.request("getCoinSupplyRequest")
    return {
        "circulatingSupply": resp["getCoinSupplyResponse"]["circulatingLeor"],
        "totalSupply": resp["getCoinSupplyResponse"]["circulatingLeor"],
        "maxSupply": resp["getCoinSupplyResponse"]["maxLeor"]
    }


async def get_circulating_coins(in_billion: bool = False):
    """
    Get circulating amount of $PYI token as numerical value
    """
    resp = await pyrin_client.request("getCoinSupplyRequest")
    coins = str(float(resp["getCoinSupplyResponse"]["circulatingLeor"]) / 100000000)
    if in_billion:
        return str(round(float(coins) / 1000000000, 2))
    else:
        return coins


async def get_circulating_coins():
    """
    Get total amount of $PYI token as numerical value
    """
    resp = await pyrin_client.request("getCoinSupplyRequest")
    return str(float(resp["getCoinSupplyResponse"]["circulatingLeor"]) / 100000000)
