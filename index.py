from memcache_db import MemcacheDB

db = MemcacheDB('database.sqlite')
index = open('index.html', 'w')

message = """
<html>
	<head>
		<title>Monitor Memcache</title>
	</head>
	<body>

            <table>

                <tr>
                    <th>KEY</th>
                    <th>VALUE</th>
                </tr>

                %s

            </table>

	</body>
</html>
"""

dump = ""

for row in db.fetch():
    dump += ("<tr><td>" + row[0] + "</td><td>" + row[1] + "</td></tr>")

index.write(message % (dump, ))
index.close()

