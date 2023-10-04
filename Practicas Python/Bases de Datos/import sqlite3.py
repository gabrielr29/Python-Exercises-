import sqlite3

conexion = sqlite3.connect('pacientes.sqlite3')

valores = (8, "Carlos", "Ferreyra", 28, "No")

cursor = conexion.cursor()

cursor.execute('INSERT INTO pacientes(id, nombre, apellido, edad, diabetico) VALUES(?,?,?,?,?)', valores)

conexion.commit()

cursor.close()
conexion.close()