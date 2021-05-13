import pygame

class Goal:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

        self.isactiv = False
    
    def draw(self, win):
        pygame.draw.line(win, (0,255,0), (self.x1, self.y1), (self.x2, self.y2), 2)
        if self.isactiv:
            pygame.draw.line(win, (255,0,0), (self.x1, self.y1), (self.x2, self.y2), 2)

# the file of shame
def getGoals():
    goals = []

    goal1 = Goal(0,200,120,200)
    goal2 = Goal(0,100,120,150)
    goal2_5 = Goal(0,0,150,130)
    goal3 = Goal(120,0,170,120)
    goal3_5 = Goal(200,0,200,120)
    goal4 = Goal(270,0,270,110)
    goal4_5 = Goal(350,0,350,110)
    goal5 = Goal(450,0,450,110)
    goal5_5 = Goal(525,0,525,110)
    goal6 = Goal(600,0,550,130)
    goal6_5 = Goal(550,130,700,60)
    goal7 = Goal(550,130,700,130)
    goal7_5 = Goal(550,130,650,200)
    goal8 = Goal(550,130,570,240)
    goal9 = Goal(410,130,430,260)
    goal9_5 = Goal(430,260,300,350)
    goal10 = Goal(430,260,260,260)
    goal10_5 = Goal(430,260,280,180)
    goal11 = Goal(430,260,400,400)
    goal12 = Goal(550,260,570,400)
    goal13 = Goal(750,400,650,200)
    goal14 = Goal(750,400,800,160)
    goal15 = Goal(750,400,950,240)
    goal16 = Goal(750,400,980,440)
    goal17 = Goal(750,400,900,600)
    goal18 = Goal(750,460,750,600)
    goal19 = Goal(670,460,670,600)
    goal19_5 = Goal(590,460,590,600)
    goal20 = Goal(510,460,510,600)
    goal20_5 = Goal(430,460,430,600)
    goal21 = Goal(350,460,350,600)
    goal21_5 = Goal(280,460,278,600)
    goal22 = Goal(210,460,190,600)
    goal22_5 = Goal(80,600,175,440)
    goal23 = Goal(150,420,0,570)
    goal23_5 = Goal(0,450,130,400)
    goal24 = Goal(0,380,130,380)

    goals.append(goal1)
    goals.append(goal2)
    goals.append(goal2_5)
    goals.append(goal3)
    goals.append(goal3_5)
    goals.append(goal4)
    goals.append(goal4_5)
    goals.append(goal5)
    goals.append(goal5_5)
    goals.append(goal6)
    goals.append(goal6_5)
    goals.append(goal7)
    goals.append(goal7_5)
    goals.append(goal8)
    goals.append(goal9)
    goals.append(goal10_5)
    goals.append(goal10)
    goals.append(goal9_5)
    goals.append(goal11)
    goals.append(goal12)
    goals.append(goal13)
    goals.append(goal14)
    goals.append(goal15)
    goals.append(goal16)
    goals.append(goal17)
    goals.append(goal18)
    goals.append(goal19)
    goals.append(goal19_5)
    goals.append(goal20)
    goals.append(goal20_5)
    goals.append(goal21)
    goals.append(goal21_5)
    goals.append(goal22)
    goals.append(goal22_5)
    goals.append(goal23)
    goals.append(goal23_5)
    goals.append(goal24)

    goals[len(goals)-1].isactiv = True

    return(goals)
