import weight_final as weight_lib
import name_final as name_lib
import product_final as product_lib 
import costprice_final as costprice_lib
import budget_final as budget_lib 

######################### Runners ###############################

#List for products 
products = []

name = name_lib.get_name()
budget = budget_lib.get_budget() 

#If user responds with 'yes'
response = 'yes'
while response.upper() == 'YES' or response.upper() == 'Y':

#Dictionary for information about each product 
  product = {
    "product_name": product_lib.product_name_base(), 
    "cost_price": costprice_lib.cost_price_base(), 
    "weight": weight_lib.weight_base(),
  }
  products.append(product)
  print(products)
  print(name)
  print(budget)
  print (product)
  

  print("Please indicate 'Y' to continue or press any other key to exit")
  
  response = input("Would you like to add another product?  ")

#Kilograms to grams conversion and then choosing best product through cost price and weight
i = 0
products_within_budget = []
while i < len(products):
  if products[i]['cost_price'] <= budget:
    products[i]['grams'] = products[i]['weight'] * 1000
    products[i]['cost_price_per_gram'] = products[i]['cost_price'] / products[i]['grams']
    products_within_budget.append(products[i])
  i = i + 1

print(sorted(products_within_budget, key=lambda x: x['cost_price_per_gram'])[0])



# eliminate everything above budget range
# turn weight(kg) to g 
# find cost per gram
# find lowest per gram price which the best product




