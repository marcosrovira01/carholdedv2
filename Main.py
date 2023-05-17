# This Python file uses the following encoding: utf-8

import os
import tkinter
from tkinter import *
from gui.formularios.FormularioLogin import *
from gui.formularios.FormularioRegistro import *
from gui.formularios.FormularioBorrado import *

'''
Created on 31 ene 2023

@author: marcthegamer
@version: 2.0

Esta clase será nuestra clase principal, que inicializará la primera ventana de nuestro formulario con la función
menuPrincipal(), en la que podremos escoger entre 3 opciones, iniciar sesión, registrarse, o eliminar cuenta.

Cuando seleccionemos una de las 3 opciones, se ejecutará uno de los siguientes
metodos: (iniciarLogin(), iniciarRegistro() e iniciarEliminacion()) de sus clases correspondientes: (
FormularioLogin, FormularioRegistro y FormularioBorrado).

'''
class Main:

    '''
    ---Declaramos la función menuPrincipal
    '''
    @staticmethod
    def menuPrincipal():

        """
        1. Primero inicializaremos una ventana. Para ello usaremos los siguientes métodos:

        -resizable(): si le pasamos 0, 0 como parámetro, evita que el usuario pueda maximizar la ventana.
        -geometry(): para establecer un tamaño de la ventana
        -title(): para establecer un título en el banner de la ventana
        -configure(): para configurar la ventana y darle un color de fondo

        inicializamos la ventana con un objeto de la clase Tk(). Este objeto
        será global, por lo que lo podremos usar en cualquier parte de nuestro
        código:
        """

        global menuFormulario

        menuFormulario= Tk(className="Carholded");
        menuFormulario.resizable(0,0)
        menuFormulario.geometry("500x600")
        menuFormulario.title("Carholded 1.0")
        menuFormulario.configure(bg="navy")

        #El código a continuación, simplemente se encarga de centrar la ventana actual del programa:
        menuFormulario.update_idletasks()
        ancho = menuFormulario.winfo_width()
        alto = menuFormulario.winfo_height()
        x = (menuFormulario.winfo_screenwidth() // 2) - (ancho // 2)
        y = (menuFormulario.winfo_screenheight() // 2) - (alto // 2)
        menuFormulario.geometry('{}x{}+{}+{}'.format(ancho, alto, x, y))

        """
        2. Necesitamos conocer el directorio de trabajo para que la aplicación se ejecute en cualquier
        entorno. Para ello, usamos la clase os y el método getcwd(), que nos devuelve el directorio de 
        trabajo.
        """
        directorioDeTrabajo = os.getcwd()

        """
        3.Insertamos la imagen que actuará de icono con el método iconphoto(boolean, PhotoImage):
        
        -En la clase PhotoImage, debemos especificar dónde se encuentra dicha imagen, que deberá
        estar en formato .png. Para ello, concatenamos el directorio de trabajo con la carpeta en 
        donde se encuentra nuestra imagen. En este caso, en /imagenes/coche.png.
        """
        imagen_coche = PhotoImage(file=directorioDeTrabajo + "/imagenes/coche.png")
        menuFormulario.iconphoto(False, imagen_coche)

        """
        4. Creamos una imagen con la clase PhotoImage, y la redimensionamos
        con el método subsample(escala x, escala y). Posteriormente, la introducimos en el label
        y la insertamos en el menuFormulario con el método pack()
        """
        imagenMenu=PhotoImage(file=directorioDeTrabajo + "/imagenes/coche.png")
        imagenMenu=imagenMenu.subsample(2,2)
        Label(image=imagenMenu, bg="navy").pack()

        """
        5. Insertamos otro label para la bienvenida, e indicarle al usuario que seleccione una opción
        """
        bienvenida=Label(text="¡Bienvenido!, selecciona una opción:", bg="navy", fg="white", width="300", height="3", font=("Calibri", 15))
        bienvenida.pack();

        """
        6. Insertamos un espaciador en el programa, con el mismo color de fondo que la ventana, para que
        parezca que no existe, pero que sin embargo se encargará de separar diferentes widgets.
        """
        espaciador=Label(text="", bg="navy")
        espaciador.pack()

        """
        7. Definimos 3 botones con la clase Button(), que ejecutarán las siguientes acciones:
        
        -Iniciar Sesion: nos abrirá el formulario de inicio de sesión y cerrará el menú.
        -Registrarse: nos abrirá el formulario de registro y cerrará el menú.
        -Eliminar cuenta: nos abrirá otro formulario para eliminar nuestra cuenta y cerrará el menú.
        
        Además, añadiremos sus correspondientes espaciadores:
        """

        #Utilizaremos el método iniciarLogin() para este boton, además, cuando lo presionemos la ventana actual se cerrará.
        #Para poder usar dicho método, que se encuentra en la clase FormularioLogin, debemos de crear una instancia de la misma,
        #pasandole como parámetro la ventana actual, en este caso, la ventana menuFormulario. La instancia se llamará formularioLogueo:
        formularioLogueo=FormularioLogin(menuFormulario)

        bIniciarSesion = Button(text="Iniciar Sesión", height="3", width="30", bg="white", fg="navy", font="Calibri",
                        command=formularioLogueo.iniciarLogin)
        bIniciarSesion.pack()

        #primer espaciador
        espaciador=Label(text="", bg="navy")
        espaciador.pack()

        #Utilizaremos el método iniciarRegistro() de la clase FormularioRegistro para este boton, además, cuando lo presionemos la ventana
        #actual se cerrará. Para ello instanciaremos un objeto de dicha clase llamado formularioRegistro, y le pasamos la ventana actual como
        #parámetro:
        formularioRegistro=FormularioRegistro(menuFormulario)

        bRegistrarse = Button(text="Registrarse", height="3", width="30", bg="white", fg="navy", font="Calibri",
                          command=formularioRegistro.iniciarRegistro)
        bRegistrarse.pack()

        #segundo espaciador
        espaciador=Label(text="", bg="navy")
        espaciador.pack()

        #Utilizaremos el método iniciarEliminacion() de la clase FormularioBorrado para este boton, además, cuando lo presionemos la ventana
        #actual se cerrará. Para ello instanciaremos un objeto de dicha clase llamado formularioBorrado y le pasamos la ventana actual como
        #parámetro:

        formularioBorrado=FormularioBorrado(menuFormulario)
        bEliminarCuenta = Button(text="Eliminar Cuenta", height="3", width="30", bg="white", fg="navy", font="Calibri",
                             command=formularioBorrado.iniciarEliminacion)
        bEliminarCuenta.pack()

        """
        8. Con el método mainloop() indicamos a la interfaz que se quede esperando a que el 
        usuario realice algún evento.
        """
        menuFormulario.mainloop()

"""
---Finalmente, ejecutamos la aplicacion:
"""
Main.menuPrincipal()
