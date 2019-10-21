from memcache_db import MemcacheDB

print "connecting to db.sqlite"
db = MemcacheDB('db.sqlite')

print "testing: insert('test', 'lorem ipsum', 123)"
#db.insert('test', 'lorem ipsum', 123)

print "testing: get key"
print db.get('test')

print "testing: select *"
db.insert('test2', 'lorem ipsum asdkfkjh', 0)
db.insert('test3', 'lorem ipsumu asjkdhf', 1123)
for row in db.fetch():
	print row

print "testing: delete from"
db.clear('test')

print "closing connection"
db.end()
