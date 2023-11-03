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
            log.info(user)
    # elif option == 2:
    #     username_var = input('Escribe el username: ')
    #     password_var = input('Escribe el password: ')
    #     usuario = Usuario(username=username_var, password=password_var)
    #     usuarios_insertados = UsuarioDAO.insertar(usuario)
    #     log.info(f'Usuarios insertados: {usuarios_insertados}')
    # elif option == 3:
    #     id_usuario_var = int(input('Escribe el id_usuario a modificar: '))
    #     username_var = input('Escribe el nuevo username: ')
    #     password_var = input('Escribe el nuevo password: ')
    #     usuario = Usuario(id_usuario_var, username_var, password_var)
    #     usuarios_actualizados = UsuarioDAO.actualizar(usuario)
    #     log.info(f'usuarios actualizados: {usuarios_actualizados}')
    # elif option == 4:
    #     id_usuario_var = int(input('Escribe el id_usuario a eliminar: '))
    #     usuario = Usuario(id_usuario=id_usuario_var)
    #     usuarios_eliminados = UsuarioDAO.eliminar(usuario)
    #     log.info(f'usuarios eliminados: {usuarios_eliminados}')
else:
    log.info('Quiting from app...')