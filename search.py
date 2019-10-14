from grid import Grid
import pygame,heapq,math

class Search(Grid):
    def __init__(self,scr,data):
        self.data = data
        self.screen = scr
        super(Search,self).__init__(self.screen)


    def dist(self,a,b):
        return math.sqrt((a[0]-b[0])**2 +(a[1]-b[1])**2)

    def retrace(self,traces,source,goal):
            path = [traces[goal]]
            if traces[goal] == source:
                return [source]
            else:
                return path + self.retrace(traces,source,traces[goal])

    def Bfs(self,s,g):
        grid = self.data
        pos = s
        goal_pos = g

        visited = []
        path = []
        footprints = {}
        n = 0

        for i in super(Search,self).get_neighbhours(pos,grid):
            path.append(i)
            footprints[i] = pos
        visited.append(pos)
        while len(path)!= 0:
            print ('.')
            next = path[0]
            path = path[1:]
            if next == goal_pos:
                    break
            if next not in visited:
                    visited.append(next)
                    if len(super(Search,self).get_neighbhours(next,grid)) > 1:
                        for i in super(Search,self).get_neighbhours(next,grid):
                                if i not in footprints.values():
                                    footprints[i] = next
                                if i not in path:
                                    path.append(i)
                        n +=1
            elif len(super(Search,self).get_neighbhours(next,grid)) == 1:
                                footprints[super(Search,self).get_neighbhours(next,grid)] = next
                                if i not in path:
                                    path.append(super(Search,self).get_neighbhours(next,grid))

            else:
                    pass
            super(Search,self).show_path(next)
            pygame.draw.circle(self.screen,(255,0,0),goal_pos,5)
            pygame.draw.circle(self.screen,(0,0,255),pos,5)
            pygame.display.flip()

        if goal_pos in footprints.keys():
            super(Search,self).show_path(next)
            pygame.draw.circle(self.screen,(255,0,0),goal_pos,5)
            pygame.draw.lines(self.screen,(0,0,255),False,[goal_pos]+self.retrace(footprints,pos,goal_pos))

            pygame.display.flip()

        else:
            blue = (0, 0, 0)
            f = pygame.font.get_default_font()
            font = pygame.font.Font(f, 32)
            text = font.render('No solution!!! :( ', True, blue)
            textRect = text.get_rect()
            textRect.center = [250,250]
            self.screen.blit(text, textRect)
            print ("no sol")

    def A_star(self,s,g):
            grid = self.data
            pos = s
            goal = g
            path = []
            footprints = {}
            visited = []
            n = 0
            for i in super(Search,self).get_neighbhours(pos,grid):
                g = self.dist(i,pos)
                h = self.dist(goal,i)
                f = g+h
                path.append((f,h,i))
                footprints[i] = pos
                #directions.append(i[1])
            visited.append(pos)
            heapq.heapify(path)
            while len(path)!=0:
                print ('.')
                next = heapq.heappop(path)[-1]
                if next == goal:
                        break
                if next not in visited:
                        visited.append(next)
                        if len(super(Search,self).get_neighbhours(next,grid)) > 1:
                            for i in super(Search,self).get_neighbhours(next,grid):
                                    g = self.dist(i,next)
                                    h = self.dist(goal,i)
                                    f = g+h

                                     # check f then h then random
                                    if i not in footprints.values():
                                        footprints[i] = next
                                    if i not in path:
                                        #directions.append(i[1])
                                        heapq.heappush(path,(f,h,i))
                            n +=1

                super(Search,self).show_path(next)
                pygame.draw.circle(self.screen,(255,0,0),goal,5)
                pygame.draw.circle(self.screen,(0,0,255),pos,5)
                pygame.display.flip()
            if goal in footprints.keys():
                super(Search,self).show_path(next)
                pygame.draw.circle(self.screen,(255,0,0),goal,5)
                pygame.draw.lines(self.screen,(0,0,255),False,[goal]+self.retrace(footprints,pos,goal))
                pygame.display.flip()
            else:
                blue = (0, 0, 0)
                f = pygame.font.get_default_font()
                font = pygame.font.Font(f, 32)
                text = font.render('No solution!!! :( ', True, blue)
                textRect = text.get_rect()
                textRect.center = [250,250]
                self.screen.blit(text, textRect)
                print ("no sol")

    def Dfs(self,s,g):
        grid = self.data
        goal_pos = g
        pos = s
        path = []
        visited = []
        n = 0
        directions = []
        footprints = {}
        for i in super(Search,self).get_neighbhours(pos,grid):
            path.append(i)
            footprints[i] = pos
        visited.append(pos)
        while len(path) !=0:
            print ('.')
            new_path = []
            next = path[0]
            if next == goal_pos:
                    break
            if next not in visited:
                    visited.append(next)
                    if len(super(Search,self).get_neighbhours(next,grid)) > 1:
                        for i in super(Search,self).get_neighbhours(next,grid):
                                if i not in footprints.values():
                                    footprints[i] = next
                                if i not in new_path:
                                    new_path.append(i)
                        n +=1
                    elif len(super(Search,self).get_neighbhours(next,grid)) == 1:
                                footprints[super(Search,self).get_neighbhours(next,grid)] = next
                                if i not in new_path:
                                    new_path.append(super(Search,self).get_neighbhours(next,grid))
                    else:
                                print ("backtracking")

            path = new_path + path[1:]
            super(Search,self).show_path(next)
            pygame.draw.circle(self.screen,(255,0,0),goal_pos,5)
            pygame.draw.circle(self.screen,(0,0,255),pos,5)
            pygame.display.flip()
        if goal_pos in footprints.keys():
            super(Search,self).show_path(next)
            pygame.draw.circle(self.screen,(255,0,0),goal_pos,5)
            pygame.draw.lines(self.screen,(0,0,255),False,[goal_pos]+self.retrace(footprints,pos,goal_pos))
        else:
            blue = (0, 0, 0)
            f  = pygame.font.get_default_font()
            font = pygame.font.Font('freesansbold.ttf', 32)
            text = font.render('No solution!!! :( ', True, blue)
            textRect = text.get_rect()
            textRect.center = [250,250]
            self.screen.blit(text, textRect)
            print ("no sol")
        pygame.display.flip()
