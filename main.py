from menu import menusito
from agregarCafe import cafesito

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
        cafesito()
    case 3:
        print('''Desea editar algun cafe
            1. si
            2. no
            ''')