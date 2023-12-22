import os
from psycopg2 import pool

# Define the maximum number of connections in the database pool
DATABASE_POOL_SIZE = 5
# Initialize the database pool variable
database_pool = None

def init_db():
    """
    Initializes the database connection pool.

    This function creates a connection pool for the PostgreSQL database using the environment variable 'DATABASE_URL'.
    The pool size is set to a minimum of 1 and a maximum defined by DATABASE_POOL_SIZE.

    The connection pool allows efficient management of database connections, reusing them across different parts of the application.
    """
    global database_pool
    database_pool = pool.SimpleConnectionPool(1, DATABASE_POOL_SIZE, os.environ.get("DATABASE_URL"))

def get_conn():
    """
    Retrieves a database connection from the pool.

    This function gets a connection from the initialized database pool. 
    If all connections are in use, it will wait until one is released.

    Returns:
        A database connection object from the pool.
    """
    return database_pool.getconn()

def release_conn(conn):
    """
    Releases a database connection back to the pool.

    Args:
        conn: The database connection object to be released.

    This function puts the used database connection back into the pool so it can be reused.
    This is important for maintaining efficient use of database resources.
    """
    database_pool.putconn(conn)
