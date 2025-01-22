FROM python:3.12.8

RUN pip install sqlalchemy psycopg2

WORKDIR /app
COPY ./create_table.sql create_table.sql
COPY ./load_db.py load_db.py

ENTRYPOINT ["python","load_db.py"]


