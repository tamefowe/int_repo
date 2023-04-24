import math

import mysql.connector
from mysql.connector import Error
import pandas as pd
from sqlalchemy import create_engine, Engine


#    ########################################################
#    # Install Mysql Community Server on Windows            #
#    # https://www.youtube.com/watch?v=2HQC94la6go          #
#    # on \windows 10, on Start type 'Services'              #
#    # right click on 'MySQL80' to start (Automatic status) #
#    ########################################################


class DBServer(object):

    def __init__(
            self,
            host: str = 'localhost',
            username: str = 'root',
            password: str = 'Otetie@79',
            port: int = 3306,
            database: str = 'cre_db',
            password_file: str = None
    ) -> None:
        self._host = host
        self._username = username
        self._password = password
        self._port = port
        self._database = database
        self._conn = None
        self._cursor = None
        self._get_password(password_file)
        self._create_server_connection()

    def _get_password(self, filename: str = None) -> None:
        if not self._password and filename:
            self._password = open(filename).read()

    def _get_engine(self) -> Engine:
        engine_str = "mysql+pymysql://{username}:{password}@{host}:{port}/{database}?charset=utf8mb4" \
            .format(
                username=self._username,
                password=self._password,
                host=self._host,
                port=self._port,
                database=self._database
            )
        engine = create_engine(engine_str)
        return engine

    def _create_server_connection(self) -> None:
        try:
            args = dict(
                host=self._host,
                user=self._username,
                passwd=self._password,
                database=self._database,
                port=self._port
            )
            self._conn = mysql.connector.connect(**args)
            self._cursor = self._conn.cursor()
            print('MySQL Database connection successful')
        except Error as err:
            print(f"Error: '{err}'")

    @property
    def conn(self):
        return self._conn

    @property
    def cursor(self):
        return self._cursor

    def create_db(self):
        self.execute_query("CREATE DATABASE CRE")

    def insert_data_dict_into_table(self, table_name, data_dict, delimiter=', '):
        placeholders = delimiter.join(['%s'] * len(data_dict))
        columns = sorted(data_dict.keys())
        column_str = delimiter.join(columns)
        sql = f"insert into {self._database}.{table_name} ( {column_str} ) VALUES ( {placeholders} )"
        rows = [data_dict[col] for col in columns]
        rows = [None if isinstance(r, float) and math.isnan(r) else r for r in rows ]
        try:
            self._cursor.execute(sql, rows)
            self._conn.commit()
            print(f"Successful insertion into `{self._database}`.`{table_name}` ...")
        except Error as err:
            print(f"Error: '{err}'")

    def insert_spreadsheet_into_table(self, table_name, spreadsheet_name, sheet_name):
        excel_df = pd.ExcelFile(spreadsheet_name).parse(sheet_name=sheet_name)
        excel_df.to_sql(table_name, self._conn, if_exists="append")

    def read_db(self, query):
        try:
            self._cursor.execute(query)
            result = self._cursor.fetchall()
            return result
        except Error as err:
            print(f"Error: '{err}'")

    def execute_sql_vals(self, sql, val):
        try:
            self._cursor.executemany(sql, val)
            self._conn.commit()
            print("Query successful")
        except Error as err:
            print(f"Error: '{err}'")

    def execute_query(self, query):
        try:
            self._cursor.execute(query)
            self._conn.commit()
            print("Query successful")
        except Error as err:
            print(f"Error: '{err}'")
