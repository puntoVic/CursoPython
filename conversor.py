def convierte_pesos(valor_dolar, tipo):
    pesos = input("¿Cuantos pesos " + tipo + " tienes?: ")
    pesos = float(pesos)
    dolares = pesos /valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes: "+dolares + " dolares")

menu = """  
Bienvenido al conversor de monedas 💰
1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos

Elige una opción:
"""
opcion = int(input(menu)) 
if opcion == 1:
    valor_dolar = 3875
    convierte_pesos(valor_dolar, "colombianos")
elif opcion == 2:
    valor_dolar = 3875
    convierte_pesos(valor_dolar, 'argentinos')
else:
    valor_dolar = 3875
    convierte_pesos(valor_dolar, 'mexicanos')