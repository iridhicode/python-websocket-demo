import asyncio
import websockets

async def connect_to_server():
    try:
        async with websockets.connect("ws://localhost:8765") as websocket:
            message = "Hello, server!"
            await websocket.send(message)
            response = await websocket.recv()
            print(f"Received response from server: {response}")
    except websockets.exceptions.ConnectionClosedError:
        print("Server disconnected")
    except OSError as e:
        print(f"Failed to connect to server: {e}")

asyncio.get_event_loop().run_until_complete(connect_to_server())
