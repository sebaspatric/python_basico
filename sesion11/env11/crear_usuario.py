import getpass
import sqlite3

def main():
    id = input('id: ')
    username = input('nombre de usuario: ')
    password = getpass.getpass('contraseña: ')
    
    crear_user(id, username, password)

def crear_user(id, username, password):
    conn = sqlite3.connect('../miaplicacion.db')
    #conn = sqlite3.connect('../miaplicacion.db', isolation_level=None) #solo conectar a la base de datos sin commit
    cursor = conn.cursor()

    #query
    #query = "INSERT INTO users (id, username, password) VALUES ({}, '{}', '{}')".format(id, username, password)
    query = 'INSERT INTO users (id, username, password) VALUES(?,?,?)'

    print("query a ejercutar: ", query)

    rows = cursor.execute(query, (id, username, password))
    print("data es", type(rows))
    conn.commit() #escribo en disco
    cursor.close()
    conn.close()


if __name__ == '__main__':
    main()

