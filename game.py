from cmu_graphics import *

app.attackstep = 0
app.anistep = 0
app.step = 0
app.width = 1000
app.height = 600


class background(object):
    def __init__(self,x):
        self.draw(x)
    def draw(self,x):
        self.drawing = Group(
            Rect(0 + x,410,1000+ x,40,fill=rgb(64,201,61)),
            Rect(0 + x,450,1000 +x,150,fill=rgb(123,72,48)),
            Polygon(200 + x,410,500 +x,-100,775 +x,410,fill=rgb(150,146,145)),
            Polygon(100 + x,410,350 +x,50,650+x,410,fill=rgb(169,161,158)),
            Polygon(350 + x,410,650 +x,30,900 +x,410,fill=rgb(158,153,151)),
            
        )
        colors = ["darkGrey","grey"]
        for i in range(100):
            x = randrange(0,1000+x)
            y = randrange(460,600)
            rad = randrange(2,10)
            color = choice(colors)
            C = Circle(x,y,rad,fill=color)
            self.drawing.add(C)
class enti(object):
    def __init__(self,x,y):
        self.health = 100
        self.draw(x,y)
        self.cx = x
        self.cy = y
        self.ani = 1
        self.moving = True
        self.attack = False
    def animation(self):
        if app.step % 10 == 0 and self.moving == True:
            if self.ani== 1:
                self.anii(2)
                self.ani=2
            elif self.ani == 2:
                self.anii(1)
                self.ani= 3
            elif self.ani ==3:
                self.anii(3)
                self.ani = 4
            elif self.ani == 4:
                self.anii(1)
                self.ani=1
        if self.moving == False:
            self.ani1()

class user(enti):
    def __init__(self,x,y):
        self.swordDamage = 10
        self.x = x
        super().__init__(x,y)
        
    def draw(self,x,y):
        self.arm1 = Rect(210,240,20,70)
        self.arm2 = Rect(210,240,20,70)
        self.sword = Group(
            Line(220,300,240,300,fill="brown",lineWidth=5),
            Line(240,290,240,310,fill="brown",lineWidth=5),
            Line(240,300,300,300,fill="brown",lineWidth=8)
            
        )
        self.leg1 = Rect(205,300,30,90)
        self.leg2 = Rect(205,300,30,90)
        self.drawing = Group(
            self.arm1,
            self.arm2,
            self.sword,
            self.leg1,
            self.leg2,
            Rect(200,200,40,40,fill="green"),
            Rect(205,240,30,80,fill="lightGreen"),
            Rect(230,210,10,10,fill="black")

        )
        self.sword.toFront()
        self.arm1.toFront()
        self.drawing.centerX = x
        self.drawing.centerY = y
    
    
    def punch(self):
        if self.attack == False:
            self.anii(1)
            self.attack = True
            self.anii(4)
        

    def punchhing(self,enemies):
        if self.attack == True:
            app.attackstep += 1
            for enemie in enemies:
                if self.sword.hitsShape(enemie.drawing):
                    enemie.health -= self.swordDamage
            if app.attackstep >= 20:
                self.attack = False
                app.attackstep = 0
                us.anii(1)


    def anii(self,i):
        if i == 1:
            self.arm1.rotateAngle = 0
            self.arm1.centerX = self.x - 30
            self.arm2.rotateAngle = 0
            self.arm2.centerX = self.x -30
            self.leg1.rotateAngle = 0
            self.leg1.centerX = self.x -30
            self.leg2.rotateAngle = 0
            self.leg2.centerX = self.x -30
            self.sword.left = self.x -30
            self.sword.centerY = self.arm1.bottom -10
            self.sword.rotateAngle = 0
            
        elif i == 2:
            self.arm1.rotateAngle = 45
            self.arm1.centerX -= 23
            self.arm2.rotateAngle = -45
            self.arm2.centerX += 23
            self.leg1.rotateAngle = 45
            self.leg1.centerX -=23
            self.leg2.rotateAngle = -45
            self.leg2.centerX += 23
            self.sword.rotateAngle = 45
            self.sword.centerX -= 40
            self.sword.centerY += 20

        elif i == 3:
            self.arm1.rotateAngle = -45
            self.arm1.centerX += 23
            self.arm2.rotateAngle = 45
            self.arm2.centerX -= 23
            self.leg1.rotateAngle = -45
            self.leg1.centerX +=23
            self.leg2.rotateAngle = 45
            self.leg2.centerX -= 23
            self.sword.rotateAngle = -45
            self.sword.centerX += 40
            self.sword.centerY -= 30
        elif i== 4:
            self.arm1.rotateAngle = -45
            self.arm1.centerX += 23
            self.sword.rotateAngle = -45
            self.sword.centerX += 30
            self.sword.centerY -= 30

class zombie(enti):
    def __init__(self,x,y):
        super().__init__(x,y)
    def draw(self,x,y):
        self.arm1 = Rect(210,240,20,70,fill="green")
        self.arm2 = Rect(210,240,20,70,fill="green")
        self.leg1 = Rect(205,300,30,90,fill="blue")
        self.leg2 = Rect(205,300,30,90,fill="blue")
        self.drawing = Group(
            self.arm1,
            self.arm2,
            self.leg1,
            self.leg2,
            Rect(200,200,40,40,fill="green"),
            Rect(205,240,30,80,fill="lightGreen"),
            Rect(200,210,10,10,fill="black")
        )
        self.arm1.toFront()
        self.drawing.centerX = x
        self.drawing.centerY = y

def main():
    pass
main()

background(0)
us = user(200,315)
app.enemies_list = [zombie(800,315),zombie(900,315)]


def onKeyHold(keys):
    if us.attack == False:
        if "d" in keys:
            us.animation()
            us.drawing.centerX += 5
            us.x += 5
        if "a" in keys:
            us.animation()
            us.drawing.centerX -= 5
            us.x -= 5

def onKeyPress(key):
    if key =="space":
        us.punch()

def onKeyRelease(key):
    if key == "d":
        us.anii(1)
    if key == "a":
        us.anii(1)
        

def onStep():
    app.step += 1
    us.punchhing(app.enemies_list)
    for ene in app.enemies_list:
        if ene.health <= 0:
            app.enemies_list.remove(ene)



cmu_graphics.run()