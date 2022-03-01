from art import vs, logo
from game_data import data
import random
import os

score = 0

def player(int):
  playerName = (data[int]['name'])
  follower_count = (data[int]['follower_count'])
  description = (data[int]['description'])
  country = (data[int]['country'])
  return playerName, follower_count, description, country

def compare(playerA, playerB, score):
    print(logo)
    if score > 0:
        print(f"You are right! Your current streak is {score}\n")
    print(f"{playerA[0]}, a {playerA[2]}, from {playerA[3]}")
    print(vs)
    print(f"{playerB[0]}, a {playerB[2]}, from {playerB[3]}")
    followerA = playerA[1]
    followerB = playerB[1]
    answer = input("Who has more followers? Type 'A' or 'B': ")
    if answer == 'A':
        if followerA >= followerB:
            score += 1
            #print(f"You are right! {playerA[0]} has {followerA} followers while {playerB[0]} has {followerB} your score is {score}")
            thirdInt = random.randint(0,49)
            personC = player(thirdInt)
            compare(playerB, personC, score)
        else: 
            #print(f"You are wrong! {playerA[0]} has {followerA} followers while {playerB[0]} has {followerB}")
            print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nYou are wrong! Your streak was {score} right.")

    if answer == 'B':
        if followerB >= followerA:
            score += 1
            #print(f"You are right! {playerA[0]} has {followerA} followers while {playerB[0]} has {followerB} your score is {score}")
            thirdInt = random.randint(0,49)
            personC = player(thirdInt)
            compare(playerB, personC, score)
        else: 
            print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nYou are wrong! Your streak was {score} right.")
    


stillPlaying = True



while stillPlaying == True:
    firstInt = random.randint(0,49)
    secondInt = random.randint(0,49)
    personA = player(firstInt)
    personB = player(secondInt)
    compare(personA, personB, 0)
    stillPlaying = False
    answer = input("Would you like to try again? Y/N: ")
    if answer == 'Y':
        stillPlaying = True
    else:
        print("Thanks for playing!")
