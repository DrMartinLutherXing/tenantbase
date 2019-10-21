# TenantBase Take Home

## Web Server
use basic example [basic example](https://docs.python.org/2/library/simplehttpserver.html) from python website

update to extend SimpleHTTPRequestHandler do_GET method to recompile the index page with new data on page reload

## sqlite db
create basic object to interface with sqlite3, `MemcacheDB`

## testing
basic python script `sql_test.py` for MemcacheDB

## html
`index.py` writes a `index.html` file

class `HTMLCompiler` opens, write, and closes a file stream to index.html based on the memcache db, database.sqlite

css style for `.hidden` and `.key`

include `main.js` for Vue component `memcache-row`

## javascript
main.js builds a Vue component

setShowing method toggles boolean `showing` value on component which in turn adjusts visibility of associate key

## main
`main.py` simple script to take optional db file name, running web server and socket server
