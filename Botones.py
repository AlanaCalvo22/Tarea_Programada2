#from this import s
from tkinter import *
from CargarBDpaises import *
from adopcion import *


class VentanaPrincipal:
    def __init__(self, master):
        #Colores 
        blanco="#ffffff"
        negro="#000000"
        
        self.master = master
        
        self.canvas = Canvas(self.master, width=500, height=500, bg=blanco)
        self.canvas.pack()
        
        self.etiqueta=Label(self.canvas, text="Adoptemos a un adulto mayor",width=32, font= "Arial 14")
        self.etiqueta.grid(row=0,column=1,padx=80, pady=10)
        self.boton1=Button(self.canvas, text="Cargar BD de países",width=50,height=1, bg= negro, fg= blanco, command=self.cargar_paises)
        self.boton1.grid(row=1,column=1,padx=10, pady=10)
        self.boton2= Button(self.canvas, text="Insertar un participante",width=50,height=1, bg= negro, fg= blanco, command=self.cargar_registrar, state="disabled")
        self.boton2.grid(row=2,column=1,padx=10, pady=10)
        self.boton3= Button(self.canvas, text="Insertar n participantes",width=50,height=1, bg= negro, fg= blanco,state="disabled")
        self.boton3.grid(row=3,column=1,padx=10, pady=10)
        self.boton4= Button(self.canvas, text="Enlazar con abuelos",width=50,height=1, bg= negro, fg= blanco,state="disabled")
        self.boton4.grid(row=4,column=1,padx=10, pady=10)
        self.boton5= Button(self.canvas, text="Dar de baja",width=50,height=1, bg= negro, fg= blanco,state="disabled")
        self.boton5.grid(row=5,column=1,padx=10, pady=10)
        self.boton6= Button(self.canvas, text="Escribe una carta a su correo",width=50,height=1, bg= negro, fg= blanco,state="disabled")
        self.boton6.grid(row=6,column=1,padx=10, pady=10)
        self.boton7= Button(self.canvas, text="Reportes",width=50,height=1, bg= negro, fg= blanco,state="disabled")
        self.boton7.grid(row=7,column=1,padx=10, pady=10)
        self.boton8= Button(self.canvas, text="Salir",width=50,height=1,bg= negro, fg= blanco)
        self.boton8.grid(row=8,column=1,padx=10, pady=10)

    def cargar_paises(self):
        self.boton1.config(state='disabled')
        self.boton2.config(state='normal')
        self.boton3.config(state='normal')
        self.boton4.config(state='normal')
        self.boton5.config(state='normal')
        self.boton6.config(state='normal')
        self.boton7.config(state='normal')
        cargarBDpaíses('regionPais1.txt')

    def cargar_registrar(self):
        self.canvas.destroy()
        ventanaRegistrar(self.master)

ventana = Tk()
ventana.geometry("500x500")
ventana.title('Proyecto')
ventanaprin = VentanaPrincipal(ventana)
ventana.mainloop()
#No se como hacer las separaciones entre los botones
#no se como activar y desactivar los botones
