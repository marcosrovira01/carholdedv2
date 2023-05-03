'''
Created on 7 feb 2023

@author: marcthegamer

Esta clase gestionará la segunda pestaña de la ventana principal de la aplicación. La pestaña "Compras".
'''

import os
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from conexionBaseDatos.BaseDatosPrincipal import *

class ThreadCompras:
    
    """
    Constructor: Entran como parámetros:
    
    -pestañaCompras: Es la pestaña sobre la que se va a ejecutar este Thread.
    -correoElectronico: Es el correo del Usuario, que va a ser utilizado para las distintas consultas a la
    base de datos.
    """
    def __init__(self, pestañaCompras, correoElectronico):
        
        self.__pestañaCompras=pestañaCompras
        self.__correoElectronico=correoElectronico
        
    """
    iniciarThreadCompras(): Método que inicia el hilo "Compras" en la pestaña que se pasa como parámetro.
    """    
    def iniciarThreadCompras(self):
        
        """
        Previamente insertamos sentencia try/except para control de errores:
        """
        try:
            """
            1. Necesitamos conocer el directorio de trabajo. Esto lo hacemos con la clase os y el método getcwd()
            """
            directorioDeTrabajo = os.getcwd()
            
            """
            2. Creamos una imagen con la clase PhotoImage, y la redimensionamos
            con el método subsample(escala x, escala y). Posteriormente, la introducimos en el label
            y la insertamos en la pestañaCompras con el método place():
            """
            self.imagen=PhotoImage(file=directorioDeTrabajo + "/imagenes/coche.png")
            self.imagen=self.imagen.subsample(2,2)
            Label(self.__pestañaCompras, image=self.imagen, bg="navy").place(x =40, y =20, width=150, height=100)
            
            """
            3. Introducimos un label llamado labelPrincipal para indicar al usuario que debe seleccionar un vehículo de los disponibles en el listado
            para comprarlo:
            """
            labelPrincipal=Label(self.__pestañaCompras, text="Formulario de compras.\n\n Nota: Selecciona un vehículo de los disponibles \nen la tabla para comprarlo:", bg="navy", fg="white", height="2", font=("Calibri", 18), anchor='w')
            labelPrincipal.place(x =200, y =10, width=600, height=150)
            labelPrincipal.config(anchor="center")
            
            """
            4. Introducimos un separador blanco con la clase ttk.Separator:
            """
            estilosSeparador=ttk.Style()
            estilosSeparador.configure('TSeparator', background="white")
            ttk.Separator(
                master=self.__pestañaCompras,
                orient=HORIZONTAL,
                style='TSeparator',
                class_= ttk.Separator,
                takefocus= 0    
            ).place(x=60, y=180, width=880, height=3)
            
            """
            5. Insertamos un entry que actuará como buscador de vehículos por modelo llamado buscador:
            """
            buscador = Entry(self.__pestañaCompras, width="40", font=("Calibri", 14))
            buscador.place(x=170, y = 220, width=300, height=40);

            """
            6. Insertamos un botón que se llamará bBuscar, que realizará una búsqueda de vehículos disponibles en función del modelo:
            """

            bBuscar = Button(self.__pestañaCompras, text="Buscar vehículos", height="3", width="30", bg="white",
                                 fg="navy", font="Calibri",
                                 command=self.iniciarThreadCompras)
            bBuscar.place(x=520, y=215, width=300, height=50)

            """
            4. Introducimos otro separador blanco con la clase ttk.Separator:
            """
            estilosSeparador = ttk.Style()
            estilosSeparador.configure('TSeparator', background="white")
            ttk.Separator(
                master=self.__pestañaCompras,
                orient=HORIZONTAL,
                style='TSeparator',
                class_=ttk.Separator,
                takefocus=0
            ).place(x=60, y=300, width=880, height=3)
            
            """
            6.Insertamos un botón que se llamará bActualizar, que ejecutará el método iniciarThreadCompras() para actualizar los datos de la tablaVehiculos:
            """
            bActualizar = Button(self.__pestañaCompras, text="Actualizar Vehículos", height="3", width="30", bg="white", fg="navy", font="Calibri", 
                                command=self.iniciarThreadCompras)
            bActualizar.place(x =350, y = 322.5, width=300, height=50)
            
            """
            7. Insertamos una tabla en nuestra pestañaCompras, la cual ofrecerá un listado de los vehículos que se encuentran actualmente en venta:
            """
            #Definimos los estilos para el heading de la tabla que crearemos a continuación con la clase ttk.Style y el método configure()
            #En el método configure, con el parámetro Treeview.Heading, indicamos que estamos dando dichos estilos al Heading de la tabla.
            estilosHeadingTabla = ttk.Style()
            estilosHeadingTabla.configure('Treeview.Heading', background="white", width=30, font="Calibri", foreground="black", padding=7)
            
            #Creamos un widget Treeview en la pestañaCompras, que nos permitirá crear una tabla. Al widget le decimos que la tabla tendrá 6 columnas:
            tablaVehiculos = ttk.Treeview(self.__pestañaCompras, columns=("col1", "col2", "col3", "col4", "col5", "col6"), show="headings")
    
            #Creamos las cabeceras de la tabla. La tabla mostrará los campos Modelo, Vendedor, Matricula, Marca, Color y Precio de la Base de datos:
            tablaVehiculos.heading("col1", text="Modelo")
            tablaVehiculos.heading("col2", text="Vendedor")
            tablaVehiculos.heading("col3", text="Matricula")
            tablaVehiculos.heading("col4", text="Marca")
            tablaVehiculos.heading("col5", text="Color")
            tablaVehiculos.heading("col6", text="Precio")
            
            # Establecemos la anchura de cada columna:
            tablaVehiculos.column("col1", width=50)
            tablaVehiculos.column("col2", width=50)
            tablaVehiculos.column("col3", width=50)
            tablaVehiculos.column("col4", width=50)
            tablaVehiculos.column("col5", width=50)
            tablaVehiculos.column("col6", width=50)
            
            #Creamos un nuevo objeto llamado "conexion", de la clase BaseDatosPrincipal, que se encargará de conectarse con la base de datos,
            #y le pasamos como parámetro el correo electrónico del usuario:
            conexion=BaseDatosPrincipal(self.__correoElectronico)
            
            #Con el objeto conexión, que tiene como atributo el correo del usuario, llamamos al método obtenerRegistroTablaVehiculos
            #de la clase BaseDatosPrincipal, el cual nos devolverá todos los datos que hemos solicitado a la base de datos. Sin embargo, para poder leer
            # e insertar todos registros en la tabla, lo deberemos de hacer con un bucle for, ya que si no, solo insertaremos un registro y no todos los 
            #resultantes de nuestra consulta:
            for modelo, vendedor, matricula, marca, color, precio in conexion.obtenerRegistroTablaVehiculos():
                tablaVehiculos.insert("", 0, text="1", values=(modelo, vendedor, matricula, marca, color, str(precio) + ' €'))
            
            
            # Establecemos alternancia de colores gris y blanco en cada registro de la tabla con el método tag_configure:
            tablaVehiculos.tag_configure("oddrow", background="gray", font=("Calibri", 12), foreground="white")
            tablaVehiculos.tag_configure("evenrow", background="white", font=("Calibri", 12), foreground="grey")
            for i, item in enumerate(tablaVehiculos.get_children()):
                if i % 2 == 0:
                    tablaVehiculos.item(item, tags=("oddrow",))
                else:
                    tablaVehiculos.item(item, tags=("evenrow",))
            
            #Colocamos la tabla en nuestra interfaz gráfica con el método place:
            tablaVehiculos.place(x =10, y =390, width=980, height=300)
            
            #Añadimos una barra de deslizamiento vertical para posteriormente colocarla en la tabla:
            scrollbar = ttk.Scrollbar(tablaVehiculos, orient="vertical", command=tablaVehiculos.yview)
            scrollbar.pack(side="right", fill="y")
            
            #Insertamos la barra de deslizamiento vertical en su correspondiente tabla:
            tablaVehiculos.configure(yscrollcommand=scrollbar.set)
            
            """
            8. Tras insertar la tabla, insertamos un entry  llamado matriculaVehiculo para que el usuario introduzca la matrícula del vehículo que desea comprar:
            """
            #insertamos previamente un label para indicar que a continuación el usuario debe de introducir la matrícula del coche que desea comprar:
            Label(self.__pestañaCompras, text="Introduzca la matrícula del vehículo \nque desea comprar, o seleccione uno:", bg="navy", fg="white", width="500", height="2", font=("Calibri", 16), anchor='w').place(x=120, y = 720, width=500, height=50);
            
            #insertamos el entry llamado matriculaVehiculo
            matriculaVehiculo=Entry(self.__pestañaCompras, width="40", font=("Calibri", 14))
            matriculaVehiculo.place(x =190, y = 790, width=250, height=30)

            """
            9. Después del entry, insertamos una función llamada on_select que se ejecutará cuando se seleccione una fila del Treeview. 
            Lo que hará la función es reflejar la matrícula del vehículo seleccionado en el entry anterior:
            """
            def on_select(event):
                # Obtenemos la fila seleccionada
                fila = tablaVehiculos.selection()[0]

                # Obtenemos los valores de la fila seleccionada
                matriculaInsertar = tablaVehiculos.item(fila)["values"]

                # Actualizamos el contenido del Entry con el valor del campo "Matrícula"
                matriculaVehiculo.delete(0, END)
                matriculaVehiculo.insert(0, matriculaInsertar[2])

            """
            10.Asociamos la función on_select al evento "Selection" del Treeview
            """
            tablaVehiculos.bind("<<TreeviewSelect>>", on_select)

            """
            11. Previo a insertar el botón que realizará la compra, crearemos el método comprar(), que recopilará los datos del entry matriculaVehiculo introducidos
            por el usuario y creará un objeto de la clase BaseDatosPrincipal. En dicho objeto, entrarán como parámetros el correo del usuario y la matrícula 
            del vehículo que desea comprar. Además, ejecutará el método comprarVehículo() de la clase BaseDatosPrincipal() para llevar a cabo la compra.
            Posteriormente, en el bComprar, usaremos este método para llevar a cabo la compra:
            """
            def comprar():

                # Antes de comenzar el proceso de compra de un vehículo, preguntamos al usuario si realmente desea comprar ese vehículo con un messagebox:
                respuesta = messagebox.askquestion("Comprar vehículo",
                                                   "¿Está seguro de que quiere comprar el vehículo seleccionado?")

                # Si presiona en sí, entonces comenzamos el proceso de venta:
                if respuesta == "yes":

                    #Primero, recuperamos lo que el usuario ha introducido en el entry matriculaVehiculo con el método get():
                    matricula = matriculaVehiculo.get()

                    #A continuación, comprobamos si el campo se encuentra vacío:
                    if matricula!='':

                        #Si hay algún dato, realizamos la conexión con la base de datos y ejecutamos el método comprarVehículo():
                        #El resultado de la ejecución del método comprarVehiculo() lo almacenamos en una variable llamada correcto:
                        nuevaConexion=BaseDatosPrincipal(self.__correoElectronico, matricula)
                        correcto=nuevaConexion.comprarVehiculo()

                        if correcto:
                            #Si la compra fué exitosa, imprimimos el mensaje correspondiente y ejecutamos el método iniciarThreadCompras() para actualizar los datos
                            tkinter.messagebox.showinfo(title="Compra Exitosa", message="La compra se llevó a cabo con éxito!")
                            self.iniciarThreadCompras()

                        else:
                            #Si la compra no fue exitosa,  simplemente eliminamos el campo matriculaVehiculo
                            matriculaVehiculo.delete(0, "end")

                    else:
                        #Si el campo se encuentra vacío, retornamos el correspondiente mensaje de error:
                        tkinter.messagebox.showinfo(title="Campo Vacío", message="El campo matrícula se encuentra vacío. \nPor favor, ingresa una matrícula válida.")
                     
                
            """
            12. Insertamos el botón comprar, que comprará el vehículo solicitado por el usuario
            en base a la matrícula introducida. El botón ejecutará el método comprar(), declarado anteriormente:
            """
            bComprar = Button(self.__pestañaCompras, text="Comprar Vehículo", height="3", width="30", bg="white", fg="navy", font="Calibri", 
                                command=comprar)
            bComprar.place(x =560, y = 750, width=300, height=50)
    
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