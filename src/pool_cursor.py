from logger_base import log
from connection import Connection

class PoolCursor:
    def __init__(self):
        self._conn = None
        self._cursor = None

    def __enter__(self):
        self._conn = Connection.get_connection()
        self._cursor = self._conn.cursor()
        return self._cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self._conn.rollback()
        else:
            self._conn.commit()

        self._cursor.close()
        Connection.free_conn(self._conn)


if __name__ == "__main__":
    with PoolCursor() as cursor:
        values = cursor.fetchall()
        print(values)