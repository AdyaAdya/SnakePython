#!/usr/bin/python3.5
#-*-coding:utf-8 -*

import threading as th
import obj.SnakeGetch as ge
import time

class InputManager(th.Thread):
    """Thread-inherit class that manage the user input during the game loop"""
    def __init__(self,specialKeys):
        th.Thread.__init__(self)
        self.isStopRequested = False
        self.lastKey = None
        self.specialKeys = specialKeys
        self.getch = ge._GetchUnix()

    def run(self):
        while not self.isStopRequested:
            keyPressed = self.getch()
            if keyPressed in self.specialKeys:
                self.lastKey = keyPressed

    def stop(self):
        self.isStopRequested = True
