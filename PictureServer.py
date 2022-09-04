import os;
class PictureServer():
  def __init__(self):
    print('init')
  def list_files(self, path):
    files = os.listdir(path)
    return files
  
  def build_link(self, path, file):
    return '<a href="{}/{}">{}</a>'.format(path, file, file)

  def build_links_string(self, path):
    links = self.build_links(path)
    lis = ''
    for link in links:
        lis += '<li>{}</li>'.format(link)

    return lis
  def build_links(self, path):
    files = self.list_files(path)
    links=[]
    for file in files:
      links.append(self.build_link(path, file))

    return links

  def build_page(self, path):
    links = self.build_links(path)
    return "<html><body>{}</body></html>".format(links)
  def build_page_string(self, path):
    links = self.build_links_string(path)
    return "<html><body><ul>{}</ul></body></html>".format(links)