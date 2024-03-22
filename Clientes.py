from Conexion import *

class CClientes:

    def mostrarClientes():
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            cursor.execute("select * from usuarios;")
            miResultado = cursor.fetchall()
            cone.commit()
            cone.close()
            return miResultado
        except mysql.connector.Error as error:
            print("Error de mostrar datos {}".format(error))

    def ingresarClientes(nombres, apellidos, sexo):
        
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            sql = "insert into usuarios values(null, %s, %s, %s);"
            valores = (nombres, apellidos, sexo)
            cursor.execute(sql, valores)
            cone.commit()
            print(cursor.rowcount, "Registro ingresado")
            cone.close()

        except mysql.connector.Error as error:
            print("Error de ingreso de datos {}".format(error))

    def modificarClientes(idUsuario, nombres, apellidos, sexo):
        
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            sql = "UPDATE usuarios SET usuarios.nombres = %s, usuarios.apellidos = %s, usuarios.sexo = %s where usuarios.id = %s;"
            valores = (nombres, apellidos, sexo, idUsuario)
            cursor.execute(sql, valores)
            cone.commit()
            print(cursor.rowcount, "Registro Actualizado")
            cone.close()

        except mysql.connector.Error as error:
            print("Error de actualización de datos {}".format(error))

    def eliminarClientes(idUsuario):
        
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            sql = "DELETE from usuarios where usuarios.id = %s;"
            valores = (idUsuario,)
            cursor.execute(sql, valores)
            cone.commit()
            print(cursor.rowcount, "Registro Eliminado")
            cone.close()

        except mysql.connector.Error as error:
            print("Error de eliminación {}".format(error))