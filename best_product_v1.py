#Chosen products 
products = [
  {'product_name': 'Salmon', 'cost_price': 30.0, 'weight': 10.0}, # 3
  {'product_name': 'Goldtuna', 'cost_price': 10.0, 'weight': 0.7},  #1.42
  {'product_name': 'Goldfish', 'cost_price': 20.0, 'weight': 2.0}, #4
  {'product_name': 'Tunafish', 'cost_price': 25.0, 'weight': 4.0}, #6.25
  {'product_name': 'Snapperfish', 'cost_price': 29.0, 'weight': 7.0}, #4.14 
]

#Chosen budget 
budget = 29

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

