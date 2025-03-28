#Joseph Saponaro - Python Script to host web server for the html.
#2/20/2025 9:24PM
import http.server
import socketserver
from pyngrok import ngrok

# Requires an Ngrok authentication token, found on the ngrok website after I signed up.
ngrok.set_auth_token("2tKV9qA2QXGm8CzaeQTH1kKLvSi_5CWNoEF7vMNQbz7znUoma")

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/GameWebsite.html'  # Change this if your HTML file has a different name
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

PORT = 8000
HOST = "0.0.0.0"

# Start Ngrok tunnel
# Note: When using ngrok, the only way I could get it to work was by installing "venv" a virtual environment extension for python,
# the command to start up the virtual env is python(python3 on linux) -m venv venv
# the command to start the web server is python webserver.py
public_url = ngrok.connect(PORT)
print(f"\nNgrok tunnel established at: {public_url}")
print("Share this URL with anyone to access your site!")
print("(Press CTRL+C to quit)")

# Starts up HTTP server and allows connections
with socketserver.TCPServer((HOST, PORT), MyHandler) as httpd:
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        # Clean up ngrok tunnel on exit
        ngrok.disconnect(public_url)
        ngrok.kill()
        print("\nServer stopped.")