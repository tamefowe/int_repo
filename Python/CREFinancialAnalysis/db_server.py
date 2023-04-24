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


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class DBServer():
    """
        Database apis to interact with the mysql installation on this machine
    """
    _instance = None

    def __new__(cls, host: str, username: str, password: str, port: int, database: str,
                 password_file: str = None, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(DBServer, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self, host: str, username: str, password: str, port: int, database: str,
                 password_file: str = None, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._host = host
        self._username = username
        self._password = password
        self._port = port
        self._database = database
        self._conn = None
        self._cursor = None
        self._get_password(password_file)

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
        print(engine_str)
        engine = create_engine(engine_str)
        return engine

    def start(self) -> None:
        try:
            self._conn = mysql.connector.connect(
                host=self._host,
                user=self._username,
                password=self._password,
                database=self._database,
                port=self._port
            )
            if self._conn.is_connected():
                self._cursor = self._conn.cursor()
                print('MySQL Database connection successful')
        except Error as err:
            print("Error while connecting to MySQL ", err)

    def close(self):
        if self._conn.is_connected():
            self._cursor.close()
            self._conn.close()
            print('MySQL connection is closed')

    def create_server_connection(self) -> None:
        try:
            engine = self._get_engine()
            self._conn = engine.raw_connection()
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
        self.execute_query(f"create database {self._database}")

    def get_next_id(self, table_name):
        query = f'''select auto_increment from information_schema.tables
                    where table_schema = "{self._database}" and table_name = "{table_name}"'''
        return self.read_db(query)

    def insert_data_dict_into_table(self, table_name: str, data_dict: dict, delimiter: str = ', ') -> None:
        placeholders = delimiter.join(['%s'] * len(data_dict))
        columns = sorted(data_dict.keys())
        column_str = delimiter.join(columns)
        sql = f"insert into {self._database}.{table_name} ( {column_str} ) values ( {placeholders} )"
        rows = [data_dict[col] for col in columns]
        rows = [None if isinstance(r, float) and math.isnan(r) else r for r in rows]
        try:
            self._cursor.execute(sql, rows)
            self._conn.commit()
            print(f"Successful insertion into `{self._database}`.`{table_name}` ...")
        except Error as err:
            print(f"Error: '{err}'")

    def insert_dataframe_into_table(self, table_name: str, df: pd.DataFrame) -> None:
        self.insert_data_dict_into_table(table_name, data_dict=df.to_dict())

    def insert_spreadsheet_into_table(self, table_name: str, spreadsheet_name: str, sheet_name: str) -> None:
        excel_dict = pd.ExcelFile(spreadsheet_name).parse(sheet_name=sheet_name).to_dict()
        self.insert_data_dict_into_table(table_name, data_dict=excel_dict)

    def read_db(self, query: str):
        try:
            self._cursor.execute(query)
            return self._cursor.fetchall()
        except Error as err:
            print(f"Error: '{err}'")

    def execute_sql_vals(self, sql: str, val: list) -> None:
        try:
            self._cursor.executemany(sql, val)
            self._conn.commit()
            print("Query successful")
        except Error as err:
            print(f"Error: '{err}'")

    def execute_query(self, query: str) -> None:
        try:
            self._cursor.execute(query)
            self._conn.commit()
            print("Query successful")
        except Error as err:
            print(f"Error: '{err}'")
