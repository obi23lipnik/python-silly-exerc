__author__ = 'obi'
"""
Simple code that takes a seed argument (or doesn't)
and spits out a map in string form.
"""
from sys import argv
import random

def gen_T():
	map = ['T'*50]*50
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


for a in argv:
	if a != "D:/projects/textmapgen.py" and a != "textmapgen.py":
		random.seed(a)
		print "SEED GIVEN!", a
print random.randint(1, 1000)
"""
for y in range(50):
    print(map[y][:])
"""
