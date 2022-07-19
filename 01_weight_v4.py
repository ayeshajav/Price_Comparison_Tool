#Functions go here

#not blank
def not_blank(question, error_message):
    valid = False

    while not valid:
        response = int(input(question))

        if response != "": 
            return response 
        else:
            print (error_message)




def get_weight():
  product_weight = {
  "weight": 0,
 }
  
  weight = not_blank("Weight: ", "Please enter the weight")
  
  end_loop = False
  
  while not end_loop:
    unit = input("(g)rams or (kg)Kilograms: ")
    if unit.upper() == "G" or unit.upper() == "GRAMS":
      converted = weight / 1000
      print(f"You are {converted} kilos")
      product_weight['weight'] = converted
      end_loop = True
    elif unit.upper() == "KG" or unit.upper() == "KILOGRAMS":
      converted = weight 
      print(f"You are {converted} kilos")
      product_weight['weight'] = converted
      end_loop = True
    else:
      print("Please choose an appropriate choice")

    return product_weight

weight = get_weight()

print(weight)


product = {
  "name": "I am rice",
}
product.update (weight)

print(product)

loop 
Productssss = [
  {'name': 'I am rice', 'weight': 0.044}
]

