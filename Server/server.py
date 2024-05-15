import asyncio
import websockets

async def handle_client(websocket, path):
    try:
        async for message in websocket:
            print(f"Received message from client: {message}")
            response = f"Server received: {message}"
            await websocket.send(response)
    except websockets.exceptions.ConnectionClosed:
        print("Client disconnected")

async def start_server():
    try:
        server = await websockets.serve(handle_client, "localhost", 8765)
        print("Server started")
        await server.wait_closed()
    except OSError as e:
        print(f"Failed to start server: {e}")

asyncio.get_event_loop().run_until_complete(start_server())