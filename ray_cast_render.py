import numpy as np
import pygame as p
from sys import exit
import math
import random

p.init()
screen=p.display.set_mode((1500,700))
p.display.set_caption("poin line")
clock=p.time.Clock()

def collition(a,b,c,d):

    
    top1=((a[1]-c[1])*(d[0]-c[0]))-((d[1]-c[1])*(a[0]-c[0]))
    bot1=((d[1]-c[1])*(b[0]-a[0]))-((d[0]-c[0])*(b[1]-a[1]))
    if bot1==0:
        return False,False
    t=top1/bot1

    top2=((c[1]-a[1])*(b[0]-a[0]))-((c[0]-a[0])*(b[1]-a[1]))
    bot2=((b[1]-a[1])*(d[0]-c[0]))-((d[1]-c[1])*(b[0]-a[0]))
    if bot2==0:
        return False,False
    u=top2/bot2

    return t,u
        

def end_pos_no_coll(ray):
    vec=ray[1]-ray[0]
    norm=(vec)*np.linalg.norm(vec)
    g=ray[0]+norm*500
    if g[0]>750:
        x=ray[0][0]-750
        tri=ray[1]-ray[0]
        angle=math.atan2(tri[1],tri[0])
        t=-1*(x/math.cos(angle))

        g=ray[0]+norm*t
    return g

def raycasting(screen,obj,rayy):
    a=[]

    for ray in rayy:
        coll=False
        minn=float("inf")
        point=[]
        final_t=0
        for i in obj:

            t,u=collition(i[0],i[1],ray[0],ray[1])
                    
            if  not(t>1 or  t<0) and u>0:
                dist=np.linalg.norm(ray[0]-(i[0]+(i[1]-i[0])*t))
                if minn>dist:
                    minn=dist
                    point=i
                    final_t=t
               
                coll=True


        if coll and minn<500:#field of view check<=300:#field of view check:
             p.draw.line(screen,"yellow",start_pos=ray[0],end_pos=point[0]+(point[1]-point[0])*final_t,width=1)
             a.append(minn)
       
        else:
            a.append(-1)
            endpos=end_pos_no_coll(ray)   
            p.draw.line(screen,"yellow",start_pos=ray[0],end_pos=endpos,width=1)

    return a
     
      
    




pos=[0,0]
prevy=0
x,y=50,50
length=100
theta=0
bh=100


#getting objets
objets=[]
for i in range(5):
    objets.append(np.array([[random.randint(50,750),random.randint(50,700)],[random.randint(50,750),random.randint(50,700)]]))

#objets=[np.array([[100,100],[250,250]]),np.array([[100,400],[250,250]])]
start=0
while True:
    
    clock.tick(60)
    screen.fill((0,0,0))
    for event in p.event.get():
        if event.type==p.QUIT:
            p.quit()
            exit()
        if event.type==p.MOUSEMOTION:
            pos=np.array(event.pos)
            if pos[0]>750:
                pos[0]=750
               
    theta+=1  

    #creating circulat ray
    keys=p.key.get_pressed()
    if keys[p.K_d]:
        start+=2
    elif keys[p.K_a]:
        start-=2
    
    ray_p=[]
    for i in range(start,start+45):
        y=math.sin(math.radians(i))
        x=math.cos(math.radians(i))

        ray_p.append(np.array([[pos[0],pos[1]],[pos[0]+x,pos[1]+y]]))

    
    
    #DRAW OBJETS    
    for i in objets:
        p.draw.line(screen,"white",start_pos=i[0],end_pos=i[1],width=5)

    p.draw.circle(screen,"white",center=pos,radius=5)
   
    arr=raycasting(screen,objets,ray_p)

    if arr:
        w = 750 // len(arr)
        for i, j in enumerate(arr):
            if j == -1:
                factor = 255
                offset = 0
            else:
                factor = (j / 2)

            
            p.draw.rect(screen, (255 - factor, 255 - factor, 255 - factor), rect=p.Rect((i*w)+750, 100 + factor + 6, w, 700))

                

    p.draw.line(screen,"white",start_pos=[750,0],end_pos=[750,700])
            

    

    p.display.update()
