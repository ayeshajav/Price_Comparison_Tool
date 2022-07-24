# Funtions go here
#Question cannot be blank 
def not_blank(question, error_message):
    valid = False

    while not valid:
        response = input(question)
        response = response.strip()
        print(response)

        if response != "" and response.isalpha(): 
            return response
        else:
            print (error_message)

#Asking for information 
name = not_blank("Name: ", "Please enter your name")

#Question cannot be blank 
def not_blank(question, error_message):
    valid = False

    while not valid:
        response = input(question)

        if response != "": 
            return response 
        else:
            print (error_message)

#Asking for information 
budget = not_blank("Budget: ", "please enter the budget")

product_name = not_blank("Product name: ", "Sorry - this can't be blank, " "please enter the product name")

cost_price = not_blank("Cost Price: ", "please enter the cost price")


#Checking if their are decimals
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


