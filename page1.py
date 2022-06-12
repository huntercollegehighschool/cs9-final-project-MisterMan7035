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
  firstname =["Ryan", "George", "Benson", "Albert", "Katya", "Lily", "Kai", "Sarah", "Lynn", "Diane", "Basil", "William", "Theo", "Ayden", "Nile", "Eric", "Levi", "Arche", "Rio", "Austin", "Georgie", "Sasha", "Jaivan", "Kiren", "Kareem", "Diya", "Bella", "Felix", "Jennie", "Xanthe", "Serena", "Maya", "Evan", "Vera", "Arbion", "Colby", "Darren", "Ayan", "Jason"]
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
  global enemyhealth1
  if enemyhealth1 < 1:
    actiondeterm = 0
    return 1
  if actiondeterm == 1:
    os.system("clear")
    x = random.randint(5, 20)
    enemyhealth = enemyhealth1 
    enemyhp = enemyhealth + x
    result = str(enemyname1) + " heals by " + str(x) + " health." + "\nTheir health is now " + str(enemyhp) + "."
    return result
  if actiondeterm == 2 or actiondeterm == 3 or actiondeterm == 4:
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
    if playerhealth < 0:
      playerhealth = 0
    result = str(enemyname1) + " attacks you for " + str(z) + " damage.\nYou have " + str(playerhealth) + " health left."
    return result

def useitem(item):
  if item.lower() == "health potion":
    global playerhealth
    global healthpotion
    global inventory
    x = healthpotion
    healthpotionminus = x - 1
    healthpotion = healthpotionminus
    y = playerhealth
    z = random.randint(10, 15)
    playerhealth = y + z
    
    result = "You use a health potion!\nYou are healed for " + str(z) + " health.\nYou have " + str(healthpotion) + " left." 
    inventory = "You have " + str(healthpotion) + " health potions."
    return result
    #placeholder


def triggeraction(): 
  actiondeterm = input("[Attack] [Use item] [Scavenge]: ")
  global enemyhealth1  
  enemyhealth = enemyhealth1
  global repeataction
  global inventory
  repeataction = 0
  if actiondeterm.lower() == "attack":
    os.system("clear")
    playerdamage = random.randint(5, 10)
    enemyhealth = enemyhealth - playerdamage
    if enemyhealth < 1:
      enemyhealth = 0
    action = ("You attack " + str(enemyname1) + " for " + str(playerdamage) + " damage!\nThey have " + str(enemyhealth) + " remaining.")
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
        item = (input("[Health potion] [Cancel]"))
        if item.lower() == "cancel":
          return 0
        if item.lower() == "health potion":
          action = useitem("health potion")
          x = 1
          return action
          
  if actiondeterm.lower() == "scavenge":
    y = random.randint(1, 2)
    if y == 1:
      z = random.randint(1, 3)
      if z == 1:
        action = "You rummage around, but don't find anything of use."
        return action
      if z == 2:
        action = "You try to find some items on the floor, but fail to get anything useful."
        return action
      if z == 3:
        action = "You look around, but can't find any items."
        return action
    if y == 2:
      healthpotionplus = healthpotion
      healthpotion = healthpotionplus + 1
      inventory = "You have " + str(healthpotion) + " health potions."
      action = "You manage to find a health potion!"
      return action
      
  if actiondeterm.lower() != "scavenge":
    if actiondeterm.lower() != "attack":
      if actiondeterm.lower() != "use item":
        return 0
        


def enemydeath():
  global enemyhealth1
  global enemyname1
  global enemydead
  global inventory
  global healthpotion
  enemyitemdeterm = random.randint(1, 2)
  if enemyhealth1 < 1: 
    print("You have defeated " + str(enemyname1) + ".")
    if enemyitemdeterm == 1:
      print("They drop a health potion!")
      healthpotion = healthpotion + 1
      inventory = "You have " + str(healthpotion) + " health potions."
    input("[Press 'Enter' to continue.]")
    os.system("clear")
    return 1

def playerdeath():
  global playerhealth
  if playerhealth < 1:
      x = 0
      print("You have been defeated by " +  
 str(enemyname1) + ".\nWould you like to try again?")
      while x == 0:
        action = input("[Yes]: ")
        if action.lower() == "yes":
          x = 1
          os.system("clear")
          print("The world has decided that you will live to see another day!")
          playerhealth = 100
      print(enemyspawn(namegen(), 100, 10, enemyclass1))
      
y = 0
x = 1 
z = 0
while True:
  print(enemyspawn(namegen(), 100, 10, enemyclass1))
  while True:
    if enemydeath() == 1:
      break
    playerdeath()
    x = triggeraction()
    while x == 0:
        x = triggeraction()
    print(x)
    input("[Press 'Enter' to continue]")
    z = (enemyaction())
    if z != 1:
      print(z)
    
    