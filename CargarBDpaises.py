import pickle
def cargarBDpaíses(regionPais):
    dicc={}
    try:
        archiRePa=open(regionPais, "r")
        for i in archiRePa.readlines():
            region=i.split(":")
            pai=region[1].replace("\n"," ")
            paises=pai.split(",")
            dicc[region[0]]=paises
        archiRePa.close()
    except:
        print("No pudo abrir regionPais")
    print(dicc)
    return(dicc)
    
#print(cargarBDpaíses("regionPais.txt"))

