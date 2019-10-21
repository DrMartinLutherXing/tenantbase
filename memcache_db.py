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

	def keys(self):
		""" return a generator of all keys """
		cursor = self.conn.cursor()
		for row in cursor.execute(FETCH_TABLE):
			yield row[0]

        def insert(self, key, value, flag):
            """ insert (or update) db row """
            if key not in self.keys():
		    #if key doesn't exist create
		    self.cur.execute(INSERT_TABLE, (key, value, flag))
            else:
		    #update the key's value
                    #memcache 'set' overwrites values
		    self.cur.execute(UPDATE_TABLE, (value, flag, key))
            self.conn.commit()

        def get(self, key):
            """ retrieve row data associated with key """
            self.cur.execute(GET_TABLE, (key, ))
            row = self.cur.fetchone()
            return row[0], row[1], row[2]

	def fetch(self):
		""" return generator for rows in memcache """
		cursor = self.conn.cursor()
		for row in cursor.execute(FETCH_TABLE):
			yield row[0], row[1], row[2]

        def clear(self, key):
            """ remove a row from db """
	    #check key exists
	    if key not in self.keys():
	        raise KeyError(key)
	    self.cur.execute(DELETE_TABLE, (key, ))
	    self.conn.commit()

        def end(self):
	    """ commit and close db connection """
	    self.conn.commit()
	    self.conn.close()

