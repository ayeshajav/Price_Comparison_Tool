import validator_v1
import general_functions

############# budget functions starts here ################
         
# base budget function 
def get_budget():
  budget = float(general_functions.get_input("Budget: $", "Please enter the budget", validator_v1.is_valid_decimal))

  return budget 
  
############# budget functions ends here ################


