from types import SimpleNamespace
import location
import sqlite3
import json

class db:
    def __init__(self, db_name, *, sql_query=None):
        self.__conn = sqlite3.connect(f'{location.data} / quote.db')
        self.curs = self.__conn.cursor()
        if not sql_query:
            self.curs.executescript(f'{location.data} / {sql_query}')

    def close_connection(self):
        self.curs.close()
        self.__conn.close()


with open('config.json', mode='r', encoding='utf-8') as fp:
    config = json.load(fp, object_hook=lambda d: SimpleNamespace(**d))
with open('token.json', mode='r', encoding='utf-8') as fp:
    token = json.load(fp, object_hook=lambda d: SimpleNamespace(**d))
