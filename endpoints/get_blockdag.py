# encoding: utf-8

from server import pyrin_client


async def get_blockdag():
    """
    Get some global Pyipad BlockDAG information
    """
    resp = await pyrin_client.request("getBlockDagInfoRequest")
    return resp["getBlockDagInfoResponse"]
