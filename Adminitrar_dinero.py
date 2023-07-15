sueldo = int(input ("Escribi tu sueldo: "))
confirma_si_ese_es_su_suldo = input (f"Tu sueldo es: {sueldo}?: ")
confirmar = "si"
denegar = "no"
if confirma_si_ese_es_su_suldo == confirmar:
    luz = int(input("Coloca tus gastos de luz: "))
    agua = int(input("Coloca tus gastos de agua: "))
    gas = int(input("Coloca tus gastos de gas: "))
    internet = int(input("Coloca tus gastos de internet: "))
    celulares = int(input("Coloca tus gastos de celular: "))
    psicologa = int(input("Coloca tus gastos de psicologa: "))
    comida = int(input("Coloca tus gastos en comida: "))
    facultad = int(input("Coloca tus gastos en facultad: "))
    trasporte= int(input("Coloca tus gastos en trasporte: "))
    ahorro = sueldo /2
else:
    sueldo = int(input ("Coloca tu sueldo: "))
    luz = int(input("Coloca tus gastos de luz: "))
    agua = int(input("Coloca tus gastos de agua: "))
    gas = int(input("Coloca tus gastos de gas: "))
    internet = int(input("Coloca tus gastos de internet: "))
    celulares = int(input("Coloca tus gastos de celular: "))
    psicologa = int(input("Coloca tus gastos de psicologa: "))
    comida = int(input("Coloca tus gastos en comida: "))
    facultad = int(input("Coloca tus gastos en facultad: "))
    trasporte= int(input("Coloca tus gastos en trasporte: "))
    ahorro = sueldo /2

total_gastos = luz+agua+gas+internet+celulares+psicologa+comida+facultad+trasporte+ahorro

resultado = total_gastos 

print (f"Tus gastos totales son: {resultado}")

balance = sueldo - total_gastos

print (f"Tu balance es de: {balance}")
print(f"Tu ahorro es de: {ahorro}")
