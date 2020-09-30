#!/usr/bin/python3

import random

char_lst = ["snake", "water", "gun"]
life = 1
score = 0
cscore = 0
print("<--------------------- Snake, Water and Gun Game --------------------->\n")

while life<=10:
    rand = random.choice(char_lst)
    print("\nChoose from snake, water or gun :")
    choice = input()
    if choice not in char_lst:
        print("Invalid Input! Try Again")
        continue
    else:
        if choice == "snake":
            if rand == "snake":
                print(rand,"- Match Tie!")
            elif rand == "water":
                score = score + 1
                print(rand,"- You Win!")
            else:
                cscore = cscore + 1
                print(rand,"- Computer Win!")
        elif choice == "water":
            if rand == "snake":
                cscore = cscore + 1
                print(rand,"- Computer Win!")
            elif rand == "water":
                print(rand,"- Match Tie!")
            else:
                score = score + 1
                print(rand,"- You Win!")
        else:
            if rand == "snake":
                score = score + 1
                print(rand,"- You Win!")
            elif rand == "water":
                cscore = cscore + 1
                print(rand,"- Computer Win!")
            else:
                print(rand,"- Match Tie!")
    print("Your Score :", score, "& Computer Score :",cscore,"                                            (",10 - life, "no. of life left )")
    life = life + 1

if life>10:
    print("Game Over!")
if score>cscore:
    print("Congrats You Won !")
elif score==cscore:
    print("Match Tie!")
else:
    print("You are a Losser !")
