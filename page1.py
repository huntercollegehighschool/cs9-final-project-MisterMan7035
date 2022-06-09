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
  firstname =["Ryan", "George", "Benson", "Albert", "Katya", "Lily"]
  midname = ["Mage", "Warrior", "Knight", "Archer"]
  global enemyclass1
  lastname = ["Alabama","Alaska","Arizona","Arkansas","California","Colorado",
  "Connecticut","Delaware","Florida","Georgia","Hawaii","Idaho","Illinois",
  "Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland",
  "Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana",
  "Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York",
  "North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania",
  "Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah",
  "Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"]
  name1 = random.choice(tuple(firstname))
  name2 = random.choice(tuple(midname))
  name3 = random.choice(tuple(lastname))
  enemyclass1 = name2
  result = str(name1) + ", " + str(name2) + " of " + str(name3)
  return result

#[variable].lower() converts it to all lowercase (very useful)


def enemyaction():
  actiondeterm = random.randint(1, 2)
  if actiondeterm == 1:
    os.system("clear")
    global playerhealth
    playerhealth1 = playerhealth
    playerhealth = playerhealth1 - enemydamage1
    result = str(enemyname1) + " attacks you for " + str(enemydamage1) + " damage." + "\n You have " + str(playerhealth) + " health left."
    return result
  if actiondeterm == 2:
    os.system("clear")
    result = "System rolled 2"
    return result
    #PLACEHOLDER

  

def useitem(item):
  if item.lower == "health potion":
    result = 0
    #placeholder


def triggeraction(): 
  actiondeterm = input("[Attack] [Use item] [Scavenge]")
  global enemyhealth1  
  enemyhealth = enemyhealth1
  if actiondeterm.lower() == "attack":
    os.system("clear")
    playerdamage = random.randint(5, 10)
    enemyhealth = enemyhealth - playerdamage
    action = ("You attack " + str(enemyname1) + " for " + str(playerdamage) + " damage!" "\nThey have " + str(enemyhealth) + " remaining.")
    enemyhealth1 = enemyhealth
    return action


""""
  if actiondeterm.lower() == "use item":
    #Placeholder action
  if actiondeterm.lower() == "scavenge":
    #placeholder action
  return action
"""


print(enemyspawn(namegen(), 100, 10, enemyclass1))
while True:
  print(triggeraction())
  input("[Next]")
  print(enemyaction())