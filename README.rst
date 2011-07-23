SQLite Wrapper
==============
Lib that stays in the middle between the code and sqlite3 module and tries to
simplify the api making it mor similar to the way I use MySQLdb.

Right now it just replaces '%s' with '?' in queries, and the cursor works
returning standard dict and it provides a working rowcount property, but because
it just redo the query is not recommended its usage, I will use it only for
testing purposes.

Contact
-------
Martin Marrese - marrese@gmail.com
