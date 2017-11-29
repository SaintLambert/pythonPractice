#this code is an example for using methods



def promptUser(jabroni):       #Asks user for their name, and returns it
  
  name = input("Please input your name: ")
  print("That is a mediocre name " + name)
  print("Also your number was " + jabroni)
  return;

promptUser(input("Please input a number"))            #Calls the promptUser Function