
def string_length(y):  # define a function that takes in a string
  n = [] #an empty list
  if type(y) == str: #check if the input is a string 
    n.append(len(y)) #add the length of the string to an empty list
    return n #return the list 
  elif type(y) == list: #if the input is a list
    for item in y: #loop through every item of a list and gets its number
      n.append(len(item)) #append the length of every item to the empty list
    return n # returns the list