# Name: Greg Smyth
# Homework MOOC Wk2
# wk2_rps.py
# 28th June 2013

print("MOOC Week 2 Homework")
print("Exercise 1.7")
player1 = raw_input("Player 1: ")
player2 = raw_input("Player 2: ")
win1="Player 1 wins"
win2="Player 2 wins"
tie="Tied game, why not play again?"
invalid="This is not a valid object selection"

if player1 == "Rock":
    if player2 == "Rock":
        result = tie
    elif player2 == "Paper":
        result=win2
    elif player2 == "Scissors":
        result=win1
    else: result = invalid
    
elif player1 == "Paper":
    if player2 == "Rock":
        result = win1
    elif player2 == "Paper":
        result=tie
    elif player2 == "Scissors":
        result=win2
    else: result = invalid

elif player1 == "Scissors":
    if player2 == "Rock":
        result = win2
    elif player2 == "Paper":
        result=win1
    elif player2 == "Scissors":
        result=tie
    else: result = invalid

else: result=invalid

print result
