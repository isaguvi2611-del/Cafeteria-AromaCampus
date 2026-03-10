print('''
    ***********************************
    Bienvenidos a AromaCampus
    ***********************************
''')
print('''Que deseas hacer?
    1. Ver menu
    2. Agregar nuevo cafe
    3. Editar Cafe
    ''')
op=int(input('Escriba su opcion'))
match op:
    case 1:
        print('''
        1. Latte       $7.000
        2. Capuccino   $8.000
        3. Americano   $9.500
        ''')
    case 2:
        print('''Desea agregar un cafe
        1. si
        2. No
        ''')
        select=int(input('Agregue respuesta'))
        match select:
            case 1:
                cafe=input('Ingrese el nombre del cafe')
                precio=int(input('Ingrese el precio del cafe'))
                print('El cafe se a agregado correctamente:' , cafe, precio)
    case 3:
        print('''Desea editar algun cafe
            1. si
            2. no
            ''')