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

############# Name functions starts here ################

# Validator: Function to check if value is a valid name
def is_valid_name(value):
  is_valid = False
  if value != '' and all(lett.isalpha() or lett.isspace() for lett in value):
    is_valid = True
  return is_valid

############# Name functions ends here ################

# base Name function
def name_base():
  name = get_input("Name: ", "Please enter your name and use letters", is_valid_name)
  return name
  
######################### Runners ###############################
name = name_base()

print(name)
