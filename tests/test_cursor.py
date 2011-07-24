import base

class TestBasicCursors(base.Base):
    '''Test basic functionality about cursors
    
    In all the tests, *_w refers to sqlite3_wrapper stuff, and *_s refers to
    sqlite3 module stuff'''

    def setUp(self):
        self._sql = '/*mycomment*/select * from recipe order by name'
        super(TestBasicCursors, self).setUp()


    def test_query(self):
        cur_w, cur_s = self._get_cursors()
        data = [row for row in cur_w]
        [self.assertTrue(dict(row) in data) for row in cur_s]
        self._close_cursors(cur_w, cur_s)


    def test_fetchone(self):
        cur_w, cur_s = self._get_cursors()
        self.assertEqual(cur_w.fetchone(), dict(cur_s.fetchone()))
        self._close_cursors(cur_w, cur_s)


    def test_fetchall(self):
        cur_w, cur_s = self._get_cursors()
        all_w = cur_w.fetchall()
        all_s = cur_s.fetchall()
        self.assertEqual(len(all_w), len(all_s))
        [self.assertTrue(dict(row) in all_w) for row in all_s]
        self._close_cursors(cur_w, cur_s)


    def test_fetchmany(self):
        cur_w, cur_s = self._get_cursors()
        all_w = cur_w.fetchmany(2)
        all_s = cur_s.fetchmany(2)
        self.assertEqual(len(all_w), len(all_s))
        [self.assertTrue(dict(row) in all_w) for row in all_s]
        self._close_cursors(cur_w, cur_s)


    def test_rowcount(self):
        cur_w, cur_s = self._get_cursors()
        all_s = cur_s.fetchall()
        total_w = cur_w.rowcount
        self.assertEqual(total_w, len(all_s))
        self._close_cursors(cur_w, cur_s)
