import sqlite3

class MemcacheDB:
	def __init__(self, filename='database.sqlite'):
                #connect
		self.conn = sqlite3.connect(filename)
                #create memcache table
                self.conn.execute()
                #cursor
		self.cur = self.conn.cursor()

        def insert(self, ):
            """ insert row into me db """

        def get(self, ):
            """ retrieve row data associated with key """

        def clear(self, ):
            """ remove a row from db """
