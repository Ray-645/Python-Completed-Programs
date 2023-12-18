# RPG World
# Ver. 0.01
# 06-25-2023

"""____________________  ________   __      __            .__       .___
\______   \______   \/  _____/  /  \    /  \___________|  |    __| _/
 |       _/|     ___/   \  ___  \   \/\/   /  _ \_  __ \  |   / __ | 
 |    |   \|    |   \    \_\  \  \        (  <_> )  | \/  |__/ /_/ | 
 |____|_  /|____|    \______  /   \__/\  / \____/|__|  |____/\____ | 
        \/                  \/         \/                         \/ 
"""
import time
import os 
import sys

print("                                                   Created By Raymon Shields                    ")

time.sleep(3)
os.system('cls')

print("                                                   WELCOME TO RPG WORLD                             ")
print("                                            Text based RPG Games made in Python 3.12                    ")
print("Ver.02")
print("By Raymon Shields")

# 12-16-2023 Disabled playsound sfx for now.

#from playsound import playsound

# playsound ('/.../Assets/eb_fanfare.wav')

print("'Press Enter To Continue'")

input()
def game1():
  time.sleep(2)
  os.system('cls')
  print("                                         1. Battle_Test   (Wait 10 Sec.)                    ")
  print()
  print("Patch Notes:      Battle Test ver.02 | Added Name and Gender Option   .")
  print("                     ")
  print("                     ")
  # print('\n') = new line
  print('\n\n\n\n\n\n\n\n')
  # Add (,end =) to combine two print functions
  # Creating a page function
  print("GAME SELECTED")
  time.sleep(10)
  sys.path.append('/.../Assets')
  from Assets import Battle_Test   
  exec(open('Battle_Test.py').read())
  
#
#       Game Menu : Choose between 4 different games tha will load each seperate py file.
#

os.system('cls')
time.sleep(3)
print("Please Select A Game:")
time.sleep(1)
print("(1) Battle Test   (2) Random Encounter [WIP]  (3)Level Test [WIP]   (4) Full Game [WIP]")
game = input()
if game == 1:
  game1()
elif game == 2:
  print('2')
  game1()
elif game == 3:
  print('3')
  game1()
elif game == 4:
  print('4')
  game1()
else:
  print("Invalid Choice")
  time.sleep(2)
  print("Selecting Default")
  os.system('cls')
  game1()







  # execute the Battle Test
  # sys.path.append() | fetch command
  # exec(open[File.py].read()) | Read and launch file
  
 
 
 # Breakup