#Use of this page is optional. If you use code here, make sure either import page1 or from page1 import * appear on your main.py page.'
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
  #Makes enemyhealth1 and enemydamage1 global variables equal to health and damage
  result = str(enemyname) + str(approachtext) + "\nTheir health is: " + str(enemyhealth) + "\nTheir class is: " + str(enemyclass)
  return result




def triggeraction(): 
  actiondeterm = input("[Attack] [Use item] [Heal]")
  if actiondeterm == "Attack":
    print("You attack for [placeholder] damage!")
  return actiontext

print(enemyspawn("Combatant", 100, 10, "Mage"))
#print(triggeraction())
print(enemyhealth1)
print(enemydamage1)