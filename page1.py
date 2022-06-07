#Use of this page is optional. If you use code here, make sure either import page1 or from page1 import * appear on your main.py page.'
import time
import os
import random

dotArray = "Loading"
x = 1
y = random.randint(30, 50)
while x < y:
  time.sleep(0.1)
  os.system("clear")
  dotArray = dotArray + '.'
  print(dotArray)
  x = x + 1

time.sleep(10)
print(x)