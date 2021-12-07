#python

# by: ilya segal

# Purpose: 2 players take turns rolling a die - 6-sided
# the first player to total rolls to 21 or greater loses.
# a player can pass a roll but only 3 times
# Preconditions: player names (strings), decisions to roll or pass (strings)
# Postconditions: prompts, display of totals and pass counts, rolls of the die
#      statement of who wins
#
#---------------------------------------------------------- main function

#---------------------------------------------------------- 
# main function
# import random libary
from random import *
def main():
    # intialize = 0
    player1_rollTotal = 0
    player2_rollTotal = 0
#  passcounts set to 3 (number of passes available at start)
    player1_passCount = 3
    player2_passCount = 3
    
#  initialize round counter to 1
    roundCount = 1
    
    # the title of the game and a newline
    
    print ("Don't get to 21!\n\n")
        # rules:
    print("Each player tries not to get to 21")
    
    print("Each player has 3 passes, which allow them to not roll on a round.\n")
    
    #  get player1 and player2 name
    player1 = input("Who is player 1? ")
        
    player2 = input("Who is player 2? ")
    
    
    
#  while both totals are < 21
    while player1_rollTotal < 21 and player2_rollTotal < 21:
        
#      display round counter
        print ("\nRound ", roundCount,":")
        
        # ask user if they pass or roll:
        #result1 = pass_or_roll(player1)
        
        #result2 = pass_or_roll(player2)
        
        #pass_or_roll(player1)
        
        #pass_or_roll(player2)
        
#      play a turn for player 1
        # call the function:
        
        name1 = play_turn( player1, player1_rollTotal, player1_passCount )
        player1_rollTotal = name1[0]
        player1_passCount = name1[1]
#      if player 1's total is < 21
        if player1_rollTotal < 21:
            
            
#           play a turn for player 2
            name2 = play_turn(player2, player2_rollTotal, player2_passCount)
            player2_rollTotal = name2[0]
            player2_passCount = name2[1]
            
#      increment round counter # not able to see roll and not able to see roll count # and each person's roll total is wrong!!
            roundCount += 1
#      display info for both players
            print( player1, "total roll", player1_rollTotal, "pass ", player1_passCount, "\t|\t", player2,"total roll", player2_rollTotal, "pass ",player2_passCount)
            
#  announce who won (roll tot < 21)

        #if player1Name 
        # fix ( i need to say if player 1's == 21 ) then display that player 2 won
        
        # fix ( else player 1 won)
    if player1_rollTotal  >= 21: # fix*
            
        print ("\n", player2, "won!")
        
    else:

        print ("\n", player1, "won!")
            
    # function 1:
 #------------------------------------------------------------ 
 # play_turn function
#Purpose: to do one player's turn, performing rolls or passes as player chooses
#Precondition: player name (string), player roll total (int), player's pass count (int)
#Postcondition: player roll total and player's pass count, both int, modified as needed
#  if player passed, pass count reduced, if player rolled, roll total increased

def play_turn(name, rollTotal, passCount): # lots of x fix !
    
#    if the players still has at least 1 pass
    if passCount > 0:
        
        ask = pass_or_roll(name)
        
#       ask do you want to roll or pass 
        #ask = input("Player "+ name + "(P)ass or (R)oll? ")
        #if they choose roll, 
        if ask.upper() == "R":
            # roll a die 
            roll = randint(1,6)
            rollTotal += roll
            print(name + " rolled ", roll) # fix
        #elif ask.upper() == "P":
            
            # otherwise roll a die and add to total (ran out of passes)
        else:
            print(name + "passed the roll\n")
            passCount -= 1
            #roll a die
            roll = randint(1,6)
            #add roll to roll total
            rollTotal += roll
            # display roll to players
            print(name+" rolled a ",roll)
    # may not be necesary to pass the dice, if the player ran out of dice.
    #else:
        # out of pass: so force the roll:
     #   roll = randint(1,6)
     #   rollTotal += roll
     #   print(name + "passed the roll\n")
     #   print(name+" rolled a ",roll)
        
    # returns total roll, passcount   
    return rollTotal, passCount
#           add roll to roll total
#           display roll to players

    # function 2:
    
#------------------------------------------------------- 
# pass_or_roll function


#Purpose: ask the player (pname) whether they want to pass the die or roll
# invalid answers are rejected until the player enters either P or R
#   upper or lower case
#precondition: the player's name (string)
#postcondition: either P or R (string) based on player's answer (always uppercase)
def pass_or_roll( name ):
#   
#     prompt the player P or R using player's name
    promptUser = input("Player "+ name+" (P)ass or (R)oll? ".upper())
    
    #promptUser = input("Player",player2Name,"(P)ass or (R)oll? ".upper())
    
#     get the player's answer
    #answer = promptUser
#     make it uppercase
    #answer = promptUser.upper()
#     while the answer is not valid
    while promptUser.upper() != "R" and promptUser.upper() != "P":
        
#        display error message
        print("Invalid response, P or R please")
        
        # get the player's answer
        # make it uppercase
        promptUser = input("Player "+name+ " (P)ass or (R)oll? ".upper())
        
        #promptUser = input("Player",player2Name,"(P)ass or (R)oll? ".upper())

#     return the player's answer
    return promptUser.upper()
main()
