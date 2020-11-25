# Direct copy of 
# https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.iterdump
# Convert file existing_db.db to SQL dump file dump.sql
import sqlite3

con = sqlite3.connect('db.sqlite3')
with open('db_backup.sql', 'w') as f:
    for line in con.iterdump():
        f.write('%s\n' % line)
con.close()