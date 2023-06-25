 #FUNCTION WITH OPUTPUTS
 
def format_name(f_name, l_name):
  if f_name== "" or l_name== "":
      return "You didnt provide a valid inputs"
  formated_f_name= f_name.title()
  formated_l_name= l_name.title()
  return f" Result: {formated_f_name} {formated_l_name}"
  
  
  print(format_name(input("what is your first name? ")))
  input("what is your last name? ")
  
  
 #DAYS IN A MONTH
 
def is_leap(year):
  if year%4==0:
    if year%100==0:
      if year%400==0:
        return True 
      else:
        return False
    else:
      return True
  else:
    return False
def days_in_month(year, month):

  month_days=[31, 28, 31, 30, 31, 30, 31, ]
  if is_leap(year) and month==2:
    return 29
  return month_days[month-1]
year=int(input("Ebter a year"))
month=int(input("Enter a month"))
days=days_in_month(year, month)
print(days)


#BUILDING MINI CALCULATOR

# Addition
def add(n1, n2):
  return n1 + n2

#Subtraction

def subtract(n1, n2):
  return n1-n2

#Multiplication

def multiply(n1, n2):
  return n1*n2

#Division

def divide(n1, n2):
  return n1/n2


operation={
 "+": add,
 "-": subtract,
 "*": multiply,
 "/": divide  
  
}



num1=int(input("what is the first letter: "))
num2=int(input("what is the second name? "))


for symbol in operation:
  print(symbol)
  
operation_symbol= input("pick an operation from the line above ")
calc_function = operation [operation_symbol]
answer = calc_function(num1, num2)


print(f"{num1} {operation_symbol} {num2} = {answer}") 
  
  
  

  
  
    

    
    