# def imprimir_mensaje():
#     print("Mensaje especial")
#     print("Aprendi endo a usar funciones")   

# imprimir_mensaje()
# imprimir_mensaje()
# imprimir_mensaje()
def conversacion(mensaje):
    print("hola")
    print("¿Cómo estás?")
    print("Elegiste la opción " + mensaje)
    print("adios")

opcion = int(input("Elige una opcion (1,2,3): "))
conversacion(str(opcion))