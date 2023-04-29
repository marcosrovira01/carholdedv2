'''
Created on 2 feb 2023

@author: marcthegamer

Esta clase servirá para gestionar la ventana Login de la aplicación.
'''
import subprocess
import os
import tkinter
from tkinter import *
from conexionBaseDatos.BaseDatosLogin import *
from gui.aplicacionPrincipal.VentanaPrincipal import *


class FormularioLogin:
    
    def __init__(self, menuFormulario):
        """
        Como parámetro, recibimos la ventana anterior, es decir, la del menú del formulario. Esto con el fin de que cuando
        llamemos al método iniciarLogin(), dicha ventana se destruya.
        """
        self.__menuFormulario=menuFormulario
    
    """
    ---iniciarLogin(): método que inicializará la ventana Login en nuestra aplicación.
    """
    def iniciarLogin(self):
    
        """
        1. Inicializamos una nueva ventana con un objeto de la clase Tk():
    
        Previamente, debemos de cerrar la ventana anterior(menuFormulario) con el método destroy():
        """
        self.__menuFormulario.destroy()
        
        ventanaLogin=Tk(className="Carholded")
        ventanaLogin.resizable(0,0)
        ventanaLogin.geometry("500x430")
        ventanaLogin.title("Carholded 1.0 - Login")
        ventanaLogin.configure(bg="navy")
        
        """
        2. Obtenemos el directorio de trabajo con la clase os y el método os.getcwd():
        """
        directorioDeTrabajo = os.getcwd()
        
        """
        3.Insertamos la imagen que actuará de icono:
        """
        ventanaLogin.iconphoto(False, PhotoImage(file=directorioDeTrabajo + "/imagenes/coche.png"))
        
        """
        4. A continuación, insertamos el primer texto del formulario con su correspondiente espaciador,
        que le indicará al usuario que en el siguiente campo debe de introducir su correo electronico. Esto lo haremos
        con un label de tkinter:
        """
        espaciador=Label(ventanaLogin, text="", bg="navy")
        espaciador.pack()
        
        introduzcaCorreo=Label(ventanaLogin, text="Introduzca su Correo Electrónico:", bg="navy", fg="white", width="300", height="2", font=("Calibri", 14))
        introduzcaCorreo.pack();
        
        '''
        5. Insertamos una nueva entrada de texto, en la que el usuario podrá escribir su correo con
        la clase Entry de tkinter. Todo lo que introduzca el usuario, se almacenará en una variable llamada correoUsuario
        , la cual utilizaremos más adelante:
        '''
        correoUsuario=Entry(ventanaLogin, width="40", font=("Calibri", 14))
        #metodo .place(): sirve para posicionar un control de tkinter en pantalla (ancho, alto, eje x, eje y...)
        correoUsuario.place(x =125, y = 75, width=250, height=40) 
        
        """
        6. añadimos un nuevo espaciador y otro label, que indicará al usuario que en el siguiente campo introduzca su 
        contraseña:
        """
        espaciador=Label(ventanaLogin, text="", bg="navy")
        espaciador.place(x=125, y = 120, width=100, height=40)
        
        introduzcaContraseña=Label(ventanaLogin, text="Introduzca su Contraseña:", bg="navy", fg="white", width="300", height="2", font=("Calibri", 14))
        introduzcaContraseña.place(x=100, y = 150, width=300, height=40);
        
        '''
        7. Insertamos otra entrada de texto, en la que el usuario podrá escribir su contraseña. Todo lo que introduzca
         el usuario, se almacenará en una variable llamada contraseñaUsuario, la cual utilizaremos más adelante. Ademas,
         añadimos el parámetro show="*", por lo que lo que introduzca el usuario estará oculto, por seguridad:
        '''
        contraseñaUsuario=Entry(ventanaLogin, width="40", font=("Calibri", 14), show="*")
        #metodo .place(): sirve para posicionar un control de tkinter en pantalla (ancho, alto, eje x, eje y...)
        contraseñaUsuario.place(x =125, y = 200, width=250, height=40) 
        
        """
        8. Antes de crear el botón de login, definimos la función que recogerá los datos que introduzca el usuario al 
        presionarlo. Dicha función se llamará login()
        """
        def login():
            
            """
            Definimos un nuevo objeto de la clase BaseDatosLogin y le pasamos los datos correo y contraseña recopilados
            en el formulario. Los datos introducidos en los Entry los recopilamos con el método .get():
            """
            correo=correoUsuario.get()
            contraseña=contraseñaUsuario.get()
            conexion=BaseDatosLogin(correo, contraseña)
            
            """
            A continuación, ejecutamos el método conexionBaseDatosLogin, que ejecutará una validación de datos del usuario. Si
            es correcto, devuelve true, y si no. El booleano que devuelva lo almacenamos en la variable validacionCorrecta
            """
            validacionCorrecta=conexion.conexionBaseDatosLogin()
            
            """
            Si la validación es correcta, creamos un nuevo objeto de la clase "VentanaPrincipal", pasandole los parámetros (correoElectronico)
            y (ventanaAnterior). Le pasamos la ventana anterior para que cuando se ejecute el método abrirVentanaPrincipal() se elimine dicha
            ventana y se mate el proceso. En este caso la ventana anterior sería la de logueo, es decir, (ventanaLogin). El objeto instanciado
            se denominará "nuevaVentana"
            """
            if validacionCorrecta:
                nuevaVentana=VentanaPrincipal(correo, ventanaLogin)
                nuevaVentana.abrirVentanaPrincipal()
            else:
                """
                Si la validación no es correcta, borramos los datos de los Entrys que había rellenado el usuario previamente:
                """
                correoUsuario.delete(0, "end")
                contraseñaUsuario.delete(0, "end")
        """
        9. Añadimos un botón, que realizará una consulta a la base de datos en base al método login():
        """
        bLogin = Button(ventanaLogin, text="Iniciar Sesión", height="3", width="30", bg="white", fg="navy", font="Calibri", 
                        command=login)
        bLogin.place(x =150, y = 270, width=200, height=50)

        """
        10. Añadimos un botón que dará la opción al usuario de volver atrás:
        """
        #Primero definimos un método que nos permitirá volver atrás:
        def volverAtras():

            #Destruimos la ventana actual, es decir, ventanaLogin.
            ventanaLogin.destroy()

            #Con la clase subprocess y el método call, llamamos a un proceso de python. Esto lo hacemos para volver a ejecutar la ventana principal del programa:
            subprocess.call(["python", directorioDeTrabajo + "/Main.py"])

        #A continuación, declaramos el botón que nos permitirá llevar a cabo la acción del método:
        bVolverAtras=Button(ventanaLogin, text="Volver atrás", height="3", width="30", bg="white", fg="navy", font="Calibri", command=volverAtras)
        bVolverAtras.place(x=150, y=330, width=200, height=50)
        
        """
        11. Finalmente, con el método mainloop() indicamos a la interfaz que se quede esperando a que el 
        usuario realice algún evento.
        """
        ventanaLogin.mainloop()
        