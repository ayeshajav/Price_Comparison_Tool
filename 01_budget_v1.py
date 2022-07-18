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
budget = not_blank("budget: ", "please enter the budget")


