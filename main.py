import constants
import utility_functions as fn
total_price = 0
 
def welcome_print():
   print('{:<32}         _______________________________'.format(''))
   print('{:<32}________|  __   ___   ___  __     ^     |_______'.format(''))
   print('{:<32}\       |  |_|   |      /   /    /_\    |      /'.format(''))
   print('{:<32} \      |  |   __|__   /__ /__  /   \   |     /'.format(''))
   print('{:<32} /      |_______________________________|     \ '.format(''))
   print('{:<32}/__________)                        (__________\ '.format(''))

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
   sub_total = constants.Sizes[size].value[1] + get_sub_total(constants.Ingredients,ingredients)   
   print('\nSubtotal a pagar por una pizza '+size+' : '+str(sub_total)+'$ \n')
   total_price = total_price + sub_total
 
 
def order_pizza(quantity):
   print('\n')
   print('------------------------- Pizza número: ',quantity,'-------------------------')
   size = fn.give_options('inline','Tamaño',constants.Sizes) #.name
   ingredients = fn.give_options('not-inline','Ingredientes',constants.Ingredients)
   print('\nUsted seleccionó una pizza '+size, end =" con ")
   for i in ingredients:
      print(i, end=", ")
   get_pizza_price(size,ingredients)

def add_drink():
    print('----------------------------------------------------------------------------')
    orden = input('\nDesea agregar bebidas a su orden ? (s/n): ')
    orden = fn.yes_or_not("Desea agregar bebidas a su orden? (s/n). Debe seleccionar una opcion correcta : ",orden)  
    drinks = fn.give_options('no-inline','Bebidas disponibles',constants.Drinks)
    print('Usted seleccionó ', len(drinks), 'bebidas, con un subtotal de : ', str(get_sub_total(constants.Drinks,drinks)), '$')        

def main():
   welcome_print()
   quantity = 1
   orden = input('\nPresione "s" para realizar una nueva orden: ')
   orden = fn.yes_or_not("Desea realizar una nueva orden? (s/n). Debe seleccionar una opcion correcta : ",orden)  
   while orden == 's':       
      order_pizza(quantity)
      orden = input('Desea continuar (s/n)? ')
      orden = fn.yes_or_not("Debe seleccionar una opcion correcta (s/n) ",orden)  
      quantity = quantity+1
   if orden == 'n':
      add_drink()
      print('{:<32}_______________________________________________________________________________________'.format(''))
      print('{:<32}            El pedido tiene un total de '.format(''),(quantity-1), ' pizzas, por un monto de ', total_price,'$')
      print('{:<32}_______________________________________________________________________________________'.format(''))
   
   
if __name__ == "__main__":
    main()
