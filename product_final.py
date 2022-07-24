import validator_v1
import general_functions

# base Name function
def product_name_base():
  product_name = general_functions.get_input("Product name: ", "Please enter the product's name without the use of special characters", validator_v1.is_valid_product_name)
  return product_name





