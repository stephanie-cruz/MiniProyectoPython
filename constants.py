import enum
class Sizes(enum.Enum): # Tamaños de las pizzas
  Grande = ['g',580]
  Mediano = ['m',430]
  Personal = ['p',280]
class Ingredients(enum.Enum): # Ingredientes de las pizzas
  Jamon = ['ja',40]
  Champiñones = ['ch',35]
  Pimentón = ['pi',30]
  DobleQueso = ['dq',40]
  Aceitunas = ['ac',57.5]
  Pepperoni = ['pp',38.5]
  Salchichón = ['sa',62.5]
