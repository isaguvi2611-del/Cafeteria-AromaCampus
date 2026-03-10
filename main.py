from menu import menusito

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
        menusito()
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