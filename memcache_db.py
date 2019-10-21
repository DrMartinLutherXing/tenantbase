import sqlite3
from sql import *

class MemcacheDB:
	def __init__(self, filename='database.sqlite'):
                #connect
		self.conn = sqlite3.connect(filename)
                #create memcache table
                self.conn.execute(CREATE_TABLE)
                #cursor
		self.cur = self.conn.cursor()

        def insert(self, key, value, flag):
            """ insert row into me db """
            self.cur.execute(INSERT_TABLE, (key, value, flag))
            self.cur.commit()

        def get(self, key):
            """ retrieve row data associated with key """
            self.cur.execute(GET_TABLE, (key, ))
            row = self.cur.fetchone()
            return row

        def clear(self, key):
            """ remove a row from db """
	    self.cur.execute(DELETE_TABLE, (key, ))
	    self.conn.commit()

        def end(self):
	    """ commit and close db connection """
	    self.conn.commit()
	    self.conn.close()
