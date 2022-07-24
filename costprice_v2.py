
#Functions go here

############# General Functions Starts ################

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

# Function to get Input from user
def get_input(question, error_message="", validator=no_validation):
    valid = False

    while not valid:
        response = (input(question)).strip()

        if validator(response): 
            return response
        else:
            print (error_message)

############# General functions ends here  ################

############# cost price functions starts here ################
         
# base budget function 
def cost_price_base():
  cost_price = float(get_input("Cost Price: $", "please enter the cost price", is_valid_decimal))

  return cost_price  
  
############# cost price functions ends here ################

######################### Runners ###############################
cost_price = cost_price_base()





