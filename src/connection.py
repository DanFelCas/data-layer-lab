import sys
from psycopg2 import pool


class AccessCredentials:
    def __init__(self, user='postgres', password='123456789', host='localhost', port=5432, database='test_db'):
        self._user = user
        self._password = password
        self._host = host
        self._port = port
        self._database = database

    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, user):
        self._user = user

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password

    @property
    def host(self):
        return self._host

    @host.setter
    def host(self, host):
        self._host = host

    @property
    def port(self):
        return self._port

    @port.setter
    def port(self, port):
        self._port = port

    @property
    def database(self):
        return self._database

    @database.setter
    def database(self, database):
        self._database = database

    def get_credentials(self):
        return {
            'user': self._user,
            'password':  self.password,
            'host': self._host,
            'port': self._port,
            'database': self._database
        }


class Connection:
    _access_credentials = AccessCredentials()
    _min_con = 1
    _max_con = 5
    _pool = None

    @classmethod
    def set_min_con(cls, min_con):
        cls._min_con = min_con

    @classmethod
    def set_max_con(cls, max_con):
        cls._max_con = max_con

    @classmethod
    def get_pool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(
                    cls._min_con, cls._max_con,
                    cls._access_credentials.get_credentials()
                )
                print(f'Pool generation successful: {cls._pool}')
                return cls._pool
            except Exception as e:
                print('Something went wrong while getting the pool.'
                      f'\nWith error: {e.__class__.__name__}, {e}')
                sys.exit()
        else:
            return cls._pool

    @classmethod
    def get_connection(cls):
        conn = cls.get_pool().getconn()
        print(f'Connection established: {conn}')
        return conn

    @classmethod
    def free_conn(cls, conn):
        cls.get_pool().putconn(conn)
        print(f'Connection back to the pool.')

    @classmethod
    def close_connections(cls):
        cls.get_pool().closeall()
        print('All connections where closed.')
