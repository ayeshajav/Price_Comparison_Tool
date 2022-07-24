

# Funtions go here
#Question cannot be left blank

def not_blank(question, error_message):
    valid = False

    while not valid:
        response = input(question)

        if response != "": 
            return response 
        else:
            print (error_message)


#Asking for information 

name = not_blank("Name: ", "Please enter your name")

budget = not_blank("Budget: ", "please enter the budget")

product_name = not_blank("Product name: ", "Sorry - this can't be blank, " "please enter the product name")

weight = not_blank("Weight: ", "Please enter the weight")

cost_price = not_blank("Cost Price: ", "please enter the cost price")