import math

brown = 10
yellow = 2
n = (brown+yellow)//2
total = brown + yellow
answer = []
for i in range(1, int(yellow**(1/2))+1):
    if yellow%i==0:
        j = yellow//i
        if 2*i+2*j == brown+4: print([j,i])
