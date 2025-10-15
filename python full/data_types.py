import random
import sys
a=input("Enter your option:\n 1.for rock \n 2.for paper\n 3.for scissor\n ")
player=int(a)
if player <1 or player >3:
    sys.exit("Enter 1,2,3")
b=random.choice("123")
print("com choose"+ b)
computer=int(b)
if player==1 and computer ==3:
    print("you win")
elif player==2 and computer==1:
    print("u win")
elif player==3 and computer==2:
    print("you win ")
elif player==computer:
    print("match draw")
else:
    print("computer win")