"""
@author: marcthegamer

Esta clase gestionará la ventana principal de la aplicación.
En el constructor entrarán como parámetros el correo del usuario, para poder
cargar sus datos en la aplicación, y la ventana anterior(ventanaLogin), para poder
cerrarla correctamente con el método destroy().
"""

import os
import tkinter
from tkinter import *
from tkinter import ttk
from gui.aplicacionPrincipal.ThreadUsuarios import *
from gui.aplicacionPrincipal.ThreadCompras import *
from gui.aplicacionPrincipal.ThreadVentas import *
import threading


class VentanaPrincipal:
    
    """
    Constructor de la clase VentanaPrincipal:
    """

    def __init__(self, correoElectronico, ventanaAnterior):
        
        """
        Parseamos a string la variable correoElectronico para evitar conflictos con la base de datos.
        """
        self.__correoElectronico=str(correoElectronico)
        self.__ventanaAnterior=ventanaAnterior
        
    
    """
    método que lanzará la ventana principal de la aplicación.
    """
    def abrirVentanaPrincipal(self):
        """
        1. Inicializamos una ventana. Para ello usaremos los siguientes métodos:
    
        -resizable()
        -geometry()
        -title()
    
        La variable con la que iniciamos la ventana será una variable global. Previamente, debemos de destruir la
        ventana anterior que pasa como parámetro con el método destroy()
        """
        self.__ventanaAnterior.destroy()
        
        global menuPrincipal
        
        menuPrincipal= Tk(className="Carholded");
        menuPrincipal.resizable(0,0)
        menuPrincipal.geometry("1000x900")
        menuPrincipal.title("Carholded 1.0")

        # El código a continuación, simplemente se encarga de centrar la ventana actual del programa:
        menuPrincipal.update_idletasks()
        ancho = menuPrincipal.winfo_width()
        alto = menuPrincipal.winfo_height()
        x = (menuPrincipal.winfo_screenwidth() // 2) - (ancho // 2)
        y = (menuPrincipal.winfo_screenheight() // 2) - (alto // 2)
        menuPrincipal.geometry('{}x{}+{}+{}'.format(ancho, alto, x, y))
        
        """
        2. Para obtener el directorio de trabajo, ejecutamos la clase os con el método getcwd():
        """
        directorioDeTrabajo = os.getcwd()
        
        """
        3.Insertamos la imagen que actuará de icono con el método iconphoto(boolean, PhotoImage):
        
        -En la clase PhotoImage, debemos especificar dónde se encuentra dicha imagen, que deberá
        estar en formato .png. Para ello, concatenamos el directorio de trabajo con la carpeta en 
        donde se encuentra nuestra imagen. En este caso, en /imagenes/coche.png.
        """
        menuPrincipal.iconphoto(False, PhotoImage(file=directorioDeTrabajo + "/imagenes/coche.png"))
        
        """
        4. A continuación, Insertamos 3 pestañas, que serán las 3 pestañas principales de nuestra aplicación: 
        Ventana Usuarios, Ventana Compras y Ventana Ventas:
        """
        #1. Insertamos el panel para las pestañas con la clase Notebook, pasandole como parámetro la ventana actual,
        #y lo posicionamos con el método pack:
        panelPrincipal=ttk.Notebook(menuPrincipal)
        panelPrincipal.pack(fill='both', expand='yes')
        
        #2. Con la clase ttk.Style, creamos unos estilos específicos para los frames que se localizan en cada ventana.
        #En este caso, a los estilos les llamamos ""Estilos.TFrame" y los configuramos para que establezcan como color
        #de fondo el color "navy" con el método configure():
        estilosFrame=ttk.Style()
        estilosFrame.configure('Estilos.TFrame', background='navy')
        
        #3. Incluimos la primera pestaña y le añadimos los estilos previamente creados en el parámetro "style":
        pestañaUsuarios=ttk.Frame(panelPrincipal, style='Estilos.TFrame')
        panelPrincipal.add(pestañaUsuarios, text='Usuarios')
        
        #4. Incluímos la segunda pestaña y le añadimos los estilos previamente creados en el parámetro "style":
        pestañaCompras=ttk.Frame(panelPrincipal, style='Estilos.TFrame')
        panelPrincipal.add(pestañaCompras, text='Compras')
        
        #5. Incluímos la tercera pestaña y le añadimos los estilos previamente creados en el parámetro "style":
        pestañaVentas=ttk.Frame(panelPrincipal, style='Estilos.TFrame')
        panelPrincipal.add(pestañaVentas, text='Ventas')
        
        """
        5. Generamos estilos para los títulos de las pestañas con la clase
        ttk.Style() y el método configure():
        """
        #estilos para cuando la pestaña no esté activa
        estilosGenerales=ttk.Style()
        estilosGenerales.configure('TNotebook.Tab', font='Calibri 14', background='#f1f1f0', foreground='black')
        
        #estilos para cuando la pestaña se encuentre activa
        estilosGenerales.map('TNotebook.Tab', background=[('selected', 'navy')], foreground=[('selected', 'white')])
        
        """
        6. Creamos 3 hilos, para que las ventanas se ejecuten de forma simultánea y los lanzamos: 
        """
        #1. Primero creamos una lista o array, que contendrá los 3 hilos:
        threads=[]
        
        #2. Creamos el primer hilo, el hilo usuarios, de la clase ThreadUsuarios.
        #Para que sea un hilo, debemos de usar la clase threading y el método Thread().
        #A dicho método, le entra un parámetro llamado target, en el que deberemos de 
        #indicar una función de otra clase para que dicha función sea un hilo. En este caso,
        #usamos la función iniciarThreadUsuarios() de la clase ThreadUsuarios:
        usuarios=ThreadUsuarios(pestañaUsuarios, self.__correoElectronico, menuPrincipal)
        t1=threading.Thread(target=usuarios.iniciarThreadUsuarios())
        
        #3. Creamos el segundo hilo, el hilo compras, de la clase ThreadCompras:
        compras=ThreadCompras(pestañaCompras, self.__correoElectronico)
        t2=threading.Thread(target=compras.iniciarThreadCompras())
        
        #4. Creamos el tercer hilo, el hilo ventas, de la clase ThreadVentas:
        ventas=ThreadVentas(pestañaVentas, self.__correoElectronico)
        t3=threading.Thread(target=ventas.iniciarThreadVentas())
        
        #5. A continuación, agregamos los hilos recién creados al array de hilos(threads) con
        #el método append():
        threads.append(t1)
        threads.append(t2)
        threads.append(t3)
        
        #6. Vamos recorriendo el array de hilos, e iniciamos los 3 hilos de forma simultánea
        #con el método start():
        for thread in threads:
            thread.start()
            
        #7. Esperamos a que todos los hilos terminen para un correcto funcionamiento del programa
        #con el método join():
        for thread in threads:
            thread.join()
       
        """
        7. Esperamos a que el usuario realice alguna acción con el método mainloop()
        """
        menuPrincipal.mainloop()