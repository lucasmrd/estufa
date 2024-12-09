import os
from peewee import PostgresqlDatabase
from dotenv import load_dotenv

load_dotenv()

#db = PostgresqlDatabase('estufapy', user='postgres', password='123',
#                        host='localhost', port=5432)

database_uri = os.getenv('DATABASE_URI', '')

db = PostgresqlDatabase(database_uri)