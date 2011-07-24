import base

class TestBasicConnection(base.Base):
    '''Test basic functionality about connection 
    
    In all the tests, *_w refers to sqlite3_wrapper stuff, and *_s refers to
    sqlite3 module stuff'''

    def setUp(self):
        self._sql = '/*mycomment*/select * from recipe order by name'
        super(TestBasicConnection, self).setUp()

    def test_execute(self):
        con_w, con_s = self._get_cons()
        cur_w = con_w.execute(self._sql)
        cur_s = con_s.execute(self._sql)
        data = [row for row in cur_w]
        [self.assertTrue(dict(row) in data) for row in cur_s]
        self._close_cursors(cur_w, cur_s)

    def test_executemany(self):
        con_w, con_s = self._get_cons()
        cur_w = con_w.executemany(self._sql, [])
        cur_s = con_s.executemany(self._sql, [])
        data = [row for row in cur_w]
        [self.assertTrue(dict(row) in data) for row in cur_s]
        self._close_cursors(cur_w, cur_s)
