#Functions go here

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
name = not_blank("Name: ", "Please enter your name and use letters")