# loops

#average height excercise

student_height=input("input a list of student heights")
for n in range(0, len(student_height)):
    student_height[n]=int(student_height[n])
    print(student_height)
    total_height=0
for height in student_height:
    total_height+=height
    
    number_of_students=0
    for student in student_height:
        number_of_students+=1
        
average_height=round(total_height/number_of_students)
print(average_height)   



#HIGHEST SCORE EXCERCISE

student_score=input("input a list of student score")
for n in range(0, len(student_score)):
    student_score[n]=int(student_score[n])
print(student_score)

heighest=0
for score in student_score:
    if score>heighest:
        heighest=score
print(f"The heighest score is {heighest}")



# Adding Evens Excercise

total=0
for number in range(2, 101, 2):
    total+=number
print(total)

total2=0
for number in range(1, 101):
    if number%2==0:
        total2+=number
print(total2)






# Fizz Buzz Buzz Excercise


for number in range(1, 101):
    if number%3==0 and number%5 ==0:
     print("FizzBuzz")
    elif number %3==0:
        print("Fizz")
    elif number %5==0:
        print("Buzz") 
    else:
      print(number)
            
            
            


#




import random
letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
numbers=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols=['!', '#', '$', '%', '&', '(', ' ', '*', '+', '_']
print("welcome to the pypasword gemerator")
nr_letters=int(input("how many letters would you like in your password?\n"))
nr_symbols=int(input(f"how many symbols would you like?\n"))
nr_numbers=int(input(f"how many numbers would you like in your password?\n"))



password=""
for char in range(1,nr_letters+1):
    
  password+=random.choice(letters)
  
  for char in range(1,nr_symbols):
      password+=random.choice(symbols)
  
  
  for char in range(1,nr_numbers):
      password+=random.choice(numbers)
      
      
      print(password)
       
      


