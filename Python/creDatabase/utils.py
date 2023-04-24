import pandas as pd
import database as db
from sqlalchemy import create_engine


def get_password():
    file_name = r"C:\Users\Trader\Desktop\mysql_password.txt"
    password = open(file_name).read()
    #    print(password)
    return password


db_CONFIG = dict(
    username="root",
    password=get_password(),
    host="localhost",
    # host = "FalconXtreme",
    port=3306,
    database="CRE",
)


def get_engine():
    engine_str = "mysql+pymysql://{username}:{password}@{host}:{port}/{database}?charset=utf8mb4".format(**db_CONFIG)
    engine = create_engine(engine_str)
    return engine


def create_db():
    pw = get_password()
    connection = db.create_server_connection('localhost', 'root', pw)
    create_database_query = "CREATE DATABASE CRE"
    db.create_database(connection, create_database_query)


def insert_into_table(table_name, spreadsheet_name, sheet_name):
    conn = get_engine().connect()
    excel_file = pd.ExcelFile(spreadsheet_name)
    excel_dataframe = excel_file.parse(sheet_name=sheet_name)
    excel_dataframe.to_sql(table_name, conn, if_exists="append")
