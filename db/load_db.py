import random
import os
from sqlalchemy import create_engine, text, insert


USER = 'ushakov'
PASSWORD = 'ushakov'
HOST = 'localhost'
PORT = '5436'
DB = 'nums_db'
FILE_PATH = './create_table.sql'
TABLE_NAME = 'nums'

def creater(engine, file_path):
    try:
        with open(file_path, 'r') as f:
            sql_script = f.read()
        with engine.begin() as con:
            con.execute(text(sql_script))
    except Exception as e:
        print(f'Ошибка при выполнении SQL файла: {e}')

def loader(engine, table_name):
    data = [random.randint(-100, 100) for i in range(100)]
    try:
        with engine.connect() as con:
            result = con.execute(
                insert(table_name),
                [
                    {'num': i} for i in data
                ]
            )
            con.commit()
    except Exception as e:
        print(f'Ошибка при загрузке данных в таблицу {table_name}: {e}')

if __name__ == '__main__':
    try:
        engine = create_engine(f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}')
    except Exception as e:
        print(f'Ошибка подключения: {e}')
    creater(engine, FILE_PATH)
    loader(engine, TABLE_NAME)

