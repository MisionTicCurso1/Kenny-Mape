
helado_nada = 0
helado_normal = 1900
helado_oreo = 1000 #2900 oreo
helado_KitKat = 1500 #3400 kitkat
helado_brownie = 2500 #4400 brownie
helado_barquillo = 950 #2850 barquillo

def ice():
     global helado_nada
     global helado_normal
     global helado_oreo
     global helado_KitKat
     global helado_brownie
     global helado_barquillo
     print("buenas tardes a ice cream:")
     print("este es el menu de helados")
     print("1): helado normal sin ningun topping.........$ 1900")
     print("2): adicion de topping de oreo...............$ 1000")
     print("3): adicion de topping de KitKat.............$ 1500")
     print("4): adicion de topping de brownie............$ 2500")
     print("5): adicion de topping de barquillo..........$  950")
     print("6): adicion de topping de arequipe...........$ 1100")

     valor = (int(input("ingrese aca el numero de su pedido: ")))
    
     if (valor == 1 ):
        print(f"el helado sin topping le cuesta {helado_normal}")

     if (valor == 2 ):
        helado2 = helado_normal + helado_oreo
        print(f"el helado con adicion de oreo le cuesta {helado2}")

     if (valor == 3):
        helado3 = helado_normal + helado_KitKat
        print(f"el helado con adicion de KitKat le cuesta {helado3}")
   
     if (valor == 4):
        helado4 = helado_normal + helado_brownie
        print(f"el helado con adicion de brownie le cuesta {helado4}")
        
     if (valor == 5):
        helado5 = helado_normal + helado_barquillo
        print(f"el helado con adicion de barquillo le cuesta {helado5}")    
    
     if (valor == 6):
        print ("lo sentimos no tenemos este topping")
        print(f"pero si desea puede selecionar otro o el helado sin topping le cuesta {helado_normal}")

     respuesta = input("Si gusta comprar otro helado digite 'Si' por el contrario digite 'No'")
     
     if(respuesta == "Si" or respuesta == "si" or respuesta == "SI"):
        ice()

     if(respuesta == "No" or respuesta == "no" or respuesta == "NO"):
        print("Gracias por su compra vuelva pronto :))) ")
ice()
















                    