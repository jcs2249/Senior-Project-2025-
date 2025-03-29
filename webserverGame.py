import http.server  
import socketserver  
import json  
import urllib.parse  
import time  
# to start the server python3 webserver.py
# To start the ngrok tunnel, ngrok http --url=aarj.ngrok.io 8000
# The website is aarj.ngrok.io
# In-memory storage for lobby users and chat messages  
lobbies = {}  
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
              
        # Handle API endpoint for chat messages  
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
  
        # Serve the main HTML file on root  
        if path == '/':  
            self.path = '/GameWebsite.html'  
  
        return http.server.SimpleHTTPRequestHandler.do_GET(self)  
  
    def do_POST(self):  
        parsed_url = urllib.parse.urlparse(self.path)  
        path = parsed_url.path  
  
        # Handle joining a lobby: POST /api/lobby/join  
        if path == '/api/lobby/join':  
            content_length = int(self.headers.get('Content-Length', 0))  
            post_data = self.rfile.read(content_length)  
  
            try:  
                data = json.loads(post_data.decode())  
                lobby_code = data.get('lobbyCode', '')  
                username = data.get('username', '')  
                is_host = data.get('isHost', False)  
            except Exception as e:  
                self.send_response(400)  
                self.end_headers()  
                self.wfile.write(json.dumps({'error': 'Invalid JSON input'}).encode())  
                return  
  
            if not lobby_code or not username:  
                self.send_response(400)  
                self.end_headers()  
                self.wfile.write(json.dumps({'error': 'Missing lobbyCode or username'}).encode())  
                return  
  
            # Create the lobby if not present  
            if lobby_code not in lobbies:  
                lobbies[lobby_code] = []  
                chat_messages[lobby_code] = []  
  
            # Check if username is already in the lobby  
            if not any(u['username'] == username for u in lobbies[lobby_code]):  
                lobbies[lobby_code].append({'username': username, 'isHost': is_host})  
                  
                # Add a system message about the new user  
                system_msg = {  
                    'username': 'System',  
                    'message': f'{username} has joined the lobby.',  
                    'timestamp': int(time.time() * 1000)  
                }  
                chat_messages[lobby_code].append(system_msg)  
  
            self.send_response(200)  
            self.send_header('Content-Type', 'application/json')  
            self.send_header('Access-Control-Allow-Origin', '*')  
            self.end_headers()  
            self.wfile.write(json.dumps(lobbies[lobby_code]).encode())  
            return  
              
        # Handle sending a chat message: POST /api/chat/send  
        elif path == '/api/chat/send':  
            content_length = int(self.headers.get('Content-Length', 0))  
            post_data = self.rfile.read(content_length)  
              
            try:  
                data = json.loads(post_data.decode())  
                lobby_code = data.get('lobbyCode', '')  
                username = data.get('username', '')  
                message = data.get('message', '')  
                timestamp = data.get('timestamp', int(time.time() * 1000))  
            except Exception as e:  
                self.send_response(400)  
                self.end_headers()  
                self.wfile.write(json.dumps({'error': 'Invalid JSON input'}).encode())  
                return  
                  
            if not lobby_code or not username or not message:  
                self.send_response(400)  
                self.end_headers()  
                self.wfile.write(json.dumps({'error': 'Missing required fields'}).encode())  
                return  
                  
            # Create the lobby's message array if it doesn't exist  
            if lobby_code not in chat_messages:  
                chat_messages[lobby_code] = []  
                  
            # Add the message  
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
  
        # Fallback to static file serving for POST if not recognized  
        return http.server.SimpleHTTPRequestHandler.do_POST(self)  
  
PORT = 8000  
HOST = "0.0.0.0"  
  
print(f"\nStarting server on http://{HOST}:{PORT}")  
print("(Press CTRL+C to quit)")  
  
with socketserver.TCPServer((HOST, PORT), MyHandler) as httpd:  
    try:  
        httpd.serve_forever()  
    except KeyboardInterrupt:  
        print("\nServer stopped.")   