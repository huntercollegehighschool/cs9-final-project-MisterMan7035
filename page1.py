#Use of this page is optional. If you use code here, make sure either import page1 or from page1 import * appear on your main.py page.'
import time
import os
import random

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

def enemyspawn(enemyname, enemyhealth, enemydamage, enemyclass):
  approachdeterm = random.randint(1, 3)
  approachtext = 0
  if approachdeterm == 1: 
    approachtext = " challenges you!"
  if approachdeterm == 2:
    approachtext = " approaches you!"
  if approachdeterm == 3: 
    approachtext = " encounters you!"
  #Randomly selects an approach text
  
  ehealth1 = enemyhealth + random.randint(1, 5)
  #Used to randomly scale enemy health up or down 5

  determ = random.randint(1, 2)
  if determ == 1: 
    enemyhealth = enemyhealth + ehealth1
  if determ == 2:
    enemyhealth = enemyhealth - ehealth1
  #Determines whether to increase enemyhealth by 1-5 or decrease by 1-5
    
  result = str(enemyname) + str(approachtext) + "\nTheir health is: " + str(enemyhealth) + "\nTheir class is: " + str(enemyclass)
  return result


print(enemyspawn("Combatant", 100, 10, "Mage"))
