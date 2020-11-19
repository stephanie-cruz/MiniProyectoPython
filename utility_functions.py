def yes_or_not(message, result): # Verifica si la opción seleccionada es 's' o 'n' , e itera hasta que lo sea
    while result not in ('s', 'n'):
            result = input(message)
    if result == 'n' or result == 's' :
        return result    

def insert_into_array(array, item): # inserta en un array sin duplicados
    into = False
    if len(array) > 0:
        for i in array:
            if i == item:
                into = True
    if into == False:
        array.append(item)
    return array

def get_enum_key(options,option): # retorna el nombre, dado el valor del enum.
    return options(option)

def give_options(format,title,options): # Dato un enum, lista las opciones disponibles e itera hasta que la respuesta sea válida. Puede darse el caso de que retorne un valor numerico, o una lista con valores (no repetidos), dependiendo de los parámetros pasados
  print('\n****** '+title+' : ******\n')
  text = ''
  for option in (options):
      if format == 'inline': 
        text = text + option.name + ' ('+option.value+') '
      else:
          print(text + option.name + ' ('+option.value+') ')
  if format != 'inline':
      array = []
      print('\n')
      text =  'Indique la opción (enter para terminar)'      
  current_option = input(text+' : ')
  correct = False
  while True:
    if current_option == "":
        return array
    for option in (options):
            if option.value == current_option:
                if format == 'inline':
                    return get_enum_key(options,current_option)
                else:
                    array = insert_into_array(array, get_enum_key(options,current_option))
                correct = True
    if correct == False:
        current_option = input(text + '. Por favor, indique una respuesta válida : ')
    else:
        current_option = input(text+ ' : ')
    correct = False
  
