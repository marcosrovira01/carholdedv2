'''
Esta clase nos servirá para gestionar nuestras conexiones a la base de datos durante el login del usuario

@author: marcthegamer
'''
import tkinter.messagebox
import mysql.connector

class BaseDatosLogin:
    
    def __init__(self, correo, contraseña):
        
        """
        cuando recibamos los atributos, los parseamos a string para que no
        haya ningún problema, por si el usuario introduce enteros u otro tipo de dato en el formulario:
        """
        self.__correo=str(correo)
        self.__contraseña=str(contraseña)
        
        """
        conexionBaseDatosLogin(): método que se encargará de conectarse a nuestra base de datos:
        
        @return: booleano:True si la validación fue exitosa o False si no lo fué.
        """
    def conexionBaseDatosLogin(self):
        """
        Bloque try para controlar excepciones, por ejemplo si el usuario introduce de forma incorrecta sus datos
        de inicio de sesión, si no se puede conectar a la base de datos, etc..:
        """
        try:
            """
            Creamos un nuevo socket, que se conectará a la base de datos "carholdedv2", con usuario root, contraseña 2585 
            y dirección del servidor localhost:
            """
            miConexion=mysql.connector.connect(
                host="localhost", 
                user="root",
                password="2585",
                database="carholdedv2"
                )
            
            """
            Creamos un objeto cursor, que será el que contendrá la consulta
            a la base de datos:
            """
            cursor=miConexion.cursor()
            
            """
            Definimos la variable que contendrá nuestra consulta (sql), y con '"+variable+"',
            insertamos una variable en el string, en este caso, el correo del usuario y su contraseña,
            que serán con los que realicemos la consulta:
            """
            sql="SELECT Contraseña from Usuarios WHERE CorreoElectronico='"+self.__correo+"' AND Contraseña='"+self.__contraseña+"'"
            
            """
            Ejecutamos la consulta con el método execute()
            """
            cursor.execute(sql)
            
            """
            Validamos la consulta con el método fetchall(). Si devuelve algún dato, entonces será porque el usuario y la contraseña
            han sido correctos y el usuario ha introducido correctamente sus datos. En caso contrario no devolverá nada, por
            lo que podemos usar if/else para hacer la distinción de si recibe o no algún dato:
            """
            
            if cursor.fetchall():
                """
                devolvemos true si el inicio de sesión fué exitoso y cerramos la conexión.
                """
                miConexion.close()
                return True
                
            else:
                
                """
                Con la clase tkinter.messagebox y el método showinfo(), devolvemos un mensaje de error en caso de que los datos
                introducidos sean incorrectos.
                """
                tkinter.messagebox.showinfo(title="Inicio de Sesion Incorrecto", message="Inicio de sesión incorrecto. Inténtelo de nuevo.")
                
                """
                Devolvemos False para indicar que el inicio de sesión no fué exitoso y cerramos la conexión:
                """
                miConexion.close()
                return False
            
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
            
            
            