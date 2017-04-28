#!/usr/bin/python3.5
#-*-coding:utf-8 -*

from pathlib import Path
import pickle
from obj import SnakeClasses as cls
from obj import SnakeFrame as fr
import os

defaultArena = cls.Arena()
defaultSnake = cls.Snake()
defaultKeybinding = cls.Keybinding()

objectsFile = Path("src/obj/Snake.objects")
if not objectsFile.is_file():  # Check if Snake.objects exists in src/obj/
    with open("src/obj/Snake.objects","wb") as settings:
        pickler = pickle.Pickler(settings) # Use a Pickler to asve the object into the file
        pickler.dump(defaultArena)
        pickler.dump(defaultSnake)
        pickler.dump(defaultKeybinding)


with open("src/obj/Snake.objects","rb") as settings: # Open the Snake.objects in order to extract the objects stored and potentially modify them
    unpickler = pickle.Unpickler(settings)
    loadedArena = unpickler.load()
    loadedSnake = unpickler.load()
    loadedKeybinding = unpickler.load()

def whereIsSnake(length,headPos,direction):
    response = [headPos]
    for i in range(1,length):
        response.append((headPos[0] + (i * direction[0] * -1), headPos[1] + (i * direction[1] * -1)))
    return response

def canSnakeBeHere(snakePos,arenaWidth,arenaHeight):
    for i in snakePos:
        if i[0] <= 1 or i[0] >= arenaWidth:
            return False
        elif i[1] <= 1 or i[1] >= arenaHeight:
            return False
    return True

def whatDirectionIsIt(direction):
    if direction == (0,-1):
        return "UP"
    elif direction == (0,1):
        return "DOWN"
    elif direction == (-1,0):
        return "LEFT"
    elif direction == (1,0):
        return "RIGHT"

quitRequested = False

while quitRequested != True:

    valueQuery = False # (Re)set the variable

    os.system("clear") # Clear the terminal

    # Draw the game the objects
    frame = fr.Frame(loadedArena,loadedSnake)
    frame.draw()

    # Displays the menu :
    print("Arena:")
    print("\t1. Width (", loadedArena.width, ")", sep="")
    print("\t2. Height (", loadedArena.height, ")", sep="")
    print("\t3. Border (", loadedArena.border, ")", sep="")
    print("\nSnake:")
    print("\t4. Length (", loadedSnake.length, ")", sep="")
    print("\t5. Head (", loadedSnake.head, ")", sep="")
    print("\t6. Body (", loadedSnake.body, ")", sep="")
    print("\t7. Speed (", loadedSnake.speed, ")", sep="")
    print("\t8. Position (x=", loadedSnake.pos[0][0], ", y=", loadedSnake.pos[0][1], ")", sep="")
    print("\t9. Direction (", whatDirectionIsIt(loadedSnake.direction), ")", sep="")
    print("\nApple:")
    print("\t10. Appareance (", loadedArena.Apple, ")", sep="")
    print("\nKeybinding:")
    print("\t11. Up (", loadedKeybinding.up, ")", sep="")
    print("\t12. Down (", loadedKeybinding.down, ")", sep="")
    print("\t13. Left (", loadedKeybinding.left, ")", sep="")
    print("\t14. Right (", loadedKeybinding.right, ")", sep="")

    print("\n\n\t15. Set everything to default")
    print("\t16. Save and quit")
    print("\t17. Quit without saving")

    rubricReq = input("\nEnter the number of the rubric : ") # Get user input and check if it's correct via the try block beyond here
    try:
        rubricReq = int(rubricReq)
    except ValueError:
        print("Please enter an integer between 1 and 17 (both included).")
    else:
        if rubricReq in range(1,18):
            while valueQuery != True:

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------#

                if rubricReq == 1: # Width
                    print("\nWidth of the Arena (borders included) is currently set to", loadedArena.width)
                    newValue = input("Enter the new value (press only ENTER to set it to default) : ")
                    if newValue == "":
                        newPosition = whereIsSnake(loadedSnake.length,(defaultSnake.pos[0][0],loadedSnake.pos[0][1]),loadedSnake.direction)
                        if canSnakeBeHere(whereIsSnake(loadedSnake.length,newPosition[0],loadedSnake.direction),defaultArena.width,loadedArena.height):
                            loadedArena.width = defaultArena.width
                            loadedSnake.pos = newPosition
                            valueQuery = True
                        else:
                            print("An Arena of this width can't contain your Snake, please enter a valid width or change the height, length, position or direction values.")
                    else:
                        try:
                            newValue = int(newValue)
                        except ValueError:
                            print("Please enter an integer number.")
                        else:
                            if newValue > 2:
                                if newValue % 2 == 0:
                                    newPosition = whereIsSnake(loadedSnake.length,(newValue / 2,loadedSnake.pos[0][1]),loadedSnake.direction)
                                else:
                                    newPosition = whereIsSnake(loadedSnake.length,(newValue // 2 + 1,loadedSnake.pos[0][1]),loadedSnake.direction)
                                if canSnakeBeHere(whereIsSnake(loadedSnake.length,newPosition[0],loadedSnake.direction),newValue,loadedArena.height):
                                    loadedArena.width = newValue
                                    loadedSnake.pos = newPosition
                                    valueQuery = True
                                else:
                                    print("An Arena of this width can't contain your Snake, please enter a valid width or change the height, length, position or direction values.")
                            else:
                                print("The arena's width must be at least equal to 3.")

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------#

                elif rubricReq == 2: # Height
                    print("\nHeight of the Arena (borders included) is currently set to", loadedArena.height)
                    newValue = input("Enter the new value (press only ENTER to set it to default) : ")
                    if newValue == "":
                        newPosition = whereIsSnake(loadedSnake.length,(loadedSnake.pos[0][0],defaultSnake.pos[0][1]),loadedSnake.direction)
                        if canSnakeBeHere(whereIsSnake(loadedSnake.length,newPosition[0],loadedSnake.direction),loadedArena.width,defaultArena.height):
                            loadedArena.height = defaultArena.height
                            loadedSnake.pos = newPosition
                            valueQuery = True
                        else:
                            print("An Arena of this height can't contain your Snake, please enter a valid height or change the width, length, position or direction values.")
                    else:
                        try:
                            newValue = int(newValue)
                        except ValueError:
                            print("Please enter an integer number.")
                        else:
                            if newValue > 2:
                                newPosition = whereIsSnake(loadedSnake.length,(loadedSnake.pos[0][0],newValue - (loadedSnake.length + 1)),loadedSnake.direction)
                                if canSnakeBeHere(whereIsSnake(loadedSnake.length,newPosition[0],loadedSnake.direction),loadedArena.width,newValue):
                                    loadedArena.height = newValue
                                    loadedSnake.pos = newPosition
                                    valueQuery = True
                                else:
                                    print("An Arena of this height can't contain your Snake, please enter a valid height or change the width, length, position or direction values.")
                            else:
                                print("The arena's height must be at least equal to 3.")

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------#

                elif rubricReq == 3: # Border
                    print("\nBorder of the Arena is currently set to", loadedArena.border)
                    newValue = input("Enter the new value (press only ENTER to set it to default) : ")
                    if newValue == "":
                        loadedArena.border = defaultArena.border
                    else:
                        loadedArena.border = newValue[0]
                    valueQuery = True

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------#

                elif rubricReq == 4: # Length
                    print("\nLength of the Snake currently set to", loadedSnake.length)
                    newValue = input("Enter the new value (press only ENTER to set it to default) : ")
                    if newValue == "":
                        if canSnakeBeHere(whereIsSnake(defaultSnake.length,loadedSnake.pos[0],loadedSnake.direction),loadedArena.width,loadedArena.height):
                            loadedSnake.length = defaultSnake.length
                            loadedSnake.pos = whereIsSnake(defaultSnake.length,loadedSnake.pos[0],loadedSnake.direction)
                            valueQuery = True
                        else:
                            print("A Snake of this length will start into a wall, please enter a valid length or change the width, height, position or direction values.") 
                    else:
                        try:
                            newValue = int(newValue)
                        except ValueError:
                            print("Please enter an integer number.")
                        else:
                            if newValue > 0:
                                if canSnakeBeHere(whereIsSnake(newValue,loadedSnake.pos[0],loadedSnake.direction),loadedArena.width,loadedArena.height):
                                    loadedSnake.length = newValue
                                    loadedSnake.pos = whereIsSnake(newValue,loadedSnake.pos[0],loadedSnake.direction)
                                    valueQuery = True
                                else:
                                    print("A Snake of this length will start into a wall, please enter a valid length or change the width, height, position or direction values.")
                            else:
                                print("Snake's length mus t be at least equal to 1.")

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------#

                elif rubricReq == 5: # Head
                    print("\nHead of the Snake currently set to", loadedSnake.head)
                    newValue = input("Enter the new value (press only ENTER to set it to default) : ")
                    if newValue == "":
                        loadedSnake.head = defaultSnake.head
                    else:
                        loadedSnake.head = newValue[0]
                    valueQuery = True

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------#

                elif rubricReq == 6: # Body
                    print("\nBody of the Snake currently set to", loadedSnake.body)
                    newValue = input("Enter the new value (press only ENTER to set it to default) : ")
                    if newValue == "":
                        loadedSnake.body = defaultSnake.body
                    else:
                        loadedSnake.body = newValue[0]
                    valueQuery = True

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------#

                elif rubricReq == 7: # Speed
                    print("\nSpeed of the Snake currently set to ", loadedSnake.speed, ". The number represents the number of characters the Snake can move every second.", sep="")
                    newValue = input("Enter the new value (press only ENTER to set it to default) : ")
                    if newValue == "":
                        loadedSnake.speed = defaultSnake.speed
                        valueQuery = True
                    else:
                        try:
                            newValue = float(newValue)
                        except ValueError:
                            print("Please enter a float number.")
                        else:
                            if newValue > 0:
                                loadedSnake.speed = newValue  
                                valueQuery = True
                            else:
                                print("Speed can't be 0 or less.")

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------#

                elif rubricReq == 8: # Position
                    print("\nPosition of the Snake currently set to x=", loadedSnake.pos[0][0], " and y=", loadedSnake.pos[0][1], sep="")
                    newValueX = input("Enter the new x value (press only ENTER to set it to default) : ")
                    if newValueX == "":
                        newValueY = input("Enter the new y value (press only ENTER to set it to default) : ")
                        if newValueY == "": # Both are default
                            if canSnakeBeHere(whereIsSnake(loadedSnake.length,defaultSnake.pos[0],loadedSnake.direction),loadedArena.width,loadedArena.height):
                                loadedSnake.pos = defaultSnake.pos
                                valueQuery = True
                            else:
                                print("Your Snake starting in this position will spawn into a wall, please enter a valid position or change the width, height, length or direction values.")
                        else: # X is default while Y isn't
                            try:
                                newValueY = int(newValueY)
                            except ValueError:
                                print("Please enter an integer number.")
                            else:
                                if newValueY > 1:
                                    if canSnakeBeHere(whereIsSnake(loadedSnake.length,(defaultSnake.pos[0][0],newValueY),loadedSnake.direction),loadedArena.width,loadedArena.height):
                                        loadedSnake.pos = whereIsSnake(loadedSnake.length,(defaultSnake.pos[0][0],newValueY),loadedSnake.direction)
                                        valueQuery = True
                                    else:
                                        print("Your Snake starting in this position will spawn into a wall, please enter a valid position or change the width, height, length or direction values.")
                                else:
                                    print("The values of position have to be at least equal to 2.")
                    else: # X isn't default
                        try:
                            newValueX = int(newValueX)
                        except ValueError:
                            print("Please enter an integer number.")
                        else:
                            newValueY = input("Enter the new y value (press only ENTER to set it to default) : ")
                            if newValueY == "": # X isn't default while Y is
                                if newValueX > 1:
                                    if canSnakeBeHere(whereIsSnake(loadedSnake.length,(newValueX,defaultSnake.pos[0][1]),loadedSnake.direction),loadedArena.width,loadedArena.height):
                                        loadedSnake.pos = whereIsSnake(loadedSnake.length,(newValueX,defaultSnake.pos[0][1]),loadedSnake.direction)
                                        valueQuery = True
                                    else:
                                        print("Your Snake starting in this position will spawn into a wall, please enter a valid position or change the width, height, length or direction values.")
                                else:
                                    print("The values of position have to be at least equal to 2.")
                            else: # Both are not default
                                try:
                                    newValueY = int(newValueY)
                                except ValueError:
                                    print("Please enter an integer number.")
                                else:
                                    if newValueX > 1 and newValueY > 1:
                                        if canSnakeBeHere(whereIsSnake(loadedSnake.length,(newValueX,newValueY),loadedSnake.direction),loadedArena.width,loadedArena.height):
                                            loadedSnake.pos = whereIsSnake(loadedSnake.length,(newValueX,newValueY),loadedSnake.direction)
                                            valueQuery = True
                                        else:
                                            print("Your Snake starting in this position will spawn into a wall, please enter a valid position or change the width, height, length or direction values.")
                                    else:
                                        print("The values of position have to be at least equal to 2.")

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------#

                elif rubricReq == 9: # Direction
                    print("\nSnake will start moving", whatDirectionIsIt(loadedSnake.direction))
                    newValue = input("Enter the new value (press only ENTER to set it to default) (Choices: UP, DOWN, LEFT, RIGHT) : ")
                    if newValue == "":
                        if canSnakeBeHere(whereIsSnake(loadedSnake.length,loadedSnake.pos[0],defaultSnake.direction),loadedArena.width,loadedArena.height):
                            loadedSnake.direction = defaultSnake.direction
                            loadedSnake.pos = whereIsSnake(loadedSnake.length,loadedSnake.pos[0],defaultSnake.direction)
                            valueQuery = True
                        else:
                            print("Your Snake starting in this direction will spawn into a wall, please enter a valid direction or change the width, height, length or position values.")
                    else:
                        if newValue in ["UP","DOWN","LEFT","RIGHT"]:
                            if newValue == "UP":
                                newDirection = (0,-1)
                            elif newValue == "DOWN":
                                newDirection = (0,1)
                            elif newValue == "LEFT":
                                newDirection = (-1,0)
                            elif newValue == "RIGHT":
                                newDirection = (1,0)
                            if canSnakeBeHere(whereIsSnake(loadedSnake.length,loadedSnake.pos[0],newDirection),loadedArena.width,loadedArena.height):
                                loadedSnake.direction = newDirection
                                loadedSnake.pos = whereIsSnake(loadedSnake.length,loadedSnake.pos[0],newDirection)
                                valueQuery = True
                            else:
                                print("Your Snake starting in this direction will spawn into a wall, please enter a valid direction or change the width, height, length or position values.")
                        else:
                            print("This isn't a correct value. The choices are : UP / DOWN / LEFT / RIGHT")
                                                        
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------#

                elif rubricReq == 10: # Apple
                    print("\nApple's apparence currently set to", loadedArena.Apple)
                    newValue = input("Enter the new value (press only ENTER to set it to default) : ")
                    if newValue == "":
                        loadedArena.Apple = defaultArena.Apple
                    else:
                        loadedArena.Apple = newValue[0]
                    valueQuery = True

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------#

                elif rubricReq == 11: # Up
                    print("\nMove the snake UP is currently set to", loadedKeybinding.up)
                    newValue = input("Enter the new key you want to use (press only ENTER to it to default) : ")
                    if newValue == "":
                        loadedKeybinding.up = defaultKeybinding.up
                    else:
                        loadedKeybinding.up = newValue
                    valueQuery = True

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------#

                elif rubricReq == 12: # Down
                    print("\nMove the snake DOWN is currently set to", loadedKeybinding.down)
                    newValue = input("Enter the new key you want to use (press only ENTER to it to default) : ")
                    if newValue == "":
                        loadedKeybinding.down = defaultKeybinding.down
                    else:
                        loadedKeybinding.down = newValue
                    valueQuery = True

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------#

                elif rubricReq == 13: # Left
                    print("\nMove the snake LEFT is currently set to", loadedKeybinding.left)
                    newValue = input("Enter the new key you want to use (press only ENTER to it to default) : ")
                    if newValue == "":
                        loadedKeybinding.left = defaultKeybinding.left
                    else:
                        loadedKeybinding.left = newValue
                    valueQuery = True

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------#

                elif rubricReq == 14: # Right
                    print("\nMove the snake RIGHT is currently set to", loadedKeybinding.right)
                    newValue = input("Enter the new key you want to use (press only ENTER to it to default) : ")
                    if newValue == "":
                        loadedKeybinding.right = defaultKeybinding.right
                    else:
                        loadedKeybinding.right = newValue
                    valueQuery = True

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------#

                elif rubricReq == 15: # Set everything to default
                    loadedArena = defaultArena
                    loadedSnake = defaultSnake
                    loadedKeybinding = defaultKeybinding
                    valueQuery = True

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------#

                elif rubricReq == 16: # Save and quit
                    with open("src/obj/Snake.objects","wb") as settings:
                        pickler = pickle.Pickler(settings)
                        pickler.dump(loadedArena)
                        pickler.dump(loadedSnake)
                        pickler.dump(loadedKeybinding)
                    quitRequested = True
                    valueQuery = True

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------#

                elif rubricReq == 17: # Quit without saving
                    quitRequested = True
                    valueQuery = True
