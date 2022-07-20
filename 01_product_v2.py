#Functions go here
#Functions go here
############# General Functions Starts ################

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

############# Product name functions starts here ################

# Validator: Function to check if value is a valid name
def is_valid_product_name(value = ''):
  is_valid = False
  if value != '' and all(lett.isalpha() or lett.isnumeric() or lett.isspace() for lett in value):
    is_valid = True
  return is_valid

############# product name functions ends here ################

# base Name function
def product_name_base():
  product_name = get_input("Product name: ", "Please enter the   product name", is_valid_product_name)
  return product_name

######################### Runners ###############################

product_name = product_name_base()
print(product_name)



