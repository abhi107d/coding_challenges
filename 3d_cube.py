import numpy as np
import pygame 
import math



sw,sh=600,600
pygame.init()
screen=pygame.display.set_mode((sw,sh))

pygame.display.set_caption("poin line")
clock=pygame.time.Clock()


def x_y_map(vector,angle):
    asp=sh/sw
    x=vector[0]/(1/math.tan(math.radians(angle/2))*vector[2])
    y=vector[1]/(1/math.tan(math.radians(angle/2))*vector[2])

    return asp*x,y

def find_point(points,angle,rot,rott):
    front=[]
    back=[]
    Points=[]
    for p in points:
        vecto=np.dot(rot,p)
        vector=np.dot(rott,vecto)
        vector[2]+=10
        Points.append(vector)

  
    for i in range(4):
        x,y=x_y_map(Points[i],angle)
        front.append([x,y])

    for i in range(4,8):
        x,y=x_y_map(Points[i],angle)
        back.append([x,y])


    return np.array(front),np.array(back)




points=np.array([
    #front
    [1,1,-1],
    [1,-1,-1],
    [-1,-1,-1],
    [-1,1,-1],

    #back
    [1,1,1],
    [1,-1,1],
    [-1,-1,1],
   [-1,1,1],
])


theta=0
angle=90

rotz=np.array([
    [math.cos(math.radians(theta)),-math.sin(math.radians(theta)),0 ],
    [math.sin(math.radians(theta)),math.cos(math.radians(theta)),0],
    [0,0,1]
    ])
roty=np.array([
    [math.cos(math.radians(theta)),0,math.sin(math.radians(theta)) ],
    [0,1,0],
    [-math.sin(math.radians(theta)),0,math.cos(math.radians(theta))],
    ])
rotx=np.array([
    [1,0,0],
    [0,math.cos(math.radians(theta)),-math.sin(math.radians(theta)) ],
    [0,math.sin(math.radians(theta)),math.cos(math.radians(theta))],
    ])

while True:
    theta+=1
    roty=np.array([
    [math.cos(math.radians(theta)),0,math.sin(math.radians(theta)) ],
    [0,1,0],
    [-math.sin(math.radians(theta)),0,math.cos(math.radians(theta))],
    ])
    rotz=np.array([
    [math.cos(math.radians(theta)),-math.sin(math.radians(theta)),0 ],
    [math.sin(math.radians(theta)),math.cos(math.radians(theta)),0],
    [0,0,1]
    ])
    
    clock.tick(60)
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
        if event.type==pygame.MOUSEMOTION:
            pos=np.array(event.pos)


    f,b=find_point(points,angle,roty,rotz)
    
    for i in f:
     
        pygame.draw.circle(screen,"red",center=i*1000+sh/2,radius=4)
    for i in b:
        pygame.draw.circle(screen,"red",center=i*1000+sh/2,radius=4)
    
    pygame.draw.polygon(screen,"black",f*1000+sh/2,width=2)
    pygame.draw.polygon(screen,"black",b*1000+sh/2,width=2)

    #join
    for i in range(0,4):

        pygame.draw.line(screen,"black",start_pos=f[i]*1000+sh/2,end_pos=b[i]*1000+sh/2,width=2)
        

            
               
  
    pygame.display.update()

