#Functions go here

#Question cannot be left blank
def not_blank(question, error_message):
    valid = False

    while not valid:
        response = int(input(question))

        if response != "": 
            return response 
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




