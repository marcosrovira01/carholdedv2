'''
Esta clase nos servirá para gestionar nuestras conexiones a la base de datos durante el registro del usuario

@author: marcthegamer
'''
import tkinter.messagebox
import mysql.connector

class BaseDatosRegistro:
    
    #constructor
    def __init__(self, nombre, primerApellido, segundoApellido, correo, contraseña):
        
        """
        cuando recibamos los atributos, los parseamos a string para que no
        haya ningún problema, por si el usuario introduce enteros u otro tipo de dato en el formulario.
        Como atributos, tendremos:
        
        -nombre: almacenará el nombre del usuario en formato string
        -primerApellido: almacenará el primer apellido del usuario en formato string
        -segundoApellido: almacenará el segundo apellido del usuario en formato string
        -correo: almacenará el correo electrónico del usuario en formato string
        -contraseña: almacenará la contraseña del usuario en formato string
        """
        self.__nombre=str(nombre)
        self.__primerApellido=str(primerApellido)
        self.__segundoApellido=str(segundoApellido)
        self.__correo=str(correo)
        self.__contraseña=str(contraseña)
        
        """
        conexionBaseDatosRegistro(): método que se encargará de conectarse a nuestra base de datos y realizar el registro:
        
        @return: booleano: True si el registro fué exitoso o False si no lo fué.
        """
    def conexionBaseDatosRegistro(self):
        """
        Bloque try para controlar excepciones, por ejemplo, si no se puede conectar a la base de datos:
        """
        try:
            """
            Creamos un nuevo socket, que se conectará a la base de datos "carholded", con usuario root, contraseña 2585 
            y dirección del servidor localhost:
            """
            miConexion=mysql.connector.connect(
                host="localhost", 
                user="root",
                password="2585",
                database="carholded"
                )
            
            """
            Creamos un objeto cursor, que será el que contendrá la consulta a la base de datos. Como parámetro, entra buffered, con valor True,
            debido a que al realizar un select y contar el número de columnas con la función count() de mysql, si no está este parámetro en true
            nos devolverá 0:
            """
            cursor=miConexion.cursor(buffered=True)
            
            """
            Debemos de comprobar que el usuario no está repetido en el sistema. Para ello consultamos a la base de datos si hay varios usuarios
            con el mismo correo con la siguiente consulta. El resultado de la misma se almacenará en una variable llamada numeroRegistros.
            Nota: La variable que se introduce a la consulta, se coloca entre signos "+" y entre comillas.
            """
            cursor.execute("SELECT COUNT(CorreoElectronico) FROM Usuarios WHERE CorreoElectronico='"+self.__correo+"'")
  
            """
            Hacemos un commit() para refrescar los datos de la base de datos:
            """
            miConexion.commit()
            
            """
            Almacenamos la lista resultante de la consulta con el método fetch(), concretamente, su variante fetchone, que nos retornará una lista de
            1 solo valor:
            """
            listaNumeroRegistros=cursor.fetchone()
            
            """
            Asignamos ese único valor de la lista a la variable numeroRegistros:
            """
            numeroRegistros=listaNumeroRegistros[0]
            
            if numeroRegistros>=1:
                """
                Si hay un usuario registrado con ese mismo correo, retornamos false y un mensaje de error.
                """
                tkinter.messagebox.showinfo(title="Ha ocurrido un error", message="El correo que estás intentando utilizar, ya está registrado.")
                return False
            else:
                """
                Si no hay ningún registro repetido, realizamos una nueva consulta, en este caso, un insert a la base de datos con los parámetros dados por el usuario. 
                Como los campos CantidadGastada y CantidadVendida son obligatorios, tambien los introducimos, pero con un valor igual a 0. Estos campos no han sido dados por 
                el usuario, por lo que se quedarán en 0 por defecto cuando un nuevo usuario se registre en el sistema. En este caso, para la consulta, usaremos el modificador %s:
                """
                sql="INSERT INTO Usuarios (CorreoElectronico, Nombre, PrimerApellido, SegundoApellido, CantidadGastada, CantidadVendida, Contraseña) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                val=(self.__correo, self.__nombre, self.__primerApellido, self.__segundoApellido, 0, 0, self.__contraseña)
                
                """
                Ejecutamos la consulta con el método execute(), pasándole como parámetros la consulta en sí y las variables a introducir en 
                la misma:
                """
                cursor.execute(sql, val)
                
                """
                Hacemos un commit() para refrescar los datos de la base de datos:
                """
                miConexion.commit()
                
                """
                Finalmente, cerramos la conexión con close(), imprimimos el mensaje de que el registro fué exitoso y retornamos True:
                """
                miConexion.close()
                tkinter.messagebox.showinfo(title="Registro Exitoso", message="El registro se realizó de forma exitosa.")
                return True
                
            
        except Exception as e:
            
            """
            Si ocurre una excepción, devolvemos un mensaje de error con la clase messagebox que indique que no se ha podido
            conectar con el servidor. Para ello, hemos debido capturar previamente la excepción que ocasiona un error
            de conexión y usar un if. Si coinciden,entonces lanzamos ese mensaje de error de conexión. De lo contrario,  mandamos 
            un mensaje de error inesperado:
            """
            codigoError="2003 (HY000): Can't connect to MySQL server on 'localhost:3306' (111)"
            errorConexion=str(e)
            
            if codigoError==errorConexion:
                tkinter.messagebox.showinfo(title="Error de conexión", message="No se pudo conectar con el servidor.")
            else:
                tkinter.messagebox.showinfo(title="Error Inesperado", message="Ocurrió un error inesperado.")
                
            """
            Devolvemos False para indicar que el inicio de sesión no fué exitoso:
            """
            return False