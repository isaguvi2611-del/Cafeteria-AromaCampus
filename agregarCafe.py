cafesito=int(input(print('''Desea agregar un cafe
        1. si
        2. No
        ''')))
match cafesito:
    case 1:
        cafe=input('Ingrese el nombre del cafe')
        precio=int(input('Ingrese el precio del cafe'))
        print('El cafe se a agregado correctamente:' , cafe, precio)