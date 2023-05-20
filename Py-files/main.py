import userdatabase
import interface
import time
import os



interface.printer(interface.welcome_str)
userdatabase.passwords()
interface.login()
interface.surf()
while (interface.active == 1):
  interface.surf()
  
if interface.active == 0:
    print("NO")
    os.system("clear")
    interface.printer("Goodbye")
    time.sleep(0.5)
    os.system("clear")
