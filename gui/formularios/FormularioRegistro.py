'''
Created on 2 feb 2023

@author: marcthegamer

Esta clase servirá para gestionar la ventana de registro de cuentas de la aplicación
'''
import subprocess
import re
import os
import tkinter
from tkinter import *
from conexionBaseDatos.BaseDatosRegistro import *

class FormularioRegistro:
    
    def __init__(self, menuFormulario):
        """
        Como parámetro, recibimos la ventana anterior, es decir, la del menú del formulario. Esto con el fin de que cuando
        llamemos al método iniciarRegistro(), dicha ventana se destruya.
        """
        self.__menuFormulario=menuFormulario
    
    """
    ---iniciarRegistro(): método que inicializará la ventana de registros de nuestra aplicación.
    """
    def iniciarRegistro(self):
    
        """
        1. Inicializamos una nueva ventana con un objeto de la clase Tk():
    
        Previamente, debemos de cerrar la ventana anterior(menuFormulario) con el método destroy():
        """
        self.__menuFormulario.destroy()
        
        ventanaRegistro=Tk(className="Carholded")
        ventanaRegistro.resizable(0,0)
        ventanaRegistro.geometry("600x930")
        ventanaRegistro.title("Carholded 1.0 - Crear una nueva cuenta")
        ventanaRegistro.configure(bg="navy")
        
        """
        2. Obtenemos el directorio de trabajo con la clase os y el método os.getcwd():
        """
        directorioDeTrabajo = os.getcwd()
        
        """
        3.Insertamos la imagen que actuará de icono:
        """
        ventanaRegistro.iconphoto(False, PhotoImage(file=directorioDeTrabajo + "/imagenes/coche.png"))
        
        """
        4.Insertamos un espaciador y el primer Label de nuestro formulario. Servirá para 
        indicar al usuario que lo que esté marcado con un asterisco, es obligatorio a la hora de realizar el registro:
        """
        espaciador=Label(ventanaRegistro, text="", bg="navy")
        espaciador.pack()
        
        notaInformativa=Label(ventanaRegistro, text="Nota: los campos marcados con (*) son obligatorios.", bg="navy", fg="white", width="300", height="2", font=("Calibri", 14))
        notaInformativa.pack();
        
        """
        5. Añadimos el primer Label junto a su espaciador, que indicará al usuario que a continuación debe de introducir su nombre:
        """
        espaciador=Label(ventanaRegistro, text="", bg="navy")
        espaciador.pack()
        
        introduzcaNombre=Label(ventanaRegistro, text="Introduzca su nombre: (*)", bg="navy", fg="white", width="300", height="2", font=("Calibri", 14))
        introduzcaNombre.pack();
        
        """
        6. Añadimos el Entry correspondiente para que el usuario introduzca su nombre. Dicho nombre se almacenará en la variable nombreUsuario:
        """
        nombreUsuario=Entry(ventanaRegistro, width="40", font=("Calibri", 14))
        #metodo .place(): sirve para posicionar un control de tkinter en pantalla (ancho, alto, eje x, eje y...)
        nombreUsuario.place(x =175, y = 150, width=250, height=40) 
        
        """
        7. Añadimos un nuevo Label para indicar al usuario que en el siguiente campo debe de introducir su primer apellido
        """
        introduzcaPrimerApellido=Label(ventanaRegistro, text="Introduzca su primer apellido: (*)", bg="navy", fg="white", width="300", height="2", font=("Calibri", 14))
        introduzcaPrimerApellido.place(x =115, y = 225, width=375, height=40) 
        
        """
        8. Añadimos el Entry correspondiente para que el usuario introduzca su primer apellido. Dicho apellido se almacenará en la variable primerApellido:
        """
        primerApellido=Entry(ventanaRegistro, width="40", font=("Calibri", 14))
        primerApellido.place(x =175, y = 275, width=250, height=40) 
        
        """
        9. Añadimos un nuevo Label para indicar al usuario que en el siguiente campo debe de introducir su segundo Apellido
        """
        introduzcaSegundoApellido=Label(ventanaRegistro, text="Introduzca su segundo apellido:", bg="navy", fg="white", width="300", height="2", font=("Calibri", 14))
        introduzcaSegundoApellido.place(x =115, y = 350, width=375, height=40) 
        
        """
        10. Añadimos el Entry correspondiente para que el usuario introduzca su segundo apellido. Dicho apellido se almacenará en la variable segundoApellido:
        """
        segundoApellido=Entry(ventanaRegistro, width="40", font=("Calibri", 14))
        segundoApellido.place(x =175, y = 400, width=250, height=40) 
        
        """
        11. Añadimos otro Label, para indicar al usuario que a continuación debe de introducir su correo electrónico:
        """
        introduzcaCorreo=Label(ventanaRegistro, text="Introduzca su correo electrónico: (*)", bg="navy", fg="white", width="300", height="2", font=("Calibri", 14))
        introduzcaCorreo.place(x =118, y = 475, width=375, height=40)
        
        """
        12. Añadimos el Entry correspondiente para que el usuario introduzca su correo electrónico. 
        El correo se almacenará en la variable correoElectronico:
        """
        correoElectronico=Entry(ventanaRegistro, width="40", font=("Calibri", 14))
        correoElectronico.place(x =175, y = 525, width=250, height=40)
        
        """
        13. Añadimos el último Label, para indicar al usuario que a continuación debe de introducir su contraseña:
        """
        introduzcaContraseña=Label(ventanaRegistro, text="Introduzca su contraseña (*). \n " + 
                                   "La contraseña deberá tener al menos 5 caracteres:", bg="navy", fg="white", width="300", height="2", font=("Calibri", 14))
        introduzcaContraseña.place(x =60, y = 600, width=500, height=40)
        
        """
        14. Añadimos el Entry correspondiente para que el usuario introduzca su contraseña. 
        La contraseña se almacenará en la variable contraseña:
        """
        contraseña=Entry(ventanaRegistro, width="40", font=("Calibri", 14))
        contraseña.place(x =175, y = 660, width=250, height=40)
        
        """
        15. Declaramos el método comprobarRegistro, que, cuando se presione el botón bRegistrar realizará las siguientes acciones:
        
        -Para el nombre y el apellido, se verificará que dichos campos no se encuentren vacíos.
        
        -Para el nombre, primerApellido y SegundoApellido, pondrá en mayúsculas el primer carácter de la cadena,
        lo haya introducido el usuario o no.
        
        -Para el campo correo electrónico, comprobará si la cadena contiene el siguiente símbolo: "@"
        
        -Para el campo contraseña, verificará que la misma contenga más de 5 caracteres
        
        -Una vez comprobado lo anterior, enviará los datos a la clase BaseDatosRegistro:
        """
        def comprobarRegistro():
            
            #comprobamos si los campos nombreUsuario y primerApellido están vacíos. Nota: para obtener los campos del formulario,
            #usaremos el método get(). :
            if nombreUsuario.get()!="" and primerApellido.get()!="":
                
                #Establecemos el primer carácter de los campos nombre, primer apellido y segundo apellido en mayúsculas con capitalize()
                #y los almacenamos en otra variable.
                nombreUsuarioMayusculas=nombreUsuario.get().capitalize()
                primerApellidoMayusculas=primerApellido.get().capitalize()
                segundoApellidoMayusculas=segundoApellido.get().capitalize()
                
                #Comprobamos si el correo electrónico del usuario contiene el símbolo "@":
                if "@" in correoElectronico.get():
                
                    #Comprobamos si la contraseña tiene una longitud mayor o igual a 5 con el método len():
                    if len(contraseña.get())>=5:
                    
                        #Si todo es correcto, instanciamos un objeto de la clase BaseDatosRegistro, y le pasamos los datos 
                        #validados como parámetro:
                        conexion = BaseDatosRegistro(nombreUsuarioMayusculas, primerApellidoMayusculas, 
                                                     segundoApellidoMayusculas, correoElectronico.get(), contraseña.get())
                        
                        #El método conexionBaseDatosRegistro, devuelve true si el registro ha sido exitoso. En caso contrario, 
                        #devuelve false y un mensaje de error. Si devuelve true, simplemente cerraremos la ventana. Si devuelve
                        #false, borraremos lo que haya escrito en todos los campos. EL booleano resultante lo almacenaremos en la
                        #variable (correcto):
                        correcto=conexion.conexionBaseDatosRegistro()
                        
                        if correcto:
                            ventanaRegistro.destroy()
                        else:
                            nombreUsuario.delete(0, "end")
                            primerApellido.delete(0, "end")
                            segundoApellido.delete(0, "end")
                            correoElectronico.delete(0, "end")
                            contraseña.delete(0, "end")
                    
                    
                    else:
                        #Si la contraseña es demasiado corta, enviamos un mensaje de error al usuario con showinfo():
                        tkinter.messagebox.showinfo(title="Contraseña no válida", 
                                                    message="¡Su contraseña debe de tener al menos 5 caracteres!.")
                        #ejecutamos el método delete() de tkinter para limpiar los datos que el usuario había introducido erróneamente.
                        nombreUsuario.delete(0, "end")
                        primerApellido.delete(0, "end")
                        segundoApellido.delete(0, "end")
                        correoElectronico.delete(0, "end")
                        contraseña.delete(0, "end")
        
                else:
                    #Si el correo no es válido, enviamos un mensaje de error al usuario con showinfo():
                    tkinter.messagebox.showinfo(title="Correo no válido", 
                                                message="Por favor, introduzca un correo válido.")
                    #ejecutamos el método delete() de tkinter para limpiar los datos que el usuario había introducido erróneamente.
                    nombreUsuario.delete(0, "end")
                    primerApellido.delete(0, "end")
                    segundoApellido.delete(0, "end")
                    correoElectronico.delete(0, "end")
                    contraseña.delete(0, "end")
            else:
                #Si algúno de los campos nombreUsuario o primerApellido están vacíos, entonces lanzamos mensaje de error con showinfo():
                tkinter.messagebox.showinfo(title="Nombre y/o Primer Apellido no válidos", 
                                            message="Por favor, introduzca correctamente su nombre y/o primer apellido")
                #ejecutamos el método delete() de tkinter para limpiar los datos que el usuario había introducido erróneamente.
                nombreUsuario.delete(0, "end")
                primerApellido.delete(0, "end")
                segundoApellido.delete(0, "end")
                correoElectronico.delete(0, "end")
                contraseña.delete(0, "end")
                
        """
        16. Añadimos un Button, que ejecutará el método anteriormente declarado (comprobarRegistro()):
        """
        bRegistrar = Button(text="Registrarse", height="3", width="30", bg="white", fg="navy", font="Calibri", command=comprobarRegistro)
        bRegistrar.place(x =100, y = 750, width=400, height=60)

        """
        17. Añadimos un botón que dará la opción al usuario de volver atrás:
        """

        # Primero definimos un método que nos permitirá volver atrás:
        def volverAtras():

            # Destruimos la ventana actual, es decir, ventanaRegistro.
            ventanaRegistro.destroy()

            # Con la clase subprocess y el método call, llamamos a un proceso de python. Esto lo hacemos para volver a ejecutar la ventana principal del programa:
            subprocess.call(["python", directorioDeTrabajo + "/Main.py"])

        # A continuación, declaramos el botón que nos permitirá llevar a cabo la acción del método:
        bVolverAtras = Button(ventanaRegistro, text="Volver atrás", height="3", width="30", bg="white", fg="navy",
                              font="Calibri", command=volverAtras)
        bVolverAtras.place(x=100, y=820, width=400, height=60)

        """
        18. Finalmente, con el método mainloop() indicamos a la interfaz que se quede esperando a que el 
        usuario realice algún evento.
        """
        ventanaRegistro.mainloop()
        