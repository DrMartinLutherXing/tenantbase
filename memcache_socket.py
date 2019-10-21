# Echo server program
import socket
from memcache_db import MemcacheDB

HOST = 'localhost'
PORT = 11211

class MemcacheSocket:
    def __init__(self, db_file='memcache.sqlite'):
        self.db = MemcacheDB(db_file)
        self.init_sock()
        self.run()

    def init_sock(self):
	self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	self.sock.bind((HOST, PORT))
	self.sock.listen(1)

    def get(self, key):
        return self.db.get(key)

    def set(self, key, val, flags):
        self.db.insert(key, val, flags)

    def delete(self, key):
        self.db.clear(key)

    def handle(self, conn):
        print "handler"

    def run(self):
        conn, addr = self.sock.accept()
        print "connection from: " + addr
	while 1:
	    try:
		self.handle(conn)
	    except socket.error as err:
	        return self.close()
        self.close()

    def close(self):
        self.db.end()
        self.sock.close()
        self.sock = None
