from visual import *
from math import *
from pymongo import MongoClient
tcol = 0

class simulation:

    def __init__(self):
        self.r = 0.5
        self.h = 10
        self.ball = sphere(pos=vector(0,self.h,0), radius=self.r, color=color.cyan, make_trail=True) #Definicion de la esfera
        self.wallB = box(pos=vector(0,0,0), size=vector(12,0.2,12), color=color.red)#Piso
        self.g = 9.8#Gravedad

        self.ball.velocity = vector(0,self.g,0)#Velocidad con la que se movera la esfera en X

        self.deltat = 0.005 #Definicion del intervalo de tiempo
        self.t = 0#Cronometro para mantener un registro del tiempo total transcurrido
        self.vscale = 0.1

        self.varr = arrow(pos=self.ball.pos, axis=self.vscale*self.ball.velocity, color=color.yellow)
        self.vpos = self.ball.velocity.x#Guardando atributo de vector
        self.tiempo()
        self.run_simulation()

    def planoTangente(self):
        self.wallT = box(pos=vector(0,self.ball.pos.y-self.r,0), size=vector(12,0.2,12), color=color.blue)
        #Plano tangente a la esfera en el eje y

    def tiempo(self):
        #2h/a=t^2
        pball = self.ball.pos.y
        tllegada = 2*float(pball)/self.g
        tllegada = math.sqrt(math.fabs(tllegada))
        print("--------------------->>> P.Y = " + str(pball) + " TARDARA >>>>>>>>>> " + str(tllegada))

    def colision(self):
        if self.ball.pos.y-self.r > self.wallB.pos.y:
            #Yn = Yn-1-g*s
            if tcol == 0:
                self.ball.pos = self.ball.pos - self.ball.velocity*self.deltat
                self.varr.axis = 0.2*vector(0,-self.g,0)
            else:
                if self.ball.pos.y < self.h:
                    self.ballmove()
                    self.varr.axis = 0.2*self.ball.velocity
                else:
                    tcol = 0
        if self.ball.pos.y-self.r < self.wallB.pos.y:
            print("Colision")
            #Yn = Yn-1/2
            global tcol
            tcol=1
            self.h = self.h-2#La altura maxima a a la que llegara
            print("La altura maxima =========" + str(self.h))
            self.ballmove()

    def ballmove(self):
        self.ball.pos = self.ball.pos + self.ball.velocity*self.deltat
        #print("avanzo >>>> " + str(self.ball.pos))

    def checkpos(self):
        #y=Yo+Vo*t+1/2*g*t**2
        y=self.ball.pos.y+0*self.t+1/2*-self.g*self.t**2
        #print("Posicion en Y == " + str(y))#Verificar la posicion del objeto en base a la formula
        #print("Posicion del objeto en el eje Y = " + str(self.ball.pos.y))

    def run_simulation(self):
        while self.h > 0:
            rate(100)#Indica que no se ejecutara el ciclo mas de 100 veces por segundo
            #tiempo()
            self.colision()
            self.varr.pos = self.ball.pos
            self.t = self.t + self.deltat
