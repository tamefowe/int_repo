import os
import pandas as pd
from config import FILE_CONFIG, FINANCIAL_POSITION
from collections import defaultdict
from openpyxl import load_workbook

FIN_FILE = os.path.join(FILE_CONFIG['path'], FILE_CONFIG['file'])


class InfoReader:

    def __init__(self, _input=FIN_FILE):
        self._data = None
        self._input = _input
        self._read()

    def _read(self):  # initially for spreadsheet reading -> DB table reading
        # convert into dataframe
        df = pd.read_excel(self._input, sheet_name=FILE_CONFIG['sheet3'])

        # convert into dictionary
        data_dict = df.to_dict()

        self._data = dict(
            [
                (k, data_dict['Value'][i])
                for i, k in data_dict['Type'].items()
                if not pd.isnull(k)
            ]
        )

    def get_data(self):
        return self._data


class InputReader:

    def __init__(self, _input=FIN_FILE):
        self._data = None
        self._input = _input
        self._read()

    def _read(self):
        self._data = defaultdict(dict)

        # convert into dataframe
        df = pd.read_excel(self._input, sheet_name=FILE_CONFIG['sheet1'])

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

    def get_data(self):
        return self._data


class DBReader:
    def __init__(self, server):
        self._server = server

    def _read(self, db_name=None, tab=None, cols=None):
        cols = ', '.join(cols) if cols else '*'
        query = f"select {cols} from {db_name}.{tab}"
        return self._server.read_db(query)

    def get_next_id(self, table_name):
        return self._server.get_next_id(table_name)

    def get_data(self, db_name=None, tab=None, cols=None):
        data = self._read(db_name, tab, cols)
        return data


class DBWriter:

    def __init__(self, server):
        self._server = server

    def write(self, data_to_tab: dict) -> None:
        for tab, data in data_to_tab.items():
            if isinstance(data, dict):
                self._server.insert_data_dict_into_table(tab, data)
            elif isinstance(data, pd.DataFrame):
                self._server.insert_dataframe_into_table(tab, data)


class ExcelWriter:

    def __init__(self, fin_output: str = FIN_FILE) -> None:
        self._path = fin_output

    def write(self, data: pd.DataFrame) -> None:
        book = load_workbook(self._path)
        writer = pd.ExcelWriter(self._path, engine='openpyxl')
        writer.book = book
        data.to_excel(writer, sheet_name=FILE_CONFIG['sheet2'], index=False)
        writer.close()
