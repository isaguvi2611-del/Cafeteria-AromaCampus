print('''
    ***********************************
    Bienvenidos a AromaCampus
    ***********************************
''')
print('''Que deseas hacer?
    1. Ver menu
    2. Agregar nuevo cafe
    3. Salir
    ''')
op=int(input('Escriba su opcion'))
match op:
    case 1:
        print('''
        1. Latte       $7.000
        2. Capuccino   $8.000
        3. Americano   $9.500
        ''')