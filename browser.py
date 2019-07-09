# server that sends messages at random intervals

import asyncio
import datetime
import random
import websockets

connected = set()

async def chat(websocket, path):
	connected.add(websocket)
	try:
	    async for message in websocket:
	    	await asyncio.wait([ws.send(message) for ws in connected])
	except:
		connected.remove(websocket)


start_server = websockets.serve(chat, "192.168.77.25", 5678)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
