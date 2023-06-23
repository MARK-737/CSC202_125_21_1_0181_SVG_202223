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
