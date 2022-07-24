import validator_v1
import general_functions

############# cost price functions starts here ################
         
# base budget function 
def cost_price_base():
  cost_price = float(general_functions.get_input("Cost Price: $", "please enter the cost price", validator_v1.is_valid_decimal))

  return cost_price  
  
############# cost price functions ends here ################







