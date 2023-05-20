import time
import userdatabase
import os
from getpass import getpass


#-----------------Global Vars------------------------#
welcome_str = "Welcome To CyberNetics Incorporated\n"
menu = "\n\n1.) Contracts\n2.) Company Updates\n3.) Archives\n4.) Recent Bounties\n5.) Log out\n"
active = 0 #current user is inside program when set to 1

#--------------------FUNCTIONS-------------------------------#
def printer(string):
  for i in string:                    #prints 1 letter at a time
    print(i,end="", flush = True)
    time.sleep(.05)



def login ():
  validID = 0          #valid password set
  enter = 0      #valid ID set
  id_amount = 0  #number of digits user enters
  user_id = ""    #user ID
  password = ""  #user password
  
  while(enter == 0):
    while (validID == 0):
      printer("\nUser ID: ")
      user_id = input()

      for i in user_id:  #loop ensures they enter a 7 digit ID number
        id_amount += 1
      if id_amount != 7:  #lets user reenter ID
        printer("Invalid ID")
        time.sleep(0.08)
        id_amount = 0
        
      else:    #allows user to now enter password
        validID = 1
  
    #printer("Password: ")
    password = getpass()  #hids password as its typed
    userdatabase.passwords()  #access passwords from master dict
    
    for id in userdatabase.id_passes.keys():
      if id == user_id:    #valid ID
        if userdatabase.id_passes.get(user_id) == password:  #valid password
          os.system('clear')
          printer("Welcome ")
          printer(userdatabase.names(user_id))
          enter = 1
        else:
          printer("Invalid Password\n")    #invalid password
          time.sleep(0.5)
          validID = 1
        


def surf():
  global active
  active = 1
  option = ""
  printer("\n\nSelect an option below")
  print(menu)
  option = input()

  if option == "1":
    return 0

  if option == "2":
    return 0

  if option == "3":
    return 0

  if option == "4":
    return 0
  
  if option == "5":
    active = 0
    return 0
  
          

