import getpass
import sqlite3

def main():
    username = input('nombre de usuario: ')
    password = getpass.getpass('contraseña: ')

    if verifica_credenciales(username, password):
        print('Bienvenido')
    else:
        print('Credenciales incorrectas')

def verifica_credenciales(username, password):
    conn = sqlite3.connect('../miaplicacion.db')
    cursor = conn.cursor()

    #query
    #query = ("SELECT id FROM users WHERE username ='?'AND password ='?'", (username, password))
    query = "SELECT id FROM users WHERE username ='{}' AND password ='{}'".format(username, password)
    #mostrar query
    #query = f'SELECT id FROM users WHERE username ="{username}" AND password ="{password}"'
    
    print("query a ejercutar: ", query)

    rows = cursor.execute(query)
    data = rows.fetchone() #devuelve 1 elemento
    print("data es", type(data))

    cursor.close()
    conn.close()

    if data == None:
        return False
    return True



if __name__ == '__main__':
    main()

