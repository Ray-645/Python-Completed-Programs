#   Random Number Guesser [Rock,Paper,Scissor]
 #  Raymon Shields
  # 7/06/2023

# import random             | Import Math Lib
# random.randint(,)         | Random generator in which it chooses between two number ranges 
import os
import time
import random
print("                                             ROCK PAPER SCISSOR                   " )
print("                                             Made in Python 3.6                    ")
print("")
print("By Raymon Shields")
print()

print("Please wait.")
time.sleep (2)

cpu = random.randint(1,3)

# 1 == Rock
# 2 == Paper
# 3 == Scissor


print("(1) Rock, (2) Paper Or (3) Scissor")

time.sleep (2)
print()
user = int(input("Enter your choice: "))

time.sleep (2)
os.system("cls")

if cpu == 1 and user == 2:
    print("You chose Paper!")
    time.sleep (2)
    print()
    print("The CPU chose Rock!")
    time.sleep (2)
    print()
    print("You Win!")
    time.sleep (2)
elif cpu == 1 and user == 1:
    print("You chose Rock!")
    time.sleep (2)
    print()
    print("The CPU chose Rock!")
    print()
    time.sleep (2)
    print("Tie!")
    time.sleep (2)
elif cpu == 1 and user == 3:
    print("You chose Paper!")
    time.sleep (2)
    print()
    print("The CPU chose Rock!")
    time.sleep (2)
    print()
    print("You Lose!")
    time.sleep (2)
elif cpu == 2 and user == 1:
    print("You chose Rock!")
    print()
    time.sleep (2)
    print("The CPU chose Paper!")
    time.sleep (2)
    print()
    print("You Lose!")
    time.sleep (2)
elif cpu == 2 and user == 2:
    print("You chose Paper!")
    time.sleep (2)
    print()
    print("The CPU chose Paper!")
    print()
    time.sleep (2)
    print("Tie!")
    time.sleep (2)
elif cpu == 2 and user == 3:
    print("You chose Scissor!")
    time.sleep (2)
    print()
    print("The CPU chose Paper!")
    print()
    time.sleep (2)
    print("You Win!")
    time.sleep (2)
elif cpu == 3 and user == 1:
    print("You chose Rock!")
    time.sleep (2)
    print()
    print("The CPU chose Scissor!")
    time.sleep (2)
    print()
    print("You Win!")
    time.sleep (2)
elif cpu == 3 and user == 3:
    print("You chose Scissor!")
    time.sleep (2)
    print()
    print("The CPU chose Scissor!")
    time.sleep (2)
    print()
    print("Tie!")
    time.sleep (2)
elif cpu == 3 and user == 2:
    print("You chose Paper!")
    time.sleep (2)
    print()
    print("The CPU chose Scissor!")
    time.sleep (2)
    print()
    print("You Lose!")
    time.sleep (2)
elif user > 3:
    print("Invaild Choice")
    time.sleep (2)
print()
print("Thanks for playing!")
time.sleep (2)

# Rock,Paper,Scissor ver. 2
 #  Raymon Shields
  # 12/14/2023

exit()