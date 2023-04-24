import os
from collections import defaultdict

import pandas as pd
from config import FILE_CONFIG, FINANCIAL_POSITION, DEFAULT_CONFIG
from database import DBServer

FINANCIAL_INPUT_OUTPUT = os.path.join(FILE_CONFIG['path'], FILE_CONFIG['file'])


class Reader(object):

    def __init__(self, input=FINANCIAL_INPUT_OUTPUT):
        self._input = input
        self._data = None
        self._read()

    def _read(self): # initially for spreadsheet reading -> DB table reading
        # convert into dataframe
        df = pd.read_excel(self._input, sheet_name=FILE_CONFIG['sheet'])

        # convert into dictionary
        data_dict = df.to_dict()

        self._data = dict(
            [
                (k, data_dict['Value'][i])
                for i, k in data_dict['Type'].items()
                if not pd.isnull(k)
            ]
        )

    def get_property_info(self):
        return self._data


class InputReader(Reader):

    def _read(self):
        self._data = defaultdict(dict)

        # convert into dataframe
        df = pd.read_excel(self._input, sheet_name=FILE_CONFIG['input sheet'])

        # convert into dictionary
        financial_data_dict = df.to_dict()

        for data_type, positions in FINANCIAL_POSITION.items():
            self._data['current'][data_type] = dict(
                zip(
                    [financial_data_dict['info (current)'][position] for position in positions],
                    [financial_data_dict['value (current)'][position] for position in positions]
                )
            )

            self._data['projected'][data_type] = dict(
                zip(
                    [financial_data_dict['info (current)'][position] for position in positions],
                    [financial_data_dict['value (projected)'][position] for position in positions]
                )
            )



class BaseDB(object):
    def __init__(self,
                 host: str = 'localhost',
                 username: str = 'root',
                 password: str = 'Otetie@79',
                 port: int = 3306,
                 database: str = 'cre_db',
                 password_file=None):
        self._server = DBServer(host, username, password, port, database, password_file)
        self._conn = self._server.conn
        self._cursor = self._server.cursor


class DBReader(BaseDB, Reader):
    def __init__(self, db_name, table_name, col_names=None):
        super().__init__()
        if col_names is None:
            col_names = []
        self._db = db_name
        self._table = table_name
        self._cols = col_names
        self._query = ''

    def _make_query(self):
        self._cols = ', '.join(self._cols) if self._cols else '*'
        self._query = f"select {self._cols} from {self._db}.{self._table}"

    def _read(self):
        self._make_query()
        self._data = self._server.read_db(self._query)

    def get_property_info(self):
        self._db, self._table, self._cols = 'cre_db', 'property_lead', None
        self._read()
        return self._data


class DBWriter(BaseDB):

    def __init__(self, table_name, data, **kwargs):
        super().__init__()
        self._table = table_name
        self._data = data
        self._file_name = kwargs.get('file')
        self._sheet_name = kwargs.get('sheet')

    def write(self):
        if isinstance(self._data, dict):
            self._server.insert_data_dict_into_table(self._table, self._data)
        if isinstance(self._data, pd.DataFrame):
            self._server.insert_spreadsheet_into_table(self._table, self._file_name, self._sheet_name)
