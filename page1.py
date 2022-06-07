#Use of this page is optional. If you use code here, make sure either import page1 or from page1 import * appear on your main.py page.'
import time
import os

x = 1
dotArray = "Loading"
print("Loading")
while x < 100:
  time.sleep(0.5)
  dotArray = dotArray + '.'
  print(dotArray)
  os.clear