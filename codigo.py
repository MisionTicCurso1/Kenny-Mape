 
print("ingrese su usuario")
usuario = input()
print("ingrese su altura en mts")
altura = float(input())
print("ingrese su masa en kg")
masa = float(input())

if (altura > 0 and masa > 0):
    imc = round((masa/(altura**2)),2)

print("su imc es :  ")
print(imc)
if(imc <= 16):
    print("infrapeso: delgadez severa")
if(imc >= 17):
    print("infrapeso: delgadez moderada")
if(imc >= 18.5):
    print("infrapeso: delgadez aceptable")
if(imc >= 25.0):
    print("peso normal")
if(imc >= 30.0):
    print("sobrepeso")
if (imc >= 35.0):
    print("obeso:  tipo I")
if(imc >= 40.0):
    print("obeso:  tipo II")
if(imc >= 40.0):
    print("obeso:  tipoIII")                        


