#!/usr/bin/python3.5
#-*-coding:utf-8 -*

from pathlib import Path
import pickle
from obj import SnakeClasses as cls
from obj import SnakeThreads as th
from obj import SnakeFrame as fr
import os
import time



# Load game objects
defaultArena = cls.Arena()
defaultSnake = cls.Snake()
defaultKeybinding = cls.Keybinding()

objectsFile = Path("src/obj/Snake.objects")
if not objectsFile.is_file():  # Check if Snake.objects exists in src/obj/
    with open("src/obj/Snake.objects","wb") as objects:
        pickler = pickle.Pickler(objects) # Use a Pickler to asve the object into the file
        pickler.dump(defaultArena)
        pickler.dump(defaultSnake)
        pickler.dump(defaultKeybinding)

with open("src/obj/Snake.objects","rb") as objects: # Open the Snake.objects in order to extract the objects stored and potentially modify them
    unpickler = pickle.Unpickler(objects)
    arenaLoaded = unpickler.load()
    snakeLoaded = unpickler.load()
    keybindingLoaded = unpickler.load()


# Create user inputs manager object
userInput = th.InputManager(keybindingLoaded.getList())

# Start user input manager Thread-inherit object
userInput.start()


isQuitRequested = False
arena = cls.Arena()
snake = cls.Snake()


# Enter game loop
while not isQuitRequested:
    os.system("clear")

    # Declares needed variables
    isGameStopped = False
    newHeadPos = None
    keepLastPos = False
    arena.copyAttrFrom(arenaLoaded)
    snake.copyAttrFrom(snakeLoaded)
    frame = fr.Frame(arena,snake)
    stats = cls.Stats()


    # Draw first Frame
    frame.draw()


    # Countdown
    i = 0
    while i != 3:
        i += 1
        print(i, end="\r\n")
        time.sleep(1)


    while not isGameStopped:
        
        os.system("clear")

        # Check for user input
        if userInput.lastKey != None:
            if userInput.lastKey == keybindingLoaded.up and snake.direction != (0,1):
                snake.direction = (0,-1)
            elif userInput.lastKey == keybindingLoaded.left and snake.direction != (1,0):
                snake.direction = (-1,0)
            elif userInput.lastKey == keybindingLoaded.down and snake.direction != (0,-1):
                snake.direction = (0,1)
            elif userInput.lastKey == keybindingLoaded.right and snake.direction != (-1,0):
                snake.direction = (1,0)
            userInput.lastKey = None



        # Check if Snake is going to crash into a wall or its own body
        newHeadPos = (snake.pos[0][0] + snake.direction[0], snake.pos[0][1] + snake.direction[1])
        if newHeadPos in frame.get("border","body"):
           # Display score
            print("SCORE:", end="\r\n")
            print("Length of Snake:", snake.length, end="\r\n")
            print("Number of Apple eaten:", stats.appleEaten, end="\r\n")

            # Display the options
            print("\r\nTry Again ? ( Yes = ", keybindingLoaded.accept, " / No = ", keybindingLoaded.refuse, " )", sep="", end="\r\n")
            while True:
                if userInput.lastKey == keybindingLoaded.refuse:
                    isQuitRequested = True
                    isGameStopped = True
                    break
                elif userInput.lastKey == keybindingLoaded.accept:
                    isGameStopped = True
                    break
                time.sleep(0.1)
            if isGameStopped:
                break
        elif newHeadPos == frame.Apple:
            keepLastPos = True
            frame.spawnApple(arena.Apple)


        # Calculate new positions of Snake
        if not keepLastPos:
            snake.move()
        else:
            snake.moveAndGrow(stats)
            keepLastPos = False 



        # Change positions of Snake in the frame
        frame.moveSnake(snake)


        # Draw the new frame
        frame.draw()


        # Wait a certain amout of time (twice more if Snake is moving horizontally)
        if snake.direction in [(1,0),(-1,0)]:
            time.sleep(0.5/snake.speed)
        else:
            time.sleep(1/snake.speed)            
    

print("Bye :'( ... Press any key to quit ...", end="\r\n")
userInput.stop()
