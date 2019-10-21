import sys, subprocess
from memcache_socket import MemcacheSocket

p = subprocess.Popen([sys.executable, './web_server.py'],
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.STDOUT)

db_file = sys.argv[2] if len(sys.argv) == 3 else "database.sqlite"
MemcacheSocket(db_file)

