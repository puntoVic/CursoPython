def convierte_km_millas():
    try:
        km = float(input('Ingresa los Kilometros '))
        resultado = km /1.609344
        print(str(km) + ' kilometros son ' + str(resultado) + 'millas')
    except:
        print('No ingresaste un dato válido')

def convierte_millas_km():
    try:
        millas = float(input('Ingresa las millas '))
        resultado = millas * 1.609344
        print(str(millas) + ' millas son ' + str(resultado) + 'kilometros')
    except:
        print('No ingresaste un dato válido')


def run():
    print("""
    Conversor de millas y kilometros

    Puedes elegir entre las siguientes opciones

    1 - Kilometros a milla
    2 - Millas a kilometros
 
    """
    )
    opcion = input("Que operación quieres realizar: ")
    if opcion == "1":
        resultado = convierte_km_millas()
    elif opcion == "2":
        resultado = convierte_millas_km()
    else:
        print('No existe esa opción')


if __name__ == '__main__':
    run()