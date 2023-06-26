#functions

def greet():
    
    print("Hello")
    print("How do you do")
    print("Is the weather not nice today?")
    
#Functions that allows for input

def greet_with_name(name):
    print(f"Hello{name}")
    print(f"How do you do {name}")
greet_with_name("Billie")



#Function with more than one input

def greet_with(name, location):
   print(f"Hello {name}")
   print(f"what is it like in {location}")
   
   greet_with("jack Bauer, Nowhere")
   
   
   #Function with keyword arguments
   
   greet_with(location="London", name="Angella")
   
   
   
#PAINT CHALLENGE

import math 

    
def paint_calc(height, width, cover):
   area=height*width
   num_of_cans=math.ceil(area / cover) 
   
   print(f"you'll need {num_of_cans} cans paint")  
   
   test_h=int(input("Height of wall:"))
   test_w=int(input("width of wall:"))
   coverage=5
   paint_calc(height=test_h, width=test_w, cover=coverage)
   
   
   #PRIME NUMBER CHEACKER
   
   def prime_cheacker(number):
       is_prime= True
       for i in range(2,number-1):
           if number%i==0:
               is_prime = False
       if is_prime: 
           print("It is a prime number")
       else:
           print("It is not a prime number")      
           
           
           
           #CEASER CIPHER [ENCODING]
           
alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']         
           
direction= input("type 'encode' to encrypt, type 'decode' to decrypt:\n")
text=input("Type your mesage:\n").lower()
shift=int(input("Type the shift number:\n"))
def encrypt(plain_text, shift_amount):
 for letter in plain_text:
  position= alphabet.index(letter)
  new_position= position + shift_amount  
  new_letter=alphabet[new_position]
  cipher_text+= new_letter
  print(f"The encoded text is {cipher_text}")
  
  
  encrypt(plain_text=text, shift_amount=shift)
  
    
     
        
               
               
      #CEASER CIPHER [DECODING] 
      
def decrypt(cipher_text, shift_amount):
  for letter in cipher_text:
      position=alphabet.index(letter)
      new_position= position-shift_amount
      plain_text += alphabet[new_position]     
      print(f"The decoded text is {plain_text}")  
      
if direction=="encode":
    encrypt(plain_text=text, shift_amount=shift)
elif direction == "decode":  
  decrypt(cipher_text=text, shift_amount=shift)    
     
      
      