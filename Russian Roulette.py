#Russian Roulette in Python!!!
#16th of April, 2026
#Tbh,I am really proud of this :3
#Plus it took me way less time than I anticipated,so thats a bonus!

import random
import time

#custom functions=========================

def adjustDifficulty(x): #x = difficulty level
    if x == 1:
        return 4
    elif x == 2:
        return 3
    else:
        return 2
        
def switchTurn(x): #x = playersTurn
    if playersTurn:
        return False
    else:
        return True
        

#variables================================

repeat = True
playersTurn = False #true - > player's turn/false - > opponent's turn
shootAtPlayer = True #true -> shoot at player/#false - > shoot at opponent
difficultyLevel = 1
chanceOfShootAtPlayer = 4
shotsTilBullet = 7 #7 is a placeholder
opponentsChoice = 1 # is a placeholder

#Game Loop================================

while repeat:
    print("Russian Roulette!")
    print("Options:")
    print("1 - Start Game")
    print("2 - Adjust Difficulty")
    print("3 - Exit")
    option = int(input("Your Option - "))
    print(" ")
    
    if option == 1: #game start
        # the setup
        print("Starting Game...")
        shotsTilBullet = random.randint(1,6)
        playersTurn = False #player always starts first
        
        #game loop
        while shotsTilBullet > 0:
            
            #turn taking
            playersTurn = switchTurn(playersTurn)
            
            #taking turns with the gun...
            if playersTurn:
                print("Current Turn : Yours")
                print("Options:")
                print("1 - Aim At Yourself")
                print("2 - Aim At Opponent")
                option = int(input("Your Option - "))
                if option == 1: #at yourself
                    print("You choose to aim it at yourself...")
                    shootAtPlayer = True
                elif option == 2: #at opponent
                    print("You choose to aim it at your opponent...")
                    shootAtPlayer = False
                else:
                    print("Thats no option.")
                    time.sleep(2)
                    print("Dumbass.")
                    time.sleep(2)
                    print("You choose to aim it at yourself...")
                    shootAtPlayer = True
            else: #opponent's turn
                print("Current Turn : Opponents")
                time.sleep(3)
                opponentsChoice = random.randint(1,chanceOfShootAtPlayer)
                if opponentsChoice == 1: #at you
                    print("Your opponent proceeds to aim it at you...")
                    shootAtPlayer = True
                else: #at themselves
                    print("Your opponent proceeds to aim it at themselves...")
                    shootAtPlayer = False
            
            #suspense...
            time.sleep(5)
            shotsTilBullet -= 1
            print(" ")
            
            #the result...
            if shotsTilBullet == 0: #bullet has been shot out
                print("BANG!!!")
                print(" ")
                time.sleep(2)
                if playersTurn:
                    if shootAtPlayer:
                        print("You fall to the ground,bleeding to death from your head...")
                        time.sleep(2)
                        print("You've died...")
                    else: #shoots at opponent
                        print("Your opponent drops back from their chair,blood oozing out from their skull...")
                        time.sleep(2)
                        print("You've won... but at what cost?")
                else: #opponents turn
                    if shootAtPlayer:
                        print("You fall to the ground,bleeding to death from your head...")
                        time.sleep(2)
                        print("You've died...")
                    else: #shoots at opponent
                        print("Your opponent drops back from their chair,blood oozing out from their skull...")
                        print("You've won... but at what cost?")
            else: #no bullet
                print("You can only hear the gun click...")
                print(" ")
        
        #game over...
        print(" ")
        time.sleep(3)
        print("Game Over...")
        time.sleep(5)
        print(" ")
        
    elif option == 2: #change difficulty
        print(f"Current Difficulty - {difficultyLevel}")
        print("Set Difficulty to:")
        print("1 - Easy")
        print("2 - Medium")
        print("3 - Hard")
        option = int(input("Your Option - "))
        if option < 4 and option > 0:
            difficultyLevel = option
            chanceOfShootAtPlayer = adjustDifficulty(difficultyLevel)
        else:
            print("Invalid Option :<")
    elif option == 3: #exit programme
        print("Quitting Program...")
        repeat = False
    else: #invalid input
        print("Invalid Input :(")
    print(" ")
