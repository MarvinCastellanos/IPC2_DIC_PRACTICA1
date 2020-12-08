aplicantes={}
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
            aux=linea.split(",")
            contador+=1
            if aux[0] not in aplicantes:
                aplicantes[aux[0]]=aux
            #print(aux)
            continue

    file.close()
    for aux in aplicantes:
        print(aux,aplicantes[aux])

#Menu principal
def menu():
    while True:
        print('---------------------------------')
        print('Ingrese una opcion:')
        print('---------------------------------')
        print('1) Lectura de archivo CSV')
        print('2) Cálculo de datos')
        print('3) Generación de archivo JSON')
        print('*********************************')
        opcion = input('Opción: ')
        if opcion == '1':
            carga()
            #print('Lectura')
            opcion=0
        elif opcion == '2':
            print('calculo')
            opcion=0
        elif opcion == '3':
            print('escritura')
            opcion=0
        elif not (opcion=='1' and opcion=='2' and opcion)=='3':
            print('Opcion invalida, intente de nuevo.')

menu()
for aux in aplicantes:
    print( aux)