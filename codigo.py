

def multiple(numero1, numero2):
    if numero1 / numero2 == 0:
        print(f"{numero1} es multiplo de {numero2}")
    else:
        print(f"{numero1} no es multiplo de {numero2}")

print("Programa para evaluar si el primer numero es multiplo del segundo...")
#ingreso de datos 
numero1= int(input("ingrese el primer numero: "))
numero2= int(input("ingrese el segundo numero: "))

#llamamos la funcion

multiple(numero1,numero2)        
                    