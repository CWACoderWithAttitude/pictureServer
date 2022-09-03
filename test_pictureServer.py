# https://docs.pytest.org/en/7.1.x/getting-started.html#get-started
import os

class PictureServer():
  def __init__(self):
    print('init')
  def list_files(self, path):
    files = os.listdir(path)
    return files
  
  def build_link(self, path, file):
    return '<a href="{}/{}">{}</a>'.format(path, file, file)

  def build_links(self, path):
    files = self.list_files(path)
    links=[]
    for file in files:
      links.append(self.build_link(path, file))

    return links

  def build_page(self, path):
    links = self.build_links(path)
    return "<html><body>{}</body></html>".format(links)
  
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
  