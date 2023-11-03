from logger_base import log
from connection import Connection

class PoolCursor:
    def __init__(self):
        self._conn = None
        self._cursor = None

    def __enter__(self):
        self._conn = Connection.get_connection()
        self._cursor = self._conn.cursor()
        log.debug(f'Cursor created: {self._cursor}')
        return self._cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self._conn.rollback()
            log.error(f'Something went wrong. {exc_type}, {exc_val}')
        else:
            self._conn.commit()
            log.debug(f'Saved changes.')

        self._cursor.close()
        Connection.free_conn(self._conn)


if __name__ == "__main__":
    with PoolCursor() as cursor:
        cursor.execute('SELECT * FROM usuario;')
        values = cursor.fetchall()
        print(values)
