#hpicking random words



word_list=["aedvark", "camel"]
import random

chosen_word=random.choice(word_list)

end_game=False
while not end_game:

 guess=input("Guess a letter: ").lower()
 for position in range(word_list):
     letter=chosen_word[position]
     print(f"current_position: {position}\n current letter: {letter}\n guessed letter:{guess}")
      
     display=[]
     if letter==guess:
        display[position]=letter
        
        print(display)
        
        
if " " not in display:
    end_game==True
    print("you win")

#hangman


print(f'pssst,the solution is{chosen_word},')


display=[]
word_lenght=len(chosen_word)
for _ in range(len(word_lenght)):
    display+=" "
    print(display)
    
    
    for position in range(word_lenght):
        letter=chosen_word[position]
        if letter==guess:
            display[position]=letter
    
    
print(display)


