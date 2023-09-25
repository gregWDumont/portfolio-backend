import os
from psycopg2 import pool

DATABASE_POOL_SIZE = 5
database_pool = None

def init_db():
		global database_pool
		database_pool = pool.SimpleConnectionPool(1, DATABASE_POOL_SIZE, os.environ.get("DATABASE_URL"))

def get_conn():
		return database_pool.getconn()

def release_conn(conn):
		database_pool.putconn(conn)
