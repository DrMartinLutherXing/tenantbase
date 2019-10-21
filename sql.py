#SQL queries 
CREATE_TABLE = "CREATE TABLE IF NOT EXISTS memcache (key text unique, value text, flags integer)"

INSERT_TABLE = "INSERT INTO memcache (key, value, flags) VALUES (?,?,?)"
UPDATE_TABLE = "UPDATE memcache SET value=?, flags=? WHERE key=?";

FETCH_TABLE  = "SELECT * FROM memcache"
GET_TABLE    = "SELECT * FROM memcache where key = ?"

DELETE_TABLE = "DELETE FROM memcache WHERE key = ?"

