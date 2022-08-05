import random
stages=['''
 +---+
 |   |
 0   |
/|\  |
/ \  |
     |
=======
''', '''
 +---+
 |   |
 0   |
/|\  |
/    |a
     |
======
''','''
 +---+
 |   |
 0   |
/|\  |
     |
     |
======iu
''','''
 +---+
 |   |
 0   |
/|   |
     | 
     |
======''','''
 +---+
 |   |
 0   |
 |   |
     |
     |
======
''','''
 +---+
 |   |
 0   |
     |
     |
======
''','''
 +---+
 |   |
     |
     | 
     |
======
''']
 
end_game=False
word_list=["about","arm","ask","shape","size","figure","same" ]
choose_word=random.choice(word_list)
word_len=len(choose_word)
#end_game=False
lives=6 
print(f'Pssst,the solution is {choose_word}.')
display=[]
for _ in range(word_len):
    display+="_"
while not end_game:
    guess=input("guess a letter:").lower()
    for position in range(word_len):
        letter=choose_word[position]
        #print(f"current position: {position}\n gussed letter:{letter}\n Guessed letter: {guess}")
        if letter==guess:
            display[position]=letter
    if guess not in choose_word:
        lives-=1
        if lives ==0:
            end_game=True
            print("you lose.")
    print(f"{' '.join(display)}")
    if "_" not in display:
        end_game=True
        print("you win")
    print(stages[lives])
       

        