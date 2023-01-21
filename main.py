#imrancoding
from Dices import dice,diceone,dicetwo,dicethree,dicefour,dicefive,dicesix
print("""
Created by imrancoding

0.Normal
1.More chances get 1
2.More chances get 2
3.More chances get 3
4.More chances get 4
5.More chances get 5
6.More chances get 6
""")
try:
    inp=int(input("Choose anyone dice: "))

    if inp==0:
        while True:
            i=input("Press any key to roll dice: ")
        print(dice.dice())
    elif inp==1:
        while True:
            i=input("Press any key to roll dice: ")
            print(diceone.dice_one())
    elif inp==2:
        while True:
            i=input("Press any key to roll dice: ")
            print(dicetwo.dice_two())
    elif inp==3:
        while True:
            i=input("Press any key to roll dice: ")
            print(dicethree.dice_three())
    elif inp==4:
        while True:
            i=input("Press any key to roll dice: ")
            print(dicefour.dice_four())
    elif inp==5:
        while True:
            i=input("Press any key to roll dice: ")
            print(dicefive.dice_five())
    elif inp==6:
        while True:
            i=input("Press any key to roll dice: ") 
            print(dicesix.dice_six()) 
    else:
        print("Wrong input!") 
except ValueError:
    print("Wrong input!")