import validator_v1
import general_functions

# base Name function
def get_name():
  name = general_functions.get_input("Name: ", "Please enter your name using appropriate letters", validator_v1.is_valid_name)
  return name
  

