from logger_base import log
from user_class import User
from pool_cursor import PoolCursor

class UserDao:
    @staticmethod
    def query_execute(query: str):
        if 'SELECT' in query.upper():
            return UserDao.select_query(query)

    @staticmethod
    def select_query(query: str) -> list[User]:
        with PoolCursor as cursor:
            cursor.execute(query)
            reg = cursor.fetchall()
            reg = [User(*r) for r in reg]
            return reg

    @staticmethod
    def insert_query(query: str):
        with PoolCursor as cursor:
            cursor.execute(query)

    @staticmethod
    def insert_user(*args: User):
        query = 'INSERT INTO usuario (user_id, username, password) VALUES (%s %s %s)'
        with PoolCursor as cursor:
            for user in args:
                cursor.execute(query, user.get_tuple())
            return cursor.rowcount


