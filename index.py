from memcache_db import MemcacheDB

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

class HTMLCompiler:
    def __init__(self):
        self.msg = message
        self.db = MemcacheDB('database.sqlite')
        self.run()

    def open(self):
        self.page = open('index.html', 'w')

    def close(self):
        self.page.close()

    def build(self):
        dump = ""
        for row in self.db.fetch():
            dump += ("<memcache-row>" +
                "<template slot='key'>" + row[0] + '</template>' +
                "<template slot='value'>" + row[1] + "</template></memcache-row>")
        return dump

    def compile(self):
        self.page.write(self.msg % (self.build(), ))

    def run(self):
        self.open()
        self.compile()
        self.close()


