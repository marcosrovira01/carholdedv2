'''
Created on 7 feb 2023

@author: marcthegamer

Esta clase gestionará la primera pestaña de la ventana principal de la aplicación. La pestaña "Usuarios".
'''

import os
import tkinter 
from tkinter import *
from tkinter import ttk
from conexionBaseDatos.BaseDatosPrincipal import *

class ThreadUsuarios:
    
    """
    Constructor: Entran como parámetros:
    
    -pestañaUsuarios: Es la pestaña sobre la que se va a ejecutar este Thread.
    -correoElectronico: Es el correo del Usuario, que va a ser utilizado para las distintas consultas a la
    base de datos.
    """
    def __init__(self, pestañaUsuarios, correoElectronico):
        
        self.__pestañaUsuarios=pestañaUsuarios
        self.__correoElectronico=correoElectronico
        
    """
    iniciarThreadUsuarios(): Método que inicia el hilo "Usuarios" en la pestaña que se pasa como parámetro.
    """    
    def iniciarThreadUsuarios(self):
        
        """
        Antes de comenzar, colocamos el código en un try/except, por si ocurriese algún tipo de excepción, como por ejemplo, un error de conexión
        con el servidor:
        """
        try:
            """
            1. Necesitamos conocer el directorio de trabajo. Esto lo hacemos con la clase os y el método getcwd()
            """
            directorioDeTrabajo = os.getcwd()
            
            """
            2. Creamos una imagen con la clase PhotoImage, y la redimensionamos
            con el método subsample(escala x, escala y). Posteriormente, la introducimos en el label
            y la insertamos en la pestañaUsuarios con el método place():
            """
            self.imagen=PhotoImage(file=directorioDeTrabajo + "/imagenes/coche.png")
            self.imagen=self.imagen.subsample(2,2)
            Label(self.__pestañaUsuarios, image=self.imagen, bg="navy").place(x =40, y =20, width=150, height=100)
            
            """
            3. Creamos un nuevo objeto de la clase BaseDatosPrincipal, y le pasamos como parámetro el correo del usuario.
            Posteriormente, ejecutaremos el método obtenerDatoUsuario(), que nos devolverá el dato que nosotros queramos en base
            a el correo del usuario. En este caso, solicito que me devuelva el Nombre:
            """
            conexion=BaseDatosPrincipal(self.__correoElectronico)
            nombreUsuario=conexion.obtenerDatoUsuario("Nombre")
            
            """
            4. Introducimos un label para indicar al usuario "Bienvenido, Usuario, con la variable extraida de la base de datos y lo centramos con anchor=w:
            """
            bienvenida=Label(self.__pestañaUsuarios, text="Bienvenido, "+nombreUsuario+"", bg="navy", fg="white", height="2", font=("Calibri", 18), anchor='w')
            bienvenida.place(x =200, y =40, width=600, height=100)
            bienvenida.config(anchor="center")
            
            #Previo a comenzar a comenzar a insertar labels, insertamos un separador con la clase ttk.Separator:
            estilosSeparador=ttk.Style()
            estilosSeparador.configure('TSeparator', background="white")
            ttk.Separator(
                master=self.__pestañaUsuarios,
                orient=HORIZONTAL,
                style='TSeparator',
                class_= ttk.Separator,
                takefocus= 0    
            ).place(x=60, y=150, width=890, height=3)
            
            """
            5. Vamos introduciendo varios labels para ir introduciendo los datos personales del usuario en cuestión en pantalla, 
            y los vamos posicionando con place():
            """
            #Label para indicar que a continuación irán los datos personales del usuario:
            Label(self.__pestañaUsuarios, text="Datos personales:", bg="navy", fg="white", height="1", font=("Calibri", 13), anchor='w').place(x =60, y =160, width=500, height=50)
            
            #Label para indicar que a continuación irá el nombre del usuario:
            Label(self.__pestañaUsuarios, text="Nombre: "+nombreUsuario+"", bg="navy", fg="white", height="1", font=("Calibri", 13), anchor='w').place(x =60, y =210, width=500, height=30)
                    
            #Label para indicar que a continuación irán los apellidos del usuario. Extraemos dichos apellidos de la base de datos:
            primerApellido=conexion.obtenerDatoUsuario("PrimerApellido")
            segundoApellido=conexion.obtenerDatoUsuario("SegundoApellido")
            Label(self.__pestañaUsuarios, text="Apellidos: "+primerApellido+" "+segundoApellido+"", bg="navy", fg="white", height="1", font=("Calibri", 13), anchor='w').place(x =60, y =240, width=500, height=30)
            
            #Label para indicar que a continuación irá el correo del usuario:
            Label(self.__pestañaUsuarios, text="Correo Electrónico: "+self.__correoElectronico+"", bg="navy", fg="white", height="1", font=("Calibri", 13), anchor='w').place(x =60, y =270, width=500, height=30)
            
            #Label para indicar que a continuación irá el total gastado y el total de dinero que se ha obtenido en la aplicación. 
            #Extraemos dichos campos de la base de datos:
            totalGastado=conexion.obtenerDatoUsuario("CantidadGastada")
            totalVendido=conexion.obtenerDatoUsuario("CantidadVendida")
            Label(self.__pestañaUsuarios, text="Cantidad Gastos: "+totalGastado+"€", bg="navy", fg="white", height="1", font=("Calibri", 13), anchor='w').place(x =60, y =300, width=500, height=30)
            Label(self.__pestañaUsuarios, text="Cantidad Ventas: "+totalVendido+"€", bg="navy", fg="white", height="1", font=("Calibri", 13), anchor='w').place(x =60, y =330, width=500, height=30)
            
            #Label para indicar que a continuación se ofrece un resúmen de las operaciones realizadas por el usuario:
            Label(self.__pestañaUsuarios, text="Resúmen de tus ventas:", bg="navy", fg="white", height="1", font=("Calibri", 15), anchor='w').place(x =365, y =380, width=500, height=30)
            
            """
            6. Insertamos un botón para actualizar los datos de la pestaña:
            """
            bActualizar = Button(self.__pestañaUsuarios, text="Actualizar\n Datos", height="3", width="30", bg="white", fg="navy", font="Calibri", 
                            command=self.iniciarThreadUsuarios)
            bActualizar.place(x =750, y = 300, width=200, height=50)
            
            
            """
            7. Insertamos una tabla en nuestra pestañaUsuarios, la cual ofrecerá un resúmen de las ventas realizadas por el usuario:
            """
            
            #Definimos los estilos para el heading de la tabla que crearemos a continuación con la clase ttk.Style y el método configure()
            #En el método configure, con el parámetro Treeview.Heading, indicamos que estamos dando dichos estilos al Heading de la tabla.
            estilosHeadingTabla = ttk.Style()
            estilosHeadingTabla.configure('Treeview.Heading', background="white", width=50, font="Calibri", foreground="black", padding=7)
            
            #Creamos un widget Treeview en la pestañaUsuarios, que nos permitirá crear una tabla. Al widget le decimos que la tabla tendrá 4 columnas:
            tablaResumenVentas = ttk.Treeview(self.__pestañaUsuarios, columns=("col1", "col2", "col3", "col4"), show="headings")
    
            #Creamos las cabeceras de la tabla. La tabla mostrará los campos Comprador, Fecha, Importe y Modelo de la Base de datos:
            tablaResumenVentas.heading("col1", text="Comprador")
            tablaResumenVentas.heading("col2", text="Fecha")
            tablaResumenVentas.heading("col3", text="Importe")
            tablaResumenVentas.heading("col4", text="Modelo")
            
            #Con el objeto conexión, que tiene como atributo el correo del usuario, y en base a este mismo, llamamos al método obtenerRegistroTablaResumenVentas
            #de la clase BaseDatosPrincipal, el cual nos devolverá todos los datos que hemos solicitado a la base de datos. Sin embargo, para poder leer
            # e insertar todos registros en la tabla, lo deberemos de hacer con un bucle for, ya que si no, solo insertaremos un registro y no todos los 
            #resultantes de nuestra consulta:
            for comprador, fecha, importe, modelo in conexion.obtenerRegistroTablaResumenVentas():
                tablaResumenVentas.insert("", 0, text="1", values=(comprador, fecha, importe, modelo))
            
            
            # Establecemos alternancia de colores gris y blanco en cada registro de la tabla con el método tag_configure:
            tablaResumenVentas.tag_configure("oddrow", background="gray", font=("Calibri", 12), foreground="white")
            tablaResumenVentas.tag_configure("evenrow", background="white", font=("Calibri", 12), foreground="grey")
            for i, item in enumerate(tablaResumenVentas.get_children()):
                if i % 2 == 0:
                    tablaResumenVentas.item(item, tags=("oddrow",))
                else:
                    tablaResumenVentas.item(item, tags=("evenrow",))
            
            #Colocamos la tabla en nuestra interfaz gráfica con el método place:
            tablaResumenVentas.place(x =60, y =430, width=892, height=150)
            
            #Añadimos una barra de deslizamiento vertical para posteriormente colocarla en la tabla:
            scrollbar = ttk.Scrollbar(tablaResumenVentas, orient="vertical", command=tablaResumenVentas.yview)
            scrollbar.pack(side="right", fill="y")
            
            #Insertamos la barra de deslizamiento vertical en su correspondiente tabla:
            tablaResumenVentas.configure(yscrollcommand=scrollbar.set)
            
        except Exception as e:

            print(e)
            
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