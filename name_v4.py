import validator_v1
import general_functions

# base name function
def name_base():
  name = general_functions.get_input("Name: ", "Please enter your name and use letters", validator_v1.is_valid_name)
  return name
  

