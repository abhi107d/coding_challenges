import random 
import pygame as p
from sys import exit
w,h=600,500
size=5
p.init()
screen=p.display.set_mode((600,500))
p.display.set_caption("falling sand")

clock=p.time.Clock()

class engin:

    def __init__(self,screen,w,h,size): 
        self.screen=screen
        self.w=w
        self.h=h
        self.size=size
        self.j=self.w//self.size
        self.i=self.h//self.size
        self.array=[[0 for i in range(0,self.j)] for j in range(0,self.i)]
        self.color=1



    #drawing grid
    def grid(self):
        for i in range(0,self.i):
            p.draw.line(self.screen,color="white",start_pos=[0,i*self.size],end_pos=[self.w,i*self.size],width=1)
        for i in range(0,self.j):
            p.draw.line(self.screen,color="white",start_pos=[i*self.size,0],end_pos=[i*self.size,self.h],width=1)



    #partical update
    def sand_update(self):
        #new array
        arr=[[0 for i in range(0,int(self.w/self.size))] for j in range(0,int(self.h/self.size))]
        
        for i in range(0,self.i):
            for j in range(0,self.j):

                if self.array[i][j]>0:#if sand is present
                    #p.draw.rect(self.screen,color=[154,self.array[i][j], 198],rect=p.Rect(j*self.size,i*self.size,self.size,self.size))
                    p.draw.circle(self.screen,color=[154,self.array[i][j], 198],center=[j*self.size+self.size/2,i*self.size+self.size/2],radius=self.size)

                    #if not sand at below move down
                    if i+1<self.i  and self.array[i+1][j]==0:
                        arr[i+1][j]=self.array[i][j]

                    # if sand is below and left and right is empty
                    elif ((i+1<self.i and j+1<self.j and self.array[i+1][j+1]==0) and 
                    (i+1<self.i and j-1>=0 and self.array[i+1][j-1]==0)):
                        pr=random.uniform(0, 1)
                        if pr<0.5:
                            arr[i+1][j+1]=self.array[i][j]
                        else:
                            arr[i+1][j-1]=self.array[i][j]

                    # if sand is below and right is empty
                    elif i+1<self.i and j+1<self.j and self.array[i+1][j+1]==0:
                        arr[i+1][j+1]=self.array[i][j]

                     # if sand is below and left is empty
                    elif i+1<self.i and j-1>=0 and self.array[i+1][j-1]==0:
                        arr[i+1][j-1]=self.array[i][j]
                    
                    #bottom row conditon so the sand does not go off screen
                    elif i+1==self.i or self.array[i+1][j]>0:
                        arr[i][j]=self.array[i][j]

        self.array=arr




    

en=engin(screen,w,h,size)

while True:
    clock.tick(60)
    p.display.update()
    screen.fill((0,0,0))
    

    for event in p.event.get():
        if event.type==p.QUIT:
            p.quit()
            exit()
        if event.type==p.MOUSEMOTION:
                #change color
                en.color+=1
                if en.color>255:
                    en.color=1  


                #finding mouse poition 
                pos=event.pos
                ii=pos[1]//en.size
                jj=pos[0]//en.size
                # making a splash of sand
                m=3
                for i in range(ii-m,ii+m):
                    for j in range(jj-m,jj+m):
                        if i<en.i and i>0 and j<en.j and j>0:
                            en.array[i][j]=en.color
                

    #en.grid()        
    en.sand_update()





