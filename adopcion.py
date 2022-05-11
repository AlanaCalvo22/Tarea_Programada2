#Elaborado por: Aarón Ortiz, Alana Calvo
#Fecha de creación: 07/05/2022 16:58
#Fecha de creación: 08/05/2022 23:16
#version: 3.10.0
#Importaciones
import re
from tkinter import *
from funciones import *
from tkinter import messagebox
import random
#Diccionario de prueba
region={"AN":["Costa Rica", "Guatemala", "Honduras", "Nicaragua", "Salvado"], "EW": ["España", "Francia", "Inglaterra"]}
adultoEnla={}
participantes={}
#Funciones reutilizadas.
def esBisiesto(año):
    """
    Funcionamiento: Analiza si un año es bisiesto o no.
    Entrada: a(int)Recibe el año a analizar.
    Salida: True/False si corresponde a un año bisiesto o no.
    """
    if año % 4 == 0:
        if año % 100 == 0:
            if año % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
#Validación de entrada.
def registrarAux():
    fecha=entradaFecha.get()
    partici=tipoOpc.get()
    nombre=entradanombre.get()
    ident=entradaIdenti.get()
    hobbies=entradaHob.get()
    profesion=entradaPrOf.get()
    corrElec=entradaCoElectr.get()
    pais=entradaPais.get()
    estado=entradaEst.get()
    descrip=entradaDes.get()
    if re.match("^\d{2}\/{1}\d{2}\/{1}\d{4}$", fecha):
        if re.match("[a-zñA-ZÑ\u00C0-\u017F]", nombre):
            if re.match("^(am|v){1}\d{4}$", ident):
                if re.match("^[1-3]$", hobbies):
                    if re.match("^[a-z]+\@(gmail.com){1}$", corrElec):
                        return registrarVol(fecha, ident, partici, nombre, hobbies, profesion, corrElec, pais, estado, descrip, participantes, adultoEnla)
                    return messagebox.showwarning("Error", "Tienes que introducir un correo con el formato: aapellido@gmail.com")
                return messagebox.showwarning("Error", "Tienes que introducir un número entre 1 a 3")
            return messagebox.showwarning("Error", "Tienes que introducir un código correcto como: av0000 o v0000")
        return messagebox.showwarning("Error", "Tienes que introducir un nombre con dos apellidos.")
    return messagebox.showwarning("Error", "Tienes que introducir una fecha correcta como: 01/02/2002")
"""
def validarFecha(evento):
    
    Funcionamiento: Valida la fecha.
    Entrada: fecha(str): Fecha indica por el usuario.
    Salida: Si es un adulto mayor, o voluntario o si no cumple con los requisitos para participar.
    
    dia30 = ["04", "06", "09", "11"]
    vali = False
    self.entradaIdenti.config(state="normal")
    self.entradaIdenti.delete(0,END)
    self.entradaPrOf.config(state="normal")
    self.entradaPrOf.delete(0, END)
    self.entradaEst.config(state="normal")
    self.entradaEst.delete(0, END)
    self.fecha=entradaFecha.get()
    if re.match("^\d{2}\/{1}\d{2}\/{1}\d{4}$",fecha):
        fecha=fecha.split("/")
        if fecha[1]=="02":
            if esBisiesto(int(fecha[2]))==True:
                if re.match("[01-29]",fecha[0]):
                    vali=True
            else:
                if re.match("[01-28]", fecha[0]):
                    vali=True
        elif fecha[1] in dia30:
            if re.match("[01-30]", fecha[0]):
                vali = True
        else:
            if re.match("[01-31]", fecha[0]):
                vali = True
    if vali==True:
        if 2022-int(fecha[2])>17 and 2022-int(fecha[2])<25:
            self.opcionVol.config(state="normal")
            self.opcionVol.select()
            self.opcionAdMy.config(state="disabled")
            self.entradaPrOf.insert(0,str(random.randint(0,1))+", "+str(random.randint(0,50)))
            self.sentradaPrOf.config(state="disabled")
            self.sentradaEst.insert(0,"Activo")
            self.entradaEst.config(state="disabled")
            while True:
                codigo = "v" + str(random.randint(1000, 9999))
                if codigo not in participantes:
                    self.entradaIdenti.insert(0,codigo)
                    self.sentradaIdenti.config(state="disabled")
                    return ""
        elif 2022-int(fecha[2])>55 and 2022-int(fecha[2])<121:
            self.opcionAdMy.config(state="normal")
            self.opcionAdMy.select()
            self.opcionVol.config(state="disabled")
            self.entradaPrOf.config(state="normal")
            self.entradaPrOf.insert(0, str(random.randint(0, 1)) + ", " + str(random.randint(0, 50)))
            self.entradaPrOf.config(state="disabled")
            self.entradaEst.insert(0,"Activo")
            self.entradaEst.config(state="disabled")
            while True:
                codigo = "am" + str(random.randint(1000, 9999))
                if codigo not in participantes:
                    entradaIdenti.insert(0, codigo)
                    entradaIdenti.config(state="disabled")
                    return ""
        else:
            return messagebox.showwarning("Error", "No eres un canditato elegible")
    else:
        messagebox.showwarning("Error", "Tienes que introducir una fecha correcta como: 01/02/2002")
"""
def validarNombre(evento):
    """
    Funcionamiento: Valida el nombre indicado.
    Entrada: nombre(str): Nombre indica por el usuario.
    Salida: Si el nombre esta bien formulado.
    """
    seleccion = 0
    entradaCoElectr.config(state="normal")
    entradaPais.config(state="normal")
    entradaPais.delete(0, END)
    entradaCoElectr.delete(0, END)
    nombre = entradaNombre.get()
    if re.match("[a-zñA-ZÑ\u00C0-\u017F]", nombre):
        if nombre.istitle():
            nombre=nombre.split(" ")
            if len(nombre)==3:
                entradaCoElectr.insert(0,nombre[0][0].lower()+nombre[1].lower()+"@gmail.com")
                num=random.randint(0, len(region)-1)
                for s in region:
                    if seleccion==num:
                        num2=random.randint(0, len(region[s])-1)
                        pais=region[s]
                        entradaPais.insert(0,s+", "+pais[num2])
                        return entradaPais.config(state="disabled")
                    seleccion+=1
                return entradaCoElectr.config(state="disabled")
            return messagebox.showwarning("Error", "Tienes que introducir un nombre con dos apellidos.")
        return messagebox.showwarning("Error", "Tienes que introducir nombre y apellido con mayúsculas al principio.")
    return messagebox.showwarning("Error", "Tienes que introducir un nombre con dos apellidos.")
#Funcionamientos de la interfaz grafica.
def limpiarRe():
    """
    Funcionamiento: Vacia el formulario de la sección de registrar.
    Entrada:
    Salida: El formulario vaciado.
    """
    entradaFecha.delete(0, END)
    entradaIdenti.config(state="normal")
    entradaIdenti.delete(0, END)
    entradaIdenti.config(state="disabled")
    opcionVol.config(state="disabled")
    opcionAdMy.config(state="disabled")
    entradaNombre.delete(0, END)
    entradaPrOf.config(state="normal")
    entradaPrOf.delete(0, END)
    entradaPrOf.config(state="disabled")
    entradaCoElectr.delete(0, END)
    entradaPais.config(state="normal")
    entradaPais.delete(0, END)
    entradaPais.config(state="disabled")
    entradaHob.delete(0, END)
    entradaEst.config(state="normal")
    entradaEst.delete(0, END)
    entradaEst.config(state="disabled")
    return entradaDes.delete(0, END)
class ventanaRegistrar:
    def __init__(self, master):
        self.master = master
        self.canvasRegistrar = Canvas(self.master, width=700, height=750)
        self.canvasRegistrar.pack(fill="both", expand=True)
        self.tituloRegistra = Label(self.canvasRegistrar, text="Inserta un participante", font=("Helvetica", 20, "bold"))
        self.tituloRegistra.place(x=25, y=30)
        #Sección de fecha.
        self.tituloFecha = Label(self.canvasRegistrar, text="Fecha de nacimiento:", font=("Helvetica", 14, "bold"))
        self.tituloFecha.place(x=40, y=100)
        self.entradaFecha = Entry(self.canvasRegistrar, font=("Helvetica", 14))
        self.entradaFecha.place(x=350, y=100, height=30, width=300)
        self.entradaFecha.bind("<Return>", self.validarFecha)
        # Tipo de participante.
        self.tituloTiParti = Label(self.canvasRegistrar, text="Tipo de participante:", font=("Helvetica", 14, "bold"))
        self.tituloTiParti.place(x=40, y=150)
        self.opcionAdMy = Radiobutton(self.canvasRegistrar, text="Adulto Mayor", font=("Helvetica", 14, "bold"), variable=tipoOpc,
                                 state="disabled", value=True)
        self.opcionAdMy.place(x=350, y=150, height=30, width=250)
        self.opcionVol = Radiobutton(self.canvasRegistrar, text="Voluntario", font=("Helvetica", 14, "bold"), variable=tipoOpc,
                                state="disabled", value=False)
        self.opcionVol.place(x=350, y=180, height=30, width=223)
        # Identificación
        self.tituloIdenti = Label(self.canvasRegistrar, text="Identificador de participante:", font=("Helvetica", 14, "bold"))
        self.tituloIdenti.place(x=40, y=235)
        self.entradaIdenti = Entry(self.canvasRegistrar, font=("Helvetica", 14), state="disabled")
        self.entradaIdenti.place(x=350, y=235, height=30, width=300)
        # Nombre completo
        self.tituloNombr = Label(self.canvasRegistrar, text="Nombre Completo:", font=("Helvetica", 14, "bold"))
        self.tituloNombr.place(x=40, y=285)
        self.entradaNombre = Entry(self.canvasRegistrar, font=("Helvetica", 15))
        self.entradaNombre.place(x=350, y=285, height=30, width=300)
        self.entradaNombre.bind("<Return>", self.validarNombre)
        # Titulo de hobbies
        self.tituloHob = Label(self.canvasRegistrar, text="Hobbies:", font=("Helvetica", 14, "bold"))
        self.tituloHob.place(x=40, y=330)
        self.entradaHob = Entry(self.canvasRegistrar, font=("Helvetica", 15))
        self.entradaHob.place(x=350, y=330, height=30, width=300)
        # Profeción u oficio.
        self.tituloPrOf = Label(self.canvasRegistrar, text="Profeción u oficio", font=("Helvetica", 14, "bold"))
        self.tituloPrOf.place(x=40, y=375)
        self.entradaPrOf = Entry(self.canvasRegistrar, font=("Helvetica", 15), state="disabled")
        self.entradaPrOf.place(x=350, y=375, height=30, width=300)
        # correo Electronico.
        self.tituloCoElectr = Label(self.canvasRegistrar, text="Correo Electronico", font=("Helvetica", 14, "bold"))
        self.tituloCoElectr.place(x=40, y=425)
        self.entradaCoElectr = Entry(self.canvasRegistrar, font=("Helvetica", 15), state="disabled")
        self.entradaCoElectr.place(x=350, y=425, height=30, width=300)
        # Pais
        self.tituloPais = Label(self.canvasRegistrar, text="País de procedencia:", font=("Helvetica", 14, "bold"))
        self.tituloPais.place(x=40, y=475)
        self.entradaPais = Entry(self.canvasRegistrar, font=("Helvetica", 15), state="disabled")
        self.entradaPais.place(x=350, y=475, height=30, width=300)
        # Estado
        self.tituloEst = Label(self.canvasRegistrar, text="Estado", font=("Helvetica", 14, "bold"))
        self.tituloEst.place(x=40, y=525)
        self.entradaEst = Entry(self.canvasRegistrar, font=("Helvetica", 14, "bold"), state="disabled")
        self.entradaEst.place(x=350, y=525, height=30, width=300)
        # Descripción.
        self.tituloDes = Label(self.canvasRegistrar, text="Descripción", font=("Helvetica", 15, "bold"))
        self.tituloDes.place(x=40, y=575)
        self.entradaDes = Entry(self.canvasRegistrar, font=("Helvetica", 15))
        self.entradaDes.place(x=350, y=575, height=30, width=300)
        # Boton Insertar
        self.botonInsert = Button(self.canvasRegistrar, text="Insertar", font=("Helvetica", 14), fg="white", bg="black",
                             command=self.registrarAux)
        self.botonInsert.place(x=65, y=640, height=50, width=150)
        # Boton limpiar
        self.botonLimpiar = Button(self.canvasRegistrar, text="Limpiar", font=("Helvetica", 14), fg="white", bg="black",
                              command=limpiarRe)
        self.botonLimpiar.place(x=275, y=640, height=50, width=150)
        # boton Regresar.
        self.botonRegresar = Button(self.canvasRegistrar, text="Regresar", font=("Helvetica", 14), fg="white", bg="black", command=self.cambiarRegistrarN)
        self.botonRegresar.place(x=485, y=640, height=50, width=150)
    def validarFecha(self, evento):
        """
        Funcionamiento: Valida la fecha.
        Entrada: fecha(str): Fecha indica por el usuario.
        Salida: Si es un adulto mayor, o voluntario o si no cumple con los requisitos para participar.
        """
        dia30 = ["04", "06", "09", "11"]
        vali = False
        self.entradaIdenti.config(state="normal")
        self.entradaIdenti.delete(0, END)
        self.entradaPrOf.config(state="normal")
        self.entradaPrOf.delete(0, END)
        self.entradaEst.config(state="normal")
        self.entradaEst.delete(0, END)
        fecha = self.entradaFecha.get()
        if re.match("^\d{2}\/{1}\d{2}\/{1}\d{4}$", fecha):
            fecha = fecha.split("/")
            if fecha[1] == "02":
                if esBisiesto(int(fecha[2])) == True:
                    if re.match("[01-29]", fecha[0]):
                        vali = True
                else:
                    if re.match("[01-28]", fecha[0]):
                        vali = True
            elif fecha[1] in dia30:
                if re.match("[01-30]", fecha[0]):
                    vali = True
            else:
                if re.match("[01-31]", fecha[0]):
                    vali = True
        if vali == True:
            if 2022 - int(fecha[2]) > 17 and 2022 - int(fecha[2]) < 25:
                self.opcionVol.config(state="normal")
                self.opcionVol.select()
                self.opcionAdMy.config(state="disabled")
                self.entradaPrOf.insert(0, str(random.randint(0, 1)) + ", " + str(random.randint(0, 50)))
                self.entradaPrOf.config(state="disabled")
                self.entradaEst.insert(0, "Activo")
                self.entradaEst.config(state="disabled")
                while True:
                    codigo = "v" + str(random.randint(1000, 9999))
                    if codigo not in participantes:
                        self.entradaIdenti.insert(0, codigo)
                        self.entradaIdenti.config(state="disabled")
                        return ""
            elif 2022 - int(fecha[2]) > 55 and 2022 - int(fecha[2]) < 121:
                self.opcionAdMy.config(state="normal")
                self.opcionAdMy.select()
                self.opcionVol.config(state="disabled")
                self.entradaPrOf.config(state="normal")
                self.entradaPrOf.insert(0, str(random.randint(0, 1)) + ", " + str(random.randint(0, 50)))
                self.entradaPrOf.config(state="disabled")
                self.entradaEst.insert(0, "Activo")
                self.entradaEst.config(state="disabled")
                while True:
                    codigo = "am" + str(random.randint(1000, 9999))
                    if codigo not in participantes:
                        entradaIdenti.insert(0, codigo)
                        entradaIdenti.config(state="disabled")
                        return ""
            else:
                return messagebox.showwarning("Error", "No eres un canditato elegible")
        else:
            messagebox.showwarning("Error", "Tienes que introducir una fecha correcta como: 01/02/2002")

    def validarNombre(self, evento):
        """
        Funcionamiento: Valida el nombre indicado.
        Entrada: nombre(str): Nombre indica por el usuario.
        Salida: Si el nombre esta bien formulado.
        """
        seleccion = 0
        self.entradaCoElectr.config(state="normal")
        self.entradaPais.config(state="normal")
        self.entradaPais.delete(0, END)
        self.entradaCoElectr.delete(0, END)
        nombre = self.entradaNombre.get()
        if re.match("[a-zñA-ZÑ\u00C0-\u017F]", nombre):
            if nombre.istitle():
                nombre = nombre.split(" ")
                if len(nombre) == 3:
                    self.entradaCoElectr.insert(0, nombre[0][0].lower() + nombre[1].lower() + "@gmail.com")
                    num = random.randint(0, len(region) - 1)
                    for s in region:
                        if seleccion == num:
                            num2 = random.randint(0, len(region[s]) - 1)
                            pais = region[s]
                            self.entradaPais.insert(0, s + ", " + pais[num2])
                            return self.entradaPais.config(state="disabled")
                        seleccion += 1
                    return self.entradaCoElectr.config(state="disabled")
                return messagebox.showwarning("Error", "Tienes que introducir un nombre con dos apellidos.")
            return messagebox.showwarning("Error",
                                          "Tienes que introducir nombre y apellido con mayúsculas al principio.")
        return messagebox.showwarning("Error", "Tienes que introducir un nombre con dos apellidos.")
    def registrarAux(self):
        fecha = self.entradaFecha.get()
        partici = tipoOpc.get()
        nombre = self.entradaNombre.get()
        ident = self.entradaIdenti.get()
        hobbies = self.entradaHob.get()
        profesion = self.entradaPrOf.get()
        corrElec = self.entradaCoElectr.get()
        pais = self.entradaPais.get()
        estado = self.entradaEst.get()
        descrip = self.entradaDes.get()
        if re.match("^\d{2}\/{1}\d{2}\/{1}\d{4}$", fecha):
            if re.match("[a-zñA-ZÑ\u00C0-\u017F]", nombre):
                if re.match("^(am|v){1}\d{4}$", ident):
                    if re.match("^[1-3]$", hobbies):
                        if re.match("^[a-z]+\@(gmail.com){1}$", corrElec):
                            validar= registrarVol(fecha, ident, partici, nombre, hobbies, profesion, corrElec, pais,
                                                estado, descrip, participantes, adultoEnla)
                            if validar==True:
                                return messagebox.showinfo("Registrado", "El usuario se registro")
                            else:
                                return messagebox.showinfo("Error", "No se pudo registrar el usuario.")
                        return messagebox.showwarning("Error", "Tienes que introducir un correo con el formato: aapellido@gmail.com")
                    return messagebox.showwarning("Error", "Tienes que introducir un número entre 1 a 3")
                return messagebox.showwarning("Error", "Tienes que introducir un código correcto como: av0000 o v0000")
            return messagebox.showwarning("Error", "Tienes que introducir un nombre con dos apellidos.")
        return messagebox.showwarning("Error", "Tienes que introducir una fecha correcta como: 01/02/2002")
    def cambiarRegistrarN(self):
        #self.canvasRegistrar.pack_forget()
        self.ventanaRegiN= Toplevel(self.master)
        self.ventanaRegiN.geometry("675x250")
        self.ventanaRegiN.resizable(False, False)
        self.ventanaRegiN.title("Registrar N Participantes.")
        self.ventana=ventanaRegistrarN(self.ventanaRegiN)
class ventanaRegistrarN:
    def __init__(self, master):
        self.ventanaRegistarN=master
        self.tituloInsertN=Label(self.ventanaRegistarN, text="Insertar n participantes", font=("Helvetica", 20, "bold"))
        self.tituloInsertN.place(y=30, height=40, width=350)
        self.tituloGene = Label(self.ventanaRegistarN, text="Cantidad a generar", font=("Helvetica", 14))
        self.tituloGene.place(y=100, height=30, width=200)
        self.entradaGene = Entry(self.ventanaRegistarN, font=("Helvetica", 15))
        self.entradaGene.place(x=320, y=85, height=40, width=325)
        self.botonInserRn = Button(self.ventanaRegistarN, text="Insertar", bg="black", font=("Helvetica", 12, "bold",),fg="white", command=self.validarNumero)
        self.botonInserRn.place(x=30, y=160, height=50, width=180)
        self.botonlimpRn = Button(self.ventanaRegistarN, text="Limpiar", bg="black", font=("Helvetica", 12, "bold"), fg="white",
                                  command=limpiarRe)
        self.botonlimpRn.place(x=250, y=160, height=50, width=180)
        self.botonRegrRn = Button(self.ventanaRegistarN, text="Regresar", bg="black", font=("Helvetica", 12, "bold"),
                                  fg="white")
        self.botonRegrRn.place(x=470, y=160, height=50, width=180)
    def validarNumero(self):
        num= self.entradaGene.get()
        if re.match("\d", num):
            crearNparti(num, participantes, adultoEnla, region)
            return messagebox.showinfo("Hecho", "Se agrego la cantidad de participantes a la base de datos.")
        return messagebox.showwarning("Error", "Tienes que introducir la cantidad en números a agregar.")
"""
class registrarN(Toplevel):
    def __init__(self, ventana=None):
        self.ventanaG=Toplevel()
        self.ventanaG.geometry("675x250")
        self.ventanaG.resizable(False, False)
        self.ventanaG.title("Registrar N Participantes.")
        self.tituloInsertN=Label(self.ventanaG, text="Insertar n participantes", font=("Helvetica", 20, "bold"))
        
        self.tituloGene=Label(self.ventanaG, text="Cantidad a generar", font=("Helvetica", 14))
        self.tituloGene.place(y=100, height=30, width=200)
        self.entradaGene= Entry(self.ventanaG, font=("Helvetica", 15))
        self.entradaGene.place(x=320, y=85, height=40, width=325)
        self.botonInserRn=Button(self.ventanaG, text="Insertar", bg="black", font=("Helvetica", 12, "bold"), fg="white")
        self.botonInserRn.place(x=30, y=160, height=50, width=180)
        self.botonlimpRn=Button(self.ventanaG, text="Limpiar", bg="black", font=("Helvetica", 12, "bold"), fg="white", command=limpiarRe)
        self.botonlimpRn.place(x=250, y=160, height=50, width=180)
        self.botonRegrRn=Button(self.ventanaG, text="Regresar", bg="black",font=("Helvetica", 12, "bold"), fg="white")
        self.botonRegrRn.place(x=470, y=160, height=50, width=180)
"""
# Sección de interfaz gráfica
ventana = Tk()
ventana.geometry("700x750")
ventana.resizable(False, False)
tipoOpc=BooleanVar()
ventanaRegis = ventanaRegistrar(ventana)

# Ventana de ingresar
"""
canvasRegistrar = Canvas(ventana, width=700, height=750)
canvasRegistrar.pack(fill="both", expand=True)
tituloRegistra = Label(canvasRegistrar, text="Inserta un participante", font=("Helvetica", 20, "bold"))
tituloRegistra.place(x=25,y=30)

# Sección Fecha
tituloFecha = Label(canvasRegistrar, text="Fecha de nacimiento:", font=("Helvetica", 14, "bold"))
tituloFecha.place(x=40, y=100)
entradaFecha=Entry(canvasRegistrar, font=("Helvetica", 14))
entradaFecha.place(x=350, y=100,height=30, width=300)
entradaFecha.bind("<Return>", validarFecha)
# Tipo de participante.
tituloTiParti=Label(canvasRegistrar, text="Tipo de participante:", font=("Helvetica", 14, "bold"))
tituloTiParti.place(x=40,y=150)
opcionAdMy=Radiobutton(canvasRegistrar, text="Adulto Mayor",font=("Helvetica", 14, "bold"), variable=tipoOpc, state="disabled", value=True)
opcionAdMy.place(x=350, y=150, height=30, width=250)
opcionVol=Radiobutton(canvasRegistrar, text="Voluntario", font=("Helvetica", 14, "bold"), variable=tipoOpc, state="disabled", value=False)
opcionVol.place(x=350, y=180, height=30, width=223)
"""
ventana.mainloop()
