#!/usr/bin/env python
import os
from index import HTMLCompiler
from BaseHTTPServer import HTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler

index_page = HTMLCompiler()

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            index_page.run()
        return SimpleHTTPRequestHandler.do_GET(self)

if __name__ == '__main__':
    httpd = HTTPServer(('127.0.0.1', 8000), MyHandler)
    httpd.serve_forever()

