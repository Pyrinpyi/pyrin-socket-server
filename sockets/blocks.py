# encoding: utf-8

from server import pyrin_client, sio

BLOCKS_CACHE = []
TASKS = []


async def config():
    async def on_new_block(e):
        try:
            block_info = e["blockAddedNotification"]["block"]
        except KeyError:
            return

        global BLOCKS_CACHE

        emit_info = {
            'block_hash': block_info["verboseData"]["hash"],
            'difficulty': block_info["verboseData"]["difficulty"],
            'blueScore': block_info["header"]["blueScore"],
            'timestamp': block_info["header"]["timestamp"],
            'txs': [{
                'txId': x["verboseData"]["transactionId"],
                'outputs': [(output["verboseData"]["scriptPublicKeyAddress"], output["amount"]) for output in
                            x["outputs"]]
            } for x in block_info["transactions"]]
        }

        BLOCKS_CACHE.append(emit_info)
        if len(BLOCKS_CACHE) > 50:
            BLOCKS_CACHE.pop(0)

        await sio.emit("new-block", emit_info, room="blocks")

    await pyrin_client.notify("notifyBlockAddedRequest", None, on_new_block)


@sio.on("last-blocks")
async def get_last_blocks(sid, msg):
    await sio.emit("last-blocks", BLOCKS_CACHE, to=sid)
