def palindromo(palabra):
    palabra = palabra.replace(' ','').lower()
    palabra_revertida = palabra[::-1]
    if palabra == palabra_revertida:
        return True
    else:
        return False


def run():
    palabra = input("Escribe una palabra: ")
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print("Es palíndromo")
    else:
        print("no es palíndromo")


if __name__ == '__main__':
    run()