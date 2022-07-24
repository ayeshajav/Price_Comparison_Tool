import validator_v1
############# General Functions Starts ################

# Function to get Input from user
def get_input(question, error_message="", validator=validator_v1.no_validation):
    valid = False

    while not valid:
        response = (input(question)).strip()

        if validator(response): 
            return response
        else:
            print (error_message)

############# General functions ends here  ################

