#!/usr/bin/python3.5
#-*-coding:utf-8 -*

class Arena():
    """Class containing informations loaded from user settings file on the Arena"""
    def __init__(self,arena=None,width=47,height=23,border="#",Apple="x"):
        self.width = width
        self.height = height
        self.border = border
        self.Apple = Apple

    def copyAttrFrom(self,arena):
        self.width = arena.width
        self.height = arena.height
        self.border = arena.border
        self.Apple = arena.Apple

class Snake():
    """Class containing informations loaded from user settings file on the Snake"""
    def __init__(self,snake=None,length=3,head="s",body="o",speed=8.0,pos=[(24,19),(24,20),(24,21)],direction=(0,-1)):
        self.length = length
        self.head = head
        self.body = body
        self.speed = speed
        self.pos = pos
        self.direction = direction

    def move(self):
        i = len(self.pos) - 1
        while i > 0:
            self.pos[i] = self.pos[i-1]
            i -= 1
        self.pos[0] = (self.pos[0][0] + self.direction[0], self.pos[0][1] + self.direction[1])

    def moveAndGrow(self, Stats):
        Stats.appleEaten += 1
        self.pos.append(self.pos[len(self.pos) - 1])
        i = len(self.pos) - 2
        while i > 0:
            self.pos[i] = self.pos[i-1]
            i -= 1
        self.pos[0] = (self.pos[0][0] + self.direction[0], self.pos[0][1] + self.direction[1])
        self.length += 1

    def copyAttrFrom(self,snake):
        self.length = snake.length
        self.head = snake.head
        self.body = snake.body
        self.speed = snake.speed
        self.pos = []
        for i in snake.pos:
            self.pos.append(i)
        self.direction = snake.direction

class Stats():
    """Class containing statistics of the game played"""
    def __init__(self):
        self.appleEaten = 0

class Keybinding():
    """Class contatining the keys that have special effects"""
    def __init__(self,up="z",down="s",left="q",right="d",accept="y",refuse="n"):
        self.up = up
        self.down = down
        self.left = left
        self.right = right
        self.accept = accept
        self.refuse = refuse

    def getList(self):
        return [self.up, self.down, self.left, self.right, self.accept, self.refuse]
