from src.logger_base import log
from src.db_connection import DatabaseConnection


class PoolCursor:
    def __init__(self):
        self._conn = None
        self._cursor = None

    def __enter__(self):
        self._conn = DatabaseConnection.get_connection()
        self._cursor = self._conn.cursor()
        log.debug(f"Cursor created: {self._cursor}")
        return self._cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self._conn.rollback()
            log.error(f"Something went wrong. {exc_type}, {exc_val}")
        else:
            self._conn.commit()
            log.debug("Saved changes.")

        self._cursor.close()
        DatabaseConnection.free_conn(self._conn)


class PoolConnection:
    def __init__(self):
        self.__conn = None

    def __enter__(self):
        self._conn = DatabaseConnection.get_connection()
        log.debug(f"Connection stablished: {self._cursor}")
        return self._conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self._conn.rollback()
            log.error(f"Something went wrong. {exc_type}, {exc_val}")
        else:
            self._conn.commit()
            log.debug("Saved changes.")

        DatabaseConnection.free_conn(self._conn)


if __name__ == "__main__":
    with PoolCursor() as cursor:
        cursor.execute("SELECT * FROM usuario;")
        values = cursor.fetchall()
        print(values)
