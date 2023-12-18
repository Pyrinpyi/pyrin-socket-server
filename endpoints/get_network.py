# encoding: utf-8

from server import pyrin_client


async def get_network():
    """
    Get some global pyrin network information
    """
    resp = await pyrin_client.request("getBlockDagInfoRequest")
    return resp["getBlockDagInfoResponse"]
