
'''
Created on 6 feb 2023

@author: marcthegamer

Esta clase nos servirá para gestionar todas las conexiones a nuestra base de datos una vez que el usuario se ha logueado en el
sistema y ha accedido a nuestra aplicación
'''

import mysql.connector
import tkinter.messagebox
from datetime import date
import mysql.connector
from mysql.connector.errors import IntegrityError


class BaseDatosPrincipal:

    def __init__(self, *args):
        '''
        Constructor: 
        
        Recibimos un array de argumentos, en el que, se crearán unos u otros atributos privados en función de si pasamos
        1, 2 o 6 argumentos. Si pasamos un solo argumento, se creará el atributo correo, si pasamos 2 argumentos, se crearán los
        atributos correo y matrícula, y si pasamos 6 argumentos, se crearán los atributos correo, matricula, modelo, color, precio y codigoMarca. 
        Es una forma de solventar la no existencia de sobrecarga de constructores en python.
        '''
        if len(args)==1:
            self.__correo=str(args[0])
        elif len(args)==2:
            self.__correo=str(args[0])
            self.__matricula=str(args[1])
        elif len(args)==6:
            self.__correo=str(args[0])
            self.__matricula=str(args[1])
            self.__modelo=str(args[2])
            self.__color=str(args[3])
            self.__precio=args[4]
            self.__codigoMarca=args[5]
            
    
    """
    Método obtenerDatoUsuario(): servirá para obtener un dato en específico del usuario. Como parámetros, tenemos:
    
     -El nombre de un campo de la tabla Usuarios de la base de datos, para que se devuelva el dato solicitado de ese campo
     en base a el correo electrónico del usuario. 
    """
    def obtenerDatoUsuario(self, nombreCampo):
        """
        Bloque try para controlar excepciones, por ejemplo si no se puede conectar con la base de datos:
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
            Realizamos la consulta a la base de datos, la cual obtendrá el dato solicitado del Usuario en base a 
            su correo electrónico:
            """
            sql="SELECT "+nombreCampo+" from Usuarios WHERE CorreoElectronico='"+self.__correo+"'"
            
            """
            Ejecutamos la consulta con el método execute()
            """
            cursor.execute(sql)
               
            """
            Ejecutamos el método fetchall() en un for, el cual nos devolverá una tupla con los valores obtenidos de la consulta.
            Posteriormente, con el método str(), transformamos esa tupla a un string, y le eliminamos todos los substrings
            que no nos interesa mostrar, como los paréntesis o las comas con el método replace(). Finalmente, lo devolvemos con return:
            """
            for dato in cursor.fetchall():
                datoStr= str(dato).replace(',', '').replace('(', '').replace(')', '').replace("'", '')
            return datoStr   
        
            """
            cerramos la conexión con close():
            """
            miConexion.close()
            
        except Exception as e:
            
            """
            Si ocurre cualquier tipo de excepción, la levantamos utilizando la palabra reservada raise, de forma que en el fragmento de código en el
            que llamemos a este método, si ocurre una excepción, ese fragmento de código recibirá dicha excepción para poder tratarla adecuadamente.
            """
            raise e
                
                
                
    """
    Método obtenerRegistroTablaResumenVentas(): servirá para obtener los registros correspondientes de la tablaResumenVentas de la pestaña Usuarios.
    
    @return: cursor.fetchall()----Devuelve una tupla con todos los valores obtenidos de la consulta.
    """
    def obtenerRegistroTablaResumenVentas(self):
        """
        Bloque try para controlar excepciones, por ejemplo, si no se puede conectar con la base de datos:
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
            Realizamos la consulta a la base de datos, la cual obtendrá los registros solicitados en base al correo electrónico del usuario.
            Los resultados de la consulta irán ordenados por orden alfabético en función de la fecha de alta del vehículo:
            """
            sql="select t2.Fecha, t2.Importe, t3.Modelo, t3.Vendido from Usuarios as t1 inner join Alta as t2 on (t1.CodigoUsuario=t2.CodigoUsuario) inner join Vehiculos as t3 on (t2.Matricula=t3.Matricula) where t1.CorreoElectronico='"+self.__correo+"' order by t2.Fecha asc"
            """
            Ejecutamos la consulta con el método execute()
            """
            cursor.execute(sql)
               
            """
            Ejecutamos el método fetchall() del objeto cursor y lo devolvemos con return. Como ya hemos comentado anteriormente, este método nos generará una tupla
            con los valores que haya obtenido de la consulta que hemos ejecutado, por lo que, en realidad, estaremos devolviendo esa tupla con todos los datos resultan-
            tes de la consulta anterior.
            """
            return cursor.fetchall()
            
            """
            cerramos la conexión con close():
            """
            miConexion.close()
            
        except Exception as e:
            """
            Si ocurre cualquier tipo de excepción, la levantamos utilizando la palabra reservada raise, de forma que en el fragmento de código en el
            que llamemos a este método, si ocurre una excepción, ese fragmento de código recibirá dicha excepción para poder tratarla adecuadamente.
            """
            raise e

    """
    Método obtenerRegistroTablaResumenCompras(): servirá para obtener los registros correspondientes de la tablaResumenCompras de la pestaña Usuarios.

    @return: cursor.fetchall()----Devuelve una tupla con todos los valores obtenidos de la consulta.
    """

    def obtenerRegistroTablaResumenCompras(self):
        """
        Bloque try para controlar excepciones, por ejemplo, si no se puede conectar con la base de datos:
        """
        try:
            """
            Creamos un nuevo socket, que se conectará a la base de datos "carholdedv2", con usuario root, contraseña 2585 
            y dirección del servidor localhost:
            """
            miConexion = mysql.connector.connect(
                host="localhost",
                user="root",
                password="2585",
                database="carholdedv2"
            )

            """
            Creamos un objeto cursor, que será el que contendrá la consulta
            a la base de datos:
            """
            cursor = miConexion.cursor()

            """
            Realizamos la consulta a la base de datos, la cual obtendrá los registros solicitados en base al correo electrónico del usuario.
            Los resultados de la consulta irán ordenados en función de la fecha de compra del vehículo:
            """
            sql = "select t2.Fecha, t2.Importe, t1.Modelo, t4.NombreMarca from Vehiculos as t1 inner join Compra as t2 on (t1.Matricula=t2.Matricula) inner join Usuarios as t3 on (t2.CodigoUsuario=t3.CodigoUsuario) inner join Marcas as t4 on (t1.CodigoMarca=t4.CodigoMarca) where t3.CorreoElectronico='"+self.__correo+"' order by t2.Fecha asc"
            """
            Ejecutamos la consulta con el método execute()
            """
            cursor.execute(sql)

            """
            Ejecutamos el método fetchall() del objeto cursor y lo devolvemos con return. Como ya hemos comentado anteriormente, este método nos generará una tupla
            con los valores que haya obtenido de la consulta que hemos ejecutado, por lo que, en realidad, estaremos devolviendo esa tupla con todos los datos resultan-
            tes de la consulta anterior.
            """
            return cursor.fetchall()

            """
            cerramos la conexión con close():
            """
            miConexion.close()

        except Exception as e:
            """
            Si ocurre cualquier tipo de excepción, la levantamos utilizando la palabra reservada raise, de forma que en el fragmento de código en el
            que llamemos a este método, si ocurre una excepción, ese fragmento de código recibirá dicha excepción para poder tratarla adecuadamente.
            """
            raise e
    
    """
    Método registrarAlta(): método que se encargará de registrar cualquier alta realizada en la pestañaAltaVehiculos de la aplicación.
    
    @return: Puede devolver True o False, dependiendo de si ha ocurrido un error o no durante el alta de un vehículo.
    """
    def registrarAlta(self):
        """
        Bloque try para controlar excepciones, por ejemplo, si no se puede conectar con la base de datos:
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
            Realizamos una consulta a la base de datos para conocer el campo CodigoUsuario en base a su correo electronico:
            """
            sql="select CodigoUsuario from Usuarios where CorreoElectronico='"+self.__correo+"'"
            
            """
            Ejecutamos la consulta con el método execute()
            """
            cursor.execute(sql)
            
            """
            Almacenamos la lista resultante de la consulta con el método fetch(), concretamente, su variante fetchone, que nos retornará una lista de
            1 solo valor:
            """
            listaCodigoUsuario=cursor.fetchone()
            
            """
            Asignamos ese único valor de la lista a la variable codigoVendedor:
            """
            codigoVendedor=listaCodigoUsuario[0]
            
            """
            Una vez que tenemos el codigo del usuario, ahora sí, podemos hacer el insert correspondiente, el cual insertará en la tabla
            Vehículos los campos Matricula, Modelo, Color, Precio, CodigoMarca y Vendido (valdrá por defecto 0, lo que nos indicará que aún nadie
            lo ha comprado):
            """
            nuevosql="insert into Vehiculos (Matricula, Modelo, Color, Precio, CodigoMarca, Vendido) values (%s, %s, %s, %s, %s, %s)"
            val=(self.__matricula, self.__modelo, self.__color, float(self.__precio), self.__codigoMarca, 0)
            """
            Ejecutamos la sentencia insert con execute():
            """
            cursor.execute(nuevosql, val)
            
            """
            Utilizamos el método commit() para refrescar la base de datos después de la inserción de algún dato:
            """
            miConexion.commit()

            """
            Por último, añadimos dicha venta a la tabla Altas, que relaciona la tabla Vehículos con la tabla Usuarios en nuestra app
            """
            #Previamente, necesitamos obtener la fecha actual. Esto lo hacemos con la clase date:
            fecha=date.today().strftime('%Y-%m-%d')

            #Realizamos la consulta para insertar los valores (Fecha, Importe, CodigoUsuario y Matrícula en la tabla Alta:
            ultimosql = "insert into Alta (Fecha, Importe, CodigoUsuario, Matricula) values (%s, %s, %s, %s)"
            ultimoval = (fecha, float(self.__precio), codigoVendedor, self.__matricula)

            """
            Ejecutamos la sentencia insert con execute():
            """
            cursor.execute(ultimosql, ultimoval)

            """
            Utilizamos el método commit() para refrescar la base de datos después de la inserción de algún dato:
            """
            miConexion.commit()

            """
            cerramos la conexión con el método close():
            """
            miConexion.close()
            
            """
            Si todo ha ido bien, devolvemos true
            """
            return True
            
        except mysql.connector.IntegrityError as e:
            """
            Devolvemos el mensaje de error adecuado para esta excepción:
            """
            tkinter.messagebox.showinfo(title="Integrity Error", message="Ya hay un vehículo registrado con esa matrícula.\nIntroduzca una matrícula diferente.")
            
            """
            Como ha ocurrido una excepción, devolvemos False
            """
            return False
        
        except ValueError as e:
            """
            Devolvemos el mensaje de error adecuado para esta excepción:
            """
            tkinter.messagebox.showinfo(title="Value Error", message="No has introducido un valor numérico en el campo precio.")
            
            """
            Como ha ocurrido una excepción, devolvemos False
            """
            return False
        
        except Exception as e:
            """
            Si ocurre otra excepción distinta a las anteriores, devolvemos un mensaje de error con la clase messagebox que indique que no se ha podido
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
            Como ha ocurrido una excepción, devolvemos False
            """
            return 
        
    """
    Método obtenerRegistroTablaVehiculos(): servirá para obtener los registros correspondientes de la tablaVehiculos de la pestaña Compras.
    """
    def obtenerRegistroTablaVehiculos(self):
        """
        Bloque try para controlar excepciones, por ejemplo, si no se puede conectar con la base de datos:
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
            Realizamos la consulta a la base de datos, la cual obtendrá los registros solicitados para poder ser enviados a la "tablaVehículos" y ser mostrados.
            Los resultados de la consulta irán ordenados por orden alfabético en función del modelo de vehículo. La consulta obtendrá los campos Modelo, Vendedor,
            Matrícula, Marca, Color y Precio:
            """
            sql="select t1.Modelo, concat(t3.Nombre, ' ', t3.PrimerApellido, ' ', t3.SegundoApellido), t1.Matricula, t4.NombreMarca, t1.Color, t1.Precio from Vehiculos as t1 inner join Alta as t2 on (t1.Matricula=t2.Matricula)  inner join Usuarios as t3 on (t2.CodigoUsuario=t3.CodigoUsuario) inner join Marcas as t4 on (t1.CodigoMarca=t4.CodigoMarca) where t1.Vendido=0 and t3.CorreoElectronico!='"+self.__correo+"' order by t1.Modelo asc"
            
            """
            Ejecutamos la consulta con el método execute()
            """
            cursor.execute(sql)
               
            """
            Ejecutamos el método fetchall() del objeto cursor y lo devolvemos con return. Como ya hemos comentado anteriormente, este método nos generará una tupla
            con los valores que haya obtenido de la consulta que hemos ejecutado, por lo que, en realidad, estaremos devolviendo esa tupla con todos los datos resultan-
            tes de la consulta anterior.
            """
            return cursor.fetchall()
            
            """
            cerramos la conexión con close():
            """
            miConexion.close()
            
        except Exception as e:
                
            """
            Si ocurre cualquier tipo de excepción, la levantamos utilizando la palabra reservada raise, de forma que en el fragmento de código en el
            que llamemos a este método, si ocurre una excepción, ese fragmento de código recibirá dicha excepción para poder tratarla adecuadamente.
            """
            raise e
        
    """
    Método comprarVehiculo(): realizará la compra solicitada por el usuario en la pestañaCompras:
    
    @return: ----True o False, dependiendo de si la compra ha sido exitosa o no.
    """  
    def comprarVehiculo(self):
        """
        Previamente hacemos un try/except para comprobar si hay alguna excepción:
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
            Creamos un objeto cursor, que será el que contendrá las consultas
            a la base de datos:
            """
            cursor=miConexion.cursor()
            
            """
            Primero, realizamos una consulta para obtener el código del usuario, que será el código del comprador:
            """
            cursor.execute("select CodigoUsuario from Usuarios where CorreoElectronico='"+self.__correo+"'")
    
            #Almacenamos la lista resultante de la consulta con el método fetch(), concretamente, su variante fetchone, que nos retornará una lista de
            #1 solo valor, y la almacenamos en la variable codigoComprador:
            listaCodigoUsuario=cursor.fetchone()
            codigoComprador=listaCodigoUsuario[0]
            
            """
            Obtenemos también el precio del vehículo mediante otra consulta:
            """
            cursor.execute("select Precio from Vehiculos where Matricula='"+self.__matricula+"'")
            listaPrecio=cursor.fetchone()
            precioVehiculo=listaPrecio[0]
            
            """
            Obtenemos el codigo del Vendedor:
            """
            cursor.execute("select t1.CodigoUsuario from Alta as t1 inner join Vehiculos as t2 on (t1.Matricula=t2.Matricula) where t2.Matricula='"+self.__matricula+"'")
            listaCodigoVendedor=cursor.fetchone()
            codigoVendedor=listaCodigoVendedor[0]  
            
            """
            Actualizamos con commit():
            """          
            miConexion.commit()

            """
            Recuperamos el campo "Vendido" de la base de datos en base al vehículo que el usuario está tratando de comprar:
            """
            cursor.execute("select Vendido from Vehiculos where Matricula='"+self.__matricula+"'")
            listaVendido = cursor.fetchone()
            vendido=listaVendido[0]

            """
            Si el vehículo se encuentra disponible, entonces procedemos con la compra:
            """
            if vendido==0:
                """
                A continuación, Ejecutamos las diversas operaciones  para llevar a cabo la compra:
                """
                #1. Agregamos la Compra realizada a la tabla "Compra" de la base de datos:
                fecha = date.today().strftime('%Y-%m-%d')

                sql1="insert into Compra(Fecha, Importe, CodigoUsuario, Matricula) values (%s, %s, %s, %s)"
                val1=(fecha, precioVehiculo, codigoComprador, self.__matricula)
                cursor.execute(sql1, val1)

                #2.Añadimos la cantidad que acaba de gastar el usuario a CantidadGastada en nuestra base de datos:

                sql2="update Usuarios set CantidadGastada=CantidadGastada+%s where CorreoElectronico=%s"
                val2=(precioVehiculo, self.__correo)
                cursor.execute(sql2, val2)

                #3.Añadimos la cantidad que acaba de vender el usuario que ha realizado la venta

                sql3="update Usuarios set CantidadVendida=CantidadVendida+%s where CodigoUsuario=%s"
                val3=(precioVehiculo, codigoVendedor)
                cursor.execute(sql3, val3)

                #4. Agregamos al campo "Vendido" el valor 1, haciendo referencia a que se ha vendido el vehículo satisfactoriamente:

                sql4="update Vehiculos set Vendido=%s where Matricula=%s"
                val3=(1, self.__matricula)
                cursor.execute(sql4, val3)

                """
                Actualizamos con commit()
                """
                miConexion.commit()

                """
                Si la compra ha sido exitosa, devolvemos True:
                """
                return True

            else:

                """
                Si por el contrario, el vehículo no se encuentra disponible, entonces lanzamos un mensaje de error y devolvemos false:
                """

                tkinter.messagebox.showinfo(title="Vehículo no disponible", message="EL vehículo que tratas de comprar no se encuentra disponible")
                return False


            
            """
            cerramos la conexión con close():
            """
            miConexion.close()
            
        except Exception as e:
            """
            Si ocurre una excepción , devolvemos un mensaje de error con la clase messagebox, dependiendo de la excepción producida. Para ello, hemos debido 
            capturar previamente la excepción  y usar una sentencia if. Si coinciden, entonces lanzamos ese determinado mensaje de error de conexión. 
            De lo contrario,  mandamos un mensaje de error inesperado. Además, devolvemos False:
            """
            codigoErrorConexion="2003 (HY000): Can't connect to MySQL server on 'localhost:3306' (111)"
            codigoErrorNoneType="'NoneType' object is not subscriptable"
            error=str(e)

            if error==codigoErrorConexion:
                tkinter.messagebox.showinfo(title="Error de conexión", message="No se pudo conectar con el servidor.")
            elif error==codigoErrorNoneType:
                tkinter.messagebox.showinfo(title="Error NoneType", message="La matrícula introducida no se corresponde con ningúna del catálogo")
            else:
                tkinter.messagebox.showinfo(title="Error Inesperado", message="Ocurrió un error inesperado.")
                
            return False

    """
    Método obtenerResultadoBusqueda(): servirá para obtener los registros correspondientes de la búsqueda en la pestañaCompras.
    
    @args: self, modelo
    -modelo: Será el modelo que introduzca el usuario para buscar vehículos en la base de datos.
    """

    def obtenerResultadoBusqueda(self, modelo):
        """
        Bloque try para controlar excepciones, por ejemplo, si no se puede conectar con la base de datos:
        """
        try:
            """
            Creamos un nuevo socket, que se conectará a la base de datos "carholdedv2", con usuario root, contraseña 2585 
            y dirección del servidor localhost:
            """
            miConexion = mysql.connector.connect(
                host="localhost",
                user="root",
                password="2585",
                database="carholdedv2"
            )

            """
            Creamos un objeto cursor, que será el que contendrá la consulta
            a la base de datos:
            """
            cursor = miConexion.cursor()

            """
            Realizamos la consulta a la base de datos, la cual obtendrá los registros solicitados para poder ser enviados a la "tablaVehículos" y ser mostrados.
            Los resultados de la consulta irán ordenados por orden alfabético en función del modelo de vehículo. La consulta obtendrá los campos Modelo, Vendedor,
            Matrícula, Marca, Color y Precio en función de la búsqueda solicitada por el usuario:
            """
            sql = "select t1.Modelo, concat(t3.Nombre, ' ', t3.PrimerApellido, ' ', t3.SegundoApellido), t1.Matricula, t4.NombreMarca, t1.Color, t1.Precio from Vehiculos as t1 inner join Alta as t2 on (t1.Matricula=t2.Matricula)  inner join Usuarios as t3 on (t2.CodigoUsuario=t3.CodigoUsuario) inner join Marcas as t4 on (t1.CodigoMarca=t4.CodigoMarca) where t1.Vendido=0 and t3.CorreoElectronico!='" + self.__correo + "'  and t1.Modelo like '%"+str(modelo)+"%' order by t1.Modelo asc"

            """
            Ejecutamos la consulta con el método execute()
            """
            cursor.execute(sql)

            """
            Ejecutamos el método fetchall() del objeto cursor y lo devolvemos con return. Como ya hemos comentado anteriormente, este método nos generará una tupla
            con los valores que haya obtenido de la consulta que hemos ejecutado, por lo que, en realidad, estaremos devolviendo esa tupla con todos los datos resultan-
            tes de la consulta anterior.
            """
            return cursor.fetchall()

            """
            cerramos la conexión con close():
            """
            miConexion.close()

        except Exception as e:

            """
            Si ocurre cualquier tipo de excepción, la levantamos utilizando la palabra reservada raise, de forma que en el fragmento de código en el
            que llamemos a este método, si ocurre una excepción, ese fragmento de código recibirá dicha excepción para poder tratarla adecuadamente.
            """
            raise e
            