#Functions go here

#not blank
def not_blank(question, error_message):
    valid = False

    while not valid:
        response = input(question)

        if response != "" and not response.isalpha(): 
            return float(response)
        else:
            print (error_message)


weight = not_blank("Weight: ", "Please enter the weight")
  
unit = input("(g)rams or (kg)Kilograms: ")

if unit.upper() == "G" or unit.upper() == "GRAMS":
      converted = weight / 1000
      print(f"You are {converted} kilos")
     
      
elif unit.upper() == "KG" or unit.upper() == "KILOGRAMS":
      converted = weight 
      print(f"You are {converted} kilos")
      
    
else:
    print("Please choose an appropriate choice")




