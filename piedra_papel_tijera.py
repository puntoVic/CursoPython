import getpass
def revisa_opcion_correcta(entrada):
    valido = entrada == '1' or entrada == '2' or entrada == '3'
    if not valido:
        print("elegiste una opción incorrecta")
    return valido


def juego(j1, j2):
    if j1 > j2:
        if j1 > j2+1:
            return 2
        else:
            return 1
    elif j2 > j1:
        if j2 > j1+1:
            return 1
        else:
            return 2
    else:
        return 3


def run():
    diccionario = {
        1 :'Piedra',
        2 : 'Papel',
        3 : 'Tijeras',
    }
    bienvenida = """
    Hola, listo para jugar Piedra, papel o tijeras??

    Las instruccines son simples, cada jugador debe elegir una de las siguientes tres opciones:

    1 - Piedra
    2 - Papel
    3 - Tijeras

    Como en el juego tradicional, quien escoja Piedra le gana al que escoja tijeras, 
    el que elija papel le gana al que selecciono piedra, y finalmente el que elije tijeras
    le gana al que elije papel.
    """
    print(bienvenida)
    bandera = False
    while not bandera:
        jugador1 = getpass.getpass("Jugador 1, elije tu opción: ")[0]
        bandera = revisa_opcion_correcta(jugador1)

    bandera = False       
    while not bandera:
        jugador2 = getpass.getpass("Jugador 2, elije tu opción: ")[0]
        bandera =revisa_opcion_correcta(jugador2)
    
    resultado = juego(int(jugador1), int(jugador2))
    if resultado == 1:
        print('El jugador 1 ganó eligiendo ' + diccionario.get(int(jugador1)))
    elif resultado == 2:
        print('El jugador 2 ganó eligiendo ' + diccionario.get(int(jugador2)))
    else:
        print('Parece que piensan igual, esto es un empate')
    

if __name__ == '__main__':
    run()