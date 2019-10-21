from memcache_db import MemcacheDB

db = MemcacheDB('database.sqlite')
index = open('index.html', 'w')

message = """
<html>
	<head>
		<title>Monitor Memcache</title>
                <style> .hidden { visibility: hidden; } </style>
                <style> .key { text-decoration: underline; color: dodgerblue; } </style>

	</head>
	<body>

            <!-- Vue binding element with memcache-row components -->
            <div id="root">
                %s
            </div>

            <script src="https://unpkg.com/vue@2.1.3/dist/vue.js"></script>

            <!-- Vue component for memcache-row -->
            <script src="main.js"></script>

	</body>
</html>
"""

dump = ""

#build the memcache-row vue object with slotted data
for row in db.fetch():
	dump += ("<memcache-row>" +
            "<template slot='key'>" + row[0] + '</template>' +
            "<template slot='value'>" + row[1] + "</template></memcache-row>")

#write index.html
index.write(message % (dump, ))
index.close()

