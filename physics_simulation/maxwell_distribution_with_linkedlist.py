#구현 대상: 0<x<1  and 0<y<1 의 구간에 해당하는 계에 속박된 입자들이 처음 -0.5~0.5의 속도로 랜덤하게 분포하고 있고
# 이 입자들이 서로 lennard-johns potential에 의해 상호작용을 할 때 시간이(충분히?)  흐른 뒤 입자들의 속력분포와 온도와의 관계를 알아본다.

from numpy import *
from vpython import *
from random import random
from math import sqrt
from pylab import plot,show



#setting condition of ensemble

N=500 #number of particle
t=0  #initial time
dt=0.0001 #time interval
cutoff=0.1122

ball=empty(N,sphere) #particle group setting with vpython module
v=empty(N,vector) #velocity setting of particles with numpy module
a=zeros(N,vector) #accelation setting of particles with numpy module
#이 후에 이 empty,zeros에 시간에 따라서 지속적으로 업데이트를 시켜준다.

Epoints=[]
velocitypoints=[]

#초기상태 설정:입자는 0~1의 위치에 -0.5~0.5의 속도로 랜덤하게 분포한다.
for i in range(170):
    ball[i]=sphere(pos=vector(5*random()+2,5*random()+2,0.5),radius=0.05,color=color.green) #각 입자상태를 설정
    v[i]=vector(sqrt(2)*2*sqrt(3/2)*700,0,0) #각 입자의 속도상태를 설정
    a[i]=vector(0,0,0) #각 입자의 초기 가속도는 0으로 설정.
for i in range(170):
    ball[i+170]=sphere(pos=vector(5*random()+2,5*random()+2,0.5),radius=0.05,color=color.green) #각 입자상태를 설정
    v[i+170]=vector(0,sqrt(2)*2*sqrt(3/2)*700,0) #각 입자의 속도상태를 설정
    a[i+170]=vector(0,0,0) #각 입자의 초기 가속도는 0으로 설정.
for i in range(160):
    ball[i+340]=sphere(pos=vector(5*random()+2,5*random()+2,0.5),radius=0.05,color=color.green) #각 입자상태를 설정
    v[i+340]=vector(0,0,0) #각 입자의 속도상태를 설정
    a[i+340]=vector(0,0,0) #각 입자의 초기 가속도는 0으로 설정.



#-------------------입자 2개 충돌 실험----------------------이걸 풀면 위에걸 주석처리 
#ball[0]=sphere(pos=vector(3,5,0.5),radius=0.05,color=color.green) #각 입자상태를 설정
#v[0]=vector(1000,0,0) #각 입자의 속도상태를 설정
#a[0]=vector(0,0,0) #각 입자의 초기 가속도는 0으로 설정.
#ball[1]=sphere(pos=vector(7,5,0.5),radius=0.05,color=color.red) #각 입자상태를 설정
#v[1]=vector(-1000,0,0) #각 입자의 속도상태를 설정
#a[1]=vector(0,0,0) #각 입자의 초기 가속도는 0으로 설정.





#linked list method:계산을 가까운 입자들에 대해서만 수행한다.

#cell 설정 파트 --------------------------------------------------------------------------------------------------------------------
lc=empty(3,int)#각 축을 나누는 개수 지정집합
rc=empty(3,float) # cell의 각 축의 길이지정집합
lc[0],lc[1],lc[2]=20,20,1 #각 축을 나누는 개수 지정
rc[0],rc[1],rc[2]=10/lc[0],10/lc[1],1/lc[2] #cell의 각 축 길이 지정

lcxyz=lc[0]*lc[1]*lc[2] #cell의 총갯수 지정


mc=empty(3,int) #cell의 좌표를 넣어 줄 집합
head=empty(lcxyz,int) #각 cell 에 속한 입자들 중 첫번째 입자들이 매겨질 집합 , 총 cell의 개수는 lcxyz개
lscl=empty(N,int)#i번째 입자가 가리키는 입자집합


for c in range(lcxyz):
    head[c]=-1  #우선 각 head는 빈 것으로 지정
for i in range(N):
    
    mc[0]=floor(ball[i].pos.x/rc[0])
    mc[1]=floor(ball[i].pos.y/rc[1])
    mc[2]=floor(ball[i].pos.z/rc[2])

    c=mc[0]+lc[0]*mc[1]+lc[0]*lc[1]*mc[2] #(mc2=0)
    lscl[i]=head[c]
    head[c]=i
print(lscl)
#-------------------------------------------------------------------------------------------------------------------------------------
#distance 함수 정의
def distance(i,j):   
    d=sqrt(((ball[i].pos-ball[j].pos).x)**2\
           +((ball[i].pos-ball[j].pos).y)**2\
           +((ball[i].pos-ball[j].pos).z)**2)
    return d


for c in range(lcxyz):
    
    i=head[c]
    while i!=-1:
        for m in range(-1,2):
            for n in range(-1,2):
                j=head[c+m*lc[1]+n]
                while j!=-1:
                    if i<j:
                        if distance(i,j)<0.1 :
                            v[i],v[j]=v[i]-dot((v[i]-v[j]),(ball[i].pos-ball[j].pos))*(ball[i].pos-ball[j].pos)\
                                       /((ball[i].pos-ball[j].pos).x**2+(ball[i].pos-ball[j].pos).y**2+(ball[i].pos-ball[j].pos).z**2),\
                                       v[j]-dot((v[j]-v[i]),(ball[j].pos-ball[i].pos))*(ball[j].pos-ball[i].pos)\
                                       /((ball[j].pos-ball[i].pos).x**2+(ball[j].pos-ball[i].pos).y**2+(ball[j].pos-ball[i].pos).z**2)
                            
                    j=lscl[j]
                    
        i=lscl[i]
       
#for n in range(N):
#    v[n]+=a[n]*dt*0.5


while t<0.05:
    
#    for n in range(N):
       
#        ball[n].pos+=v[n]*dt
    
    
    for c in range(lcxyz):
        head[c]=-1  #우선 각 head는 빈 것으로 지정
    for i in range(N):
        
        mc[0]=floor(ball[i].pos.x/rc[0])
        mc[1]=floor(ball[i].pos.y/rc[1])
        mc[2]=floor(ball[i].pos.z/rc[2])

        c=mc[0]+lc[0]*mc[1]+lc[0]*lc[1]*mc[2] #(mc2=0)
        lscl[i]=head[c]
        head[c]=i
    
    for c in range(lcxyz):
        i=head[c]
        a[i]=vector(0,0,0)
        while i!=-1:
            for m in range(-1,2):
                for n in range(-1,2):
                    j=head[c+m*lc[1]+n]
                    while j!=-1:
                        if i<j:
                            if distance(i,j)<0.1:
                                v[i],v[j]=v[i]-dot((v[i]-v[j]),(ball[i].pos-ball[j].pos))*(ball[i].pos-ball[j].pos)\
                                       /((ball[i].pos-ball[j].pos).x**2+(ball[i].pos-ball[j].pos).y**2+(ball[i].pos-ball[j].pos).z**2),\
                                       v[j]-dot((v[j]-v[i]),(ball[j].pos-ball[i].pos))*(ball[j].pos-ball[i].pos)\
                                       /((ball[j].pos-ball[i].pos).x**2+(ball[j].pos-ball[i].pos).y**2+(ball[j].pos-ball[i].pos).z**2)
                        j=lscl[j]
                        
            i=lscl[i]
    E=0
    

    for i in range(N):
        if ball[i].pos.x<2:
            v[i].x=abs(v[i].x)
        if ball[i].pos.x>7:
            v[i].x=-abs(v[i].x)
        if ball[i].pos.y<2:
            v[i].y=abs(v[i].y)
        if ball[i].pos.y>7:
            v[i].y=-abs(v[i].y)
        if ball[i].pos.z<2:
            v[i].z=abs(v[i].z)
        if ball[i].pos.z>7:
            v[i].z=-abs(v[i].z)

#        v[i]+=a[i]*dt
        ball[i].pos+=v[i]*dt
        E+=v[n].x**2+v[n].y**2+v[n].z**2
        velocity=sqrt(v[i].x**2+v[i].y**2+v[i].z**2)
        if t>0.0018 and t<0.0022:
            E1=E
        if t>0.00008 and t<0.00012:
            velocitypoints.append(velocity) 
        
    #print(E)


    t+=dt
    Epoints.append(E)        

vp=sorted(velocitypoints)
number=[]
for i in range(N):
    vp[i]=vp[i]/30
    vp[i]=floor(vp[i])

for a in range(N):
    count1=1
    
    
    for b in range(N):
        
        if a!=b:
            if vp[a]==vp[b]:
                count1+=1
    number.append(count1)
print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
for i in range(N):
    vp[i]=vp[i]*30
for i in range(N):
    print(vp[i])
print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa22222222222")
for i in range(N):
    print(number[i])
print(E1,E)
plot(Epoints)
show()
#plot(vp,number)
#show()












