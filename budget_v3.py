import validator_v1
import general_functions

############# budget functions starts here ################
         
# base budget function 
def budget_base():
  budget = float(general_functions.get_input("budget: $", "please enter the budget", validator_v1.is_valid_decimal))

  return budget 
  
############# budget functions ends here ################

######################### Runners ###############################
budget = budget_base()

