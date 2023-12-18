# RPG Battle Test    
# 12/16/2023
# Ver. 0.2

import os
import time
#
# Default Values
#
gender = 1
name = 'Matthew'
battle = 1
attack = 5
defense = 2
magic = 5
mana = 20

os.system('cls')
time.sleep(3)
print("Setting Up Game...")
time.sleep(3)

print("                                                RPG Battle Test                            "'\n')
print("                                             'Please wait ...'                       ")
print("Ver.0.2")
print("By Raymon Shields")

time.sleep(3)

print("You can press ENTER now.")
input()
os.system('cls')

# Pronoun Check
# People do be mad.


print('Before we continue with the battle test are you a boy or are you a girl?')
time.sleep(2)
print("Select (1) Boy (2) Girl (3) They/Them ")
gender = input()
if gender == 1:
    player = ['"He","he","His","his"']
elif gender == 2:
     player = ['"She","she","Her","her"']
elif gender == 3:
     player = ['They/Them,"They","they","Their","their"']

def gender_function():
 print('Before we continue with the battle test are you a boy or are you a girl?')
 time.sleep(2)
 print("Select (1) Boy (2) Girl (3) They/Them ")
 gender = input()
 if gender == 1:
     player = ['"He","he","His","his"']
 elif gender == 2:
     player = ['"She","she","Her","her"']
 elif gender == 3:
     player = ['"They","they","Their","their"']
 else:
     print("Invalid Gender")
     print("Try Again")
     time.sleep(2)
     os.system('cls')
     gender_function()

print("Nice now. what is your character's name:")
name = input()
time.sleep(2)
print("Great nice to meet you, "+ name )
print('\n\n\n\n')
time.sleep(2)
print("Alright last one. What testing module do you want?")
print("(1) Slime")
battle = input()
time.sleep(2)
os.system('cls')
time.sleep(2)





####################################################################################
#
#                              Player Stats
#
####################################################################################

print('                         Player Stats Menu                                     ')
print('############################################################################')

print('Name:'+ name,'\n')
print("Pronouns: "+ gender,'\n')
print("Attack") 
print("Defense: "+ defense,'\n')
print("Magic: "+ magic,'\n')

print("Press ENTER to continue")

input()










####################################################################################
#
#                             Slime Stats
#
####################################################################################





























####################################################################################
#
#                              Battle Mechanics
#
####################################################################################