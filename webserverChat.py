import http.server  
import socketserver  
import json  
import urllib.parse  
import time  
# to start the server python3 webserver.py
# To start the ngrok tunnel, ngrok http --url=aarj.ngrok.io 8000
# The website is aarj.ngrok.io
# In-memory storage for lobby users and chat messages  
# In-memory storage for lobby users and chat messages  
lobbies = {}  # Format: { lobbyCode: [username1, username2, ...] }  
chat_messages = {}  # Format: { lobbyCode: [{ username, message, timestamp }, ...] }  
  
class MyHandler(http.server.SimpleHTTPRequestHandler):  
    def do_GET(self):  
        # Parse the URL and query parameters  
        parsed_url = urllib.parse.urlparse(self.path)  
        path = parsed_url.path  
        query_params = urllib.parse.parse_qs(parsed_url.query)  
          
        # Handle API endpoint for lobby users  
        if path == '/api/lobby/users':  
            self.send_response(200)  
            self.send_header('Content-type', 'application/json')  
            self.send_header('Access-Control-Allow-Origin', '*')  
            self.end_headers()  
              
            lobby_code = query_params.get('lobbyCode', [''])[0]  
            if lobby_code and lobby_code in lobbies:  
                response = lobbies[lobby_code]  
            else:  
                response = []  
            self.wfile.write(json.dumps(response).encode())  
            return  
          
        # Handle API endpoint for chat messages (GET)  
        elif path == '/api/chat/messages':  
            self.send_response(200)  
            self.send_header('Content-type', 'application/json')  
            self.send_header('Access-Control-Allow-Origin', '*')  
            self.end_headers()  
              
            lobby_code = query_params.get('lobbyCode', [''])[0]  
            since_timestamp = int(query_params.get('since', ['0'])[0])  
              
            if lobby_code and lobby_code in chat_messages:  
                # Filter messages newer than the provided timestamp  
                response = [msg for msg in chat_messages[lobby_code] if msg['timestamp'] > since_timestamp]  
            else:  
                response = []  
            self.wfile.write(json.dumps(response).encode())  
            return  
  
        # Fallback to static file serving  
        return http.server.SimpleHTTPRequestHandler.do_GET(self)  
      
    def do_POST(self):  
        # Parse the URL path  
        parsed_url = urllib.parse.urlparse(self.path)  
        path = parsed_url.path  
          
        content_length = int(self.headers.get('Content-Length', 0))  
        post_data = self.rfile.read(content_length)  
          
        try:  
            data = json.loads(post_data.decode())  
        except Exception as e:  
            self.send_response(400)  
            self.end_headers()  
            self.wfile.write(json.dumps({'error': 'Invalid JSON input'}).encode())  
            return  
          
        # Endpoint for joining a lobby (connecting all users)  
        if path == '/api/lobby/join':  
            lobby_code = data.get('lobbyCode', '')  
            username = data.get('username', '')  
              
            if not lobby_code or not username:  
                self.send_response(400)  
                self.end_headers()  
                self.wfile.write(json.dumps({'error': 'Missing required fields'}).encode())  
                return  
              
            # If the lobby doesn't exist, create it.  
            if lobby_code not in lobbies:  
                lobbies[lobby_code] = []  
            # Add user to the lobby if not already there.  
            if username not in lobbies[lobby_code]:  
                lobbies[lobby_code].append(username)  
              
            self.send_response(200)  
            self.send_header('Content-Type', 'application/json')  
            self.send_header('Access-Control-Allow-Origin', '*')  
            self.end_headers()  
            self.wfile.write(json.dumps({'lobbyCode': lobby_code, 'users': lobbies[lobby_code]}).encode())  
            return  
  
        # Endpoint for posting chat messages  
        elif path == '/api/chat/messages':  
            lobby_code = data.get('lobbyCode', '')  
            username = data.get('username', '')  
            message = data.get('message', '')  
            timestamp = data.get('timestamp', int(time.time() * 1000))  
              
            if not lobby_code or not username or not message:  
                self.send_response(400)  
                self.end_headers()  
                self.wfile.write(json.dumps({'error': 'Missing required fields'}).encode())  
                return  
              
            # Ensure the chat_messages list exists for the lobby  
            if lobby_code not in chat_messages:  
                chat_messages[lobby_code] = []  
              
            new_message = {  
                'username': username,  
                'message': message,  
                'timestamp': timestamp  
            }  
            chat_messages[lobby_code].append(new_message)  
              
            self.send_response(200)  
            self.send_header('Content-Type', 'application/json')  
            self.send_header('Access-Control-Allow-Origin', '*')  
            self.end_headers()  
            self.wfile.write(json.dumps(new_message).encode())  
            return  
  
        # Fallback if the path is not recognized  
        self.send_response(404)  
        self.end_headers()  
        self.wfile.write(json.dumps({'error': 'Endpoint not found'}).encode())  
        return  
  
PORT = 8000  
HOST = "0.0.0.0"  
  
print(f"\nStarting server on http://{HOST}:{PORT}")  
print("(Press CTRL+C to quit)")  
  
with socketserver.TCPServer((HOST, PORT), MyHandler) as httpd:  
    try:  
        httpd.serve_forever()  
    except KeyboardInterrupt:  
        print("\nServer stopped.")   