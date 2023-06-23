#import random 

#test_seed=int(input("enter seed number"))
#random.seed(test_seed)


#random_side=random.randint(0,1)

#if random_side==0:
    #print("Heads")
#else:
    #print("Tails")
    

import random

names=input("enter your names separated by comma \n")

names_in_list=names.split(",")

non=len(names_in_list)
random_size=random.randint(0,non-1)
who_pays=names_in_list[random_size]
print(who_pays)




#rock paper scissors



user_choice= int(input("what do you want to choose? Type 0 for rock, 1 for scissors and 2 for scissors"))
computer_choice=random.randint(0,2)
if user_choice>= 3 or user_choice<0:
    print("you typed an invalid number, you lose")
if user_choice==0 and computer_choice==2:
    print("you win")
elif computer_choice==0 and user_choice==2:
    print("you lose")
elif computer_choice>user_choice:
    print("you win")
elif user_choice>computer_choice:
    print("you win")
elif computer_choice==user_choice:
    print("its a draw")
  
 






