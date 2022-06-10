"""
Name(s): David Li, Diane He
Name of Project: 
"""
import random
import os

def rten(x):
  x = random.randint(1, 10)
  return x

prg = 0
while prg != 1:
  Sinput = input("[Start] [Quit] [Info]: ")
  if Sinput.lower() == "start":
    import page1
    os.system("clear")
    prg = 1 


  if Sinput.lower() == "quit":
    print("Choose another option.")

  if Sinput.lower() == "info":
    print("This program was created by David Li and Diane He. \nAll the enemies in this game are randomly generated, using functions. \nAll the names for randomly generated enemies were taken (with permission) from those of classmates and peers.")
    input("[Close]")
    os.system("clear")