def ask_question (question):
  return input(question) 
  
def blank_not_allowed (value):
  if value == "":
    print("Empty value not allowed")

name = ask_question("Name: ")
weight = ask_question("Weight: ")

blank_not_allowed(name)