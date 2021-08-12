from types import SimpleNamespace
from . import location
import sqlite3
import json


class db:
    def __init__(self, db_name: str, *, sql_query=None):
        self.__conn = sqlite3.connect(str(location.data / db_name))
        self.curs = self.__conn.cursor()
        if sql_query is not None:
            with open(location.data / sql_query, mode='r') as db_fp:
                self.curs.executescript(db_fp.read())

    def commit(self):
        self.__conn.commit()

    def close_connection(self):
        self.curs.close()
        self.__conn.close()

    def get_all(self, tb_name):
        self.curs.execute(f'SELECT * FROM {tb_name}')
        return self.curs.fetchall()


with open('config.json', mode='r', encoding='utf-8') as fp:
    config = json.load(fp, object_hook=lambda d: SimpleNamespace(**d))
with open('token.json', mode='r', encoding='utf-8') as fp:
    token = json.load(fp, object_hook=lambda d: SimpleNamespace(**d))
