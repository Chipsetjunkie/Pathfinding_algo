"""
Instruction on how to use this

*Search wont work before selecting start and goal position

start >> hover mouse over location and press 's'
goal >> hover mouse over location and press 'g'

wall >> hover mouse over location and left click to add wall and right click to remove wall


A* >> press 'a'
Bfs >> press 'b'
Dfs >> press 'd'

reset >> press 'r'

Press enter key to continue
"""


from grid import Grid
from search import Search
import pygame

print (__doc__)
raw_input()

pygame.init()

source= (25,25)
goal = (275,275)
Width,Height = 500,500
screen = pygame.display.set_mode((Width,Height))
G = Grid(screen)
G.create([Width,Height])
grid = G.grid
data = [grid,None,None]
srch = Search(screen,data[0])

#print len(grid) # get centre_points of grid, animation toggled with bool
#print G.get_count((225,225),True)


done = 0
state = 0
while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                    coord = pygame.mouse.get_pos()
                    coord_new =  50*(coord[0]/50)+25, 50*(coord[1]/50)+25
                    if state == 0:
                        if pygame.mouse.get_pressed()[0] == 1:
                            if  coord_new not in data[1:]:
                                G.add_wall(coord_new)
                        else:
                            if  coord_new not in data[1:]:
                                G.del_wall(coord_new)


            if event.type == pygame.KEYDOWN:
                    pressed = pygame.key.get_pressed()
                    if state != 1:
                        if pressed[pygame.K_s]:
                            coord = pygame.mouse.get_pos()
                            coord_new =  50*(coord[0]/50)+25, 50*(coord[1]/50)+25
                            if coord_new in G.grid and data[1]==None:
                                data[1] = coord_new
                                pygame.draw.circle(G.screen,(0,0,255),data[1],5)
                        if pressed[pygame.K_g]:
                            coord = pygame.mouse.get_pos()
                            coord_new =  50*(coord[0]/50)+25, 50*(coord[1]/50)+25
                            if coord_new in G.grid and data[2]==None:
                                data[2] = (coord_new)
                                pygame.draw.circle(G.screen,(255,0,0),data[2],5)
                        if pressed[pygame.K_b]:
                            if None in data:
                                print ("choose location")
                            else:
                                srch.Bfs(data[1],data[2])
                                state = 1
                        if pressed[pygame.K_d]:
                            if None in data:
                                print ("choose location")
                            else:
                                srch.Dfs(data[1],data[2])
                                state = 1
                        if pressed[pygame.K_a]:
                            if None in data:
                                print ("choose location")
                            else:
                                srch.A_star(data[1],data[2])
                                state = 1
                    if pressed[pygame.K_r]:
                            G.create([Width,Height])
                            srch.data = G.grid
                            data[1:] = None,None
                            state = 0
            pygame.display.flip()
