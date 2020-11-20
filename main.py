import utility_functions as fn
import pizza_functions as pf


def welcome_print():
  print('{:<32}         _______________________________'.format(''))
  print('{:<32}________|  __   ___   ___  __     ^     |_______'.format(''))
  print('{:<32}\       |  |_|   |      /   /    /_\    |      /'.format(''))
  print('{:<32} \      |  |   __|__   /__ /__  /   \   |     /'.format(''))
  print('{:<32} /      |_______________________________|     \ '.format(''))
  print('{:<32}/__________)                        (__________\ '.format(''))
 

def main():
  while True:
    welcome_print()
    quantity = 1
    orden = input('\nPresione "s" para realizar una nueva orden: ')
    orden = fn.yes_or_not("Desea realizar una nueva orden? (s/n). Debe seleccionar una opcion correcta : ",orden) 
    while orden == 's':      
        pf.order_pizza(quantity)
        orden = input('Desea ordenar otra pizza (s/n)? ')
        orden = fn.yes_or_not("Debe seleccionar una opcion correcta (s/n) ",orden) 
        quantity = quantity+1
        if orden == 'n':
            pf.add_drink()
            print('{:<16}_______________________________________________________________________________________'.format(''))
            print('{:<16}            El pedido tiene un total de '.format(''),(quantity-1), ' pizzas, y ',pf.total_drinks, 'bebidas, por un monto de ', pf.total_price,'$')
            if pf.promo != 0:
                discount = (100 - pf.promo) * pf.total_price / 100
                print('{:<16}      🎊🎊🎊🎊Con un descuento del '.format(''),pf.promo,'%',' el total a pagar será de : ',discount,'$ 🎊🎊🎊🎊')
            print('{:<16}_______________________________________________________________________________________'.format(''))
 
if __name__ == "__main__":
   main()
