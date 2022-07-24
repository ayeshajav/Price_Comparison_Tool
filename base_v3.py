
# Funtions go here
#Question cannot be left blank

def not_blank(question, error_message):
    valid = False

    while not valid:
        response = input(question)
        response = response.strip()
        print(response)

        if response != "" and response.isalpha(): 
            return response
        else:
            print (error_message)

#Asking for information 
name = not_blank("Name: ", "Please enter your name")

#Question cannot be blank
def not_blank(question, error_message):
    valid = False

    while not valid:
        response = input(question)

        if response != "": 
            return response 
        else:
            print (error_message)

#Asking for information 
budget = not_blank("Budget: ", "please enter the budget")

product_name = not_blank("Product name: ", "Sorry - this can't be blank, " "please enter the product name")

cost_price = not_blank("Cost Price: ", "please enter the cost price")

#Question cannot be blank
def not_blank(question, error_message):
    valid = False

    while not valid:
        response = input(question)

        if response != "" and not response.isalpha(): 
            return float(response)

        else:
            print (error_message)

#Asking for information 
weight = not_blank("Weight: ", "Please enter the weight")

unit = input("(g)rams or (kg)Kilograms: ")

#Grams and kilograms conversion 
if unit.upper() == "G" or unit.upper() == "GRAMS":
      converted = weight / 1000
      print(f"You are {converted} kilos")
     
      
elif unit.upper() == "KG" or unit.upper() == "KILOGRAMS":
      converted = weight 
      print(f"You are {converted} kilos")
      
    
else:
    print("Please choose an appropriate choice")

