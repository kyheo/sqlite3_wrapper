import unittest

import sqlite3
from lib.sqlite3_wrapper import *

class Base(unittest.TestCase):

    def setUp(self):
        self.con = {'sqw': SQL3_Connection(":memory:"),
                    'sql': sqlite3.connect(':memory:')}
        self.con['sql'].row_factory = sqlite3.Row
        self._create_tables()


    def tearDown(self):
        for name, con in self.con.iteritems():
            del(con)

    def _get_cons(self):
        return self.con['sqw'], self.con['sql']

    def _get_cursors(self):
        con_w, con_s = self._get_cons()
        cur_w = con_w.cursor()
        cur_s = con_s.cursor()
        cur_w.execute(self._sql)
        cur_s.execute(self._sql)
        return cur_w, cur_s
   
    
    def _close_cursors(self, cur_w, cur_s):
        cur_w.close()
        cur_s.close()


    def _create_tables(self):
        for name, con in self.con.iteritems():
            cur = con.cursor()
            cur.execute("create table recipe (name, ingredients)")
            cur.executescript("""
                insert into recipe (name, ingredients) values ('broccoli stew', 'broccoli peppers cheese tomatoes');
                insert into recipe (name, ingredients) values ('pumpkin stew', 'pumpkin onions garlic celery');
                insert into recipe (name, ingredients) values ('broccoli pie', 'broccoli cheese onions flour');
                insert into recipe (name, ingredients) values ('pumpkin pie', 'pumpkin sugar flour butter');
                """)
            cur.close()
