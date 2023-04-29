'''
Created on 2 feb 2023

@author: marcthegamer

Esta clase servirá para gestionar la ventana de borrado de cuentas de la aplicación
'''
import os
import tkinter
from tkinter import *
from conexionBaseDatos.BaseDatosEliminacion import *


class FormularioBorrado:
    
    def __init__(self, menuFormulario):
        """
        Como parámetro, recibimos la ventana anterior, es decir, la del menú del formulario. Esto con el fin de que cuando
        llamemos al método iniciarEliminacion(), dicha ventana se destruya.
        """
        self.__menuFormulario=menuFormulario
    
    """
    ---iniciarEliminacion(): método que inicializará la ventana de borrado de cuentas en nuestra aplicación.
    """
    def iniciarEliminacion(self):
    
        """
        1. Inicializamos una nueva ventana con un objeto de la clase Tk():
    
        Previamente, debemos de cerrar la ventana anterior(menuFormulario) con el método destroy():
        """
        self.__menuFormulario.destroy()
        
        ventanaBorrado=Tk(className="Carholded")
        ventanaBorrado.resizable(0,0)
        ventanaBorrado.geometry("500x400")
        ventanaBorrado.title("Carholded 1.0 - Eliminar Cuenta")
        ventanaBorrado.configure(bg="navy")
        
        """
        2. Obtenemos el directorio de trabajo con la clase os y el método os.getcwd():
        """
        directorioDeTrabajo = os.getcwd()
        
        """
        3.Insertamos la imagen que actuará de icono:
        """
        ventanaBorrado.iconphoto(False, PhotoImage(file=directorioDeTrabajo + "/imagenes/coche.png"))
        
        """
        4. A continuación, insertamos el primer texto del formulario con su correspondiente espaciador,
        que le indicará al usuario que en el siguiente campo debe de introducir su correo electronico. Esto lo haremos
        con un label de tkinter:
        """
        espaciador=Label(ventanaBorrado, text="", bg="navy")
        espaciador.pack()
        
        introduzcaCorreo=Label(ventanaBorrado, text="Introduzca su Correo para borrar su cuenta:", bg="navy", fg="white", width="300", height="2", font=("Calibri", 14))
        introduzcaCorreo.pack();
        
        '''
        5. Insertamos una nueva entrada de texto, en la que el usuario podrá escribir su correo con
        la clase Entry de tkinter. Todo lo que introduzca el usuario, se almacenará en una variable llamada correoUsuario
        , la cual utilizaremos más adelante:
        '''
        correoUsuario=Entry(ventanaBorrado, width="40", font=("Calibri", 14))
        #metodo .place(): sirve para posicionar un control de tkinter en pantalla (ancho, alto, eje x, eje y...)
        correoUsuario.place(x =125, y = 75, width=250, height=40) 
        
        """
        6. añadimos un nuevo espaciador y otro label, que indicará al usuario que en el siguiente campo introduzca su 
        contraseña:
        """
        espaciador=Label(ventanaBorrado, text="", bg="navy")
        espaciador.place(x=125, y = 120, width=100, height=40)
        
        introduzcaContraseña=Label(ventanaBorrado, text="Introduzca su Contraseña:", bg="navy", fg="white", width="300", height="2", font=("Calibri", 14))
        introduzcaContraseña.place(x=100, y = 150, width=300, height=40);
        
        '''
        7. Insertamos otra entrada de texto, en la que el usuario podrá escribir su contraseña. Todo lo que introduzca
         el usuario, se almacenará en una variable llamada contraseñaUsuario, la cual utilizaremos más adelante. Ademas,
         añadimos el parámetro show="*", por lo que lo que introduzca el usuario estará oculto, por seguridad:
        '''
        contraseñaUsuario=Entry(ventanaBorrado, width="40", font=("Calibri", 14), show="*")
        #metodo .place(): sirve para posicionar un control de tkinter en pantalla (ancho, alto, eje x, eje y...)
        contraseñaUsuario.place(x =125, y = 200, width=250, height=40) 
        
        """
        8. Antes de crear el botón de borrado, definimos la función que recogerá los datos que introduzca el usuario al 
        presionarlo. Dicha función se llamará borrado()
        """
        def borrado():
            
            """
            Definimos un nuevo objeto de la clase BaseDatosEliminacion y le pasamos los datos correo y contraseña recopilados
            en el formulario. Los datos introducidos en los Entry los recopilamos con el método .get():
            """
            correo=correoUsuario.get()
            contraseña=contraseñaUsuario.get()
            conexion=BaseDatosEliminacion(correo, contraseña)
            
            """
            A continuación, ejecutamos el método conexionBaseDatosEliminacion(), que ejecutará una validación de datos del usuario. Si
            es correcto, devuelve True y un mensaje que dice que se ha completado con éxito el borrado de datos. Si no lo es, devuelve False y
            otro mensaje diciendo que el usuario no ha sido eliminado. Dicho booleano lo almacenaremos en la variable correcto
            """
            correcto=conexion.conexionBaseDatosEliminacion()
            
            if correcto:
                #si todo ha ido bien, destruimos la ventana actual
                ventanaBorrado.destroy()
            else:
                #si la baja no se ha realizado correctamente, eliminamos todos los campos del formulario para que el usuario lo
                #vuelva a intentar. Esto lo haremos con el método delete()
                correoUsuario.delete(0, "end")
                contraseñaUsuario.delete(0, "end")
                
        """
        9. Añadimos un botón, que realizará una consulta a la base de datos en base al método borrado():
        """
        bLogin = Button(ventanaBorrado, text="Borrar Cuenta", height="3", width="30", bg="white", fg="navy", font="Calibri", 
                        command=borrado)
        bLogin.place(x =150, y = 270, width=200, height=50)
        
        """
        10. Finalmente, con el método mainloop() indicamos a la interfaz que se quede esperando a que el 
        usuario realice algún evento.
        """
        ventanaBorrado.mainloop()
