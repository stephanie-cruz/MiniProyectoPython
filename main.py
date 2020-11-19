import constants
import utility_functions as fn


def welcome_print():
    print('{:<32}         _______________________________'.format(''))
    print('{:<32}________|  __   ___   ___  __     ^     |_______'.format('')) 
    print('{:<32}\       |  |_|   |      /   /    /_\    |      /'.format(''))
    print('{:<32} \      |  |   __|__   /__ /__  /   \   |     /'.format(''))
    print('{:<32} /      |_______________________________|     \ '.format(''))
    print('{:<32}/__________)                        (__________\ '.format(''))

def order_pizza(quantity):
    print('\n')
    print('------------------------- Pizza número: ',quantity,'-------------------------')
    size = fn.give_options('inline','Tamaño',constants.Sizes).name
    ingredients = fn.give_options('not-inline','Ingredientes',constants.Ingredients)
    print('\nUsted seleccionó una pizza '+size, end =" con ")
    for i in ingredients:
        print(i.name, end=", ")
    print('\n')

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

    


if __name__ == "__main__":
    main()