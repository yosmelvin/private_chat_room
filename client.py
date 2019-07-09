# client example

import asyncio
import websockets

async def hello():
    uri = "ws://localhost:5678"
    async with websockets.connect(uri) as websocket:
        while True:
            message = input("Type your message: ")

            await websocket.send(message)
            print(f"> {message}")

        #greeting = await websocket.recv()
        #print(f"< {greeting}")

asyncio.get_event_loop().run_until_complete(hello())
