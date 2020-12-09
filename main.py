import json

aplicantes={}
puestos={}
aux={'candidatos':0,'edad Pormedio':0,'pretencion salarial':0}

#Carga de datos
def carga():
    direccion=input('Ingrese la direccion: ')
    file = open(direccion,"r")
    contador=0
    for linea in file:
        if contador==0:
            contador+=1
            continue
        else:
            i=1
            lineAux=""
            for letra in linea:
                lineAux+=letra
                i+=1
                if i == len(linea):
                    break
            aux=lineAux.split(",")
            contador+=1
            if aux[0] not in aplicantes:
                aplicantes[aux[0]]=aux
            #print(aux)
            continue

    file.close()
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Datos cargados satisfactoriamente")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    #for auxiliar in aplicantes:
        #print(auxiliar,aplicantes[auxiliar])

def calculo():
    global aux

    for aplicante in aplicantes:
        if aplicantes[aplicante][4] not in puestos:
            aux['candidatos']=aux['candidatos']+1
            aux['edad Pormedio']+=int(aplicantes[aplicante][3])
            aux['pretencion salarial']+=int(aplicantes[aplicante][5])
            puestos[aplicantes[aplicante][4]]=aux
            aux={'candidatos':0,'edad Pormedio':0,'pretencion salarial':0}
        else:
            puestos[aplicantes[aplicante][4]]['candidatos']+=1
            puestos[aplicantes[aplicante][4]]['edad Pormedio'] += int(aplicantes[aplicante][3])
            puestos[aplicantes[aplicante][4]]['pretencion salarial'] += int(aplicantes[aplicante][5])
    for puesto in puestos:
        puestos[puesto]['edad Pormedio']/=puestos[puesto]['candidatos']
        puestos[puesto]['pretencion salarial'] /= puestos[puesto]['candidatos']

    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Datos Calculados satisfactoriamente")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

def generaJSON():
    with open('puestos.json','w') as file:
        json.dump(puestos,file,indent=2)
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("JSON creado satisfactoriamente")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

#Menu principal
def menu():
    while True:

        print('\n---------------------------------')
        print('Ingrese una opcion:')
        print('---------------------------------')
        print('1) Lectura de archivo CSV')
        print('2) Cálculo de datos')
        print('3) Generación de archivo JSON')
        print('*********************************')
        opcion = input('Opción: ')
        if opcion == '1':
            carga()
            opcion=0
        elif opcion == '2':
            calculo()
            opcion=0
        elif opcion == '3':
            generaJSON()
            opcion=0
        elif not (opcion=='1' and opcion=='2' and opcion)=='3':
            print('Opcion invalida, intente de nuevo.')

menu()
