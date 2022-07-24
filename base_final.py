import weight_final as weight_lib
import name_final as name_lib
import product_final as product_lib 
import costprice_final as costprice_lib
import budget_final as budget_lib 
 
######################### Runners ###############################

products = []

name = name_lib.get_name()
budget = budget_lib.get_budget() 

response = 'yes'
while response.upper() == 'YES' or response.upper() == 'Y':

  #Dictionary 
  product = {
    "product_name": product_lib.product_name_base(), 
    "cost_price": costprice_lib.cost_price_base(), 
    "weight": weight_lib.weight_base(),
  }
  products.append(product)

  print("Please indicate 'Y' / 'yes' to continue or press any other key to exit")
  
  response = input("Would you like to add another product?  ")

#Grams to kilograms conversion and checking best product through weight and cost price 
i = 0
products_within_budget = []
while i < len(products):
  if products[i]['cost_price'] <= budget:
    products[i]['grams'] = products[i]['weight'] * 1000
    products[i]['cost_price_per_gram'] = products[i]['cost_price'] / products[i]['grams']
    products_within_budget.append(products[i])
  i = i + 1

best_product = sorted(products_within_budget, key=lambda x: x['cost_price_per_gram'])[0]

print("The best product is ",best_product['product_name'])



