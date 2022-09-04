# https://docs.pytest.org/en/7.1.x/getting-started.html#get-started
from PictureServer import PictureServer
from PictureServer import *
from http.server import BaseHTTPRequestHandler, HTTPServer
import time

from http.server import BaseHTTPRequestHandler, HTTPServer
import time

hostName = "localhost"
serverPort = 8080
# https://pythonbasics.org/webserver/
class MyServer(BaseHTTPRequestHandler):
#    def __init__(self):
#        print('MyServer::init')
#        self.path="/Users/volker/Pictures/misc"
#        self.ps = PictureServer(self)
#        self.ps.build_page(self.path)

    def do_GET(self):
        ps = PictureServer()
        path="/Users/volker/Pictures/misc"
        page = ps.build_page_string(path)
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(page, encoding='utf-8'))
        #self.wfile.write(bytes("<html><head><title>https://pythonbasics.org</title></head>", "utf-8"))
        #self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        #self.wfile.write(bytes("<body>", "utf-8"))
        #self.wfile.write(bytes("<p>This is an example web server.</p>", "utf-8"))
        #self.wfile.write(bytes("</body></html>", "utf-8"))

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")