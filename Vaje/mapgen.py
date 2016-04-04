__author__ = 'obi'
import random
"""
Legenda node-ov:
T = Trava
P = Pot
V = Voda
M = Mesto
B = Bruna

"""


#Mapo napolnes s travo
map = ["T"*100]*50

def get_node(x,y):
    x-=1
    y-=1
    aram = map[y]
    return aram[x]
def set_node(a,x,y):
    f=0
    x-=1
    y-=1
    aram = map[y]
    if x == 0:
        aram = a+aram[1:]
        f=1
    if x == 99:
        aram = aram[:99]+a
        f=1
    if f==0:
        aram = aram[0:x]+a+aram[x+1:]
    map[y] = aram
def set_hline(a,x,y,l):
    f=0
    x-=1
    y-=1
    aram = map[y]
    if x == 0:
        aram = a*l+aram[l:]
        f=1
    if x+l >= 99:
        aram = aram[:99-l+1]+a*l
        f=1
    if f==0:
        aram = aram[0:x+1]+a*l+aram[x+l+1:]
    map[y] = aram
def set_vline(a,x,y,l):
    for i in range(y,y+l):
        set_node(a,x,i)
def set_circ(a,x,y,r):
    set_hline(a,x-r,y,r)
    set_hline(a,x,y,r-1)
    set_vline(a,x,y-r+1,r)
    set_vline(a,x,y,r)
def seed(a):
    random.seed(a)
def draw_road_west(x,y,l):
    lastturn = 0
    node="P"
    sx = x
    j=0
    for i in range(x,x+l):
        j+=1
        if j % 5 == 0:
            node = "O"
        if i > 99:
            break
        if lastturn >= random.randint(1,6):
            lastturn = 0
            if random.randint(0,1) == 1:
                y+=1
            else:
                y-=1
            set_node(node,i,y)
        else:
            lastturn+=1
            set_node(node,i,y)
        sx = i
        node = "P"
    return sx, y
def draw_road_east(x,y,l):
    lastturn = 0
    node = "P"
    sx = x
    j=0
    for i in range(x,x-l,-1):
        j+=1
        if j % 5 == 0:
            node = "O"
        if i < 1:
            break
        sx = i
        if lastturn >= random.randint(1,6):
            lastturn = 0
            if random.randint(0,1) == 1:
                y+=1
            else:
                y-=1
            set_node(node,i,y)
        else:
            lastturn+=1
            set_node(node,i,y)
        node = "P"
    return sx, y
def draw_road_south(x,y,l):
    lastturn = 0
    j = 0
    node = "P"
    sy=y
    for i in range(y,y+l):
        j += 1
        if j%5==0:
            node = "O"
        if i > 50:
            break
        if lastturn >= random.randint(1,6):
            lastturn = 0
            set_node(node,x,i)
            if random.randint(0,1) == 1:
                x+=1
            else:
                x-=1
        else:
            lastturn+=1
            set_node(node,x,i)
        sy = i

        node = "P"
    return x, sy
def draw_road_north(x,y,l):
    lastturn = 0
    node = "P"
    j = 0
    sy=y
    for i in range(y,y-l,-1):
        j+=1
        if j % 5 == 0:
            node = "O"
        if i < 1:
            break
        if lastturn >= random.randint(1,6):
            lastturn = 0
            set_node(node,x,i)
            if random.randint(0,1) == 1:
                x+=1
            else:
                x-=1
        else:
            lastturn+=1
            set_node(node,x,i)
        sy = i
        node = "P"
    return x, sy
def start_E(x,y,n,s):
    switch = 1
    if switch == 1:
        a=draw_road_west(x,y,11)
        fl=False
        nstik=False
        sstik=False
        if random.randint(1,2) == 2:
            fl=True
            a1=draw_road_south(a[0],a[1],6)
            a=draw_road_west(a1[0],a1[1],11)
            a1=draw_road_south(a[0],a[1],6)
        else:
            a1=draw_road_north(a[0],a[1],6)
            a=draw_road_west(a1[0],a1[1],11)
            a1=draw_road_north(a[0],a[1],6)

        a=draw_road_west(a1[0],a1[1],11)
        if fl:
            a=draw_road_north(a[0],a[1],11)
        else:
            if random.randint(1,2) == 2:
                draw_road_north(a[0],a[1],30)
                nstik=True
            a=draw_road_south(a[0],a[1],6)
        a=draw_road_west(a[0],a[1],11)
        if a[1] > 25:
            a=draw_road_north(a[0],a[1],11)
            a=draw_road_west(a[0],a[1],11)
            a=draw_road_south(a[0],a[1],6)
        elif random.randint(1,2) == 2:
            a=draw_road_south(a[0],a[1],11)
            a=draw_road_west(a[0],a[1],16)
        else:
            a=draw_road_south(a[0],a[1],11)
            if random.randint(1,2) == 2:
                sstik=True
                draw_road_south(a[0],a[1],30)
            a=draw_road_west(a[0],a[1],11)
            if random.randint(1,2) == 2:
                a=draw_road_south(a[0],a[1],6)
                a=draw_road_west(a[0],a[1],6)
            else:
                a=draw_road_west(a[0],a[1],11)
        if not nstik and n:
            draw_road_north(a[0],a[1],101)
        if not sstik and s:
            draw_road_south(a[0],a[1],101)
        if a[0] < 60:
            a=draw_road_west(a[0],a[1],11)
        a=draw_road_west(a[0],a[1],11)
        if random.randint(1,2) == 2:
            a=draw_road_west(a[0],a[1],6)
            a=draw_road_south(a[0],a[1],16)
            a=draw_road_west(a[0],a[1],16)
            a=draw_road_north(a[0],a[1],6)
            a=draw_road_west(a[0],a[1],50)
        else:
            a=draw_road_north(a[0],a[1],16)
            a=draw_road_west(a[0],a[1],16)
            a=draw_road_south(a[0],a[1],6)
            a=draw_road_west(a[0],a[1],50)
def stranskaS():
    y = 0
    while y == 0:
        x = random.randint(50,75)
        for y_ in range(50):
            if get_node(x,y_) == "P":
                print(y_)
                y = y_
                print("Y = ",y)
    print(x,y)
    draw_road_south(x,y,50-y)
def stranskaN():
    y = 0
    while y == 0:
        x = random.randint(50,75)
        for y_ in range(50):
            if get_node(x,y_) == "P":
                print(y_)
                y = y_
                print("Y = ",y)
    print(x,y)
    draw_road_north(x,y,y)




seed(input("Gimme Seed!"))
draw_road_west(1,25,100)

stranskaS()
stranskaN()





for y in range(50):
    print(map[y][:])



