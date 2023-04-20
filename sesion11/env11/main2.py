import sqlite3

conn = sqlite3.connect('../miaplicacion.db') 
#conexion accede a un fichero

#cursor variable que va almacenar los resultados de la consulta
# si hay muchos va a ir iterando

cursor = conn.cursor()

#ejecutar consulta
rows = cursor.execute("SELECT * FROM users WHERE username = 'vroman'")

for row in rows:
    print(row)


cursor.close()

conn.close()
