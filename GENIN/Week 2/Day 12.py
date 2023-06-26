#SCOPE
enemies=1

def increase_enemies():
    enemies=2
    print(f"enemies inside function: {enemies}")
    
    
    #LOCAL SCOPE
def drink_portion():
    portion_strenght=2
    print(portion_strenght)
drink_portion() 

#GLOBALSCOPE

player_health=10

def drink_portion():
    portion_strenght=2
    print(player_health)
    
drink_portion()



# There is no Block scope

game_level=3
def create_enemy():
  enemies=["skeleton","Zombie","Allien"]
  if game_level<5:
   new_enemy = enemies[0]
   print(new_enemy)
   


 #MODIFYING GLOBAL SCOPE
 
enemies= 1

def increase_enemies():
    print(f"enemies outside function: {enemies}")
    return enemies+1

    
enemies=increase_enemies()
print(f"enemies outside function {enemies}")

PI=3.14159
URL="https://www.google.com"
TWITTER_HANDLE= "m_jay59"




#NUMBER GUESSING GAME
from random import randint

EASY_LEVEL_TURNS=10
HARD_LEVEL_TURNS=5
turns=0
def check_answer(guess, answer, turns ):
    if guess> answer:
        print("too high")
        return turns-1
        
    elif guess< answer:
        print("Too low")
        return turns-1
    else:
        print(f"you got it! the answer was {answer}")

def set_difficulty():
    level = input("choose a difficulty. Type easy or hard")
    if level== "easy":
     global turns
     return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS
    
def game():            

 print("welcome to the guessing game")
 print("im thinking of  number between 1 and 100")
answer=randint(1, 100)
print(f"pssst, the correct answer is {answer}")


turns=set_difficulty()

guess=0
while guess != answer:
    print(f"you have {turns} attempt remaining to guess a number")
   
    guess=int(input("make a guess"))
    turns=check_answer(guess, answer, turns)
    if turns==0:
        print("youve run out of guesses, you lose")
    

(game)
     


    
