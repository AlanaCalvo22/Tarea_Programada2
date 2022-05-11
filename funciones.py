#Elaborado por: Aarón Ortiz, Alana Calvo.
#Fecha de creación: 07/05/2022 16:58
#Fecha de modificación: 08/05/2022 23:17
#version: 3.10.0
from random import *
#----------------------------------Funcionamiento de Registrar-------------------------------------------
def registrarVol(pfecha, pidentif, ptipoPart, pnombre, phobies, pprofesion, pcorreo, ppais, pestado, pdescripcion, participante, adultoEnla):
    """
    Funcionamiento: Registra un participante en la base de datos con toda su información.
    Entrada: nombre(str): Nombre indica por el usuario.
    pfecha(str): Fecha de nacimiento.
    pidentif(str): Número de identificación del participante.
    ptipoPart(str): True: Adulto Mayor, False: Voluntario.
    pnombre(str): Nombre del participante.
    phobies(int): Número de hobbies indicados.
    pprofesion(str): 0/1 profesión u oficio, número de trabajo.
    pcorreo(str): correo del usuario.
    ppais(str): Región y país de procedencía del participante.
    pestado(str): Se define activo al Ingresar.
    pdescripcion(str): Descripción indicada por el autor.
    participante(dicc): Base de datos con todos los participantes.
    adultoEnla(dicc): Base de datos con los adultos mayores y sus enlaces.
    Salida: Registro del participante a las bases de datos correspondientes.
    """
    lista=[]
    hobbies=[]
    lista.append(pfecha)
    lista.append(ptipoPart)
    nombre=pnombre.split(" ")
    nombre=tuple(nombre)
    lista.append(nombre)
    for c in range(int(phobies)):
        hobbies.append("hobbie"+str(randint(0,25)))
    lista.append(hobbies)
    lista.append(tuple(pprofesion.split(",")))
    lista.append(pcorreo)
    lista.append(tuple(ppais.split(",")))
    if pestado=="Activo":
        lista.append((1, ""))
    lista.append(pdescripcion)
    if ptipoPart==True:
        lista.append(False)
        adultoEnla[pidentif]=""
        print(adultoEnla)
    participante[pidentif] = lista
    if pidentif in participante:
        return True
    else:
        return False
def crearNparti(num, participantes, adultoEnla, region):
    """
    Funcionamiento: Registra un participante en la base de datos con toda su información.
    Entrada: nombre(str): Nombre indica por el usuario.
    num(int): Número de participantes a crear.
    participante(dicc): Base de datos con todos los participantes.
    adultoEnla(dicc): Base de datos con los adultos mayores y sus enlaces.
    Salida: Registro del participante a las bases de datos correspondientes.
    """
    dia30 = ["04", "06", "09", "11"]
    meses=["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
    dias30=["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22","23",
            "24", "25", "26", "27", "28", "29", "30"]
    dias31=["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22","23",
            "24", "25", "26", "27", "28", "29", "30", "31"]
    dia28=["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22","23",
            "24", "25", "26", "27", "28"]
    apellidos=["Gonzalez","Gomez", "Diaz", "Rodriguez", "López", "Perez", "Martinez", "Silva", "Romero", "Cruz", "Fernández", "Ruiz", "Sanchez",
               "Martinez", "Florez", "Chavez", "Garcia", "Jara", "Valverde", "Morales", "Castro", "Gutierrez", "Cortes", "Campos", "Guzman", "Peña",
               "Ortega", "Venegas", "Mendoza", "Reyes", "Castillo", "Jimenez"]
    nombres=["Juan", "Jose", "Antonio", "Pedro", "Jesús", "Alejandro", "Margarita", "Manuel", "Roberto", "Francisco", "Walter", "Ernesto", "Fernando"
             "Roberto", "Daniel", "Carlos", "Ricardo", "Alberto", "Eduardo", "Manuel", "Daniela", "Angel", "María", "Guadalupe", "Juana", "Luis", "Raquel",
             "Pilar", "Ana", "Carmen", "Isabel", "Silvia", "Rosa", "Monica", "Paula", "Sara"]
    tipo=False
    for n in range(int(num)):
        info=[]
        mes= choice(meses)
        if tipo==False:
            if mes=="02":
                info.append(choices(dia28)+"/"+mes+"/"+str(randint(1997, 2005)))
            elif mes in dia30:
                info.append(choice(dias30)+"/"+mes+"/"+str(randint(1997, 2005)))
            else:
                info.append(choice(dias31) + "/" + mes + "/" + str(randint(1997, 2005)))
        else:
            if mes=="02":
                info.append(choices(dia28)+ "/" + mes +"/"+str(randint(1905, 1967)))
            elif mes in dia30:
                info.append(choice(dias30)+"/"+mes+"/"+str(randint(1905, 1967)))
            else:
                info.append(choice(dias31) + "/" + mes + "/" + str(randint(1905, 1967)))
        info.append(tipo)
        if tipo==False:
            while True:
                codigo = "v" + str(randint(1000, 9999))
                if codigo not in participantes:
                    break
        else:
            while True:
                codigo = "am" + str(randint(1000, 9999))
                if codigo not in participantes:
                    break
        nombre= (choice(nombres), choice(apellidos), choice(apellidos))
        info.append(nombre)
        num= randint(1, 3)
        listaH=[]
        for h in range(num):
            listaH.append("hobbie"+str(randint(1,25)))
        info.append(listaH)
        info.append((randint(0,1), randint(1,50)))
        info.append(nombre[0][0].lower()+nombre[1].lower()+"@gmail.com")
        num = randint(0, len(region) - 1)
        seleccion=0
        for s in region:
            if seleccion == num:
                num2 = randint(0, len(region[s]) - 1)
                pais = region[s]
                info.append((s, pais[num2]))
                break
            seleccion+=1
        info.append((1, ""))
        info.append("")
        if tipo==True:
            info.append(False)
            tipo=False
            adultoEnla[codigo]=""
        else:
            tipo=True
        participantes[codigo]=info
    print(adultoEnla)
    print(participantes)