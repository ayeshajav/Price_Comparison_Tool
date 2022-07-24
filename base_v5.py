# Validator: Function to check if value is a valid decimal
def is_valid_decimal(value):
  is_valid = False
  try:
      value_in_float = float(value)
      if value_in_float > 0:
        is_valid = True
  except ValueError:
    is_valid = False
  return is_valid

# Validator: Function to use if there is no validator required
def no_validation(value):
  return value

# Validator: Function to check if value is a valid name
def is_valid_name(value):
  is_valid = False
  if value != '' and all(lett.isalpha() or lett.isspace() for lett in value):
    is_valid = True
  return is_valid

# Validator: Function to check if value is a valid name
def is_valid_product_name(value = ''):
  is_valid = False
  if value != '' and all(lett.isalpha() or lett.isnumeric() or lett.isspace() for lett in value):
    is_valid = True
  return is_valid

# Validator: function to check valid unit
def is_valid_unit(value):
  is_valid = False
  valid_values = ['G', 'KG', 'GRAMS', 'KILOGRAMS']
  valid_values_set = set(valid_values)
  if value.upper() in valid_values_set :
    is_valid = True
  return is_valid

# Function to get Input from user
def get_input(question, error_message="", validator=no_validation):
    valid = False

    while not valid:
        response = (input(question)).strip()

        if validator(response): 
            return response
        else:
            print (error_message)
          
 ############# Name functions starts here ################

# base Name function
def name_base():
  name = get_input("Name: ", "Please enter your name and use letters", is_valid_name)
  return name
  
######################### Runners ###############################
name = name_base()

print(name)

############# budget functions starts here ################
         
# base budget function 
def budget_base():
  budget = float(get_input("budget: $", "please enter the budget", is_valid_decimal))

  return budget 
  
############# budget functions ends here ################

######################### Runners ###############################
budget = budget_base()

# base Name function
def product_name_base():
  product_name = get_input("Product name: ", "Please enter the   product name", is_valid_product_name)
  return product_name

######################### Runners ###############################

product_name = product_name_base()
print(product_name)

# base budget function 
def cost_price_base():
  cost_price = float(get_input("Cost Price: $", "please enter the cost price", is_valid_decimal))

  return cost_price  

######################### Runners ###############################
cost_price = cost_price_base()

# Function to convert gram into kilogram
def convert_gram_into_kg(value):
  return value / 1000

# base weight function
def weight_base():
  weight = float(get_input("Weight: ", "Please enter the weight", is_valid_decimal))
  
  unit = get_input("(g)rams or (kg)Kilograms: ", "Please choose an appropriate choice", is_valid_unit)

  if unit.upper() in set(['G', 'GRAMS']):
    weight = convert_gram_into_kg(weight)
  
  return weight
############# Weight functions ends here ################


######################### Runners ###############################
weight = weight_base()

print(f"You are {weight} kilos")


