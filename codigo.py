
# print("ingrese su usuario")
# usuario = input()
# print("ingrese su altura en mts")
# altura = float(input())
# print("ingrese su masa en kg")
# masa = float(input())

# if (altura > 0 and masa > 0):
#     imc = round((masa/(altura**2)),2)

# print("su imc es :  ")
# print(imc)
# if(imc <= 16):
#     print("infrapeso: delgadez severa")
# if(imc >= 17):
#     print("infrapeso: delgadez moderada")
# if(imc >= 18.5):
#     print("infrapeso: delgadez aceptable")
# if(imc >= 25.0):
#     print("peso normal")
# if(imc >= 30.0):
#     print("sobrepeso")
# if (imc >= 35.0):
#     print("obeso:  tipo I")
# if(imc >= 40.0):
#     print("obeso:  tipo II")
# if(imc >= 40.0):
#     print("obeso:  tipoIII")

# def multiple(numero1, numero2):
#     if numero1 / numero2 == 0:
#         print(f"{numero1} es multiplo de {numero2}")
#     else:
#         print(f"{numero1} no es multiplo de {numero2}")

# print("Programa para evaluar si el primer numero es multiplo del segundo...")
# #ingreso de datos 
# numero1= int(input("ingrese el primer numero: "))
# numero2= int(input("ingrese el segundo numero: "))

# #llamamos la funcion

# multiple(numero1,numero2)   




helado_nada = 0
helado_normal = 1900
helado_oreo = 1000 #2900 oreo
helado_KitKat = 1500 #3400 kitkat
helado_brownie = 2500 #4400 brownie
helado_barquillo = 950 #2850 barquillo



        
print("buenas tardes aca tiene el menu de los helados:")
print("1): helado normal sin ningun topping.........$ 1900")
print("2): adicion de topping de oreo...............$ 1000")
print("3): adicion de topping de KitKat.............$ 1500")
print("4): adicion de topping de brownie............$ 2500")
print("5): adicion de topping de barquillo..........$  950")
print("6): adicion de topping de arequipe...........$ 1100")


    
valor = (int(input("cual es su pedido: ")))

if (valor > 0 and helado_normal > 0):
    helado = helado_nada + helado_normal
    helado2 = helado_normal + helado_oreo
    helado3 = helado_normal + helado_KitKat
    helado4 = helado_normal + helado_brownie
    helado5 = helado_normal + helado_barquillo
    


if (valor == 1 ):
        print(f"el helado sin topping le cuesta {helado}")

if (valor == 2 ):
        print(f"el helado con adicion de oreo le cuesta {helado2}")

  
if (valor == 3):
        print(f"el helado con adicion de KitKat le cuesta {helado3}")
  
if (valor == 4):
        print(f"el helado con adicion de brownie le cuesta {helado4}")
        
if (valor == 5):
        print(f"el helado con adicion de barquillo le cuesta {helado5}")    
    
if (valor == 6):
    print ("lo sentimos no tenemos este topping")
    print(f"pero si desea puede selecionar otro o el helado sin topping le cuesta {helado}")

















                    