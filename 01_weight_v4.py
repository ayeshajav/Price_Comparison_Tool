#Functions go here
# Weight validator
def is_valid_decimal(value):
  is_valid = False
  try:
      weight = float(value)
      if weight > 0:
        is_valid = True
  except ValueError:
    is_valid = False
  return is_valid

def no_validation(value):
  return value

def is_valid_unit(value):
  return value # TODO: write unit validation here

  
# Get Input from user
def get_input(question, error_message="", validator=no_validation):
    valid = False

    while not valid:
        response = input(question)

        if validator(response): 
            return response
        else:
            print (error_message)

          
weight = float(get_input("Weight: ", "Please enter the weight", is_valid_decimal))

unit = get_input("(g)rams or (kg)Kilograms: ", "Please choose an appropriate choice", is_valid_unit)

if unit.upper() == "G" or unit.upper() == "GRAMS":
      converted = weight / 1000
      print(f"You are {converted} kilos")
     
      
elif unit.upper() == "KG" or unit.upper() == "KILOGRAMS":
      converted = weight 
      print(f"You are {converted} kilos")
      
  
else:
    print("Please choose an appropriate choice")




