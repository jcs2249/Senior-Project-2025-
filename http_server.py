import http.server  
import socketserver  
import os  
import socket  
import random  
  
# Create a simple favicon.ico file if it doesn't exist  
if not os.path.exists('favicon.ico'):  
    with open('favicon.ico', 'wb') as f:  
        # Write a minimal 16x16 ICO file  
        f.write(bytes.fromhex('00000100010010100000010020006804000016000000'))  
        f.write(bytes([0] * 1024))  # Add empty pixel data  
  
# Custom handler with better error logging  
class CustomHandler(http.server.SimpleHTTPRequestHandler):  
    def log_message(self, format, *args):  
        # Only log actual page requests, not favicon or other resource requests  
        if not args[0].startswith("GET /favicon.ico"):  
            super().log_message(format, *args)  
      
    def log_error(self, format, *args):  
        # Ignore 404 errors for favicon.ico  
        if "favicon.ico" not in str(args):  
            super().log_error(format, *args)  
  
def find_free_port():  
    """Find a free port to use for the HTTP server"""  
    # Try a list of common ports first  
    ports_to_try = [8000, 8080, 8888, 9000, 9090]  
    random.shuffle(ports_to_try)  # Try in random order to avoid conflicts  
      
    for port in ports_to_try:  
        try:  
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:  
                s.bind(('', port))  
                return port  
        except OSError:  
            continue  
      
    # If all preferred ports are taken, let the OS choose a port  
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:  
        s.bind(('', 0))  
        return s.getsockname()[1]  
  
# Find an available port  
try:  
    PORT = find_free_port()  
      
    with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:  
        print(f"HTTP server started at http://localhost:{PORT}")  
        print(f"Open your browser and navigate to: http://localhost:{PORT}/simple_client.html")  
        try:  
            httpd.serve_forever()  
        except KeyboardInterrupt:  
            print("HTTP server shutting down...")  
            httpd.server_close()  
except Exception as e:  
    print(f"Error starting HTTP server: {e}")  
      
    # Fallback to a very simple server if the above fails  
    print("Trying fallback server...")  
    import webbrowser  
    from http.server import HTTPServer, SimpleHTTPRequestHandler  
      
    server = HTTPServer(('localhost', 0), SimpleHTTPRequestHandler)  
    port = server.server_port  
    print(f"Fallback server started on port {port}")  
      
    # Open browser automatically  
    webbrowser.open(f'http://localhost:{port}/simple_client.html')  
      
    try:  
        server.serve_forever()  
    except KeyboardInterrupt:  
        print("Server shutting down...")  
        server.server_close()  