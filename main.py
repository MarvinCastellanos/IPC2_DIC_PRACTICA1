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
        print('Lectura')
        opcion=0
    elif opcion == '2':
        print('calculo')
        opcion=0
    elif opcion == '3':
        print('escritura')
        opcion=0
    elif not (opcion=='1' and opcion=='2' and opcion)=='3':
        print('Opcion invalida, intente de nuevo.')