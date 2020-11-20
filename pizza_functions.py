total_price = 0
import enums 
import utility_functions as fn
import pizza_functions as pf

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
  sub_total = enums.Sizes[size].value[1] + pf.get_sub_total(enums.Ingredients,ingredients)  
  print('\nSubtotal a pagar por una pizza '+size+' : '+str(sub_total)+'$ \n')

def order_pizza(quantity):
  print('\n')
  print('------------------------- Pizza número: ',quantity,'-------------------------')
  size = fn.give_options('inline','Tamaño',enums.Sizes) #.name
  ingredients = fn.give_options('not-inline','Ingredientes',enums.Ingredients)
  print('\nUsted seleccionó una pizza '+size, end =" con ")
  for i in ingredients:
     print(i, end=", ")
  get_pizza_price(size,ingredients)
 
def add_drink():
   global total_price
   print('----------------------------------------------------------------------------')
   orden = input('\nDesea agregar bebidas a su orden ? (s/n): ')
   orden = fn.yes_or_not("Desea agregar bebidas a su orden? (s/n). Debe seleccionar una opcion correcta : ",orden) 
   if orden == 's':
       drinks = fn.give_options('no-inline','Bebidas disponibles',enums.Drinks)
       sub_total = pf.get_sub_total(enums.Drinks,drinks)
       print('Usted seleccionó ', len(drinks), 'bebidas, con un subtotal de : ', str(sub_total), '$')  