import weight_final as weight_lib
import name_final as name_lib
import product_final as product_lib 
import costprice_final as costprice_lib
import budget_final as budget_lib 

######################### Runners ###############################


name = name_lib.get_name()
budget = budget_lib.get_budget() 

product = {
  "product_name": product_lib.product_name_base(), 
  "cost_price": costprice_lib.cost_price_base(), 
  "weight": weight_lib.weight_base(),
}


print(name)
print(budget)
print (product)
