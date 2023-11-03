from src.user_class import User
from src.user_dao import UserDao
from src.logger_base import log

option = None
while option != 5:
    print('Options:')
    print('1. List users')
    print('2. Add user')
    print('3. Modify user')
    print('4. Delete user')
    print('5. Quit')
    option = int(input('Write your option (1-5): '))
    print("\n")
    if option == 1:
        users = UserDao.select_query()
        for user in users:
            log.info(user.__str__().replace("\n", " "))
    elif option == 2:
        username_var = input('Write the username: ')
        password_var = input('Write the password: ')
        user = User(username=username_var, password=password_var)
        UserDao.insert_user(user)
    elif option == 3:
        user_id_var = int(input('Write the user_id to be modified: '))
        username_var = input('Write the new username: ')
        password_var = input('Write the new password: ')
        user = User(user_id_var, username_var, password_var)
        UserDao.update_user(user)
    elif option == 4:
        user_id_var = int(input('Write the user_id to delete: '))
        user = User(user_id=user_id_var)
        UserDao.delete_user(user)
else:
    log.info('Quiting from app...')