# Echo server program
import socket
from memcache_db import MemcacheDB

HOST = 'localhost'
PORT = 11211
BUFFER = 1024
PROTOCOL = [ 'set', 'get', 'delete' ]

class MemcacheSocket:
    def __init__(self, db_file='database.sqlite'):
        self.db = MemcacheDB(db_file)
        self.init_sock()
        self.run()

    def init_sock(self):
	self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	self.sock.bind((HOST, PORT))
	self.sock.listen(1)

    def get(self, req):
        try:
            row = self.db.get(req[1])
            resp = "VALUE %s %i 0 %i\r\n%s\r\nEND\r\n" % (row[0], row[2], len(row[1]), row[1])
        except KeyError:
            resp = "END\r\n"
        return resp

    def set(self, req, conn):
        if len(req) == 5:
            buffer_size = int(req[4])
            value = ""
            #go thru buffer building value until full size specified
            while buffer_size > 0:
                _BUFFER = buffer_size if buffer_size < BUFFER else BUFFER
                _value = conn.recv(_BUFFER)
                if not _value: break
                value += _value
                buffer_size -= BUFFER
            #clear newline
            conn.recv(BUFFER)
            self.db.insert(req[1], value, int(req[2]))
            resp = "STORED\r\n"
        else:
            resp = "CLIENT_ERROR insufficient arguments\r\n"
        return resp

    def delete(self, req):
        try:
            row = self.db.clear(req[1])
            resp = "DELETED\r\n"
        except KeyError:
            resp = "NOT_FOUND\r\n"
        return resp

    def handle(self, conn):
        data = conn.recv(BUFFER)[::]
        #check non empty
        if not data:
            resp = "CLIENT_ERROR empty input\r\n"
        else:
            req = data.split()
            #check command exists
            if req[0] not in PROTOCOL:
                resp = "ERROR\r\n"
            elif req[0] == 'get':
                resp = self.get(req)
            elif req[0] == 'set':
                resp = self.set(req, conn)
            elif req[0] == 'delete':
                resp = self.delete(req)
        conn.send(resp)

    def run(self):
        conn, addr = self.sock.accept()
	while 1:
	    try:
		self.handle(conn)
	    except socket.error as err:
                print err
	        return self.close()
        self.close()

    def close(self):
        self.db.end()
        self.sock.close()
        self.sock = None

