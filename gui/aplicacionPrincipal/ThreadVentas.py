'''
Created on 7 feb 2023

@author: marcthegamer

Esta clase gestionará la última pestaña de la ventana principal de la aplicación. La pestaña "Ventas".
'''

import os
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from conexionBaseDatos.BaseDatosPrincipal import *

import mysql.connector
from mysql.connector.errors import IntegrityError

class ThreadVentas:
    
    """
    Constructor: Entran como parámetros:
    
    -pestañaVentas: Es la pestaña sobre la que se va a ejecutar este Thread.
    -correoElectronico: Es el correo del Usuario, que va a ser utilizado para las distintas consultas a la
    base de datos.
    """
    def __init__(self, pestañaVentas, correoElectronico):
        
        self.__pestañaVentas=pestañaVentas
        self.__correoElectronico=correoElectronico
        
    """
    iniciarThreadVentas(): Método que inicia el hilo "Ventas" en la pestaña que se pasa como parámetro.
    """    
    def iniciarThreadVentas(self):
        
        
        """
        1. Necesitamos conocer el directorio de trabajo. Esto lo hacemos con la clase os y el método getcwd()
        """
        directorioDeTrabajo = os.getcwd()
        
        """
        2. Creamos una imagen con la clase PhotoImage, y la redimensionamos
        con el método subsample(escala x, escala y). Posteriormente, la introducimos en el label
        y la insertamos en la pestañaVentas con el método place():
        """
        self.imagen=PhotoImage(file=directorioDeTrabajo + "/imagenes/coche.png")
        self.imagen=self.imagen.subsample(2,2)
        Label(self.__pestañaVentas, image=self.imagen, bg="navy").place(x =40, y =20, width=150, height=100)
        
        
        """
        4. Introducimos un label llamado labelPrincipal para indicar al usuario que los datos marcados con (*) son obligatorios,
         y lo centramos con anchor=w:
        """
        labelPrincipal=Label(self.__pestañaVentas, text="Formulario para dar de alta un vehículo.\n\n Nota: Los campos marcados con (*) \n son obligatorios:", bg="navy", fg="white", height="2", font=("Calibri", 18), anchor='w')
        labelPrincipal.place(x =200, y =10, width=600, height=150)
        labelPrincipal.config(anchor="center")
        
        #Previo a comenzar a diseñar el formulario, insertamos un separador con la clase ttk.Separator:
        estilosSeparador=ttk.Style()
        estilosSeparador.configure('TSeparator', background="white")
        ttk.Separator(
            master=self.__pestañaVentas,
            orient=HORIZONTAL,
            style='TSeparator',
            class_= ttk.Separator,
            takefocus= 0    
        ).place(x=60, y=180, width=880, height=3)
        
        """
        5. Insertamos un label para indicar que a continuación el usuario debe seleccionar una marca de las ya preestablecidas:
        """
        Label(self.__pestañaVentas, text="Seleccione una marca: (*)", bg="navy", fg="white", width="300", height="2", font=("Calibri", 16), anchor='w').place(x=365, y = 220, width=300, height=40);
        
        """
        6. Insertamos un combobox con el nombre de las marcas de la tabla Marcas de la base de datos, que le permitirá al 
        usuario seleccionar una de las disponibles:
        """
        seleccionarMarca = ttk.Combobox(self.__pestañaVentas, values=("Volswagen", "Audi", "Mercedes", "Renault", "Porche", "Seat", "Chevrolet", "BMW", "Nissan", "Citroen"), font=("Calibri", 14), state="readonly")
        seleccionarMarca.current(0)
        seleccionarMarca.place(x =402, y =270, width=200, height=30)
        
        """
        7. Insertamos un label para indicar que a continuación el usuario debe introducir la matrícula de su vehículo:
        """
        Label(self.__pestañaVentas, text="Introduzca la matrícula \nde su vehículo: (*)", bg="navy", fg="white", width="300", height="2", font=("Calibri", 16), anchor='w').place(x=200, y = 340, width=500, height=45);
        
        """
        8. Introducimos un entry para que el usuario introduzca su matrícula:
        """
        matriculaVehiculo=Entry(self.__pestañaVentas, width="40", font=("Calibri", 14))
        matriculaVehiculo.place(x =200, y = 406, width=250, height=30) 
        
        """
        9. Insertamos un label para indicar que a continuación el usuario debe introducir el modelo de su vehículo:
        """
        Label(self.__pestañaVentas, text="Introduzca el modelo \nde su vehículo: (*)", bg="navy", fg="white", width="300", height="2", font=("Calibri", 16), anchor='w').place(x=557, y = 340, width=500, height=45);
        
        """
        10. Introducimos un entry para que el usuario introduzca el modelo de su vehículo:
        """
        modeloVehiculo=Entry(self.__pestañaVentas, width="40", font=("Calibri", 14))
        modeloVehiculo.place(x =550, y = 406, width=250, height=30) 
        
        """
        11. Insertamos un label para indicar que a continuación el usuario debe introducir el color de su vehículo:
        """
        Label(self.__pestañaVentas, text="Introduzca el color \nde su vehículo: (*)", bg="navy", fg="white", width="300", height="2", font=("Calibri", 16), anchor='w').place(x=225, y = 470, width=500, height=45);
        
        """
        12. Introducimos un entry para que el usuario introduzca el color de su vehículo:
        """
        colorVehiculo=Entry(self.__pestañaVentas, width="40", font=("Calibri", 14))
        colorVehiculo.place(x =200, y = 536, width=250, height=30)  
        
        """
        13. Insertamos un label para indicar que a continuación el usuario debe introducir el precio de su vehículo:
        """
        Label(self.__pestañaVentas, text="Introduzca el precio \nde su vehículo: (*)", bg="navy", fg="white", width="300", height="2", font=("Calibri", 16), anchor='w').place(x=559, y = 470, width=500, height=45);
        
        """
        14. Introducimos un entry para que el usuario introduzca el precio de su vehículo:
        """
        precioVehiculo=Entry(self.__pestañaVentas, width="40", font=("Calibri", 14))
        precioVehiculo.place(x =550, y = 536, width=250, height=30) 
        
        """
        16. Insertamos una función llamada vender() que se ejecutará cuando presionemos el botón declarado a continuación de la misma. Esta función se encargará del proceso de venta
        de un vehículo.
        """
        def realizarVenta():

            #Antes de comenzar el proceso de venta de un vehículo, preguntamos al usuario si realmente desea poner a la venta ese vehículo con un messagebox:
            respuesta = messagebox.askquestion("Vender vehículo", "¿Está seguro de que quiere vender el vehículo introducido?")

            #Si presiona en sí, entonces comenzamos el proceso de venta:
            if respuesta == "yes":

                #En primer lugar, creamos una variable llamada resultadoSeleccion para almacenar el resultado de la selección de marca del usuario:
                resultadoSeleccion=seleccionarMarca.get()

                #Ahora insertamos sentencia if/else, para que dependiendo de la marca del vehículo seleccionada, nos devuelva un código de marca
                #u otro. Estos códigos hacen referencia al campo CodigoMarca de la tabla Marcas de la base de datos. Se debe hacer así por que no exi-
                #ste la sentencia switch en python:
                if resultadoSeleccion=="Volswagen":
                    codigoMarca=1
                elif resultadoSeleccion=="Audi":
                    codigoMarca=2
                elif resultadoSeleccion=="Mercedes":
                    codigoMarca=3
                elif resultadoSeleccion=="Renault":
                    codigoMarca=4
                elif resultadoSeleccion=="Porche":
                    codigoMarca=5
                elif resultadoSeleccion=="Seat":
                    codigoMarca=6
                elif resultadoSeleccion=="Chevrolet":
                    codigoMarca=7
                elif resultadoSeleccion=="BMW":
                    codigoMarca=8
                elif resultadoSeleccion=="Nissan":
                    codigoMarca=9
                else:
                    codigoMarca=10

                #Posteriormente, necesitamos obtener los datos de los entrys que ha introducido el usuario. Esto lo
                #haremos con el método get()
                matricula=matriculaVehiculo.get()
                modelo=modeloVehiculo.get()
                color=colorVehiculo.get()
                precio=precioVehiculo.get()

                #previamente, creamos una función llamada borradoDatos() que eliminará los datos de los campos introducidos por el usuario:
                #para ello, usará el método delete:
                def borradoDatos():
                    matriculaVehiculo.delete(0, "end")
                    modeloVehiculo.delete(0, "end")
                    colorVehiculo.delete(0, "end")
                    precioVehiculo.delete(0, "end")


                #A continuación, revisamos si la longitud de la matrícula es igual a 10 y si todos los campos están rellenados. De no ser
                #El caso, lanzamos un mensaje de error y borramos todos los campos del formulario:
                if matricula!='' and modelo!='' and color!='' and precio!='':

                    if len(matricula)==10:

                        #Si todo está correcto, creamos un objeto llamado conexión que se encargará de abrir una conexión con la base de datos,
                        #al cual le pasamos los parámetros correspondientes:
                        conexion=BaseDatosPrincipal(self.__correoElectronico, matricula, modelo, color, precio, codigoMarca)

                        #Finalmente, ejecutamos el método registrarVenta() de la clase BaseDatosPrincipal:
                        #El método devuelve un booleano, que almacenaremos en la variable correcto:
                        correcto=conexion.registrarVenta()

                        if correcto:
                            #si todo es correcto, imprimimos un mensaje de que el vehículo se ha puesto a la venta correctamente y borramos todos los campos:
                            tkinter.messagebox.showinfo(title="Venta correcta", message="El vehículo se ha puesto a la venta de forma exitosa.")
                            borradoDatos()

                        else:
                        #si devuelve False, eliminamos todos los campos introducidos por el usuario con borradoDatos():
                            borradoDatos()
                    else:
                        #Si la longitud de la matrícula es distinta de 10, mandamos el mensaje de error correspondiente, y
                        #borramos todos los campos introducidos por el usuario con borradoDatos()
                        tkinter.messagebox.showinfo(title="Length Error", message="El campo matrícula debe de tener 10 caracteres.\nIntroduzca una matrícula diferente.")
                        borradoDatos()

                else:
                    #Si hay algún campo vacio, mandamos el mensaje de error correspondiente, y
                    #borramos todos los campos introducidos por el usuario con borradoDatos()
                    tkinter.messagebox.showinfo(title="Value Error", message="Alguno de los campos marcados con (*) se encuentra vacío")
                    borradoDatos()
        """
        17. A continuación insertamos el botón bVender, el cual ejecutará la función realizarVenta() declarada anteriormente:
        """
        bVender=ttk.Button()
        bVender = Button(self.__pestañaVentas, text="Dar de Alta", height="3", width="30", bg="white", fg="navy", font="Calibri",
                        command=realizarVenta)
        bVender.place(x =400, y = 630, width=200, height=50)