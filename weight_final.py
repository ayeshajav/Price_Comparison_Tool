import validator_v1
import general_functions


# Function to convert gram into kilogram
def convert_gram_into_kg(value):
  return value / 1000

# base weight function
def weight_base():
  weight = float(general_functions.get_input("Weight (Must be in g or kg): ", "Please enter the appropriate weight", validator_v1.is_valid_decimal))
  
  unit = general_functions.get_input("(g)rams or (kg)Kilograms: ", "Please choose an appropriate choice", validator_v1.is_valid_unit)

  if unit.upper() in set(['G', 'GRAMS']):
    weight = convert_gram_into_kg(weight)
  
  return weight

