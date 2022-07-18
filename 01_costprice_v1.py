#Functions go here

#not blank
def not_blank(question, error_message):
    valid = False

    while not valid:
        response = input(question)

        if response != "": 
            return response 
        else:
            print (error_message)


#Main Routine goes here
cost_price = not_blank("Cost Price: ", "please enter the cost price")


