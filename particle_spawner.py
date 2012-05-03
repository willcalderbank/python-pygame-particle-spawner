""" drawDemo.py 
    demonstrate using the drawing
    features in pygame"""
    
import pygame, math, random
pygame.init()

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480

MAXDISTANCE = 250

POINTS = []
C = 1

ADDCHANCE = 0.2
START_NUM = 100
START_SIZE = 2


class Track():
    #m = 0
    #c = 0
    #o = 0
    #positive = False

    def __init__(self,*args, **kwargs):
        #yeah there degrees so what!
        self.o = kwargs.pop('center')
        degree = random.randint(0,360) 
        self.m = math.tan(math.radians(degree))
        self.c = (self.m *self.o[0])-self.o[1]
        
        if random.randint(0,1) == 1:
            self.positive = True
        else:
            self.positive = False
            
    def __str__(self):
        return "Track <M:" + str(self.m) + " C:" +str(self.c) + " O:" +str(self.o[0]) + "," + str(self.o[1]) +">"
        
        
class Point():
    #track = None
    #position = None
    #life_distance = None
    #colour = (0,0,0)
        
    def __init__(self, *args, **kwargs):
        self.track = kwargs.pop('track')
        self.colour = self.set_colour()
        self.life_distance = random.randint(1,MAXDISTANCE)
        self.position = self.track.o

        
    def calc_position(self):
        if not self.track.positive:
            x = float(self.position[0])-(C/math.sqrt(1+math.pow(self.track.m,2)))
        else:
            x = float(self.position[0])+(C/math.sqrt(1+math.pow(self.track.m,2)))
        y = (x*self.track.m)-self.track.c
        
        #print self.position, CENTER
        self.position = (x,y)
        
    def set_colour(self):
        return (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    
    def calc_distance_travelled(self):            

        deltaX = self.position[0] - self.track.o[0]
        deltaY = self.position[1] - self.track.o[1]
        #print "X:",deltaX,"Y:", deltaY ,"---", math.sqrt((deltaX*deltaX) + (deltaY*deltaY))
        return math.sqrt((deltaX*deltaX) + (deltaY*deltaY))
    
    def __str__(self):
        print self.position, self.life_distance, self.colour, self.track
        
        

def drawCircle(background, point):
    pygame.draw.circle(background, point.colour, (int(point.position[0]),int(point.position[1])), START_SIZE)


def addPoint(center):
    POINTS.append(Point(track=Track(center = center)))

def getPoints():
    return POINTS

def removePoint(i):
    del POINTS[i]


class Debug_text():
    def __init__(self, *args, **kwargs):
        self.points = kwargs.pop('points')
        self.screen = kwargs.pop('screen')
        self.clock = kwargs.pop('clock')
        self.font = pygame.font.SysFont("Monospaced", 20)
    
    def print_text(self):
        label_numOfPoint = self.font.render("# Points: " + str(len(self.points)), 1, (255,255,255))
        label_frameRate = self.font.render("FPS: " + str(self.clock.get_fps()), 1, (255,255,255))
        self.screen.blit(label_numOfPoint, (10, 10))
        self.screen.blit(label_frameRate, (10, 30))

#def main():
#    track = generateTrack()
#    print track 
#    for tick in range(1,100):
#        print getPointonTrack(track,tick)

def main():
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    
    pygame.display.set_caption("Drawing commands")
    
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 0))
    clock = pygame.time.Clock()
    
    debug =Debug_text(points=getPoints(), screen = screen, clock = clock)
    
    keepGoing = True

    center = WINDOW_WIDTH/2, WINDOW_HEIGHT/2
    
    for i in xrange(0,START_NUM):
        addPoint(center)
           
    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                center = pygame.mouse.get_pos()
                addPoint(center)
                print pygame.mouse.get_pos()    
        
        background.fill((0, 0, 0))
        
        for i, point in enumerate(getPoints()) :
            point.calc_position()
            if point.calc_distance_travelled() < point.life_distance:
                drawCircle(background, point = point)
            else:
                removePoint(i)
                
        if ADDCHANCE >= 1:
            if random.randint(1, ADDCHANCE) == 1:
                addPoint(center)
        else:
            for i in xrange(0,int(1/ADDCHANCE)):
                addPoint(center)

            
        screen.blit(background, (0, 0)) # put the label object on the screen at point x=100, y=100
        debug.print_text()
        pygame.display.flip()
       
if __name__ == "__main__":
    main()



 

