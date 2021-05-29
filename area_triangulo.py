def obtiene_area(base, altura):
    return ((base * altura)/2)


def run():
    bienvenida = """

    Hola, este programa calcula el área de un triángulo 

    """
    print(bienvenida)
    base = float(input("Puedes darme la dimensión de la base del triángulo: "))
    altura = float(input("Puedes darme la dimensión de la altura del triángulo: "))
    area_triangulo = obtiene_area(base,altura)
    print("El área del triángulo es: " + str(area_triangulo))


if __name__ == '__main__':
    run()