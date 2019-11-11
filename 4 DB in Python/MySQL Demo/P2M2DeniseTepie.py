list_of = ['cat', 'goat', 'turtle']

def list_o_matic():
  if user_input in list_of:
    list_of.remove(user_input)
    return print("animals left, one died: ", user_input, "was removed")
  elif user_input == "":
    return print("animals left, one was popped: ", user_input, "was popped",  list_of.pop())
  elif (user_input in list_of) == False:
    list_of.append(user_input)
    return print("animals left, one was saved: ", user_input, "was added")

while list_of != []:
  print("look at all the animals", list_of)
  user_input = input("Enter animal")
  if user_input == "Quit":
    break
  else:
    list_o_matic()
print("Goodbye")


