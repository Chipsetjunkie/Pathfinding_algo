import pygame




class Grid(object):
    def __init__(self,scr):
        self.screen = scr
        self.state = False
        self.clock = pygame.time.Clock()
        self.matrix = []
        self.wall = []
        self.grid = []


    def show_path(self,pos):
        if pos != None:
            x1,y1 = pos[0]-25,pos[1]-25
            pygame.draw.rect(self.screen,(0,255,0),  pygame.Rect(x1, y1,49,49))

            self.clock.tick(20)


    def add_wall(self,pos):
        if pos in self.grid:
                self.grid.remove(pos)
                self.wall.append(pos)#just for debug
                x1,y1 = pos[0]-25,pos[1]-25
                pygame.draw.rect(self.screen,(107,62,36),  pygame.Rect(x1, y1,51,51))
                pygame.display.flip()

    def del_wall(self,pos):
        if pos not in self.grid:
            self.grid.append(pos)
            self.wall.remove(pos)#just for debug
            x1,y1 = pos[0]-25,pos[1]-25
            pygame.draw.rect(self.screen,(255,255,255),  pygame.Rect(x1, y1,51,51))
            pygame.draw.rect(self.screen,(0,0,0),  pygame.Rect(x1, y1,51,51),1)
            pygame.display.flip()


    def create(self,data):
        Width,Height = data[0],data[1]
        size = (50,50)
        self.screen.fill((255,255,255))
        #Verticals
        for i in range(Width//size[0]):
                pygame.draw.line(self.screen,(0,0,0),(size[0]+size[0]*i,0),(size[0]+size[0]*i,Height))

        for i in range(Height//size[0]):
                pygame.draw.line(self.screen,(0,0,0),(0,size[1]+size[1]*i),(Width,size[1]+size[1]*i))


        #pygame.draw.rect(self.screen,(255,99,52),pygame.Rect(0,500,500,100))

        points = (10,10) # Width//size
        size = (50,50)
        centre = (25,25)
        centre_points = []
        for x in range(points[0]):
            for y in range(points[1]):
                pt = (centre[0]+50*x,centre[1]+50*y)
                centre_points.append(pt)

        self.grid =  centre_points

        pygame.display.flip()

    def get_screen(self):
        return self.screen

    def get_grid(self):
        return self.grid

    def show_grid(self):
        if len(self.grid) != 0:
            for pt in self.grid:
                pygame.draw.circle(self.screen,(255,0,0),pt,2)
                pygame.display.flip()

        else:
            print ("call Grid.Create()")


    def get_neighbhours(self,pos,grid):
            left = (pos[0]-50,pos[1])
            right = (pos[0]+50,pos[1])
            up = (pos[0],pos[1]-50)
            down = (pos[0],pos[1]+50)
            neigh = []
            if left in grid:
                neigh.append(left)

            if down in grid:
                neigh.append(down)

            if right in grid:
                neigh.append(right)

            if up in grid:
                neigh.append(up)



            return neigh


    #create_maze recur dfs
    '''
        def maze(self):
    '''
    ## Debug tools ##
    '''
    def test_me(self):
        print "Success"
    '''
