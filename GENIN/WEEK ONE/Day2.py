#Data types

#strings
print("Hello"[4])
print("123"+"345")

#integers

print( 123 + 345)

#float
3.56
1.47


#Boolean

True
False
#Changing of data types-(int to string)
num_char=len(input("what is your name? \n"))
num_char=str(num_char)
print(type(num_char))
print("your name has "+num_char+"characters")

#int to string
A=1124
print(type(A))
A=str(A)
print(type(A))

#float to int
b=29.5
print(type(b))
b=int(b)

#string concatenation
print(str(70)+str(100))

#Exercise 1
#write a program that adds the digit in a 2 digit number e.g 
#if the input was 35 then the output should be 3+5=8

two_d=19
two_d=str(two_d)
a=(two_d[0])
b=(two_d[1])
a=int(a)
b=int(b)
print(a+b)


#python operators

6/3
2**3
5+4
2-8
print((3+3)-3+3-3)

#Body mass index

height=input("enter your height in m\n")
weight=input("enter your weight in m\n")
height=float(height)
height=height**2
weight=float(weight)
BMI=weight/height
print(f"your BMI is {BMI}")


#Rounding up of floats using round function

print(round(8/3,2))

#f-strings
hiegh=1.8
iswinning=True
score=10
print(f"your score is {score},your height is {hiegh},you are wining is{iswinning}")


#your life in weeks(project 3)

#create a programme using math and f-strings that tells us how
#many days,weeks and months we have left if we live untill 90
#years old

current_age=input("enter your current age\n")
current_age=int(current_age)
days=365
weeks=52
months=12
years=90
remaining_years=years-current_age
remaining_days=remaining_years*days
remaining_weeks=remaining_years*weeks
remaining_months=remaining_years*months
print(f"you have {remaining_days} days,{remaining_weeks} weeks,{remaining_months} months and {remaining_years} years left")



#project-4(tip calculator)

print("welcome to the tip calculator")
bill=float(input("what was the bill total "))
tip=int(input("How much tip would you like to give? 10,12, or 15?"))
people=int(input("How many people to split the bill?"))
tip_as_percent=tip/100
total_tip_amount=bill*tip_as_percent
total_bill=bill+total_tip_amount
bill_per_person=total_bill/people

final_amt=round(bill_per_person,2)
print(f"Each person should pay{final_amt} Naira")