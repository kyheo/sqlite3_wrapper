import sqlite3

class SQL3_Row(sqlite3.Row):
    pass


class SQL3_Cursor(sqlite3.Cursor):

    def __init__(self, *args, **kwargs):
        super(SQL3_Cursor, self).__init__(*args, **kwargs)
        self._sql = None

    def execute(self, sql, *args, **kwargs):
        self._sql = sql.replace('%s', '?')
        return super(SQL3_Cursor, self).execute(self._sql, *args, **kwargs)

    def executemany(self, sql, *args, **kwargs):
        self._sql = sql.replace('%s', '?')
        return super(SQL3_Cursor, self).executemany(self._sql, *args, **kwargs)

    def next(self, *args, **kwargs):
        return dict(super(SQL3_Cursor, self).next(*args, **kwargs))

    def fetchone(self, *args, **kwargs):
        return dict(super(SQL3_Cursor, self).fetchone(*args, **kwargs))

    def fetchall(self, *args, **kwargs):
        rows = super(SQL3_Cursor, self).fetchall(*args, **kwargs)
        return [dict(row) for row in rows]

    def fetchmany(self, *args, **kwargs):
        rows = super(SQL3_Cursor, self).fetchmany(*args, **kwargs)
        return [dict(row) for row in rows]

    @property
    def rowcount(self):
        sql = self._sql.strip()
        # Remove comments from begining of the query
        if sql.startswith('/*'):
            index = sql.find('*/') + 2
            sql = sql[index:]
        # Only when working with selects
        if sql.lower().startswith('select'):
            cur = self.connection.cursor()
            cur.execute(self._sql)
            # This is really low performance. If working with big data sets this
            # could take really long. I'm using it only on testing purposes.
            rows = cur.fetchall()
            cur.close()
            return len(rows)
        return super(SQL3_Cursor, self).rowcount


class SQL3_Connection(object):

    def __init__(self, database, *args, **kwargs):
        self.con = sqlite3.connect(database, *args, **kwargs)
        self.con.row_factory = SQL3_Row

    def cursor(self):
        return self.con.cursor(SQL3_Cursor)

    def execute(self, *args, **kwargs):
        return self.cursor().execute(*args, **kwargs)

    def executemany(self, *args, **kwargs):
        return self.cursor().executemany(*args, **kwargs)
