#Gioco dell'impiccato
from stages import stages,logo
from wordList import word_list
import os
import random
print(logo)
#Estraggo a random una parola dalla lista di parole
secret_word=random.choice(word_list)
crypto_word_count=0
for secretNumber in range(len(secret_word)+1):
    crypto_word_count=secretNumber
  
print(f"Your secret answer is: {crypto_word_count * '*'} !!")
word_length=len(secret_word)

lives=6
end_of_game=False
display=[]

#Inserisco nel display gli underscore in numero uguale alle lettere
#che compongono la parola segreta
for _ in range(word_length):
    display.append("_")


#Creo un ciclo per chiedere all'utente di inserire una lettera
while not end_of_game:
    user_word=input("Guess a letter: ").lower()
    #Pulisco lo schermo ogni volta che l'utente inserisce una lettera
    os.system('cls')  
    #Se la lettera è già presente allora avverto l'utente in proposito
    if user_word in display:
            print(f"You have already guessed: {user_word} !\n")    
    
    #Verifico se la lettera è presente all'interno della mia parola segreta
    for position in range(word_length):
        letter=secret_word[position]
        if user_word in letter:
            display[position]=letter
         
    #Nel caso non fosse presente, l'utente perde una vita
    if user_word not in secret_word:
        lives-=1
        print(f"Ops!, the letter {user_word} is not in the secret word. You lose a life !!")
        
        
        #Se hai esaurito tutti i tentativi, hai perso !, il gioco finisce.
        if lives==0:
            print("You lose !")
            end_of_game=True
            
    print(f"{' '.join(display)}\n")       
    
    #Se ha completato la sequenza il gioco finisce, hai vinto !
    if "_" not in display:
        print("You Win !")
        end_of_game=True

    print(stages[lives])  
    

          