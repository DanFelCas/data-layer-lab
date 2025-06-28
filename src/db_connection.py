import psycopg2
import threading

from psycopg2 import pool
from src.logger_base import log
from src.db_credentials import DatabaseCredentials


class PasswordError(Exception):
    pass


class DatabaseConnection:
    _pool = None
    _max_con = 5
    _lock = threading.lock()

    @classmethod
    def set_max_con(cls, max_con):
        with cls._lock:
            cls._max_con = max_con

    @classmethod
    def get_pool(cls):
        with cls._lock:
            if cls._pool is None:
                credentials = DatabaseCredentials.get_credentials()

                if credentials['password'] is None:
                    raise PasswordError("Database password is not set.")
                
                try:
                    cls._pool = pool.ThreadedConnectionPool(minconn=1, maxconn=cls._max_con, **credentials)
                    log.debug("PostgreSQL connection pool initializad.")
                except psycopg2.Error as err:
                    raise ConnectionError(f"Error initializing connection pool: {err}")
            
            return cls._pool

    @classmethod
    def get_connection(cls):
        try: 
            conn = cls.get_pool().getconn()
            if conn is None:
                raise ConnectionError("Failed to obtain a database connection.")
            return conn
        except psycopg2.Error as err:
            raise ConnectionError(f"Error obtaining database connection: {err}")

    @classmethod
    def free_conn(cls, conn):
        if conn:
            try:
                cls.get_pool().putconn(conn)
            except psycopg2.Error as err:
                raise ConnectionError(f"Error releasing connection: {err}")

    @classmethod
    def close_connections(cls):
        with cls._lock:
            if cls._pool is not None:
                try:
                    cls._pool.closeall()
                    cls._pool = None
                except psycopg2.Error as err:
                    raise ConnectionError(f"Error closing connection pool: {err}")
