#Prints out current data set of active users inside the company
id_passes = {}

#def users_list():  #needs updating
  #file = open("userdatabase.txt", "r")
  #file = file.readlines()
  
  #for x in file:
   # if x.isnumeric():
    # print ("\n")
     #print(x)
    ## print(x)


def passwords():
  file = open("passwords.txt", "r")
  for line in file:
    line = line.split("|")                  #separate at | in file
    id_passes.update({line[0]: line[1].strip()})    #pairs ID numbers with passwords

def names(id_num):
  file = open("userdatabase.txt", "r")
  file = file.readlines()
  for line in file:
    line = line.split("|")
    if line[1] == "ID:" + id_num:
      return line[0]
    
  
    
