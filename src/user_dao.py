from logger_base import log
from user_class import User
from pool_cursor import PoolCursor

class UserDao:
    @staticmethod
    def select_query(query: str) -> list[User]:
        with PoolCursor() as cursor:
            cursor.execute(query)
            reg = cursor.fetchall()
            reg = [User(*r) for r in reg]
            return reg

    @staticmethod
    def regular_query(query: str):
        with PoolCursor() as cursor:
            cursor.execute(query)

    @staticmethod
    def insert_user(*args: User):
        query = 'INSERT INTO usuario (username, password) VALUES (%s, %s)'
        with PoolCursor() as cursor:
            for user in args:
                cursor.execute(query, user.get_tuple())

    @staticmethod
    def update_user(*args: User):
        query = 'UPDATE usuario SET username=%s, password=%s WHERE user_id = %s'
        with PoolCursor() as cursor:
            for user in args:
                cursor.execute(query, (user.username, user.password, user.user_id))

    @staticmethod
    def delete_user(*args: User):
        query = 'DELETE FROM usuario WHERE user_id=%s'
        with PoolCursor() as cursor:
            values = tuple((user.user_id,) for user in args)
            cursor.executemany(query, values)


if __name__ == "__main__":
    # Insert v1
    q = "INSERT INTO usuario (username, password) VALUES ('daniela', '2345')"
    # UserDao.regular_query(q)
    # Insert v2
    user1 = User(7, "paula", "4567")
    user2 = User(2, "valentina", "5678")
    # UserDao.insert_user(user1, user2)
    # Update
    # UserDao.update_user(user1)
    # Delete
    # UserDao.delete_user(user2, user1)
    # Select
    register = UserDao.select_query("SELECT * FROM usuario;")
    for value in register:
        print(value)
