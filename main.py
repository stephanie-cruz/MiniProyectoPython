print('         _______________________________')
print('________|  __   ___   ___  __     ^     |_______') 
print('\       |  |_|   |      /   /    /_\    |      /')
print(' \      |  |   __|__   /__ /__  /   \   |     /')
print(' /      |_______________________________|     \ ')
print('/__________)                        (__________\ ')

import constants
import utility_functions as fn


  

def main():
    quantity = 0
    orden = input('Presione "s" para realizar una nueva orden: ')
    orden = fn.yes_or_not("Desea realizar una nueva orden? (s/n). Debe seleccionar una opcion correcta : ",orden)
    print(orden)
    if orden == 's':
        quantity = 1
        print('Pizza número: ',quantity)
    print(fn.give_options('inline','Tamaño',constants.Sizes)) 
    print(fn.give_options('not-inline','Ingredientes',constants.Ingredients)) 

  # print(constants.PIZZA_GRANDE)


if __name__ == "__main__":
    main()