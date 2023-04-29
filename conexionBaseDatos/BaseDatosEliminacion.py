'''
Esta clase nos servirá para conectarnos a la base de datos y eliminar un usuario determinado.

@author: marcthegamer
'''
import tkinter.messagebox
import mysql.connector

class BaseDatosEliminacion:
    
    def __init__(self, correo, contraseña):
        
        """
        cuando recibamos los atributos, los parseamos a string para que no
        haya ningún problema, por si el usuario introduce enteros u otro tipo de dato en el formulario:
        """
        self.__correo=str(correo)
        self.__contraseña=str(contraseña)
        
        """
        conexionBaseDatosEliminacionn(): método que se encargará de conectarse a nuestra base de datos:
        
        @return: True si el borrado de datos fué exitoso o false en caso contrario.
        """
    def conexionBaseDatosEliminacion(self):
        """
        Bloque try para controlar excepciones, por ejemplo si el usuario introduce de forma incorrecta sus datos
        , si no se puede conectar a la base de datos, etc..:
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
                Si los datos son correctos, procedemos a eliminar el registro del Usuario dado:
                """
                nuevosql="DELETE FROM Usuarios WHERE CorreoElectronico='"+self.__correo+"'"
                cursor.execute(nuevosql)
                miConexion.commit()
                
                """
                Creamos un mensaje que diga que el usuario se eliminó con éxito. Además, cerramos 
                la conexión y devolvemos False.
                """
                tkinter.messagebox.showinfo(title="Borrado exitoso", message="Su usuario se ha eliminado de forma exitosa.")
                miConexion.close()
                return True
                
            else:
                
                """
                Con la clase tkinter.messagebox y el método showinfo(), devolvemos un mensaje de error en caso de que los datos
                introducidos sean incorrectos. Además, cerramos la conexión y devolvemos False.
                """
                tkinter.messagebox.showinfo(title="Borrado no realizado", message="Los datos introducidos son incorrectos. Inténtelo de nuevo.")
                miConexion.close()
                return False
                
                
            """
            Finalmente, cerramos el socket "miConexion" con el metodo .close() 
            """
           
            
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
                
            return False