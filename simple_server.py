import asyncio  
import websockets  
  
# Set to keep track of connected clients  
connected_clients = set()  
  
async def websocket_handler(websocket):  
    # Add client to the set  
    connected_clients.add(websocket)  
    client_id = id(websocket)  
    print(f"Client connected: {client_id}")  
      
    try:  
        # Handle messages  
        async for message in websocket:  
            print(f"Received from client {client_id}: {message}")  
              
            # Echo the message back  
            await websocket.send(f"Server received: {message}")  
              
            # Broadcast to all other clients  
            for client in connected_clients:  
                if client != websocket:  
                    try:  
                        await client.send(f"Client {client_id} says: {message}")  
                    except:  
                        pass  
      
    except Exception as e:  
        print(f"Error with client {client_id}: {e}")  
      
    finally:  
        # Remove client from the set  
        connected_clients.remove(websocket)  
        print(f"Client disconnected: {client_id}")  
  
async def main():  
    # Start WebSocket server  
    async with websockets.serve(websocket_handler, "localhost", 8765):  
        print("WebSocket server started on ws://localhost:8765")  
        await asyncio.Future()  # Run forever  
  
if __name__ == "__main__":  
    try:  
        asyncio.run(main())  
    except KeyboardInterrupt:  
        print("Server shutting down...")  