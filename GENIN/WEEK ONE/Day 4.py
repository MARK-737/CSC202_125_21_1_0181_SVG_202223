import random

names=input("enter your names separated by comma \n")

names_in_list=names.split(",")

non=len(names_in_list)
random_size=random.randint(0,non-1)
who_pays=names_in_list[random_size]
print(who_pays)

# TREASURE MAP

row1=["", "", ""]
row2=["", "", ""]
row3=["", "", ""]
map=[row1, row2, row3]
position=input("where you want to put the treasure")
horizontal=int(position[0])
vertical=int(position[1])
selected_row=map[horizontal-1]
selected_row[vertical-1]="X"
print(f"{row1}\n{row2}\n{row3}")





#ROCK-PAPER-SISSORS GAME

user_choice=int(input("what do you choose? Type o for rock, 1 for paper, or 2 for sissors"))
computer_choice=random.randint(0,2)
print(f"computer choose {computer_choice}")
if user_choice>=3 or user_choice<0:
    print("you typed an invalid number, Game Over")
elif user_choice==0 and computer_choice==2:
    print("you wins")
elif computer_choice==0 and user_choice==2:
    print("you lose")
elif computer_choice>user_choice:
    print("you lose")
elif user_choice>computer_choice:
    ptint("you win")
elif computer_choice==user_choice:
    print("ita a draw")    
 






