#debuggin
def my_function():
    for i in range(1, 21):
        if i == 20:
            print("you got it")
#for i to reach 20 in the range, then the upper limit should be set ti 21
#if i is  20 then it is a bug

#bug 2

from random import randint
dice=["1", "2", "3", "4", "5", "6"]
dice_num=randint(0, 5)
print(dice[dice_num])

# if 1,6 was used in the rand int funcrion occationally there would be an error


#bug 3
year=int(input("what is your year of birth"))
if year>1980 and year<1994:
    print("you are a millenia")
elif year>=1994:
    print("you are a gen z")
    


#bug 4

age=int(input("How old are you?"))
if age>18:
    print(f"you can drive at age {age}")
    

#bug 5
number= int(input("which number do you want to check."))
if number %2==0:
    print("This is an even number")
else:
    print("This is an odd number")
   
   
   #bug 6

year=int(input("which year do you want to check?"))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("leap year")
        else:
            print("Not a leap year")
    else:
        print("Leap year")
else:
    print("Not a leap year")
    
     
    
    

       
    

             
        
    
    