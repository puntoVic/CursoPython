def es_primo(numero):
    if numero < 4:
        return True
    raiz_entera = int(numero**0.5)
    residuos = (numero % (raiz_entera)) == 0 or (numero % 2) == 0
    if residuos:
        return False
    else:
        for i in range(3,raiz_entera,2):
            if numero % i == 0:
                print("es divisible en " + str(i))
                return False
        return True

def run():
    numero = int(input("dame el número a comprobar: "))
    if es_primo(numero):
        print('Es primo')
    else:
        print('No es primo')


if __name__ == '__main__':
    run()
