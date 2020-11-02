import pygame
from pygame.locals import *
import time
import math
from random import randint, random, uniform
from pygame import gfxdraw


def get(arr, i, j):
    ans = 0
    for x in range(i-1, i+2):
        for y in range(j-1, j+2):
            if((i,j) != (x,y) and x > 0 and y > 0 and x < 199 and y < 199 and arr[x][y] == 1):
                ans+=1
    return ans

def update(arr):
    newarr = [[0] * 200 for k in range(200)]
    for i in range(200):
        for j in range(200):
            if arr[i][j] == 1:  
                if get(arr, i, j) == 2 or get(arr, i, j) == 3:
                    newarr[i][j] = 1
            else:
                if get(arr, i, j) == 3:
                    newarr[i][j] = 1

    return newarr
            
            
    

class Game:
    def __init__(self):
        # initialize
        pygame.init()
        pygame.display.set_caption("Conway's Game of Life")
        self.width = 1000
        self.height = 1000
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.exit = False

    def run(self):   
        
        arr = [[0] * 200 for i in range(200)]

        arr[1][1] = 1
        arr[2][2] = 1
        arr[2][3] = 1
        arr[3][1] = 1
        arr[3][2] = 1


        while not self.exit:
            for event in pygame.event.get():
                # quit
                if event.type == pygame.QUIT:
                    pygame.quit()
                

            # refresh screen
            self.screen.fill((200, 200, 200))
            
            arr = update(arr).copy()
            
            for i in range(200):
                for j in range(200):
                    if arr[i][j] == 1:
                        r = pygame.Rect(i*5, j*5, 5, 5)
                        pygame.draw.rect(self.screen, (0,0,0), r)
                        
            pygame.display.flip()
                        

            


if __name__ == '__main__':
    game = Game()
    game.run()
