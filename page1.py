import time
import os
import random



"""

dotArray = "Loading"
x = 1
t = 0.001
y = random.randint(8, 12)
while x < y:
  time.sleep(t)
  t = t * 2
  os.system("clear")
  dotArray = dotArray + '.'
  print(dotArray)
  x = x + 1

time.sleep(3)
os.system("clear")
time.sleep(3)

UNCOMMENT THIS SOMETIME!
"""

playerhealth = 100
enemyhealth1 = 0
enemydamage1 = 0
healthpotion = 3
inventory = "You have " + str(healthpotion) + " health potions."


def enemyspawn(enemyname, enemyhealth, enemydamage, enemyclass):
  approachdeterm = int(random.randint(1, 3))
  approachtext = 0
  if approachdeterm == 1: 
    approachtext = " challenges you!"
  if approachdeterm == 2:
    approachtext = " approaches you!"
  if approachdeterm == 3: 
    approachtext = " encounters you!"
  #Randomly selects an approach text
  ehp1 = int(enemyhealth / 6)
  ehp2 = int(enemyhealth / 4)
  ehealth1 = random.randint(ehp1 , ehp2)
  #Used to randomly scale enemy health up or down by 1/4 - 1/6 of its health

  determ = random.randint(1, 2)
  if determ == 1: 
    enemyhealth = enemyhealth + ehealth1
  if determ == 2:
    enemyhealth = enemyhealth - ehealth1
  #Determines whether to increase or decrease enemyhealth by 1/4 - 1/6 of health 
    
  edmg1 = int(enemydamage / 6)
  edmg2 = int(enemydamage / 4)
  edamage1 = random.randint(edmg1, edmg2)
  #Used to randomly scale enemy damage up or down by 1/4 - 1/6 of its damage
  determ = random.randint(1, 2)
  if determ == 1: 
    enemydamage = enemydamage + edamage1
  if determ == 2:
    enemydamage = enemydamage - edamage1
  #Determines whether to increase or decrease enemydeamage by 1/4 - 1/6 of damage
  global enemyhealth1 
  enemyhealth1 = enemyhealth
  global enemydamage1
  enemydamage1 = enemydamage
  global enemyname1
  enemyname1 = enemyname
  #Makes several global variables
  result = str(enemyname) + str(approachtext) + "\nTheir health is: " + str(enemyhealth) + "\nTheir class is: " + str(enemyclass)
  return result

def namegen():
  firstname =["Ryan", "George", "Benson", "Albert", "Katya", "Lily", "Kai", "Sarah", "Lynn", "Diane", "Basil", "William", "Theo", "Ayden", "Nile", "Eric", "Levi", "Arche", "Rio", "Austin", "Georgie", "Sasha", "Jaivan", "Kiren", "Kareem", "Diya", "Bella", "Felix", "Jennie"]
  midname = ["Mage", "Warrior", "Knight", "Archer"]
  global enemyclass1
  lastname = ["Alabama","Alaska","Arizona","Arkansas","California","Colorado", "Connecticut","Delaware","Florida","Georgia","Hawaii","Idaho","Illinois", "Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland", "Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana",
  "Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York", "North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania", "Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah", "Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"]
  name1 = random.choice(tuple(firstname))
  name2 = random.choice(tuple(midname))
  name3 = random.choice(tuple(lastname))
  enemyclass1 = name2
  result = str(name1) + ", " + str(name2) + " of " + str(name3)
  return result

#[variable].lower() converts it to all lowercase (very useful)


def enemyaction():
  actiondeterm = random.randint(1, 4)
  if actiondeterm == 1:
    os.system("clear")
    x = random.randint(5, 20)
    global enemyhealth1
    enemyhealth = enemyhealth1 
    enemyhp = enemyhealth + x
    result = str(enemyname1) + " heals by " + str(x) + " health." + "\nTheir health is now " + str(enemyhp) + "."
    return result
  else:
    os.system("clear")
    global playerhealth
    playerhealth1 = playerhealth
    intdeterm = random.randint(1, 2)
    x = random.randint(1, 3)
    y = enemydamage1
    if intdeterm == 1:
      z = y + x
    if intdeterm == 2:
      z = y - x
    playerhealth = playerhealth1 - z
    result = str(enemyname1) + " attacks you for " + str(z) + " damage." + "\n You have " + str(playerhealth) + " health left."
    return result
    

  

def useitem(item):
  if item.lower == "health potion":
    global playerhealth
    global healthpotion
    x = healthpotion
    healthpotion = x - 1
    y = playerhealth
    z = random.randint(10, 15)
    playerhealth = y + z
    
    result = "You use a health potion! \n You are healed for " + str(z) + " health. \nYou have " + str(healthpotion) + " left." 
    return result
    #placeholder


def triggeraction(): 
  actiondeterm = input("[Attack] [Use item] [Scavenge]")
  global enemyhealth1  
  enemyhealth = enemyhealth1
  global repeataction
  repeataction = 0
  if actiondeterm.lower() == "attack":
    os.system("clear")
    playerdamage = random.randint(5, 10)
    enemyhealth = enemyhealth - playerdamage
    action = ("You attack " + str(enemyname1) + " for " + str(playerdamage) + " damage!" "\nThey have " + str(enemyhealth) + " remaining.")
    enemyhealth1 = enemyhealth
    return action
    
  if actiondeterm.lower() == "use item":
    global healthpotion
    if healthpotion == 0:
      action = ("You have no items.")
      return action
    if healthpotion != 0:
      print(inventory)
      x = 0
      while x == 0:
        item = (input("[Use an item] [Cancel]"))
        if item.lower() == "cancel":
          return 0
        if item.lower() == "health potion":
          action = useitem(item)
          x = 1
          return action

  if actiondeterm.lower() != "use item":
      return 0
  if actiondeterm.lower() != "attack":
      return 0
    
"""
  if actiondeterm.lower() == "scavenge":
    #placeholder action
  return action
"""

x = 1 
while True:
  print(enemyspawn(namegen(), 100, 10, enemyclass1))
  while True:
    x = triggeraction()
    while x == 0:
      x = triggeraction()
    print(x)
    input("[Next]")
    print(enemyaction())