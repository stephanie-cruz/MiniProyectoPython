total_price = 0
total_drinks =0
promo = False
import enums 
import utility_functions as fn

def get_sub_total(items,itemChoise):
   global total_price
   sub_total = 0
   for i in (items):
      for j in itemChoise:
          if i.name == j:
              sub_total = sub_total + i.value[1]
   total_price = total_price + sub_total
   return sub_total

def get_pizza_price(size,ingredients):
  global total_price
  total_price = total_price + enums.Sizes[size].value[1]
  sub_total = enums.Sizes[size].value[1] + get_sub_total(enums.Ingredients,ingredients)  
  print('\nSubtotal a pagar por una pizza '+size+' : '+str(sub_total)+'$ \n')

def get_personal_data():
    global promo
    empty = True
    while empty == True:
        name = input('Ingrese nombre y apellido: ')
        ci = input('Ingrese su CI: ')
        phone = input('Ingrese su número telefónico: ')
        if name == '' or ci == '' or phone == '': 
            empty = True
            print('Debe ingresar todos los datos solicitados del cliente')
        else:
            empty = False
    user = fn.get_enum_key(enums.TopClients,ci,0)
    if user == None:
        print('El usuario que ha ingresado no posee promoción. Proceda con la orden')
        promo = 0
    else:
        promo = enums.TopClients[user].value[1]
        print('🎊🎊🎊🎊---------------Enhorabuena. El usario que ha ingresado tendrá un descuento del',promo,'% . Favor notificar. ---------------🎊🎊🎊🎊')
        

def order_pizza(quantity):
  get_personal_data()
  print('\n')
  print('------------------------- Pizza número: ',quantity,'-------------------------')
  size = fn.give_options('inline','Tamaño',enums.Sizes,False) #.name
  ingredients = fn.give_options('not-inline','Ingredientes',enums.Ingredients,False)
  print('\nUsted seleccionó una pizza '+size, end =" con ")
  for i in ingredients:
     print(i, end=", ")
  get_pizza_price(size,ingredients)
 
def add_drink():
   global total_price
   global total_drinks
   print('----------------------------------------------------------------------------')
   orden = input('\nDesea agregar bebidas a su orden ? (s/n): ')
   orden = fn.yes_or_not("Desea agregar bebidas a su orden? (s/n). Debe seleccionar una opcion correcta : ",orden) 
   if orden == 's':
       drinks = fn.give_options('not-inline','Bebidas disponibles',enums.Drinks,True)
       sub_total = get_sub_total(enums.Drinks,drinks)
       total_drinks = len(drinks)
       print('Usted seleccionó ', total_drinks ,'bebidas, con un subtotal de : ', str(sub_total), '$')  