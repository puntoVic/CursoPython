import math

def mensaje_error():
    print('No ingresaste un dato válido')

def volumen_cilindro():
    try:
        radio = float(input('Ingresa el radio de la base: '))
        altura = float(input('Ingresa la altura: '))
        resultado = (math.pi * radio * radio * altura)
        print('El volumen de tu cilindro es ' + str(round(resultado,2)) )
    except:
        mensaje_error()

def volumen_esfera():
    try:
        radio = float(input('Ingresa el radio de la esfera: '))
        resultado = (math.pi * (radio**3) * (4/3))

        print('El volumen de tu esfera es ' + str(round(resultado,2)) )
    except:
        mensaje_error()

def volumen_cubo():
    try:
        lado = float(input('Ingresa el tamaño de un lado del cubo: '))
        resultado = lado ** 3

        print('El volumen de tu cubo es ' + str(round(resultado,2)) )
    except:
        mensaje_error()

def volumen_cono():
    try:
        radio = float(input('Ingresa el radio de la base: '))
        altura = float(input('Ingresa la altura del cono: '))
        resultado = (math.pi * radio * radio * altura)/3

        print('El volumen de tu cono es ' + str(round(resultado,2)) )
    except:
        mensaje_error()

def volumen_prisma_rectangular():
    try:
        ladoa = float(input('Ingresa el tamaño de un lado de la base: '))
        ladob = float(input('Ingresa el tamaño del otro lado de la base: '))
        altura = float(input('Ingresa la altura del prisma: '))
        resultado = ladoa * ladob * altura
        print('El volumen de tu cilindro es ' + str(round(resultado,2)) )
    except:
        mensaje_error()

def volumen_piramide():
    try:
        lado = float(input('Ingresa el tamaño de un lado de la base: '))
        altura = float(input('Ingresa la altura de la piramide: '))
        resultado = (altura * altura ** 2 )/ 3

        print('El volumen de tu piramide es ' + str(round(resultado,2)) )
    except:
        mensaje_error()



def run():
    print("""
    Calculadora de volumen

    Puedes elegir entre las siguientes opciones de figuras para calcular su volumen

    1 - Cilindro
    2 - Esfera
    3 - Cubo
    4 - Cono
    5 - Prisma rectangular
    6 - Piramide (base cudrangular)
     
    """)
    opcion = input("Que operación quieres realizar: ")
    if opcion == "1":
        resultado = volumen_cilindro()
    elif opcion == "2":
        resultado = volumen_esfera()
    elif opcion == "3":
        resultado = volumen_cubo()
    elif opcion == "4":
        resultado = volumen_cono()
    elif opcion == "5":
        resultado = volumen_prisma_rectangular()
    elif opcion == "6":
        resultado = volumen_piramide()
    else:
        mensaje_error()

if __name__ == '__main__':
    run()