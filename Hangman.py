# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 23:29:38 2021

@author: robin
"""


# =============================================================================
#import json
#word = json.load(open("C:\\Users\\robin\\Desktop\\data.json"))
# =============================================================================

import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]

answer = random.choice(word_list)
lives = 6
num = len(answer)
fill_in = []

# for letter in answer:
#     fill_in.append("_")


while num > 0:
    fill_in.append("_")
    num -= 1
print(" ".join(fill_in))


End = False
while not End:
    guess = input("Give me your alphabet.\n")

#    if guess.lower() in answer:
#       uncover = [guess if guess == x else "_" for x in answer]
    
    for position in range(len(answer)):
        if guess.lower() == answer[position]:
            fill_in[position] = guess.lower()

#loop位置而不是list item，学习了！
            
    print(" ".join(fill_in))
    if guess.lower() not in answer:
        lives -= 1
        if lives == 0:
            End = True
            print("You lose.")
        print(stages[lives])
        print("Oops, try again.\n")
    
    if "_" not in fill_in:
        End = True
        print("You win.")




