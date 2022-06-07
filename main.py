"""
Name(s): David Li, Diane He
Name of Project: 
"""
import random

def rten(x):
  x = random.randint(1, 10)
  return x

prg = 0
while prg != 1:
  Sinput = input("[Start] [Quit] [Options]: ")
  if Sinput == "start":
    import page1
    prg = 1 
  if Sinput == "Start":
    import page1
    prg = 1 

  if Sinput == "quit":
    quit()

  if Sinput == "Quit":
    quit()

  if Sinput == "Options":
    print("There are no options.")

  if Sinput == "options":
    print("There are no options.")


