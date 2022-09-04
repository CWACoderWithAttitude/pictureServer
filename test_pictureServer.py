# https://docs.pytest.org/en/7.1.x/getting-started.html#get-started
from PictureServer import PictureServer
from PictureServer import *
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
# https://pythonbasics.org/webserver/
class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>https://pythonbasics.org</title></head>", "utf-8"))
        self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>This is an example web server.</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

  
def test_init():
  ps = PictureServer()
  assert ps != ""

def test_list_files():
  ps = PictureServer()
  path="/Users/volker/Pictures/misc"
  files = ps.list_files( path)
  assert len(files) >= 0

def test_build_link():
  ps = PictureServer()
  path="/Users/volker/Pictures/misc"
  files = ps.list_files( path)
  link = ps.build_link(path, files[1])
  assert link == '<a href="/Users/volker/Pictures/misc/homeoffice_kontrolle.jpg">homeoffice_kontrolle.jpg</a>'

def test_build_link_list():
  ps = PictureServer()
  path="/Users/volker/Pictures/misc"
  links = ps.build_links(path)

  assert len(links) > 1
  #assert links == ''

def test_build_page():
  ps = PictureServer()
  path="/Users/volker/Pictures/misc"
  page = ps.build_page(path)
  assert 0 < page.find('</html>')

def test_link_count_on_page():
  ps = PictureServer()
  path="/Users/volker/Pictures/misc"
  page = ps.build_page(path)
  assert 0 < page.find('<a href')  
  assert len(ps.list_files(path)) == page.count('<a href')  
  
if __name__ == "__main__":  
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")