
#Conditional Statements
 
print("welcome to the rollercoaster")
height=int(input("what is your height in cm?"))
if height>=120:
    print("you can ride the rollercoaster")
    age=int(input("what is your age?"))
    if age<12:
        print("please pay 5$")
    elif age<=18:
       print("please pay 7$")
    else:
        print("please pay 12$")
        
else:
    print("sorry,you have to grow taller before you can ride.")

# project 1

j=int(input("enter a number"))
if j % 2==0:
    print("This is an even number")
else:
    print("This is an odd number")
    
    #Body mass index

height=input("enter your height in m\n")
weight=input("enter your weight in kg\n")
height=float(height)
height=height**2
weight=float(weight)
BMI=weight/height
if BMI<18.5:
 print("You are underweight")
elif BMI<25:
    print("You have a normal weight")
elif BMI<30:
    print("you are over weight")
elif BMI<35:
    print("You are obese")
else:
    print("You are clinically obese")
    
    #calculating if a year is a leap year or not
    
year=int(input("input the year you wanted to check"))
if year%4==0:
 if year%100==0:
   if year%400==0: 
    print("It is a leap year")
   else:
       print("Not a leap year")
 else:
     print("It is a leap year")  
else:
    print("Not a leap year")
    
    
    print("welcome to the rollercoater")
height=float(input("Enter your height(in meters) "))
age=int(input("enter your age" ))
photo=input("Do you want a photo for your rollercoster? Enter yes or no ")
if height>=120:
    print("you can ride")
    if age<12:
     price=5
    elif age<=18:
     price=7
    elif age<45:
     price=12
    elif age>=45:
        price=0
        print("Rollercoster is free for you")
    if photo=="yes":
     if age<12:
         print(f"your bill is {price+3}$")
     if age<=18:
         print(f"your bill is {price+3}$") 
     if age<45:
         print(f"your bill is {price+3}$")
     if age>=45:
         print(f"your bill is {price+0}$")
    else:
        print(f" your bill is {price}$ ")   
else:
    print("Sorry,you cant ride a rollercoster-You have to grow taller!")
    
print("Welcome to python pizza diliveries")
size=input("What size of pizza will you like to have? enter small, medium or large: ")
peperoni=input("would you like to add peperoni? enter yes or no: ")
extral_chesse=input("would you like to add extral cheese? enter yes or no: ")
if size=="small":
        bill=15
        peperoni_bll=2
        extralchesse_bill=1
        if peperoni=="yes":
         if extral_chesse=="yes":
                 print(f"your bill is {bill+extralchesse_bill+peperoni_bll}$ THANKS FOR YOUR PARTRONAGE")
         else:
                 print(f"your bill is {bill+peperoni_bll}$ THANKS FOR YOUR PATRONAGE")
        else:
                print(f"your bill is {bill+extralchesse_bill}$ THANKS FOR YOUR PATRONAGE")
elif size=="medium":
        bill=20
        peperoni_bll=3
        extralchesse_bill=1
        if peperoni=="yes":
          if extral_chesse=="yes":
                  print(f"your bill is {bill+peperoni_bll+extralchesse_bill}$ THANKS FOR YOUR PATRONAGE")
          else:
                  print(f"your bill is {bill+peperoni_bll}$ THANKS FOR YOUR PATRONAGE")
        else:
                print(f"your bill is {bill+extralchesse_bill}$ THANKS FOR YOUR PATRONAGE")
else:
    bill =25
    peperoni_bll=3
    extralchesse_bill=1
    if peperoni=="yes":
     if extral_chesse=="yes" :
             print(f"your bill is {bill+peperoni_bll+extralchesse_bill}$ THANKS FOR YOUR PATRONAGE")
     else:
             print(f"your bill is {bill+peperoni_bll}$ THANKS FOR YOUR PATRONAGE")                                                                     
    else:
            print(f"your bill is {bill+extralchesse_bill}$ THANKS FOR YOUR PATRONAGE") 

    
    #love calculator print("welcome to the love calculator")=input("enter your lover's name ")
    
    your_name=input("Enter your name")
    your_name .lower()
    print(your_name)
    
heigh=float(input("Enter your height"))
if heigh>=120:
    print("can ride")
    agi=int(input("enter your age"))
    if agi<12:
        bill=5
        print("your price is 5$")
    elif agi <=18:
        bill=7
        print("pay 7$") 
    else:
        bill=12
        print("pay 12$") 
    want_photo=input("do you want photo? enter yes or no  ")
    if want_photo=="yes":
        new_bill=bill+3
        print(f"your new bill is {new_bill}$,THANKS FOR YOUR PATRONAGE!")
    else:
        print(f"your bill is {bill}$,THANKS FOR YOUR PATRONAGE!")
else:
    print("you cant ride")
    
your_name=input("Enter your name ")
your_lovers_name=input("Enter your lover's name ")
combined_name=your_name+your_lovers_name
lowercase=combined_name.lower()
t=lowercase.count("t")
r=lowercase.count("r")
u=lowercase.count("u")
e=lowercase.count("e")
l=lowercase.count("l")
o=lowercase.count("o")
v=lowercase.count("v")
e=lowercase.count("e")

true=t+r+u+e

love=l+o+v+e

LOVESCORE=str(true)+str(love)

LOVESCORE=int(LOVESCORE)

if LOVESCORE<=39:
    print("YOU CAN NOT BE TOGETHER")
elif LOVESCORE<=45:
    print("YOU ARE NOT LIKELY TO BE TOGETHER")
elif LOVESCORE<=50:
    print("YOU CAN BE TOGETHER IF YOURE LUCKY")
elif LOVESCORE<=60:
    print("YOU ARE LIKELY TO BE TOGETHER")
elif LOVESCORE<=75:
    print("YOU ARE MOST LIKELY TO BE TOGETHER")
else:
    print("YOU ARE MEANT FOR EACH OTHER,CONGRATULATIONS!!!")              


#TREASURE FINDER GAME

print("WELCOME TO TREASURE ISLAND\nYOUR MISSION IS TO FIND THE TREASURE")
direction=input("would you like to go left or right? Enter ")
lower=direction.lower()
if lower==("left"):
 print("do you want to swim or wait for a boat? ")
 s=input("swim or wait")
 lowers=s.lower()
 if lowers=="wait":
   print("which door did you want to open?")
   door=input("enter red or yellow or blue")
   lowerd=door.lower()
   if lowerd=="red" or "blue":
       print("Game Over")
   else:
       print("CONGRATULATION YOU FOUND THE TREASURE")
 else:
     print("Game Over")
else:
    print("Game Over")