
from msilib.schema import Class
import pygame, sys, time
from pygame.locals import *
from B_star import*
from BFS_DFS_HASH import*
import time
import button

WINDOWWIDTH = 600
WINDOWHEIGHT = 600
notFound_flag=1
BLACK = (0, 0, 0)
RED = (255, 100, 0)
GREEN = (255, 100, 0)
BLUE = (0, 0, 255)
WHITE=(255,255,255)
Text=(0,0,0)
blockTOP=150
blockLEFT=150
blocks=[]
blockNumber=0


class Button():
    def __init__(self,x,y,image):
        self.image = image
        self.rect = self.image.getrect()
        self.rect.topleft=(x,y)
    def draw(self):
        windowSurface.blit(self.image,(self.rect.x,self.rect.y))


def validation(state):
    state=bfs.int_to_oneD(state)

    for i in range(0,len(state)):
        
        for j in range(1+i,len(state)):
            
            if state[i] == state[j]:
                return False
    return True
# 1 mins 44 seconds total time , 74 seconds dfs , 30 seconds path calc on 125 , 348 , 670
# time 4 seconds , 3.5 seconds dfs , 0.5 seconds path calc on 125 , 348 , 670

#123456780 62500 path dfs 25 sec
#125348670 16604 path dfs 1.3 sec
#162378450 54444 path dfs 16 sec
#867254301 57477 path dfs 23 sec
#647850321 66041 path dfs 35 sec
#123804765 unsolvable 74 sec
#806547231 59023 path dfs 21 sec 


#102754863 16604 path dfs 1.3 sec






#algorithms: DFS       BFS     A*:manhaten   A*:Euclidean
#123456780   26.08    1.139       0.269         0.586
#125348670   1.419    0.001       0.0009        0.0009
#162378450   16.67    0.603       0.2244        0.326
#867254301   20.17    2.448       5.2539        9.221
#647850321   37.27    2.107       2.5222        6.935
#123804765 unsolvable in 0 secs
#806547231   22.27    2.683       13.18        73.809 31 34761


#102754863 

def getInvCount(arr):
    inv_count = 0
    empty_value = 0
    for i in range(0, 9):
        for j in range(i + 1, 9):
            if arr[j] != empty_value and arr[i] != empty_value and arr[i] > arr[j]:
                inv_count += 1
    if inv_count%2 == 0:
        return True
    else:
        return False

algorithm=input("enter desired algorithm:")
if algorithm == "BFS" or algorithm == "DFS":
    bfs=Dfs_Bfs()
    if algorithm == "BFS":
        variation=0
        speed=0.3
    else:
        variation=-1
        speed=0.0001
else:
    hurostic=input("enter huristic used in A*:")
    if hurostic == "manhaten":
        variation=0
        speed=0.3
    else:
        variation=-1
        speed=0.5
    bfs=A_star()

            
while True:
    initial_state_input=int(input("input your initial state:"))
    if initial_state_input > 876543210 or initial_state_input < 12345678:
        print("invalid initial state!!!!")
    elif not validation(initial_state_input):
        print("state has repeated numbers state!!!!")
        initial_state_input=input("input your initial state:")
    else:
        bfs.Inital_State=initial_state_input
        break

# bfs.Inital_State=162378450
Initial_mateix=bfs.int_to_oneD(bfs.Inital_State)
solvable=getInvCount(Initial_mateix)
if solvable== False:   
    print("unsolvable")
    notFound_flag=0



state=bfs.int_to_oneD(bfs.Inital_State)
Goal_state=bfs.int_to_oneD(bfs.Goal_State)
start_time=time.time()
parent , found = bfs.BFS(bfs.Inital_State,bfs.Goal_State,variation)
end_time=time.time()
taken_time=end_time-start_time
print("taken time :"+str(taken_time))




pygame.init()
BASICFONT = pygame.font.Font('freesansbold.ttf',50)
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('8 Puzzle')
white = (255, 255, 255)
green = (255, 100, 0)
blue = (0, 0, 128)
font = pygame.font.Font('freesansbold.ttf', 20)
#display_surface = pygame.display.set_mode((100, 100))
#display_surface.fill(white)
start_img = pygame.image.load('start.PNG').convert_alpha()
# exit_img = pygame.image.load('exit.PNG').convert_alpha()
pause_img = pygame.image.load('pause.png').convert_alpha()
# DFS_img = pygame.image.load('DFS.png').convert_alpha()
# BFS_img = pygame.image.load('B.jpg').convert_alpha()
#create button instances
start_button = button.Button(300, 50, start_img,2)
pause_button = button.Button(380, 50, pause_img, 2)
# resume = button.Button(460, 50, exit_img, 2)
# DFS = button.Button(460,90, DFS_img, 2)
# BFS = button.Button(460, 150, BFS_img, 2)




if solvable:
    path=bfs.get_path(bfs.Goal_State,parent,bfs.Inital_State)
 
    path_time=time.time()-end_time
    print("path time:"+str(path_time))
    path.reverse()
    print("path length:"+str(len(path)))
    print("explored count:"+str(bfs.explored_count()))

# initial grid based on initial state
    for i in range(3):
        for j in range(3):
        
            if state[blockNumber]==0:
                blocks.append({'rect':pygame.Rect(blockLEFT,blockTOP,99,99),'color':BLACK,'block':str(0)})
            else:
                blocks.append({'rect':pygame.Rect(blockLEFT,blockTOP,99,99),'color':GREEN,'block':str(state[blockNumber])})
            blockNumber+=1
            blockLEFT+=100
        blockTOP+=100
        blockLEFT=150

    for b in blocks:        
            pygame.draw.rect(windowSurface, b['color'], b['rect'])
            textSurf = BASICFONT.render(b['block'], True,Text)
            textRect = textSurf.get_rect()
            textRect.center = b['rect'].left+50,b['rect'].top+50
            windowSurface.blit(textSurf, textRect)

    pygame.display.update()
    time.sleep(1)     
run = True

textRect2 = textSurf.get_rect()
def start(path):
    for p in path:
        textRect2.center = (70, 40)
        text = font.render("path_time:" + str(round(path_time, 5)), True, green, BLACK)
        windowSurface.blit(text, textRect2)
        textRect2.center = (70, 70)
        text = font.render("taken_time:" + str(round(taken_time, 3)), True, green, BLACK)
        windowSurface.blit(text, textRect2)
        textRect2.center = (70, 100)
        text = font.render("path_length:" + str(len(path)), True, green, BLACK)
        windowSurface.blit(text, textRect2)
        pause = False
        #resume.draw(windowSurface)

        if pause_button.draw(windowSurface):
            pause = True
            time.sleep(5)

        # time.sleep(5)

        # while pause:
        #
        #     if resume.clicked:
        #         pause = False
        #         print("in button")
        #     itrator=0
        #     for b in blocks:
        #
        #         # the main updating of blocks
        #         b['block'] = str(p[itrator])
        #         itrator += 1
        #         if b['block'] == '0':
        #             b['color'] = BLACK
        #         else:
        #             b['color'] = GREEN
        #         pygame.draw.rect(windowSurface, b['color'], b['rect'])
        #         textSurf = BASICFONT.render(b['block'], True, Text)
        #         textRect = textSurf.get_rect()
        #         textRect.center = b['rect'].left + 50, b['rect'].top + 50
        #         windowSurface.blit(textSurf, textRect)
        #     pygame.display.update()
        #     time.sleep(speed)

        for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
        itrator = 0
        for b in blocks:


            #the main updating of blocks
            b['block'] = str(p[itrator])
            itrator += 1
            if b['block'] == '0':
                b['color'] = BLACK
            else:
                b['color'] = GREEN
            pygame.draw.rect(windowSurface, b['color'], b['rect'])
            textSurf = BASICFONT.render(b['block'], True, Text)
            textRect = textSurf.get_rect()
            textRect.center = b['rect'].left + 50, b['rect'].top + 50
            windowSurface.blit(textSurf, textRect)
        pygame.display.update()
        time.sleep(speed)
    # wait for exit

    while True:
        # check for the QUIT event
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()


while run :
    # DFS.draw(windowSurface)
    # BFS.draw(windowSurface)
    if start_button.draw(windowSurface):
        start(path)

    for event in pygame.event.get():
        # quit game
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
    #updating the grid with all new states in order of path

